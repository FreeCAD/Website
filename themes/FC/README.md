# FC Theme

FC Theme is a forked version of [PaperModX](https://github.com/reorx/hugo-PaperModX) based on [PaperMod](https://github.com/adityatelange/hugo-PaperMod) based on [Paper](https://github.com/nanxiaobei/hugo-paper/). Adding new features, improving code quality and make it easier to read and modify by anyone with basic knowledge of Hugo, HTML and CSS, it is specially developed for the [FreeCAD website](https://www.freecad.org/).

## Theme Overview

The `FC` theme is based on a standard Hugo theme structure: it uses a set of `HTML` wrapping template actions to transform content, data and resources (in `layout` folder), some `CSS` stylesheets and `JavaScript` (in `assets` folder). Translations tables for theme strings are in `i18n` folder. Some SVG icons are available in `data` folder.

## Features

TODO

## Structure

TODO

## Style

The style of the theme is defined in `CSS` stylesheets in `assets/css`. Reusable variables are found in `theme_vars.css` in both `Light` and `Dark` variants. General selectors and properties are in `body.css`. Style for the `Main` content area for both **List** and **Single** pages are defined in `main.css`. The site Header is defined in `header.css` and the site Footer is defined is `footer.css`. The `404.css`, `archive.css` and `term.css` define the style for the Main area of these special pages respectively. The `gallery.css` and `highlight.css` define the style for these particular features. The `media.css` defines the style for different devices and screen sizes via media queries (flex and responsive changes).

## Layouts

Each layout inherits from `layouts/_default/baseof.html` which contains the main structure of the page, including the head and meta tags.

Default layouts use either:

- `list.html` for **List** pages, such as the Homepage `_index.md`, the Releases list, the News list, the Categories lists and the Donate page.

- `single.html` for **Single** pages, such as the Features `index.md`, the Release Notes pages, the News articles, the Community page, the Documentation page and the Contribute page.

- `archives.html` for listing all relevant pages in a section within an `Archives` layout.

- `terms.html` for listing all relevant terms (Tags, Categories) in a page within an `Terms` layout.

To organize the code and avoid duplications, the default layouts may include `partials` depending on the context. A `partial` is just another piece of code that also performs template actions, to keep the code *DRY*.

## Shortcodes

TODO

## Files processing

TODO

## InstantClick integration

[InstantClick](http://instantclick.io/) makes navigation behaves like Single Page Application. It is enabled in the `params.yaml` config:

```yaml
params:
  EnableInstantClick: true
```

## Customize pagniator size

In section or list pages, the paginator size be different from the [global config](https://gohugo.io/templates/pagination/#configure-pagination). Add the `paginate` field in the Front Matter to customize:

```yaml
---
paginate: 6
---
```

## Highlight code with Chroma

FC Theme uses Chroma as per Hugo's [official docs](https://gohugo.io/content-management/syntax-highlighting/), so changing the code highlight is easy.

By default the themes are `github` for light and `dracula` for dark. It can be changed in the main `hugo.yaml` config. Custom code highlight can be specified in the theme `assets/css/highlight.css`.

## Icons

Social icons from [Simple Icons](https://simpleicons.org/)
