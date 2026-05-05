---
title: Website introduction
description: Get involved with the FreeCAD website.
weight: 1
---


> [!IMPORTANT]
> The FreeCAD website is still in active development.
> The following documentation is not yet accurate or up-to-date.
> Have a question or feedback? Feel free to [open an issue](https://github.com/freecad/website).


## Contributions

Contributions are always welcome!

The FreeCAD website source is freely accessible and open just like the FreeCAD software.

When contributing to the website, keep in mind that it acts as the public face of the FreeCAD organization and community. Substantial changes must be discussed beforehand via its usual communication channels (e.g. [GitHub](https://github.com/FreeCAD/website/issues), [Matrix chat](https://matrix.to/#/#FreeCAD_FreeCAD:gitter.im), [Forum](https://forum.freecad.org/)). [FreeCAD's code of conduct](https://github.com/FreeCAD/website/blob/main/CODE_OF_CONDUCT.md) must be observed at any time. Please also read the [Guidelines](#guidelines) below.

Contributions of all kinds are welcome: content, translations, bug fixes, theme improvements, testing, documentation, bug reports, and more... Depending on the scope, some basic know-how of Git, Markdown, HTML, CSS, Javascript, YAML/JSON and Hugo template syntax is recommended. Create appropriate [feature issues](https://github.com/FreeCAD/website/issues) to discuss substantial changes before submitting Pull Requests. Also use the appropriate [Pull Request template](https://github.com/FreeCAD/website/pulls) and make sure reviewers are assigned.

For bug report, use the provided [bug issues](https://github.com/FreeCAD/website/issues) template.

Thank you!


## Website ecosystem

- [FreeCAD website](https://www.freecad.org/) and [its source](https://github.com/FreeCAD/website)
- [FreeCAD software source](https://github.com/FreeCAD/FreeCAD)
- [FreeCAD Wiki](https://wiki.freecad.org/)
- [FreeCAD Developers Handbook](https://freecad.github.io/DevelopersHandbook/) and [its source](https://github.com/FreeCAD/DevelopersHandbook)
- [FreeCAD Forum](https://forum.freecad.org/)
- [FreeCAD Project Association](https://fpa.freecad.org/) and [its source](https://github.com/FreeCAD/FPA)


## Development

### Building

> [!NOTE]
> The FreeCAD repository and its theme are currently compatible with Hugo 0.160.0

To build the website locally:

1. Install [Hugo](https://gohugo.io/installation/).
2. Install [Git](https://git-scm.com/).
3. Optionally if developing Hugo modules, install [Go](https://go.dev/doc/install).
4. Clone this repository (or download the Code Zip via the green button on the top-right and unzip it):

```shell
git clone -b main https://github.com/FreeCAD/website.git
```

5. Open the terminal at the cloned or downloaded repository location.
6. Build the site locally and launch the [live server](https://gohugo.io/commands/hugo_server/) from within the root directory of the site:

```shell
hugo server
```

Building should be relatively fast (about 10 seconds) and without errors.

To view the website locally, open the web browser at the indicated address, by default `https://localhost:1313/`.

### Deployment

This project uses a `development` > `testing` > `production` environments logic:

- The `development` environment is the local clone. The result can be seen on the web browser after following the [Building instructions above](#building).
- The `testing` environment is the `main` branch of this `website` repository. The result can be seen on [GitHub Pages](https://freecad.github.io/website/).
- The `production` environment is hosted on FreeCAD's server. The result can be seen on [FreeCAD website](https://www.freecad.org).

Testing builds deployment to GitHub Pages is done automatically by workflow Actions whenever the `main` branch receives a new commit. The built artifacts are stored in the `pages` branch (extracted from the `public` dir when the `hugo` command is run). The official website version is built from the `prod` branch instead.

### Browser support

> [!IMPORTANT]
> Internet Explorer isn't supported.

When using and making changes, keep in mind this website only supports *evergreen browsers*:

- Firefox (latest version, N-1 version, and latest ESR version)
- Chrome (latest version and N-1 version)
- Edge (latest version and N-1 version)
- Opera (latest version and N-1 version)
- Safari (latest version and N-1 version)
