---
title: Dependencies
description: How addons declare, install, and ship third-party code.
weight: 6
---

FreeCAD addons can also take advantage of third-party Python libraries. There are two main way to deal with such dependencies: the [allow-list](#the-python-allow-list) and [vendoring](#vendoring).

## The Python allow-list

FreeCAD's Addon Manager will only install Python packages that appear on a curated allow-list. This page describes what that list is, where it lives, what format it uses, and how to get a new package added.

### What it is, and why

When your addon declares a Python package as a `<depend>` in its [Manifest](manifest), the Addon Manager looks that package up in a list of explicitly allowed Python dependencies. Packages on the list are installed automatically when a user installs your addon. Packages not on the list are not installed automatically.

The allow-list exists for several reasons:

- **Security.** Arbitrary `pip install` from PyPI is a common supply-chain attack vector. Gating dependencies behind a reviewed list reduces the chance of an addon silently pulling in malicious code.
- **Version consistency.** Different addons often depend on the same library (numpy, scipy, etc.). If each addon pinned its own version, the user's FreeCAD Python environment would end up with conflicting installs. A shared, version-controlled list lets the ecosystem coordinate. No addon's package requirements conflict with another's, by construction.
- **Quality control.** Packages that are unmaintained, abandoned, or require compiling against specific system libraries can be kept off the list entirely.

### Where the list lives

Two lists are maintained in parallel, corresponding to the two supported versions of the Addon Manager currently in the field.

#### FreeCAD v1.1 and later (or Addon Manager 2026.2.19 and later)

The current list lives in the [FreeCAD/Addons](https://github.com/FreeCAD/Addons) repository, split by Python version:

```
Data/Python/<python-version>/Allowed-Packages
```

For example, `Data/Python/3.11/Allowed-Packages`. A companion `constraints.txt` in the same directory pins each allowed package to a specific version, so every user gets a consistent install regardless of when they run the Addon Manager. Constraints is generated automatically from the Allowed-Packages file, and is updated automatically by a Dependabot process.

#### Pre-v1.1 (legacy)

Older FreeCAD builds read `ALLOWED_PYTHON_PACKAGES.txt` from the root of the [FreeCAD/FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) repository. That file is still maintained so older FreeCAD versions keep working, but new package requests should go to the new repository above.

### Format

Both files are plain text. Each non-empty, non-comment line is the PyPI package handle:

```
numpy
matplotlib
lxml
```

Version specifiers and wildcards are not supported in the allow-list itself. Version pinning happens in the companion `constraints.txt`, which the infrastructure maintains centrally so addon authors do not need to 9and indeed, *cannot*) specify versions themselves.

### What happens when a dependency is not on the list

The Addon Manager will not automatically install a Python package that is not on the allow-list. In practice this means:

- Your addon's manifest can still declare the dependency.
- Users who already have the package installed in FreeCAD's Python environment will see the addon work normally.
- Users who do not have the package will see the dependency flagged as unavailable. They can install it manually through their system's Python package manager, but this is awkward and error-prone, and often not an option for users who are not comfortable at a command line.

If your addon requires a Python package that is not on the allow-list, most users will not be able to install the addon successfully. Getting the package added is usually the appropriate next step. If that fails, see [Vendoring](#vendoring) for when it might be appropriate to ship a copy of the package with your addon instead.

### Requesting a new package

Open an issue in the [FreeCAD/Addons](https://github.com/FreeCAD/Addons) repository using the **Package - Addition** template. You will be asked for:

- The package handle as it appears on [PyPI](https://pypi.org/) (e.g. `numpy`, not the display name "NumPy").
- A short reason for the request. A normal answer is "my addon *X* needs this package to do *Y*."

Similar issue templates exist for requesting removal of a package from the list (`Package - Removal`) and for requesting that one package be replaced by another (`Package - Replace`).

There is no formal review SLA. Requests for well-known, well-maintained packages tend to move quickly; more obscure packages may need additional discussion. Ultimate responsibility for the curation of the allow-list falls to the [FreeCAD Maintainers team](https://freecad.github.io/DevelopersHandbook/maintainersguide).

## Vendoring

Vendoring means shipping a copy of a third-party Python library inside your addon's source tree, rather than declaring it as a dependency for the Addon Manager to install. This page describes when vendoring is appropriate, when it is not, and how to do it correctly when it is. TL;DR? Basically, don't.

### The default answer is "do not vendor"

FreeCAD's addon ecosystem coordinates Python dependencies through the [allow-list](#the-python-allow-list). That coordination provides basic security review, version pinning across addons, and a single point of update. Vendoring opts your addon out of all of those benefits.

The [quality requirements](addons-index) for inclusion in the Addon Index reflect this directly: an addon should "only vendor dependencies when technically necessary and not attempt to circumvent the package allow list." Vendoring a package that could be on the allow-list works against the ecosystem.

Before vendoring, consider the alternatives:

1. **Is the package on the allow-list?** If yes, declare it as a `<depend>` in your [Manifest](manifest). This is the standard path and by far the most common method for including a dependency.
2. **Could the package reasonably be added to the allow-list?** If it is well-maintained, generally useful, and available on PyPI, request its addition. See [The Python allow-list](#the-python-allow-list) for the procedure.
3. **Could you avoid the dependency?** Reimplementing a small piece of functionality in-house is sometimes simpler than carrying a third-party library through your addon's lifetime.

Only if none of the above applies should vendoring enter the discussion.

### When vendoring is acceptable

Roughly in order of strength:

- **The package is too niche to belong on the allow-list.** A small, single-purpose utility that no other addon in the ecosystem is likely to need.
- **You need only a small fraction of the package.** When one or two functions are all you actually use, copying just those (with attribution per the upstream license) is often cleaner than vendoring the whole package.
- **You have forked and modified the upstream.** A modified copy is your addon's code, not a dependency, and treating it as such is appropriate.
- **You need a specific pinned version that conflicts with the allow-list pin.** Rare, since the allow-list pins versions centrally, but possible.

### When vendoring is not acceptable

- **The package is on the allow-list.** Declaring the dependency is correct. Vendoring duplicates the install footprint across every addon that does it, and your vendored copy will drift from the version the allow-list pins, leading to inconsistent behavior across addons in the same FreeCAD installation.
- **The package could reasonably be added to the allow-list.** Request the addition; do not work around the process.
- **The package has compiled extensions** (numpy, scipy, lxml, Pillow, and similar). Vendoring binary wheels across every Python version, operating system, and architecture FreeCAD ships on is a significant maintenance burden. Which is to say: basically infeasible.
- **The license is restrictive or unclear.** Without explicit redistribution rights, vendoring may not be legal. See the licensing requirements below.
- **The package is large or rapidly evolving.** A multi-megabyte vendored library bloats your repository, and a fast-moving upstream means you will perpetually trail behind, inheriting bugs that have already been fixed.

### License requirements

You may only vendor code whose license permits redistribution. Common permissive licenses (MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, MPL-2.0) all allow vendoring with attribution. The LGPL family allows vendoring as long as the user can replace the LGPL component, which a vendored Python library generally satisfies.

The GPL is more restrictive: vendoring GPL-licensed code into a non-GPL addon makes the combined work GPL. If your addon is itself GPL-licensed, this is fine; otherwise it is not.

Proprietary, custom, or unclear licenses are usually unsuitable for vendoring. When in doubt, consult the upstream package's `LICENSE` file and, if necessary, the package authors. See [Licensing](license) for broader license guidance.

Whatever the upstream license, you must:

- Preserve the upstream `LICENSE` file inside your vendored copy.
- Acknowledge the vendored package in your addon's documentation or `README`.
- Comply with any other terms the upstream license imposes (e.g., notice files for Apache-2.0).

### Decision tree

```
Need a Python package?
│
├─ On the allow-list?
│  └─ Yes ─► declare <depend> in package.xml.
│
├─ Could reasonably be added to the allow-list?
│  └─ Yes ─► request addition.
│
└─ Neither, AND
   ├─ pure Python (no compiled extensions)
   ├─ permissively licensed
   ├─ small or used only fragmentarily
   ├─ relatively stable upstream
   └─ all yes ─► vendor with care (see below).
      any no  ─► rework your addon to avoid the dependency.
```

### How to vendor

Place the vendored code under a clearly internal subdirectory of your namespace package:

```
freecad/MyAddon/
├─ __init__.py
├─ init_gui.py
├─ ...
└─ _vendor/
   └─ somepkg/
      ├─ LICENSE       (preserved from upstream)
      ├─ README.md     (your notes on version, source URL, modifications)
      ├─ __init__.py
      └─ ...
```

The leading underscore on `_vendor` signals "internal; do not depend on this from outside the addon." This is a Python convention, not enforced by the language, but readers (and future maintainers) recognize it.

Import vendored code through your addon's namespace, not the original package name:

```py
# Good: clear that this is your vendored copy.
from freecad.MyAddon._vendor.somepkg import thing

# Bad: looks like a system-installed dependency, and may clash with one.
import somepkg
from somepkg import thing
```

Importing through your namespace prevents your vendored copy from interfering with a system-installed version of the same package, and prevents another addon's vendored or system-installed `somepkg` from interfering with yours.

Document what you vendored, where it came from, and which version. A short `_vendor/README.md` is the conventional place. At minimum, record:

- The upstream package name and PyPI link.
- The exact version vendored (commit SHA if vendored from a repository).
- Any modifications made to the upstream code.
- The reason vendoring was chosen rather than declaring a dependency.

### Maintenance

Vendored code freezes at the version you ship. Each subsequent upstream release, including security fixes, is your responsibility to track and re-vendor. Practical mitigations:

- **Pin the upstream version explicitly** in `_vendor/README.md` so a future maintainer (or you, in a year) can compare against current upstream.
- **Watch the upstream repository** for releases, especially security advisories.
- **Avoid modifying the vendored code.** A clean copy is easy to update; a heavily-patched copy means every upstream update requires re-applying patches.
- **Re-evaluate periodically** whether vendoring is still appropriate. If the package has since been added to the allow-list, switch.

## See also

- [Manifest: `<depend>`](manifest#depend): how to declare a dependency in `package.xml`.
- [Licensing](license): license guidance, including what licenses are compatible with redistribution.
- [Quality requirements for indexed addons](addons-index): the rules an indexed addon must meet, including the vendoring guidance.