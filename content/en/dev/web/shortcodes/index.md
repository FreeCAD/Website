---
title: Shortcodes
description: Bundled Trigo Theme and Hugo shortcodes to augment your content with custom stuff.
weight: 4
---


[Hugo Shortcodes](https://gohugo.io/content-management/shortcodes/) are snippets inside your content files calling built-in or custom templates.

Trigo provides a collection of shortcodes to enhance your content. Additional shortcodes are also provided directly by Hugo.

Shortcode syntax include `{{</* */>}}` tags, the shortcode name and optional attributes.


## Details

Trigo shortcode to display a collapsible detail block and renders inner content.

```html {file="markdown"}
{{</* details summary="Details" >}}

This is the content of the details.

Markdown is **supported**.

{{< /details */>}}
```

```html {file="markdown"}
{{</* details summary="Click me to reveal" open="false" >}}

This will be hidden by default.

{{< /details */>}}
```

<u>How it renders:</u>

{{< details summary="Details" >}}

This is the content of the details.

Markdown is **supported**.

{{< /details >}}

{{< details summary="Click me to reveal" open="false" >}}

This will be hidden by default.

{{< /details >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | summary | string | "Details" | | "Click me" |
| 1 | open | bool/string | `true` | | "open" |
| 2 | name | string | *optional* | | "name" |
| 3 | title | string | *optional* | | "title" |
| 4 | id | string | *optional* | | "id" |
| 5 | class | string | *optional* | | "CSS class" |


## Tabs

Trigo shortcode to display content is several tabs.
The `tabs` shortcode renders the inner content with multiple `tab` shortcodes.

````html {file="markdown"}
{{</* tabs >}}

  {{< tab JSON >}}
  **JSON**: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data.
  ```json
  { "hello": "world" }
  ```
  {{< /tab >}}
  {{< tab YAML >}}
  **YAML**: YAML is a human-readable data serialization language.
  ```yaml
  hello: world
  ```
  {{< /tab >}}
  {{< tab TOML >}}
  **TOML**: TOML aims to be a minimal configuration file format that's easy to read due to obvious semantics.
  ```toml
  hello = "world"
  ```
  {{< /tab >}}

{{< /tabs */>}}
````

<u>How it renders:</u>

{{< tabs >}}
  {{< tab JSON >}}
  **JSON**: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data.
  ```json
  { "hello": "world" }
  ```
  {{< /tab >}}
  {{< tab YAML >}}
  **YAML**: YAML is a human-readable data serialization language.
  ```yaml
  hello: world
  ```
  {{< /tab >}}
  {{< tab TOML >}}
  **TOML**: TOML aims to be a minimal configuration file format that's easy to read due to obvious semantics.
  ```toml
  hello = "world"
  ```
  {{< /tab >}}
{{< /tabs >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | "Tab" | | "Tab label" |


## Steps

Trigo shortcode to display a series of steps with numbered bullets..

You can use the Markdown attribute `{class="no-step"}` to prevent a heading from being counted as a step.

> [!WARNING]
> Please note that this shortcode is intended **only for Markdown content**.
> If you put HTML content or other shortcodes as step content, it may not render as expected.

```html {file="markdown"}
{{</* steps >}}

#### Step 1

This is the first step.

#### Step 2

This is the second step.

###### Step subheading {class="no-step"}

This will not be counted as a step.

#### Step 3

This is the third step.

{{< /steps */>}}
```

<u>How it renders:</u>

{{< steps >}}

#### Step 1

This is the first step.

#### Step 2

This is the second step.

###### Step subheading {class="no-step"}

This will not be counted as a step.

#### Step 3

This is the third step.

{{< /steps >}}


## Tree

Trigo shortcode to display a filetree list with inner content/branches/leaves and optional icon and label. Branches are collapsible with nested children (e.g. branches or leaves).

```html {file="markdown"}
{{</* tree label="example" >}}
  {{< branch label="content" >}}
    {{< leaf label="_index.md" >}}
    {{< branch label="docs" state="closed" >}}
      {{< leaf label="_index.md" style="color: red;" >}}
      {{< leaf label="introduction.md" >}}
      {{< leaf label="introduction.fr.md" >}}
    {{< /branch >}}
  {{< /branch >}}
  {{< leaf label="hugo.toml" >}}
{{< /tree */>}}
```

<u>How it renders:</u>

{{< tree label="example" >}}
  {{< branch label="content" >}}
    {{< leaf label="_index.md" >}}
    {{< branch label="docs" state="closed" >}}
      {{< leaf label="_index.md" style="color: red;">}}
      {{< leaf label="introduction.md" >}}
      {{< leaf label="introduction.fr.md" >}}
    {{< /branch >}}
  {{< /branch >}}
  {{< leaf label="hugo.toml" >}}
{{< /tree >}}

### Options

| Parameter | Description |
|-----------|---|
| `label`    | The label of the branch or leaf. |
| `type`    | The type and icon of the branch or leaf. Can be `folder`, `document`, `container`, `group`, `part`, `assembly`, `arrow`, `branch`, `fork`, or `merge`. Default is `folder`. |
| `state`   | The state of the branch: can be `open` or `closed`. Default is `open`. |

**Tree**:

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | *optional* | | "Tree label" |
| 1 | class | string | *optional* | | "CSS class" |
| 2 | style | string | *optional* | | "CSS style" |

**Branch**:

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | *optional* | | "label" |
| 1 | type | string | "folder" | "folder", "document", "container", "group", "part", "assembly", "arrow", "branch", "fork", or "merge" | "type" |
| 2 | state | string | "open" | | "state" |
| 3 | class | string | *optional* | | "CSS class" |
| 4 | style | string | *optional* | | "CSS style" |

**Leaf**:

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | *optional* | | "label" |
| 1 | icon | string | "file" | "file", "body", "feature", "sketch", "item", "element", "leaf", "commit" | "icon" |
| 2 | class | string | *optional* | | "CSS class" |
| 3 | style | string | *optional* | | "CSS style" |



## Carousel

Trigo shortcode to display a carousel of images with drag, scroll support and optional automatic mode.

Specify a directory where all image resources are used for the carousel:

```html {file="markdown"}
{{</* carousel dir="path/to/directory" mode="auto" */>}}
```

Specify a list of images to use with an `images` parameter:

```html {file="markdown"}
{{</* carousel images="1.webp, 2.webp, 3.webp" */>}}
```

Specify a list of images to use:

```html {file="markdown"}
{{</* carousel "1.webp" "2.webp" "3.webp" */>}}
```

The path is relative to the current page bundle. To use resources in the `static` or `assets` directories of the site, prefix the path with a `/` slash. The URL of an external image can be use as well.

<u>How it renders:</u>

{{< carousel dir="dir" mode="auto" images="/FreeCAD-symbol.png" >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| | unnamed | string[] | *optional* | | "1.webp" |
| | images | string | *optional* | | "1.webp, 2.webp" |
| | dir | string | *optional* | | "path/to/dir" |
| | mode | string | "fixed" | | "auto" |
| | duration | int[ms] | 5000 | | 1000 |


## Compare

Trigo shortcode to display two stacked images with a movable vertical clipping path.

Specify two image paths:

```html {file="markdown"}
{{</* compare "1.webp" "2.webp" */>}}
```

The path is relative to the current page bundle. To use resources in the `static` directory of the site, prefix the path with a `/` slash. The URL of an external image can be use as well.

<u>How it renders:</u>

{{< compare "dir/1.webp" "dir/3.webp" >}}


<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| | before/left | string | **required** | | "before.webp" |
| | after/right | string | **required** | | "after.webp" |


## Canvas

Trigo shortcode to display an animated canvas based on a sequence of images with screen, mouse and keyboard controls.

Specify a directory path with the sequence of named images, optionally the animation speed as FPS and a title.

```html {file="markdown"}
{{</* canvas path="frames-dir" fps="12" title="Animation title" */>}}
```

The path is relative to the current page bundle. To use resources in the `static` directory of the site, prefix the path with a `/` slash. External resources (defined from a URL) are not supported at this time. The animation takes the image filenames as order, e.g. `001.webp`, `002.webp` or other named sorted schema.

<u>How it renders:</u>

{{< canvas path="frames" fps="12" title="Press spacebar to animate me! Or grab, scroll and use keyboard arrows too!" >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | path | string | **required** | | "path/to/dir" |
| 1 | fps | int[fps] | 12 | | 1 |
| 2 | title | string | *optional* | | "Canvas title" |


## Button

Trigo shortcode to add a link as a clickable button with optional icon and label.

```html {file="markdown"}
{{</* button url="/news" label="See the latest news" icon="time" */>}}
```

<u>How it renders:</u>

{{< button url="/news" label="See the latest news" icon="time" >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | url | string | **required** | | "news" |
| 1 | label | string | *optional* | | "Button label" |
| 2 | icon | string | *optional* | | "heart" |
| 3 | class | string | *optional* | | "CSS class" |
| 4 | style | string | *optional* | | "CSS style" |


## Merge

Trigo shortcode to link to a git commit or Pull Request (short commit hash or #id).

```html {file="markdown"}
{{</* merge url="https://github.com/user/repo/pull/123" */>}}

{{</* merge "https://gitlab.com/user/repo/-/commit/abcdef123456" */>}}

```

<u>How it renders:</u>

{{< merge url="https://github.com/user/repo/pull/123" >}}

and

{{< merge "https://gitlab.com/user/repo/-/commit/abcdef123456" >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | url | string | **required** | | "https://github.com/user/repo/pull/123" |


## PDF

Trigo shortcode to display an embedded PDF file.

```html {file="markdown"}
{{</* pdf "https://example.com/sample.pdf" */>}}
```

The PDF file can also be located in the project directory and use the relative path.

```html {file="markdown"}
{{</* pdf "path/to/file.pdf" */>}}
```

<u>How it renders:</u>

{{< pdf "https://upload.wikimedia.org/wikipedia/commons/0/0c/Wikimedia_Commons_web_en.pdf" >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | path | string | **required** | | "path/to/file.pdf" |


## Video

Trigo shortcode to display a video with optional poster.

```html {file="markdown"}
{{</* video src="video.mp4" poster="dir/3.webp" */>}}
```

<u>How it renders:</u>

{{< video src="video.mp4" poster="dir/3.webp" >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | src | string | **required** | | "path/to/video.mp4" |
| 1 | poster | string | | | "poster.webp" |


## Peertube

Trigo shortcode to embed a Peertube video.

```html {file="markdown"}
{{</* peertube url="https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" */>}}
```

<u>How it renders:</u>

{{< peertube url="https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" >}}


## YouTube

Hugo built-in shortcode to embed a YouTube video.

```html {file="markdown"}
{{</* youtube id=VIDEO_ID title="My video title" start=30 loading=lazy */>}}
```

<u>How it renders:</u>

{{< youtube id=x5oXSGhK7EY title="My video title" start=30 loading=lazy >}}

For more information, see [Hugo's YouTube Shortcode](https://gohugo.io/content-management/shortcodes/#youtube).


## Code block highlight

Hugo built-in shortcode to highlight a code block.

```text {file=Markdown}
{{</* highlight html >}}

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Example HTML5 Document</title>
        <meta name="description" content="Basic Markdown syntax.">
    </head>
    <body>
        <p>Test</p>
    </body>
</html>

{{< /highlight */>}}
```

<u>How it renders:</u>

{{< highlight html >}}

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Example HTML5 Document</title>
        <meta name="description" content="Basic Markdown syntax.">
    </head>
    <body>
        <p>Test</p>
    </body>
</html>

{{< /highlight >}}


## Collection

Trigo shortcode to display a full-width pages collection, section, or taxonomy term pages with cards.

```html {file="markdown"}
{{</* collection collection="dev" first=3 */>}}
```

<u>How it renders:</u>

{{< collection collection="dev" first=3 >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | collection | string | | | "news" |
| 1 | first | int | 0 | | 1 |
| 2 | taxonomy | string | *optional* | | "categories" |
| 3 | term | string | *optional* | | "event" |
| 4 | sort | string | *optional* | | "date" |
| 5 | reverse | bool | `false` | | `true` |
| 6 | title | string | *optional* | | "Collection title" |
| 7 | title_icon | string | *optional* | | "heart" |
| 8 | title_class | string | *optional* | | "CSS class" |
| 9 | title_style | string | *optional* | | "CSS style" |


## Block

Trigo shortcode to display a full-width block layout container with custom inner content.

Use the `{{</* group */>}}` shortcode to nest and group related content into vertical columns.

```html {file="markdown"}
{{</* block title="My Title" style="background: linear-gradient(135deg, var(--accent-hover), var(--accent));" */>}}

{{</* group */>}}

This is **Markdown** content between `block` and `group` shortcode tags.

| Style       | Syntax          | Example output           |
| ----------- | --------------- | ------------------------ |
| Bold        | `**bold**`      | Some **bold** text       |
| Italic      | `*italic*`      | Some *italic* text       |
| Mark        | `==mark==`      | Some ==marked== text.    |
| Deleted     | `~~deleted~~`   | Some ~~deleted~~ text    |
| Inserted    | `++inserted++`  | Some ++inserted++ text   |
| Subscript   | `~subscript~`   | Some ~subscript~ text.   |
| Superscript | `^superscript^` | Some ^superscript^ text. |

 Images can be added too:

{{</* /group */>}}

![](/FreeCAD-symbol.png)

{{</* /block */>}}
```

<u>How it renders:</u>

{{< block title="My Title" style="background: linear-gradient(135deg, var(--accent-hover), var(--accent));" >}}

{{< group >}}

This is **Markdown** content between `block` and `group` shortcode tags.

| Style       | Syntax          | Example output           |
| ----------- | --------------- | ------------------------ |
| Bold        | `**bold**`      | Some **bold** text       |
| Italic      | `*italic*`      | Some *italic* text       |
| Mark        | `==mark==`      | Some ==marked== text.    |
| Deleted     | `~~deleted~~`   | Some ~~deleted~~ text    |
| Inserted    | `++inserted++`  | Some ++inserted++ text   |
| Subscript   | `~subscript~`   | Some ~subscript~ text.   |
| Superscript | `^superscript^` | Some ^superscript^ text. |

 Images can be added too:

{{< /group >}}

![](/FreeCAD-symbol.png)

{{< /block >}}

<u>Attributes:</u>

| Position | Attribute | Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | content | string | `InnerDeindent` | | "**Markdown** *content*" |
| 1 | title | string | *optional* | | "Block title" |
| 2 | class | string | *optional* | | "CSS block class" |
| 3 | style | string | *optional* | | "CSS block style" |
| 4 | title_class | string | *optional* | | "CSS title class" |
| 5 | title_style | string | *optional* | | "CSS title style" |
| 6 | content_class | string | *optional* | | "CSS content class" |
| 7 | content_style | string | *optional* | | "CSS content style" |