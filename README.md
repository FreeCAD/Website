> [!NOTE]
> This is a temporary development repository : the [official repository](https://github.com/FreeCAD) will be available at a later time. More documentation will be added later as well.

[Contributing](#contributing) • [Development](#development) • [Structure](#structure) • [Guidelines](#guidelines) • [Theme](#theme) • [Resources](#resources) • [License](#license)

# FreeCAD Website

Welcome to the source code of [FreeCAD website](https://www.freecad.org). The content, assets and theme used are currently all gathered in this very repository.

The site is statically generated thanks to [Hugo](https://gohugo.io/), a fast and flexible static site generator written in Golang.

For other parts of FreeCAD web ecosystem, head to :

- [FreeCAD software source](https://github.com/FreeCAD/FreeCAD)
- [FreeCAD user documentation `Wiki`](https://wiki.freecad.org/)
- [FreeCAD developer documentation `Handbook`](https://freecad.github.io/DevelopersHandbook/) and [its source](https://github.com/FreeCAD/DevelopersHandbook).
- [FreeCAD forum](https://forum.freecad.org/)
- [FreeCAD Project Association](https://fpa.freecad.org/) and [its source](https://github.com/FreeCAD/FPA).

## Contributing

Contributions are always welcome ! FreeCAD website is free and open source just like FreeCAD.

When contributing to the website, keep in mind that it acts as the public face of the FreeCAD organization and community. Thus, substantial changes have to be discussed beforehand via its usual communication channels (e.g. GitHub issues, [Matrix chat](https://matrix.to/#/#FreeCAD_FreeCAD:gitter.im), [Forum](https://forum.freecad.org/), [Discord](https://discord.com/invite/F4hdxzYZfc)). [FreeCAD's code of conduct](https://github.com/FreeCAD/FreeCAD/blob/main/CODE_OF_CONDUCT.md) have to be observed at any time. Read the [Guidelines](#guidelines) below.

Contributions of all kind can be accepted : content, translations, bug fixes and theme improvements. Depending on the scope, some basic know-how of Git, YAML, Markdown, HTML, CSS, Javascript and Hugo template syntax is recommended. Create appropriate issues discussing your changes before submitting Pull Requests.

For bug report, please use the provided GitHub issue template.

### Browser support

When using and making changes, keep in mind this website only supports *evergreen browsers* :

- Firefox (latest version, N-1 version, and latest ESR version)
- Chrome (latest version and N-1 version)
- Edge (latest version and N-1 version)
- Opera (latest version and N-1 version)
- Safari (latest version and N-1 version)

> [!IMPORTANT]
> Internet Explorer isn't supported.

## Development

### Building

To build the website locally :

1. Install [Hugo](https://gohugo.io/installation/).
2. Install [Git](https://git-scm.com/).
3. Optionally if developing Hugo modules, install [Go](https://go.dev/doc/install).
4. `Git` clone this repository or download the Code Zip and unzip it.
5. Open the terminal at your cloned or downloaded repository location.
6. Build the site locally and launch the [live server](https://gohugo.io/commands/hugo_server/) : within the root directory of the site, run

```shell
hugo server
```

To build with [Draft pages](https://gohugo.io/methods/page/draft/), run

```shell
hugo server -D
```

Building should be relatively fast (about 10 seconds) and without errors.

To view the website locally, open your web browser at the indicated address, by default `https://localhost:1313/`.

> [!IMPORTANT]
> This temporary repo is currently compatible with Hugo 0.145

### Deployment

This project uses a `development` > `testing` > `production` environments logic :

- The `development` environment is your local clone. The result can be seen on your web browser after following the [Building instructions above](#building).
- The `testing` environment is this current repository. The result can be seen on [GitHub Pages](https://marcuspollio.github.io/FreeCAD-website/).
- The `production` environment is hosted on FreeCAD's sever. The result can be seen on [FreeCAD website](https://www.freecad.org).

Testing builds deployment to GitHub Pages is done automatically by GitHub Actions whenever the `testing` branch receives a new commit. The `testing` branch itself should not be deployed, as it only contains the source files. The built version of the website is in the `public` folder, generated from the `hugo` command. The official website version is built from the `production` branch instead.

> [!NOTE]
> Currently no production branch. Will be added when migrated to the official FreeCAD repository.

## Structure

### Use and navigation overview

The website is structured following a tree logic (directory), where each branch (folders) contains sub-branches (sub-folders) and/or leafs (files) where content is stored. The Homepage is the trunk giving access to the various main branches (called `sections` in Hugo lingo) of the navigation menu (e.g. `features`,`download`, `news`, etc). Some of these main branches give access to further sub-branches (e.g. news articles categories). To keep the site simple, only three branch levels are used for the moment, making the navigation easier to understand and maintain, limiting the necessity of a search function.

The website is multilingual, with English being the default language. That means that available translated content in any enabled language is accessible using the language dropdown in the header.

> [!NOTE]
> Currently no detection of the User Agent language is implemented, so the English version is always presented first.

A light and dark version of the theme is available on the sun/moon icon on the top header.

> [!NOTE]
> This temporary development version does not have all features available yet.

### Technical overview

[Hugo](https://gohugo.io), the static site generator used, takes the plain-text content (typically Markdown) and data files (typically CSV, JSON, XML and YAML), marries them to an appropriate set of templates and produces a complete set of HTML pages (with CSS and Javascript) that can be served by any generic stand-alone web server.

To understand how Hugo works, read its [Official documentation](https://gohugo.io/documentation/).

### Content and metadata

To simply change or create content, such as news articles, read first the [Guidelines](#guidelines), then read about the [Content Management System](#content-management-system) or [Archetypes](#archetypes). If curious how content is organized, carry on reading below.

There are two main types of content files : **Single** (`index.md`) and **List** (`_index.md`) pages. **Single** pages are where most changes will be made.**List** pages gathers content from **Single** pages and should not be changed in most cases. All linked resources for a specific page (e.g. illustrations, translations, assets) can be stored in the same folder as the page itself ([leaf bundle](https://gohugo.io/content-management/page-bundles/) method), making relative links easy and content tidy.

These files are mostly written with Markdown and contain a metadata header called the Front Matter, at the top of the file in-between the YAML `---` characters. How content from **Single** and **List** pages generated into HTML is defined by templates actions used by the [Theme](#theme).

The content is structured as follows :

- `content/_index.md` : the Homepage file. This is a **List** gathering content from other pages, mainly in the News and Homepage sections.

- `content/homepage` : **Single** with overview and features displayed on the Homepage and used by the previous **List**.

- `content/features` : **Single** showcasing FreeCAD features.

- `content/download` : **Single** allowing to download FreeCAD latest release per platform, links to development, previous versions and other useful resources. Read how to [update the Releases builds](#releases).

- `content/releases` : **List** gathering the release notes. Each release is organized in sub-folders. The following metadata fields are required for the release notes to be correctly displayed throughout the website : `title` (version of the release), `description`, `date`, `params` and `cover` (splashscreen of the release). Read how to [update the Releases builds](#releases).

- `content/news` : **List** gathering articles for the news blog. Articles are organized in `categories` sub-folders. The following metadata fields are required for the article to be correctly displayed throughout the website: `title`, `description`, `date`, `author`, `categories`,`tags` and `cover image`. The name of the folder acts as a slug in the generated URL. `Draft` articles or articles with a `date` in the future are not published in the production environment. To have an article featured at the top of the Homepage, the `hero` Params have to be set.

- `content/documentation` : **Single** helping users to get started with FreeCAD (wiki, manual, tutorials, learning network).

- `content/community` : **Single** to get involved with the FreeCAD community (events, online groups, association).

- `content/contribute` : **Single** to start contributing to FreeCAD development (bug reports, translations, code, grants).

- `content/donate` : **List** gathering donations to the FreeCAD Project Association. The following metadata fields are required for the sponsors to be correctly displayed throughout the website: `title` (name of the sponsor), `link` (link of the sponsor if applicable) `type` (sponsor level e.g. bronze, silver or gold), `date` (start of the sponsorship).

- `content/about` : **Single** with info about the website (credits, term of use, etc).

> [!NOTE]
> `content/theme-docs` : only temporary for the website development.

### Root folders skeleton

```
FreeCAD-website/
├── .github/
├── archetypes/
├── assets/
├── config/
├── content/
├── data/
├── i18n/
├── layouts/
├── public/     <-- generated when building the site, not in git repository
├── resources/  <-- generated when building the site, not in git repository
├── static/
├── themes/
├── .gitignore
├── LICENSE
└── README.md
```

Hugo [Lookup order](https://gohugo.io/templates/lookup-order/) and [Union file system](https://gohugo.io/getting-started/directory-structure/#union-file-system) logic allows to resolve duplicate file and folder names, using their different paths to take precedence. When two files have the same filename, the file in the root project directory takes precedence. This allows to override a `theme` template by placing a copy of the same name within the project root.

- `.github` : configuration and template files for GitHub.

- `archetypes` : pre-made template files to easily add new content. Read below about [Archetypes](#archetypes).

- `assets` : global resources used throughout the website that can be modified using pipes. This includes CSS, JS and images. For media content used in articles and other pages check their respective folders.

- `config` : configuration files for the site generator, languages, the [Theme](#theme) and the [Content Management System](#content-management-system).

- `content` : [Content](#content-and-metadata) files.

- `data` : local data resources (e.g. JSON, YAML, XML) to augment or create content. Currently empty, it may be used in the future to store e.g. authors data.

- `i18n` : translation tables for the theme in a multilingual website.

- `layouts` : wrapping templates actions to transform content, data and resources into a complete set of HTML pages.

- `public` : website generated by the `hugo` and `hugo server` commands. It does not have to be version-controlled by git. When creating a Pull Request, please do not include it.

- `resources` : cached output from Hugo pipelines generated by the `hugo` and `hugo server` commands, e.g. CSS and images. It does not have to be version-controlled by git. When creating a Pull Request, please do not include it.

- `static` : global static resources used throughout the website. This includes favicons and fonts.

- `theme` : [Theme](#theme) files with its specific templates actions, layouts, assets and translation tables. It is currently called `FC` theme.

## Guidelines

### Overview

> [!NOTE]
> Guidelines are currently work-in-progress.

### Text style

TODO

### Illustrations

Images in hero cover and page content are used to illustrate the page message and purpose, and additionally highlight related and successful projects.

Texts in illustrations are to be avoided if possible. Attribution and license have to be respected at all times. If photos depict human beings, a consent agreement has to be submitted accordingly.

It is highly recommended to add illustrations files along the page Markdown file ([leaf bundle](https://gohugo.io/content-management/page-bundles/) method), so they can be processed by the static site generator templates. Relative links have to be used instead of absolute links. Alternate `alt` text and tooltip `title` text have to be added as well.

```markdown
![alt](img.webp “image title”)
```

Currently, only static images (no animations) are used. A minimum width of about 2000 pixels is recommended. The WebP graphics file format is recommended as well. AVIF is currently not supported.

Template actions in the FC Theme resize and crop images at build time depending on their use. The Content Management System also resize uploaded images at the correct resolution. That means content contributors only need to add one WebP file about 2000px wide.

### Releases

All download information for the current stable version and future new release you may add is stored in the front matter of release notes pages in `content/releases`. The download box on top of the download page uses the latest release notes page info.

To create a new release, use the following Front Matter :

```yaml
---
title: "FreeCAD X.Y Release"        <-- X is the major version number and Y minor
description: "The release description"
date: yyyy-mm-dd
author: "FreeCAD"
tags:
  - X.Y
params:
  release: X.Y
  windows_msi: link-to-windows-msi-build
  windows_zip: link-to-windows-zip-build
  mac_x86: link-to-mac-x86-build
  mac_arm: link-to-mac-arm-build
  linux_x86: link-to-linux-x86-build
  linux_aarch64: link-to-linux-aarch64-build
cover:
  image: splashscreen-x-y.jpg
  caption: "the X.Y splashscreen"
  alt: "the X.Y splashscreen"
---
```

Use a similar release notes page content structure as previous ones for consistency.

### Translations

Current supported languages are defined in the general site configuration `config/languages.yaml`.

Translations of the content are stored in the same folder ([leaf bundle](https://gohugo.io/content-management/page-bundles/) method) as the default language file (English) using a [translation by file name](https://gohugo.io/content-management/multilingual/#translate-your-content) approach.

Translations of the theme are handled by translations tables in `themes/FC/i18n`.

Before a new language is enabled, the main navigation pages (homepage, features, download, news, community, documentation, contribute and donate) and the theme strings have to be translated. If willing to add a new language, please use the provided GitHub issue template indicating who will translate and who will proofread.

### Content Management System

> [!NOTE]
> Currently the CMS is work-in-progress and its structure and content may change in the near future. More documentation will be added later as well.

A server-less Content Management System is available to manage content easily. It is based on the [Sveltia CMS](https://github.com/sveltia/sveltia-cms) project. It's a single JavaScript that interacts with the Git repository of the website. It can be used locally on supported web browsers (currently only Chromium-based) or via GitHub login. Pages, translations and resources such as illustrations can be added, edited or deleted directly from the content panel of available collections.

### Archetypes

> [!NOTE]
> Currently archetypes are only partially set up and not really useful for now, only the basic `default.md` and `news/index.md` can be used. It is recommended to use the [Content Management System](#content-management-system) instead.

Archetypes are templates for new content, making creation of new content easier and consistent. The following command creates a new content file named Base-Name.md with the specified PATH :

```shell
hugo new content PATH/Base-Name.md
```

Some fields in the Front Matter or page content will be pre-filled or pre-populated with Archetype template functions, e.g. the `title` field will use the Base-Name without hyphens.

## Theme

> [!NOTE]
> The FC Theme is work-in-progress and its structure and methods may change in the near future. The code is also pretty messy and YOLO. It will gradually be cleaned up, simplified and refactored so it can _live more than once_... More documentation will be added later as well.

Currently the FC Theme is used. It is included directly in the `themes/FC` folder. Read its [own documentation](themes/FC/README.md) to find out more.

## Resources

- Please consider [website usage stats](https://caniuse.com/) when relying on modern web technologies (web standards support, file type support, etc).

- Before submitting changes, please test thoroughly, ideally on several devices, using browser built-in web tools/extensions, such as Firefox Inspector that displays Responsive Design Mode (Ctrl+Shift+M).

- Have a look at [Recommended Accessibility Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/list/) and use online tools when evaluating the website performance and compliance.

- If developing with the IDE `VSCodium`, the extension `Hugo Language and Syntax Support` is handy.

## License

This repository is licensed under the [GNU Lesser General Public License Version 2.1](https://github.com/marcuspollio/FreeCAD-website/blob/testing/LICENSE "Read the license text").

### Content

Content of the website (folder "/content/") is licensed under [Creative Commons Attribution ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/ "Read the license").
By default, it is copyrighted by and attributed to "FreeCAD contributors". If they wish so, authors can specify the respective attribution for the content they produce. For Markdown files, the attribution is specified in the "author" field of the front matter.

By submitting Pull Requests to this repository, please make sure you are the author of the content uploaded, or otherwise that you have right to share it here under the CC-BY-SA 4.0 license and make sure the original author is mentioned. Also note that sharing images with people is subject to obtaining appropriate consent.

### FreeCAD branded resources

The trademark of FreeCAD branded resources (e.g. FreeCAD logo) is registered and owned by the [FreeCAD Project Association](https://fpa.freecad.org/handbook "Read the FPA Handbook").

### Theme

The FC theme folder is licensed under the [MIT License](https://github.com/marcuspollio/FreeCAD-website/blob/testing/themes/FC/LICENSE "Read the license text").
