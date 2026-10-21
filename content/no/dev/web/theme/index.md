---
title: Setup and Theme
description: Enhance the website project structure, configuration, and the Trigo Theme.
weight: 9
---

> [!Note]
> The following reflects the state of the FreeCAD website as of July 2026.
>
> If major changes are made to the structure, this documentation must be updated accordingly.

## Website setup

The FreeCAD website is organized in a single git repository. External Hugo or git modules are not used yet.

The Trigo theme lives in the `themes` directory and, apart from a few needed configuration parameters, works as a standalone system.

The FreeCAD website content is developed specifically along the Trigo theme.
That means that features only provided by the Trigo theme will not be available if using another theme.
This includes custom front matter fields, metadata, shortcodes, layouts, languages fallbacks, assets, styling, etc.

As explained in the [structure page](structure), the `/content` directory uses a multilingual structure with the language key as top-level folder (e.g. `en`, `zh`).
The homepage resides at the root of each localized trees, next to the nested directories for each collection sections.

Automatic Continuous Integration (CI) and Continuous Deployment (CD) workflows are set in the `/.github` directory, with a few respository templates.
Some of these workflow use Python scripts located in the \`/tools/workflows/ directory.

Finally, development notes are stored in the `/notes` directory to keep track of past decisions and discussions.

## Konfigurasjon

The FreeCAD website has two main environments:

- The default development environment whose configuration is defined in `/config/_default`
- The production environment whose configuration is defined in `/config/production` and overrides the default one

The project configuration is split into several files, so it is easier to manage:

- `hugo.yaml` is the main configuration with the most important settings
- `languages.yaml` defines the multilingual locales and if they are enabled or disabled
- `module.yaml` defines the modules mounts and serves as languages fallback strategy to the default language site (English)
- `params.yaml` defines all theme-specific and custom parameters

## Trigo Theme for Hugo

Trigo is a custom made theme for the [Hugo Static Side Generator](https://gohugo.io/).
It is developed specifically for the [FreeCAD website](https://www.freecad.org/).

Trigo aims for simplicity, ease of use and flexibility.
Contributions of new features, tweaks and improvements are very much welcome!
Anyone with basic knowledge of Hugo, web standards, HTML, CSS and a bit of JavaScript will hopefully feel at ease.
Its architecture, methods and documentation are made simple yet efficient in a _FOSS_ spirit.

Trigo is inspired by numerous existing Hugo themes, such as PaperMod, Hextra, the official Hugo docs theme and many more.

> [!Note]
> Capitalized words refer to specific web concepts, or relevant to the Trigo theme used in a FreeCAD website context.

### Theme Overview

The Trigo theme is based on a standard Hugo theme structure: it uses a set of HTML wrapping template actions to transform Content, Data and Resources (in `layouts` directory), some CSS stylesheets and JavaScript (the last two in `assets`).
Translations tables for theme `i18n` strings are used as well.
Bundled icons are available in `assets/svg`.

### Stil

The style of the theme is defined in CSS stylesheets in `assets/css`.
The `main.css` file defines the stylesheet files to import.
Reusable variables (e.g. `var(--accent)`) are found in `vars.css` in both **Light** and **Dark** chroma variants.
Some additional project-specific variables are defined the project configuration parameters (`/config/_default/params.yaml`) under the `style` key, such as `accent-color`, `font-sans`, `font-mono`, etc.

General selectors and properties are in `body.css`.
The site Header, Footer, Hero and Content sections are defined in `header.css`, `footer.css`, `hero.css`, and `content.css` respectively.
The `404.css`, `archive.css`, and `share.css` define the style for these special pages respectively.
The `highlight.css` defines the style for code highlighting.
The `media.css` defines the style for different devices and screen sizes via media queries (flex and responsive changes).
The `shortcodes.css` defines the style for bundled shortcodes.
Finally, the `custom.css` defines the style of project-specific custom partials and reusable classes.

### Custom classes

TODO

### Layouts

Each Layout inherits from `layouts/_default/baseof.html` which contains the Main structure of the Page, including the Head.

Default Layouts use either:

- `home.html` for the Homepage at the Content Root (i.e. `/content/<locale>/_index.md`).

- `list.html` for **List** Pages in each Sections (e.g. Releases list, News list, Documentation lists).

- `single.html` for **Single** RegularPages (e.g. Release notes, News articles, Manual pages).

- `archives.html` for listing all relevant RegularPages in a Section with an `archives.md` file.

- `taxonomy.html` for listing all relevant Terms of a Taxonomy (e.g. Event, Announcement for the Categories Taxonomy).

- `term.html` for listing all relevant Pages associated with a specific Term.

To organize the code and avoid duplications, the default Layouts may include **Partials** depending on the context. A Partial is just another piece of code that also performs template actions, to keep the code _DRY_.

### Code formatting and syntax

Hugo SSG templates, methods and functions generally use `PascalCase` formatting (e.g. `{{- with .RegularPages -}}`) and `camelCase` for default fields and method aliases (e.g. `{{- hasPrefix $foo $bar -}}`).

Trigo custom naming uses `snake_case` for `custom_param`, `custom_partial.html`, and `$local_variables`, to help distinguish from official Hugo syntax.

CSS classes and IDs use hyphens like `custom-class`.

Naming should be as short and explicit as possible. A variable assigned from the result of a boolean test should be named `$is_test`, while numbers, strings, dates, arrays (slice), map (dict), and other types should be named appropriately (e.g. singular vs plural, limits, enable vs disable).

Beware of Hugo **Context** and **whitespace trimming** concepts, as they are tricky to get at first. See [Hugo official docs](https://gohugo.io/templates/introduction) as reference.