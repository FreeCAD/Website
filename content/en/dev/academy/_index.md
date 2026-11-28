---
title: Addon Academy
description: Design, code, and share FreeCAD Addons.
weight: 6
icon: puzzle
---

Welcome to the **Addon Academy**, your one-stop place for documentation about creating and maintaining a FreeCAD Addon of any variety!

The **Guides** section below is a top-down list of steps you'll want to go through to author an Addon, while the **Topics** section covers several specific topics, and of course the **Demos** section contains sample code (all licensed CC0, so you are welcome to take whatever you need, no attribution is required).

## [Guides](guides)

Step-by-step how-tos.
For complete runnable examples that exercise these patterns end to end, see the [Demos](demos).

- [Creating an addon](create): starting from the GitHub template repository or the cookiecutter generator. Pros and cons of each.

- [Writing addon code](workbenches): the details of creating an Addon: workbenches, commands, Qt UI, preferences, custom document objects, icons, translations, and logging.

- [Developing locally](install): installing your addon into FreeCAD's `Mod/` directory, debugging, and writing tests.

- [Publishing your addon](portable): ZIP archives, repository URLs, and the official Addon Index.

- [Polishing for users](overview): making things look nice: writing an overview page, manifest metadata, and selecting screenshots.

- [Maintaining an addon](compatibility): cross-version compatibility, data migrations, and handing the project off to a new maintainer.

## [Topics](topics)

Reference material on how addons fit into FreeCAD.

- [Types of addon](types): workbench, macro, preference pack, bundle, and other.

- [Layout of an Addon](layout): modern namespaced layout, legacy layout, and the `package.xml` manifest.

- [Dependencies](dependency): the Addon Manager's allow-list, and when to vendor a library instead.

- [Licensing](license): choosing licenses for code and assets, and SPDX identifiers.

- [Addon Index](addons-index): the official registry, its quality requirements, and addons that have been removed from it.

- [Glossary](glossary): terminology used throughout the Academy and the wider FreeCAD ecosystem.

## [Demos](demos)

Worked examples with runnable source code.

- [Add a command to an existing toolbar](toolbar-demo): the smallest unit of addon functionality, building on what FreeCAD already ships.

- [Minimal Workbench](workbench-demo): a complete but stripped-down workbench, suitable as a starting point for a new one.

- [Parametric Feature](feature-demo): a custom document object with an `execute()` method and its own ViewProvider.

- [Preferences Page](preference-demo): an addon-supplied page under **Edit → Preferences** driven by a Qt Designer `.ui` file.

- [Macro](macro-demo): distributing a single-file `.FCMacro` as a standalone addon.

## See also

- [Template](https://github.com/FreeCAD/Addon-Template)
- [Index](https://github.com/FreeCAD/Addons)

## Community

- [Discord](https://discord.com/channels/870877411049357352/1458130438294999174)
- [Forum](https://forum.freecad.org/viewforum.php?f=65)y