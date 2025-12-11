---
title: Site and Theme Setup
description: Get started with Hugo and the Trigo Theme.
date: 2020-01-01
authors: FreeCAD
weight: 1
tags:
  - Theme
  - Guide
---


> [!WARNING]
> Trigo Theme is still in active development.
> The following documentation is not yet accurate or up-to-date.
> Have a question or feedback? Feel free to [open an issue](https://github.com/FreeCAD/website)!


## What is the Trigo Theme?

Trigo is a simple, modern, fast, feature-packed and flexible [Hugo][hugo] theme to build static websites for documentation, blogs, portfolios and more.

Hugo is a one of the most popular static site generator. Hugo is a single binary, making it easy to install and run on various platforms. Extremely fast and reliable, it renders a site with thousands of pages in milliseconds.

Trigo is a custom made theme focused on efficiency, flexibility and with a minimal footprint. No extra dependencies are required. A single YAML configuration file and Markdown content is all what is needed. Focus on writing quality content and tweak the theme style if desired.

### Features

- **Responsive Layout and Dark Mode** - Works on all devices: mobile, tablet to desktop. Dark mode is also supported to accommodate various lighting conditions.
- **Fast and Lightweight** - Powered by Hugo, a lightning-fast static-site generator housed in a single binary file, its footprint is minimal. Additional JavaScript features to progressively enhance the user experience are optional and can be disabled easily.
- **Features** - Markdown, syntax highlighting, LaTeX math formulae, diagrams and Shortcodes elements to enrich the content. Table of contents, breadcrumbs, pagination, sidebar navigation and more are all automatically generated if enabled.
- **Multi-language and SEO Ready** - Multi-language sites are made easy with Hugo's multilingual mode. Out-of-the-box support is included for SEO tags, Open Graph, sharing to social media and much more.


> [!NOTE]
> The content below is a placeholder and will be changed soon.


## Start as New Project

There are two main ways to add the Trigo Theme to your Hugo project:

1. **Hugo Modules (Recommended)**: The simplest and recommended method. [Hugo modules](https://gohugo.io/hugo-modules/) let you pull in the theme directly from its online source. Theme is downloaded automatically and managed by Hugo.

2. **Git Submodule**: Alternatively, add Trigo as a [Git Submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules). The theme is downloaded by Git and stored in your project's `themes` folder.

### Setup Trigo as Hugo module

#### Prerequisites

Before starting, you need to have the following software installed:

- [Hugo (extended version)](https://gohugo.io/installation/)
- [Git](https://git-scm.com/)
- [Go](https://go.dev/)

{{% steps %}}

### Initialize a new Hugo site

```shell
hugo new site my-site --format=yaml
```

### Configure Trigo theme via module

```shell
# initialize hugo module
cd my-site
hugo mod init github.com/username/my-site

# add Trigo theme
hugo mod get github.com/FreeCAD/website
```

Configure `hugo.yaml` to use Trigo theme by adding the following:

```yaml
module:
  imports:
    - path: github.com/FreeCAD/website
```

### Create your first content pages

Create new content page for the home page and the documentation page:

```shell
hugo new content/_index.md
hugo new content/docs/_index.md
```

### Preview the site locally

```shell
hugo server --buildDrafts --disableFastRender
```

Your new site preview is available at `http://localhost:1313/`.

{{% /steps %}}

{{< details summary="How to update the Theme?" open="false" >}}

To update all Hugo modules in your project to their latest versions, run the following command:

```shell
hugo mod get -u
```

To update Trigo to the [latest released version](https://github.com/FreeCAD/website/releases), run the following command:

```shell
hugo mod get -u github.com/FreeCAD/website
```

If you want to try the most recent changes before the next release, update the module to the development branch directly (⚠️ may contain unstable/breaking changes):

```shell
hugo mod get -u github.com/FreeCAD/website@main
```

See [Hugo Modules](https://gohugo.io/hugo-modules/use-modules/#update-all-modules) for more details.

{{< /details >}}

---

### Setup Trigo as Git submodule

#### Prerequisites

Before starting, you need to have the following software installed:

- [Hugo (extended version)](https://gohugo.io/installation/)
- [Git](https://git-scm.com/)

{{% steps %}}

### Initialize a new Hugo site

```shell
hugo new site my-site --format=yaml
```

### Add Trigo theme as a Git submodule

Switch to the site directory and initialize a new Git repository:

```shell
cd my-site
git init
```

Then, add Trigo Theme as a Git submodule:

```shell
git submodule add https://github.com/FreeCAD/website.git themes/Trigo
```

Configure `hugo.yaml` to use Trigo Theme by adding the following:

```yaml
theme: Trigo
```

### Create your first content pages

Create new content page for the homepage and the documentation page:

```shell
hugo new content/_index.md
hugo new content/docs/_index.md
```

### Preview the site locally

```shell
hugo server --buildDrafts --disableFastRender
```

Your new site preview is available at `http://localhost:1313/`.

{{% /steps %}}


When using [CI/CD](https://en.wikipedia.org/wiki/CI/CD) for Hugo website deployment, it's essential to ensure that the following command is executed before running the `hugo` command.

```shell
git submodule update --init
```

Failure to run this command results in the theme folder not being populated with Trigo theme files, leading to a build failure.


{{< details summary="How to update the Theme?" open="false" >}}

To update all submodules in your repository to their latest commits, run the following command:

```shell
git submodule update --remote
```

To update Trigo to the latest commit, run the following command:

```shell
git submodule update --remote themes/Trigo
```

See [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for more details.

{{< /details >}}


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
  showCopy: false

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


[hugo]: https://gohugo.io/