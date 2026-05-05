---
title: Structure and organization
description: How to organize the website files.
weight: 2
---


## Directory Structure

By default, Hugo searches for Markdown files in the `content` directory, and the structure of the directory determines the final output structure of your website.

Take this site as an example:

{{< tree >}}
  {{< branch label="content" >}}
    {{< leaf label="_index.md  ← /" >}}
    {{< branch label="docs" state="open" >}}
      {{< leaf label="_index.md  ← /docs/" >}}
      {{< branch label="getting-started" >}}
        {{< leaf label="index.md  ← /docs/getting-started/" >}}
      {{< /branch >}}
      {{< branch label="guide" >}}
        {{< leaf label="_index.md  ← /docs/guide/" >}}
        {{< leaf label="organize-files.md  ← /docs/guide/organize-files/" >}}
      {{< /branch >}}
    {{< /branch >}}
    {{< branch label="blog" state="open" >}}
      {{< leaf label="_index.md  ← /blog/" >}}
      {{< leaf label="post.md  ← /blog/post/" >}}
      {{< branch label="article" >}}
        {{< leaf label="index.md  ← /docs/article/" >}}
      {{< /branch >}}
    {{< /branch >}}
  {{< /branch >}}
{{< /tree >}}

Each `_index.md` file is the index page for the corresponding section. The other Markdown files are regular pages, placed directly in the section directory, or nested in their own sub-directory.

### Configure Content Directory

By default, the root `content/` directory is used by Hugo to build the site.
If you need to use a different directory for content, for example `docs/`, this can be done by setting the [`contentDir`](https://gohugo.io/getting-started/configuration/#contentdir) parameter in the site configuration `hugo.yaml`.


## Add resources

To add resources such as images, videos, and more, the easiest way is to place these files in the same directory as the Markdown file.

For example, add an image file `image.webp` alongside the `my-page.md` file:

{{< tree >}}
  {{< branch label="content" >}}
    {{< branch label="section" >}}
        {{< leaf label="my-page.md" >}}
        {{< leaf label="image.webp" >}}
    {{< /branch >}}
  {{< /branch >}}
{{< /tree >}}

Then, can use the following Markdown syntax to add the image to the content:

```markdown {file="content/section/my-page.md"}
![alt](image.webp "title")
```

### Page bundles

The [page bundles][page-bundles] feature of Hugo allows to organize resource files together with the Markdown file. To achieve that, turn the `my-page.md` file into a directory `my-page` and put the content into a file named `index.md`, and put the resource files inside the `my-page` directory.

> [!NOTE]
> For the FreeCAD website, page bundles are used, so it is easier to organize large amount of content and resources in a nested structure.
>
> Additionally, each language is organized into its own root content directory (e.g `/content/en/section`, `/content/fr/section`, etc). Resources only need to go into the default language site (`en` for English), as other languages are linked automatically.
>
> The strategy illustrated below (e.g. `index.en.md`) is currently not used.

For multi-lingual sites, it is also possible to organize translated content in the same directory with the language code in the file name.

{{< tree >}}
  {{< branch label="content" >}}
    {{< branch label="section" >}}
        {{< branch label="my-page" >}}
            {{< leaf label="index.en.md" >}}
            {{< leaf label="index.fr.md" >}}
            {{< leaf label="image.webp" >}}
        {{< /branch >}}
    {{< /branch >}}
  {{< /branch >}}
{{< /tree >}}

```markdown {file="content/section/my-page/index.en.md"}
![alt](image.webp "title")
```

### Static and Assets

Alternatively, it is possible to place resources in the `static` and `assets` root directories, which will make the resources available for all pages:

{{< tree >}}
  {{< branch label="static" >}}
    {{< branch label="images" >}}
        {{< leaf label="image.webp" >}}
    {{< /branch >}}
  {{< /branch >}}
  {{< branch label="content" >}}
    {{< branch label="section" >}}
        {{< leaf label="my-page.md" >}}
    {{< /branch >}}
  {{< /branch >}}
{{< /tree >}}

> [!NOTE]
> The path for a resource in the static directory begins with a slash `/`.

```markdown {file="content/section/my-page.md"}
![alt](/images/image.webp "title")
```

[page-bundles]: https://gohugo.io/content-management/page-bundles/#leaf-bundles
