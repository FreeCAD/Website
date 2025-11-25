---
title: "Installation | Update"
description: "Read Install and Update instructions here"
date: 2021-01-20
authors: FreeCAD
cover:
  image: 3.webp
  caption: "a cover caption"
  alt: "a cover alternative title"
---

## Intro

- **We'll be using `yml/yaml` format for all examples down below, I recommend using `yml` over `toml` as it is easier to read.**
- You can find any [YML to TOML](https://www.google.com/search?q=yml+to+toml) converters if necessary.

## Guide

Follow [Quick Start](https://gohugo.io/getting-started/quick-start/) guide to setup hugo and create a new site.

> Note: Use -f to select yml format
>
> `hugo new site <name of site> -f yml`

Make sure you install latest version of **`hugo`**.

After you have created a new site, at [Step 3](https://gohugo.io/getting-started/quick-start) follow the steps:

### Method 1

Inside the folder of your Hugo site, run:

```bash
git clone https://github.com/FreeCAD/website PATH_TO_YOUR_LOCAL_GIT_DIRECTORY --depth=1
```

> Updating theme :
>
> ```bash
> cd PATH_TO_YOUR_LOCAL_GIT_DIRECTORY
> git pull
> ```

### Method 2

Or you can Download as Zip from Github Page and extract in your themes directory

### Finally ...

Add in `config.yml`:

```yml
theme: Trigo
```
### Method 4

- Install [Go programming language](https://go.dev/doc/install) in your operating system.

- Intialize your own hugo mod

```
hugo mod init PATH_TO_YOUR_LOCAL_GIT_DIRECTORY
```

- Add Trigo Theme in your `config.yml` file

```
module:
  imports:
  - path: github.com/FreeCAD/website/tree/main/themes/Trigo
```
- Update theme

```
hugo mod get -u
```

## Sample `config.yml`

**Use appropriately**

```yml
baseURL: https://examplesite.com/
title: "ExampleSite"
paginate: 6
theme: Trigo

enableRobotsTXT: true
buildDrafts: false
buildFuture: false
buildExpired: false
pygmentsUseClasses: true

googleAnalytics: UA-123-45

minify:
  disableXML: true
  minifyOutput: true

params:
  env: production # to enable google analytics, opengraph and schema.
  title: "ExampleSite"
  description: "ExampleSite description"
  keywords: [Blog, Portfolio]
  authors: [Me, You, Tom Sawyer]
  images: [<link or path of image for opengraph>]
  DateFormat: January 2, 2006
  defaultChroma: auto # dark, light

  showReadingTime: true
  showShareButtons: true
  showPagination: true
  showCopyCodeButton: false

  label:
    text: Home
    icon: /apple-touch-icon.webp
    iconHeight: 35

  analytics:
    google:
      SiteVerificationTag: XYZabc
```

## Sample `Page.md`

```yml
---
title: "My first post"
date: 2020-09-15T11:30:03+00:00
# weight: 1
# aliases: [/first]
tags: [first]
authors: [Me, You, Tom Sawyer]

draft: false
description: "Desc Text."
disableShare: false
showReadingTime: true
showPagination: true
cover:
  image: <image path/url> # image path/url
  alt: <alt text> # alt text
  caption: <text> # display caption under cover
---
```

You can use it by creating `archetypes/post.md`

```shell
hugo new --kind post <name>
```