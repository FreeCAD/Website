> [!NOTE]
> This new unified FreeCAD website is in a WIP migration phase.
> The current official website repository is still [FreeCAD-Homepage](https://github.com/FreeCAD/FreeCAD-Homepage) for now.


# FreeCAD website

[Contributions](#contributions) •
[Development](#development) •
[Structure](#structure) •
[Guidelines](#guidelines) •
[CMS](#cms) •
[Theme](#theme) •
[Tips](#tips) •
[License](#license)


Welcome to the source of the [FreeCAD website](https://www.freecad.org)!

The content, assets, theme code and style are all gathered in this repository.
The site is statically generated thanks to [Hugo](https://gohugo.io/), a fast and flexible static site generator written in Golang.

For other parts of FreeCAD web ecosystem, head to:

- [FreeCAD software source](https://github.com/FreeCAD/FreeCAD)
- [FreeCAD Wiki](https://wiki.freecad.org/)
- [FreeCAD Developers Handbook](https://freecad.github.io/DevelopersHandbook/) and [its source](https://github.com/FreeCAD/DevelopersHandbook)
- [FreeCAD Forum](https://forum.freecad.org/)
- [FreeCAD Project Association](https://fpa.freecad.org/) and [its source](https://github.com/FreeCAD/FPA)


## Contributions

Contributions are always welcome!
The FreeCAD website source is freely accessible and open just like FreeCAD.

When contributing to the website, keep in mind that it acts as the public face of the FreeCAD organization and community.
Substantial changes must be discussed beforehand via its usual communication channels
(e.g. [GitHub](https://github.com/FreeCAD/website/issues), [Matrix chat](https://matrix.to/#/#FreeCAD_FreeCAD:gitter.im), [Forum](https://forum.freecad.org/)).
[FreeCAD's code of conduct](https://github.com/FreeCAD/website/blob/main/CODE_OF_CONDUCT.md) must be observed at any time.
Please also read the [Guidelines](#guidelines) below.

Contributions of all kinds are welcome: content, translations, bug fixes, theme improvements, testing, documentation, bug reports, and more...
Depending on the scope, some basic know-how of Git, Markdown, HTML, CSS, Javascript, YAML/JSON and Hugo template syntax is recommended.
Create appropriate [feature issues](https://github.com/FreeCAD/website/issues) to discuss substantial changes before submitting Pull Requests.
Also use the appropriate [Pull Request template](https://github.com/FreeCAD/website/pulls) and make sure reviewers are assigned.

For bug report, use the provided [bug issues](https://github.com/FreeCAD/website/issues) template.

Thank you!

### Browser support

> [!IMPORTANT]
> Internet Explorer isn't supported.

When using and making changes, keep in mind this website only supports *evergreen browsers*:

- Firefox (latest version, N-1 version, and latest ESR version)
- Chrome (latest version and N-1 version)
- Edge (latest version and N-1 version)
- Opera (latest version and N-1 version)
- Safari (latest version and N-1 version)


## Development

### Building

> [!IMPORTANT]
> Currently compatible with Hugo 0.158.0

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

Testing builds deployment to GitHub Pages is done automatically by workflow Actions whenever the `main` branch receives a new commit.
The built artifacts are stored in the `pages` branch (extracted from the `public` dir when the `hugo` command is run).
The official website version is built from the `prod` branch instead.


## Structure

### Use and navigation overview

The website uses a simple folder-based structure.
The Homepage links to main sections (e.g. Features, Download, News) which may contain sub-sections (e.g. Release notes, User documentation).
All content is stored in files and the structure is kept to a minimum number of levels for ease.

The website is multilingual, with English being the default language.
Available translated content in any enabled language is accessible using the language dropdown in the header.

A light and dark chroma version of the Theme is available on the sun/moon icon on the top header.

### Technical overview

[Hugo](https://gohugo.io), the static site generator used, takes the plain-text content (typically Markdown) and data files (typically CSV, JSON, XML and YAML),
marries them to an appropriate set of templates and produces a complete set of HTML pages (with CSS and Javascript) that can be served by any generic standalone web server.

To understand how Hugo works, read its [Official documentation](https://gohugo.io/documentation/).

### Content and metadata

To simply change or create content (e.g News articles), first read the [Guidelines](#guidelines) and
then the [Content Management System](#cms) that provides a user-friendly way to manage content.

Here is how content is organized for curious and tech-savvy contributors:

There are two main types of content files:
- **Single** (`index.md`) pages are in general where most changes are made.
- **List** (`_index.md`) pages in general gather content from related **Single** pages and need little changes.

All linked resources for a specific page (e.g. illustrations, translations, assets) are stored in the same folder as the page itself.
This method is called a [leaf bundle](https://gohugo.io/content-management/page-bundles/) and makes relative links easy and content tidy.

These files are mostly written with Markdown and contain a metadata header called the Front Matter at the top of the file in-between the YAML `---` characters.
How content from **Single** and **List** pages is generated into HTML is defined by Hugo templates in the [Theme](#theme).


## Guidelines

> [!NOTE]
> Guidelines are currently WIP.

### Text

- Texts use a clear, concise, straightforward and inclusive language that welcomes readers from diverse backgrounds and communities (e.g. non-tech, skills, cultures).
- A friendly and supportive tone is used reflecting the free and open-source community collaborative spirit.
- Texts should be easy to translate. If in doubt, ask a translator.
- Texts focus on user benefits in practical and relatable terms that highlight how FreeCAD contribute to solving real-world challenges (e.g. design, engineering, community, free and open-source development).
- Prefer using the active voice when possible (e.g. subject is the agent: "subject does action", instead of passive voice where subject is recipient: "action is done by subject") and break complex ideas into simpler and digestible explanations.
- Sometimes an illustration is worth a thousand words.

### Illustrations

- Images in hero cover and page content are used to illustrate the page message and purpose, and additionally highlight related and successful projects.
- Texts in illustrations are avoided if possible. Attribution and license are respected at all times. If photos depict human beings, a consent agreement is submitted accordingly.
- It is highly recommended to add illustrations files along the page Markdown file ([leaf bundle](https://gohugo.io/content-management/page-bundles/) method), so they can be processed by the static site generator templates. For internal resources, relative links are used instead of absolute links.
- Caption and alternate text are provided:

```md
![alternative text for image](img.webp “image caption”)
```

Please avoid adding links to images (e.g. `[![alt](img.webp)](link)`) as the Markdown parser and render hooks mix HTML block-level with inline elements, which is invalid.
Use the `figure` shortcode instead, or add links to nearby heading, text or caption.

Currently, only static images (no animations) are used. A minimum width of about 2000 pixels is recommended.
The WebP graphics file format is recommended as well. AVIF is currently not supported.

Template actions in the Theme resize and crop images at build time depending on their use.
The [Content Management System](#cms) also resize uploaded images at the correct resolution.
Content contributors only need to add one WebP file about 2000px wide.

### Translations

Current supported languages are defined in the general site configuration `config/_default/languages.yaml`.

Translations of the content are stored in the same folder ([leaf bundle](https://gohugo.io/content-management/page-bundles/) method) as the default language file (English) using a [translation by file name](https://gohugo.io/content-management/multilingual/#translate-your-content) approach.

Translations of the Theme are handled by translations tables in `themes/Trigo/i18n`.

Before a new language is enabled, the main navigation pages (Homepage, Features, Download, News, Community, Documentation and Donate) and the Theme strings must be translated.
If willing to add a new language, use the provided [feature issue](https://github.com/FreeCAD/website/issues) template indicating who will translate and who will proof-read/review.


## CMS

> [!NOTE]
> Currently the CMS is WIP and its structure and content may change in the near future.

A server-less Content Management System is available to manage content easily. It is based on the [Sveltia CMS](https://github.com/sveltia/sveltia-cms) project.
A single JavaScript interacts with the Git repository of the website. It can be used locally on supported web browsers (currently only Chromium-based) or via GitHub login.
Pages, translations and resources such as illustrations can be added, edited or deleted directly from the content panel of available collections.


## Theme

> [!NOTE]
> The Trigo Theme is WIP and its structure and methods may change in the near future.

The custom-made Trigo Theme is used. It is included directly in the `themes/Trigo` directory. Read its [own documentation](themes/Trigo/README.md) to find out more.


## Tips

- Consider [website usage stats](https://caniuse.com/) when relying on modern web technologies (e.g. web standards support, file type support).
- Before submitting changes, please test thoroughly, ideally on several devices, using browser built-in web tools/extensions, such as Firefox Web Developer Tools and Chromium DevTools (Ctrl+Shift+I) to display Responsive Design Mode (Ctrl+Shift+M).
- Have a look at [Recommended Accessibility Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/list/) and use online tools when evaluating the website performance and compliance.
- If developing with the IDE VSCode/VSCodium, the extension `Hugo Language and Syntax Support` is handy.


## License

This repository is licensed under the [GNU Lesser General Public License Version 2.1](https://github.com/FreeCAD/website/blob/main/LICENSE "Read the license text").

### Content

Content of the website is licensed under [Creative Commons Attribution ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/ "Read the license").
By default, it is copyrighted by and attributed to "FreeCAD". If they wish so, authors can specify the respective attribution for the content they produce.
For Markdown files, the attribution is specified in the `author` field of the Front Matter.

By submitting Pull Requests to this repository, make sure who is the author of the content.
Make sure rights to share under the CC-BY-SA 4.0 license and original author mention are respected.
Also note that sharing images with people is subject to obtaining appropriate consent.

### FreeCAD branded resources

The trademark of FreeCAD branded resources (e.g. FreeCAD logo) is registered and owned by the [FreeCAD Project Association](https://fpa.freecad.org/handbook "Read the FPA Handbook").

### Theme

The `Trigo` Theme is licensed under the [MIT License](https://github.com/FreeCAD/website/blob/main/themes/Trigo/LICENSE "Read the license text").
