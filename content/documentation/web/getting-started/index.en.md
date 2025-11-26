---
title: Getting Started
description: How to get started with the Trigo Theme.
date: 2020-01-01
authors: FreeCAD
weight: 2
tags:
  - Docs
  - Guide
cover:
  image: 4.webp
  caption: "a cover caption"
  alt: "a cover alternative title"
---

> [!WARNING]
> Trigo Theme is still in active development.
> The following documentation is not yet accurate or up-to-date.
> Have a question or feedback? Feel free to [open an issue](https://github.com/FreeCAD/website)!

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
