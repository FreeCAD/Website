# Trigo Theme for Hugo

Trigo is a custom made theme for the [Hugo Static Side Generator](https://gohugo.io/). It is developed specifically for the [FreeCAD website](https://www.freecad.org/).

Trigo aims for simplicity, ease of use and flexibility. Contributions of new features, tweaks and improvements are very much welcome! Anyone with basic knowledge of Hugo, web standards, HTML, CSS and a bit of JavaScript will hopefully feel at ease. Its architecture, methods and documentation are made simple yet efficient in a *FOSS* spirit.

Trigo is inspired by numerous existing Hugo themes, such as PaperMod, Hextra, the official Hugo docs theme and many more.

> [!Note]
> Capitalized words refer to specific web concepts, or relevant to the Trigo theme used in a FreeCAD website context.
> Hugo lingo, template methods and functions generally use CamelCase.


## Theme Overview

The Trigo theme is based on a standard Hugo theme structure: it uses a set of HTML wrapping template actions to transform Content, Data and Resources (in `layouts` directory), some CSS stylesheets and JavaScript (the last two in `assets`). Translations tables for theme `i18n` strings are used as well. Bundled icons are available in `assets/svg`.


## Style

The style of the theme is defined in CSS stylesheets in `assets/css`. Reusable variables are found in `theme_vars.css` in both **Light** and **Dark** variants. General selectors and properties are in `body.css`. Style for the Main Content area for both **List** and **Single** pages are defined in `main.css`. The site Header is defined in `header.css` and the site Footer is defined is `footer.css`. The `404.css`, `archive.css` and `terms.css` define the style for the Main area of these special pages respectively. The `highlight.css` define the style for code highlighting. The `media.css` defines the style for different devices and screen sizes via media queries (flex and responsive changes).


## Layouts

Each Layout inherits from `layouts/_default/baseof.html` which contains the Main structure of the Page, including the Head.

Default Layouts use either:

- `home.html` for the Homepage at the Content Root (i.e. `/content/<locale>/_index.md`).

- `list.html` for **List** Pages in each Sections (e.g. Releases list, News list, Documentation lists).

- `single.html` for **Single** RegularPages (e.g. Release notes, News articles, Manual pages).

- `archives.html` for listing all relevant RegularPages in a Section with an `archives.md` file.

- `taxonomy.html` for listing all relevant Terms of a Taxonomy (e.g. Event, Announcement for the Categories Taxonomy).

- `term.html` for listing all relevant Pages associated with a specific Term.

To organize the code and avoid duplications, the default Layouts may include **Partials** depending on the context. A Partial is just another piece of code that also performs template actions, to keep the code *DRY*.


## Code formatting and syntax

Hugo SSG templates, methods and functions generally use CamelCase formatting.

Trigo custom naming uses `snake_case` for `custom_param`, `custom_partial.html`, and `$local_variables`, to help distinguish from official Hugo syntax.

CSS classes and IDs use hyphens like `custom-class`.

Naming should be as short and explicit as possible. A variable assigned from the result of a boolean test should be named `$is_test`, while numbers, strings, dates, arrays (slice), map (dict), and other types should be named appropriately (e.g. singular vs plural, limits, enable vs disable).

Beware of Hugo **Context** and **whitespace trimming** concepts, as they are tricky to get at first. See [Hugo official docs](https://gohugo.io/templates/introduction) as reference.