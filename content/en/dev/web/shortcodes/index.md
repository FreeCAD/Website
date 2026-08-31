---
title: Shortcodes
description: Bundled Trigo Theme and Hugo shortcodes to enhance content.
weight: 5
---


> Shortcodes are special code snippets inside your Markdown content files calling built-in or custom templates.
>
> They allow to add specialized content to pages or format their layout with ease.

The Trigo theme provides several custom shortcodes detailed below.

> [!NOTE]
> Additional shortcodes are also provided directly by Hugo.
>
> See the [built-in Hugo shortcodes list](https://gohugo.io/content-management/shortcodes/#embedded) on its official documentation.

Shortcodes require the special `{{</* */>}}` tags, the shortcode name and optional arguments.
Some shortcodes only require one tag, while others need both opening and closing tags with Markdown content in-between.
Some shortcodes can even be nested, allowing for complex content and layout.
Most shortcodes support both named and positional arguments.

See the examples below to understand their use cases, structure, and syntax.


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

<u>`details` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | summary | string | "Details" | | "Click me" |
| 1 | open | bool | `true` | | `false` |
| 2 | name | string | *optional* | | "name" |
| 3 | title | string | *optional* | | "title" |
| 4 | id | string | *optional* | | "id" |
| 5 | css_class | string | *optional* | | CSS class |


## Tabs and tab

Trigo shortcode to display content in multiple tabs.
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

<u>`tab` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | "Tab" | | "Tab label" |


## Steps

Trigo shortcode to display a series of numbered steps based on headings.

You can use the Markdown attribute `{class="no-step"}` to prevent a heading from being counted as a step.

> [!IMPORTANT]
> Please note that this shortcode is intended **for Markdown content only**.
> HTML or other shortcodes as step content may not render as expected.

```html {file="markdown"}
{{</* steps >}}

## Step 1

This is the first step.

### Step 2

This is the second step.

#### Step subheading {class="no-step"}

This will not be counted as a step.

### Step 3

- Item 1
- Item 2
- Item 3

{{< /steps */>}}
```

<u>How it renders:</u>

{{< steps >}}

## Step 1

This is the first step.

### Step 2

This is the second step.

#### Step subheading {class="no-step"}

This will not be counted as a step.

### Step 3

- Item 1
- Item 2
- Item 3

{{< /steps >}}


## Tree, branch and leaf

Trigo shortcode to display a filetree list with inner content/branches/leaves and optional icon and label. Branches are collapsible with nested children (e.g. branches or leaves).

```html {file="markdown"}
{{</* tree label="example" >}}
  {{< branch label="content" >}}
    {{< leaf label="_index.md" >}}
    {{< branch label="docs" state="closed" >}}
      {{< leaf label="_index.md" css_class="pastel1" >}}
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
      {{< leaf label="_index.md" css_class="pastel1" >}}
      {{< leaf label="introduction.md" >}}
      {{< leaf label="introduction.fr.md" >}}
    {{< /branch >}}
  {{< /branch >}}
  {{< leaf label="hugo.toml" >}}
{{< /tree >}}

<u>`tree` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | *optional* | | "Tree label" |
| 1 | css_class | string | *optional* | custom CSS classes | "accent" |

<u>`branch` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | *optional* | | "Branch label" |
| 1 | icon | string | "folder" | "folder", "document", "container", "group", "part", "assembly", "arrow", "branch", "fork", "pr", or "versions" | "group" |
| 2 | state | string | "open" | | "state" |
| 3 | css_class | string | *optional* | custom CSS classes | "accent" |

<u>`leaf` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | *optional* | | "Leaf label" |
| 1 | icon | string | "file" | "file", "body", "feature", "sketch", "item", "element", "leaf", "commit" | "item" |
| 2 | css_class | string | *optional* | custom CSS classes | "accent" |


## Carousel

Trigo shortcode to display a carousel of images with drag, scroll support and optional automatic mode.

Use either `dir`, `images`, or positional image arguments. Do not combine them.

Directory where all image resources are used for the carousel:

```html {file="markdown"}
{{</* carousel dir="path/to/directory" mode="auto" */>}}
```

List of images to use with an `images` parameter:

```html {file="markdown"}
{{</* carousel images="1.webp, 2.webp, 3.webp" */>}}
```

Images as positional arguments:

```html {file="markdown"}
{{</* carousel "1.webp" "2.webp" "3.webp" */>}}
```

The path is relative to the current page bundle. To use resources in the `static` or `assets` directories of the site, prefix the path with a `/` slash. External image URLs are also supported.

<u>How it renders:</u>

{{< carousel dir="dir" mode="auto" >}}

<u>`carousel` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| | unnamed | string[] | *optional* | | "1.webp" |
| | images | string | *optional* | | "1.webp, 2.webp" |
| | dir | string | *optional* | | "path/to/dir" |
| | mode | string | "fixed" | "fixed" or "auto" | "auto" |
| | duration | int[ms] | 5000 | | 1000 |


## Compare

Trigo shortcode to display two stacked images with a movable vertical clipping path.

Specify two image paths:

```html {file="markdown"}
{{</* compare "1.webp" "2.webp" */>}}
```

The path is relative to the current page bundle. To use resources in the `static` directory of the site, prefix the path with a `/` slash. External image URLs are also supported.

<u>How it renders:</u>

{{< compare "dir/1.webp" "dir/3.webp" >}}


<u>`compare` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| | before (alias: left) | string | **required** | | "before.webp" |
| | after (alias: right) | string | **required** | | "after.webp" |


## Canvas

Trigo shortcode to display an animated canvas based on a sequence of images with screen, mouse and keyboard controls.

Specify a directory path with the sequence of named images, optionally the animation speed as FPS and a title.

```html {file="markdown"}
{{</* canvas path="frames-dir" fps="12" title="Animation title" */>}}
```

The path is relative to the current page bundle. To use resources in the `static` directory of the site, prefix the path with a `/` slash. External resources (defined from a URL) are not supported at this time. Frames are ordered lexicographically by filename, e.g. `001.webp`, `002.webp`.

<u>How it renders:</u>

{{< canvas path="frames" fps="12" title="Press spacebar to animate me! Or grab, scroll and use keyboard arrows too!" >}}

<u>`canvas` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | path | string | **required** | | "path/to/dir" |
| 1 | fps | int[fps] | 12 | | 1 |
| 2 | title | string | *optional* | | "Canvas title" |


## Button

Trigo shortcode to add a link as a clickable button with optional icon and label.

```html {file="markdown"}
{{</* button url="/news" label="Button label" icon="time" */>}}
```

<u>How it renders:</u>

{{< button url="/news" label="Button label" icon="time" >}}

<u>`button` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | url | string | **required** | | "/news" |
| 1 | label | string | *optional* | | "Button label" |
| 2 | icon | string | *optional* | | "heart" |
| 3 | css_class | string | *optional* | custom CSS classes | "button-accent" |


## Marker

Trigo shortcode to add a marker with optional icon and label.

```html {file="markdown"}
{{</* marker label="Marker label" icon="heart" */>}}
```

<u>How it renders:</u>

{{< marker label="Marker label" icon="heart" >}}

<u>`button` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | label | string | *optional* | | "Marker label" |
| 1 | icon | string | *optional* | | "heart" |
| 2 | css_class | string | *optional* | custom CSS classes | "accent" |


## Git

Trigo shortcode to link to a git commit or pull request (short commit hash or #id respectively).

```html {file="markdown"}
A git commit: {{</* git "https://gitlab.com/user/repo/-/commit/abcdef123456" */>}},

and a pull request: {{</* git url="https://github.com/user/repo/pull/123" */>}}.
```

<u>How it renders:</u>

A commit: {{< git "https://gitlab.com/user/repo/-/commit/abcdef123456" >}},

and a pull request: {{< git url="https://github.com/user/repo/pull/123" >}}.

<u>`merge` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
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

<u>`pdf` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | path | string | **required** | | "path/to/file.pdf" |
| 1 | title | string | *optional* | | "My PDF document" |


## Video

Trigo shortcode to display a video with optional poster.

```html {file="markdown"}
{{</* video src="video.mp4" poster="dir/3.webp" */>}}
```

<u>How it renders:</u>

{{< video src="video.mp4" poster="dir/3.webp" >}}

<u>`video` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | src | string | **required** | | "path/to/video.mp4" |
| 1 | poster | string | | | "poster.webp" |


## Peertube

Trigo shortcode to embed a Peertube video.

```html {file="markdown"}
{{</* peertube url="https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" */>}}
```

You can optionally specify a start and/or stop time.

```html {file="markdown"}
{{</* peertube url="https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" start="30s" stop="2m15s" */>}}
```

<u>How it renders:</u>

{{< peertube url="https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" >}}

<u>`peertube` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | url | string | **required** | | "https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" |
| 1 | start | string  | *optional* | | "30s" |
| 2 | stop | string  | *optional* | | "2m15s" |
| 3 | width | int[px] | 0=responsive | | 1280 |
| 4 | autoplay | boolean | `false` | | `true` |
| 5 | mute | boolean | `false` | | `true` |

By default, videos are displayed responsively, lazy-loaded, and allow fullscreen playback.


## YouTube

Hugo built-in shortcode to embed a YouTube video.

```html {file="markdown"}
{{</* youtube id=a9biWv_M8p8 title="My video title" start=30 loading=lazy */>}}
```

<u>How it renders:</u>

{{< youtube id=a9biWv_M8p8 title="My video title" start=30 loading=lazy >}}

For more information, see [Hugo's YouTube shortcode](https://gohugo.io/shortcodes/youtube/).


## Vimeo

Hugo built-in shortcode to embed a Vimeo video.

```html {file="markdown"}
{{</* vimeo id=19899678 loading=lazy title="Barn Owl" */>}}
```

<u>How it renders:</u>

{{< vimeo id=19899678 loading=lazy title="Barn Owl" >}}

For more information, see [Hugo's Vimeo shortcode](https://gohugo.io/shortcodes/vimeo/).


## Card

Trigo shortcode to display an internal page card.

```html {file="markdown"}
{{</* card url="thanks" */>}}
```

<u>How it renders:</u>

{{</* card url="thanks" */>}}

<u>`card` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | url | string | | | "thanks" |


## Collection

Trigo shortcode to display a full-width layout with a collection of pages as cards. These pages come from a section, a specific taxonomy term or are part of a taxonomy.

```html {file="markdown"}
{{</* collection collection="dev" first=3 css_class="gradient" */>}}
```

<u>How it renders:</u>

{{< collection collection="dev" first=3 css_class="gradient" >}}

<u>`collection` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | collection | string | | | "news" |
| 1 | first | int | 0 | | 1 |
| 2 | taxonomy | string | *optional* | | "categories" |
| 3 | term | string | *optional* | | "event" |
| 4 | sort | string | *optional* | | "date" |
| 5 | reverse | bool | `false` | | `true` |
| 6 | css_class | string | *optional* | custom CSS classes | "gradient" |


## Block and group

Trigo shortcode to display a full-width layout block container with custom inner content.

Use the `{{</* group */>}}` shortcode to nest and group related content into vertical columns within a block.

```html {file="markdown"}
{{</* block title="My Title" css_class="section" */>}}

{{</* group */>}}

This is **Markdown** *content* between `block` and `group` shortcode tags.

| Format      | Syntax          | Example output           |
| ----------- | --------------- | ------------------------ |
| Bold        | `**bold**`      | Some **bold** text       |
| Italic      | `*italic*`      | Some *italic* text       |
| Mark        | `==mark==`      | Some ==marked== text.    |
| Deleted     | `~~deleted~~`   | Some ~~deleted~~ text    |
| Inserted    | `++inserted++`  | Some ++inserted++ text   |
| Subscript   | `~subscript~`   | Some ~subscript~ text.   |
| Superscript | `^superscript^` | Some ^superscript^ text. |

> [!TIP]
> - Content such as images and other shortcodes can be added as well
> - Each individual HTML block-level element (e.g. heading, paragraph, figure, list, quote) form a "sub-block" and creates its own vertical layout.
> - Use the `group` shortcode to group them vertically and control the flow.

{{</* button url="https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout" label="Reference: Block and inline layout in normal flow" icon="tip" */>}}

{{</* /group */>}}

![](/FreeCAD-symbol.webp)

{{</* /block */>}}
```

<u>How it renders:</u>

{{< block title="My Title" css_class="section" >}}

{{< group >}}

This is **Markdown** *content* between `block` and `group` shortcode tags.

| Format      | Syntax          | Example output           |
| ----------- | --------------- | ------------------------ |
| Bold        | `**bold**`      | Some **bold** text       |
| Italic      | `*italic*`      | Some *italic* text       |
| Mark        | `==mark==`      | Some ==marked== text.    |
| Deleted     | `~~deleted~~`   | Some ~~deleted~~ text    |
| Inserted    | `++inserted++`  | Some ++inserted++ text   |
| Subscript   | `~subscript~`   | Some ~subscript~ text.   |
| Superscript | `^superscript^` | Some ^superscript^ text. |

> [!TIP]
> - Content such as images and other shortcodes can be added as well
> - Each individual HTML block-level element (e.g. heading, paragraph, figure, list, quote) form a "sub-block" and creates its own vertical layout.
> - Use the `group` shortcode to group them vertically and control the flow.

{{< button url="https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout" label="Reference: Block and inline layout in normal flow" icon="tip" >}}

{{< /group >}}

![](/FreeCAD-symbol.webp)

{{< /block >}}

<u>`block` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | content | string | `InnerDeindent` | | Note: Place **Markdown** *content* inside block tags |
| 1 | title | string | *optional* | | "Block title" |
| 2 | css_class | string | *optional* | custom CSS classes | "section" |
| 3 | title_class | string | *optional* | custom CSS classes | "accent" |
| 4 | content_class | string | *optional* | custom CSS classes | "accent" |

<u>`group` arguments:</u>

| Position | Argument| Type | Default | Options | Example value |
| --- | --- | --- | --- | --- | --- |
| 0 | content | string | `InnerDeindent` | | Note: Place **Markdown** *content* inside group tags |
| 1 | css_class | string | *optional* | custom CSS classes | "accent" |
