---
title: Website introduction
description: Get involved with the FreeCAD website.
weight: 1
---


> [!IMPORTANT]
> The FreeCAD website is still in active development.
> The following documentation is not yet accurate or up-to-date.
> Have a question or feedback? Feel free to [open an issue](https://github.com/freecad/Website).


## Contributions

Contributions are always welcome!

The FreeCAD website source is freely accessible and open just like the FreeCAD software.

When contributing to the website, keep in mind that it acts as the public face of the FreeCAD organization and community. Substantial changes must be discussed beforehand via its usual communication channels (e.g. [GitHub](https://github.com/FreeCAD/Website/issues), [Matrix chat](https://matrix.to/#/#FreeCAD_FreeCAD:gitter.im), [Forum](https://forum.freecad.org/)). [FreeCAD's code of conduct](https://github.com/FreeCAD/Website/blob/main/CODE_OF_CONDUCT.md) must be observed at any time. Please also read the [Guidelines](guidelines).

Want to join the current [website team](teams)? Get in touch!

Contributions of all kinds are welcome: content, translations, bug fixes, theme improvements, testing, documentation, bug reports, and more... Depending on the scope, some basic know-how of Git, Markdown, HTML, CSS, Javascript, YAML/JSON and Hugo template syntax is recommended. Create appropriate [feature issues](https://github.com/FreeCAD/Website/issues) to discuss substantial changes before submitting Pull Requests. Also use the appropriate [Pull Request template](https://github.com/FreeCAD/Website/pulls) and make sure reviewers are assigned.

For bug report, use the provided [bug issues](https://github.com/FreeCAD/Website/issues) template.

Thank you!


## Website ecosystem

- [FreeCAD website](https://www.freecad.org/) and [its source](https://github.com/FreeCAD/Website)
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

1. Install [Hugo](https://gohugo.io/installation/) (standard edition).
2. Install [Git](https://git-scm.com/).
3. Optionally if developing Hugo modules, install [Go](https://go.dev/doc/install).
4. Clone this repository (or download the Code Zip via the green button on the top-right and unzip it):

```shell
git clone -b main https://github.com/FreeCAD/Website.git
```

5. Open the terminal at the cloned or downloaded repository location.
6. Build the site locally and launch the [live server](https://gohugo.io/commands/hugo_server/) from within the root directory of the site:

```shell
hugo server
```

Building should be relatively fast (about 10 seconds) and without errors.

To view the website locally, open the web browser at the indicated address, by default `http://localhost:1313/`.

### Deployment

Changes reach the public website through pull requests to the `main` branch, which require an approving review, except for bloggers' news posts within set limits (see [Publishing news](news)). Every environment is built from `main`:

- **Development:** your local clone. The result can be seen on the web browser after following the [Building instructions above](#building).
- **Testing:** [GitHub Pages](https://freecad.github.io/Website/), rebuilt automatically by the `Main build & deploy` workflow whenever `main` receives a new commit. The built site is stored in the `pages` branch. Maintainers can also publish a preview of a pull request at `https://freecad.github.io/Website/pr-<number>/` with the `Preview` workflow; it is removed when the pull request is closed.
- **Staging:** [staging.freecad.org](https://staging.freecad.org/), on FreeCAD's server. Same server setup as production, but hidden from search engines.
- **Production:** [www.freecad.org](https://www.freecad.org/), on FreeCAD's server.

Staging and production are updated by the `Deploy` workflow. It deploys production on every new commit on `main` and every hour, so that posts dated in the future appear within an hour of their date. Staging is deployed by starting the workflow by hand from the repository's Actions tab, and a maintainer must approve the run; production can be deployed the same way. The server then fetches `main`, builds it with Hugo, and switches the site to the new build only if the build succeeds.

> [!NOTE]
> Until the new website replaces the current one, www.freecad.org still serves the previous website from the [FreeCAD-Homepage](https://github.com/FreeCAD/FreeCAD-Homepage) repository.

### Browser support

> [!IMPORTANT]
> Internet Explorer isn't supported.

When using and making changes, keep in mind this website only supports *evergreen browsers*:

- Firefox (latest version, N-1 version, and latest ESR version)
- Chrome (latest version and N-1 version)
- Edge (latest version and N-1 version)
- Opera (latest version and N-1 version)
- Safari (latest version and N-1 version)
