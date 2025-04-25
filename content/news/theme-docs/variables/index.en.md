---
title: "Variables | Front Matter"
description: "List of Front Matter variables used by FC Theme"
date: 2021-01-20
author: "FreeCAD"
draft: false
cover:
  image: 7.webp
  caption: "a cover caption"
  alt: "a cover alternative title"
---

**Below are variables used with this theme...**

---

### Site Variables under `Params`

| name                                   | type          | example                  | Description                                                                               |
| -------------------------------------- | ------------- | ------------------------ | ----------------------------------------------------------------------------------------- |
| `env`                                  | string        | "production"             | To set env to production                                                                  |
| `title`                                | string        | "My Blog"                | To set title                                                                              |
| `description`                          | string        | "This is a blog of mine" | To set site description                                                                   |
| `author`                               | string \|list | "Me" \| ["Me","You"]     | To show multiple Authors                                                                  |
| `images`                               | string        | "myimage.webp"            | Link or path of image for opengraph                                        |
| `keywords`                             | list          | [blog, page]             | Add keywords for Home page                                                                |
| `DateFormat`                           | string        | January 2, 2006        | The format of date strings in the website. [Details](https://gohugo.io/functions/format/) |
| `languageAltTitle`                     | string        | English                | Alternate title in Multilingual Mode                                                      |
| `ShowReadingTime`                      | boolean       | true \| false            | To show read time in post meta                                                            |
| `ShowShareButtons`                     | boolean       | true \| false            | To show/hide share buttons under post                                                     |
| `ShowCopyCodeButton`                  | boolean       | true \| false            | To show/hide Code Copy button                                                             |
| `defaultTheme`                         | string        | light \| dark \| auto    | To set default theme                                                                      |
| `disableThemeToggle`                   | boolean       | true \| false            | To disable theme toggle icon shown besides label                                          |
| `hideSummary`                          | boolean       | true \| false            | To Hide summary being shown in list pages                                                 |
| `ShowPaginationLinks`                     | boolean       | true \| false            | Show Previous and Next Posts below a Post                                                 |
| `analytics.google.SiteVerificationTag` | string        | XYZabc                 | Site Verification Tag for Google Analytics                                                |
| `schema`                               | -             | -                        | [Details](#schema)                                                                        |
| `label`                                | -             | -                        | [Details](#label)                                                                         |
| `assets`                               | -             | -                        | [Details](#assets)                                                                        |
| `editPost`                             | -             | -                        | [Details](#editPost)                                                                      |

### Site Variables

| name        | type   | example                                    | Description                                                                                                                   |
| ----------- | ------ | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `copyright` | string | `**[example.site](https://example.site)**` | This is [HUGO's site variable](https://gohugo.io/variables/site/#site-variables-list), which can also render markdown content |

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


---

### Page Variables

| Name                      | Type          | Example                         | Description                                                                         |
| ------------------------- | ------------- | ------------------------------- | ----------------------------------------------------------------------------------- |
| `description`             | string        | "description text"              | Show Post Description under Title                                                   |
| `disableShare`            | boolean       | true \| false                   | To hide/show share icons under a page                                               |
| `hideSummary`             | boolean       | true \| false                   | To Hide summary being shown in list pages                                           |
| `ShowReadingTime`         | boolean       | true \| false                   | To show read time in post meta                                                      |
| `ShowPaginationLinks`        | boolean       | true \| false                   | Show Previous and Next Posts below a Post                                           |
| `author`                  | string \|list | "Me" \| ["Me","You"]            | To show multiple Authors                                                            |
| `cover.image`             | string        | "featured.jpg"                  | To add a cover image                                                                |
| `cover.caption `          | string        | "caption for image"             | To add caption to cover image                                                       |
| `cover.alt`               | string        | "this is cover image"           | Alternate text to show if image doesn't load/show up                                |
| `weight `                 | integer       | 5                               | To set page order or to pin a post to Top of list                                   |
