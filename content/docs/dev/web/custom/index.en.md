---
title: Customization
description: How to customize the Trigo Theme.
date: 2020-01-01
authors: FreeCAD
weight: 7
tags:
  - Config
  - Theme
  - Guide
---


> [!NOTE]
> The content below is a placeholder and will be changed soon.


The Trigo Theme defines its own defaults and offers options to further customize the theme.
Cascading Style Sheets (CSS) Variables are used throughout the theme and can be easily overridden.


## Font Family

The font family of the content can be customized using:

```css {file="assets/css/theme_vars.css"}
:root {
  --sans: Arial, Verdana, BlinkMacSystemFont, Helvetica, 'Helvetica Neue', 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', sans-serif;
  --mono: "Lucida Console", Monaco, "Consolas", monospace;
}
```


## Text Size

The size of the text can be customized using:

```css {file="assets/css/theme_vars.css"}
:root {
/* Variables for text sizes: small (terms, footnotes), medium (normal text), large (h3), extra large (h2), extra extra large (h1) */
  --s: 0.75rem;
  --m: 1rem;
  --l: 1.5rem;
  --xl: 2.25rem;
  --xxl: 3.5rem;
}
```


## Primary Colors

The primary colors can be customized using:

```css {file="assets/css/theme_vars.css"}
:root {
  --primary-hue: 100deg;
  --primary-saturation: 90%;
  --primary-lightness: 50%;
}
```


## Element Sizes

The size of the main page elements such as content blocks, hero, navbar and other can be customized using:

```css {file="assets/css/theme_vars.css"}
:root {
  --content-width: 90ch;
}
```


## Syntax Highlighting

List of available syntax highlighting themes are available at [Chroma Styles Gallery](https://xyproto.github.io/splash/docs/all.html). The stylesheet can be generated using the command:

```shell
hugo gen chromastyles --style=github
```

To override the default syntax highlighting theme, we can add the generated styles to the custom CSS file.


## Custom Layouts

The layouts of the theme can be overridden by creating a file with the same name in the `layouts` directory of your site.
For example, to override the `single.html` layout for docs, create a file `layouts/docs/single.html` in your site.

For further information, refer to the [Hugo Templates][hugo-template-docs].


## Further Customization

Didn't find what you were looking for? Feel free to [open a discussion](https://github.com/FreeCAD/website/discussions) or make a contribution to the theme!

[hugo-template-docs]: https://gohugo.io/templates/


---


## List of Site and Front Matter variables used by Trigo Theme


## Site Variables under `Params`

| name                                   | type          | example                  | Description                                                                               |
| -------------------------------------- | ------------- | ------------------------ | ----------------------------------------------------------------------------------------- |
| `env`                                  | string        | "production"             | To set env to production                                                                  |
| `title`                                | string        | "My Blog"                | To set title                                                                              |
| `description`                          | string        | "This is a blog of mine" | To set site description                                                                   |
| `author`                               | string \|list | "Me" \| ["Me","You"]     | To show multiple Authors                                                                  |
| `images`                               | string        | "myimage.webp"            | Link or path of image for opengraph                                        |
| `keywords`                             | list          | [blog, page]             | Add keywords for Home page                                                                |
| `DateFormat`                           | string        | January 2, 2006        | The format of date strings in the website. [Details](https://gohugo.io/methods/time/format/) |
| `languageAltTitle`                     | string        | English                | Alternate title in Multilingual Mode                                                      |
| `showReadingTime`                      | boolean       | true \| false            | To show read time in post meta                                                            |
| `showShareButtons`                     | boolean       | true \| false            | To show/hide share buttons under post                                                     |
| `showCopy`                  | boolean       | true \| false            | To show/hide Code Copy button                                                             |
| `defaultChroma`                         | string        | light \| dark \| auto    | To set default theme                                                                      |
| `showPagination`                     | boolean       | true \| false            | Show Previous and Next Posts below a Post                                                 |
| `analytics.google.SiteVerificationTag` | string        | XYZabc                 | Site Verification Tag for Google Analytics                                                |
| `schema`                               | -             | -                        | [Details](#schema)                                                                        |
| `label`                                | -             | -                        | [Details](#label)                                                                         |
| `assets`                               | -             | -                        | [Details](#assets)                                                                        |
| `editPost`                             | -             | -                        | [Details](#editPost)                                                                      |

### Site Variables

| name        | type   | example                                    | Description                                                                                                                   |
| ----------- | ------ | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `copyright` | string | `**[example.site](https://example.site)**` | This is [HUGO's site variable](https://gohugo.io/methods/site/), which can also render markdown content |

#### label

| name               | type    | example                 | Description                                      |
| ------------------ | ------- | ----------------------- | ------------------------------------------------ |
| `label.text`       | string  | "Home"                  | To display different label text other than title |
| `label.icon`       | string  | "/apple-touch-icon.webp" | To display a logo image in label                 |
| `label.iconHeight` | integer | 35                      | To set size of label logo image                  |

#### cover

| name                     | type    | example       | Description                                             |
| ------------------------ | ------- | ------------- | ------------------------------------------------------- |
| `cover.linkFullImages`   | boolean | true \| false | To open full size cover images on click on cover        |
| `cover.responsiveImages` | boolean | true \| false | To enable/disable generation of responsive cover images |

#### schema

| name                   | type   | example          | Description                   |
| ---------------------- | ------ | ---------------- | ----------------------------- |
| `schema.publisherType` | string | "Organization"   | https://schema.org/publisher  |
| `schema.sameAs`        | list   | [URL1, URL2] | Set https://schema.org/sameAs |


## Page Variables

| Name                      | Type          | Example                         | Description                                                                         |
| ------------------------- | ------------- | ------------------------------- | ----------------------------------------------------------------------------------- |
| `description`             | string        | "description text"              | Show Post Description under Title                                                   |
| `disableShare`            | boolean       | true \| false                   | To hide/show share icons under a page                                               |
| `showReadingTime`         | boolean       | true \| false                   | To show read time in post meta                                                      |
| `showPagination`        | boolean       | true \| false                   | Show Previous and Next Posts below a Post                                           |
| `author`                  | string \|list | "Me" \| ["Me","You"]            | To show multiple Authors                                                            |
| `cover.image`             | string        | "featured.jpg"                  | To add a cover image                                                                |
| `cover.caption `          | string        | "caption for image"             | To add caption to cover image                                                       |
| `cover.alt`               | string        | "this is cover image"           | Alternate text to show if image doesn't load/show up                                |
| `weight `                 | integer       | 5                               | To set page order or to pin a post to Top of list                                   |
