---
title: Shortcodes
description: Bundled Trigo Theme and Hugo shortcodes to augment your content with custom stuff.
weight: 6
cover:
  image: 2.webp
  caption: "a cover caption"
  alt: "a cover alternative title"
---

[Hugo Shortcodes](https://gohugo.io/content-management/shortcodes/) are snippets inside your content files calling built-in or custom templates.

Trigo provides a collection of shortcodes to enhance your content. Additional shortcodes are provided directly by Hugo (see the last ones).


## Details shortcode

Trigo shortcode to display a collapsible content.

### Example

{{< details summary="Details" >}}

This is the content of the details.

Markdown is **supported**.

{{< /details >}}

{{< details summary="Click me to reveal" open="false" >}}

This will be hidden by default.

{{< /details >}}

### Usage

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


## Tabs shortcode

Trigo shortcode to display content is several tabs.

### Example

{{< tabs >}}
  {{< tab JSON >}}
  **JSON**: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax.
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

### Usage

````html {file="markdown"}
{{</* tabs >}}

  {{< tab JSON >}}
  **JSON**: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax.
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


## Steps shortcode

Trigo shortcode to display a series of steps.

You can use the Markdown attribute `{class="no-step"}` to prevent a heading from being counted as a step.

### Example

{{% steps %}}

#### Step 1

This is the first step.

#### Step 2

This is the second step.

###### Step subheading {class="no-step"}

This will not be counted as a step.

#### Step 3

This is the third step.

{{% /steps %}}

### Usage

> [!WARNING]
> Please note that this shortcode is intended **only for Markdown content**.
> If you put HTML content or other shortcodes as step content, it may not render as expected.

```html {file="markdown"}
{{%/* steps %}}

#### Step 1

This is the first step.

#### Step 2

This is the second step.

###### Step subheading {class="no-step"}

This will not be counted as a step.

{{% /steps */%}}
```


## Tree shortcode

Trigo shortcode to display a filetree with branches and leaves.

### Example

{{< tree name="example" style="border: var(--border);" >}}
  {{< branch name="content" >}}
    {{< leaf name="_index.md" >}}
    {{< branch name="docs" state="closed" >}}
      {{< leaf name="_index.md" style="color: red;">}}
      {{< leaf name="introduction.md" >}}
      {{< leaf name="introduction.fr.md" >}}
    {{< /branch >}}
  {{< /branch >}}
  {{< leaf name="hugo.toml" >}}
{{< /tree >}}

### Usage

```html {file="markdown"}
{{</* tree name="example" style="border: var(--border);" >}}
  {{< branch name="content" >}}
    {{< leaf name="_index.md" >}}
    {{< branch name="docs" state="closed" >}}
      {{< leaf name="_index.md" style="color: red;" >}}
      {{< leaf name="introduction.md" >}}
      {{< leaf name="introduction.fr.md" >}}
    {{< /branch >}}
  {{< /branch >}}
  {{< leaf name="hugo.toml" >}}
{{< /tree */>}}
```

### Options

#### `branch`

| Parameter | Description |
|-----------|---|
| `name`    | The name of the branch. |
| `type`    | The type of the branch. Can be `folder`, `document`, `container`, `group`, `part`, `assembly`, `arrow`, `branch`, `fork`, or `merge`. Default is `folder`. |
| `state`   | The state of the branch: can be `open` or `closed`. Default is `open`. |


## PDF

Trigo shortcode to display a PDF file.

### Example

{{< pdf "https://upload.wikimedia.org/wikipedia/commons/0/0c/Wikimedia_Commons_web_en.pdf" >}}

### Usage

```html {file="markdown"}
{{</* pdf "https://example.com/sample.pdf" */>}}
```

The PDF file can also be located in the project directory and use the relative path.

```html {file="markdown"}
{{</* pdf "path/to/file.pdf" */>}}
```


## YouTube

> [!NOTE]
> These are Hugo built-in shortcodes. They may be changed anytime. See [Hugo Documentation](https://gohugo.io/shortcodes/ "Hugo Shortcodes").

Embed a YouTube video.

### Example

{{< youtube id="x5oXSGhK7EY" loading="lazy" >}}

### Usage

```html {file="markdown"}
{{</* youtube id="VIDEO_ID" loading="lazy" */>}}
```

For more information, see [Hugo's YouTube Shortcode](https://gohugo.io/content-management/shortcodes/#youtube).