---
title: Front matter
description: Define content metadata and parameters.
weight: 6
---


> [!NOTE]
> The FreeCAD website uses the `yaml` format for its configuration, front matter and examples, as it is easier to read than `toml` or `json`.
> Converters from YAML to TOML or JSON and vice-versa are available online if necessary.


## What is a front matter?

Content pages can store custom metadata to enhance their semantics. In most Static Site Generator like Hugo, this is achieved via the **front matter** fields. The front matter is defined at the top of every content text file such as Markdown in between tags, e.g. `---` for YAML.

By default, a `title` front matter field must be provided for each page. Additionally, many more fields can be specified. Field values can be rather minimal, such as a single string, number, boolean, but can also contain lists (also called slices), maps (also called dictionaries), or even a combination of different nested types.


## Front matter fields and values

> [!Note]
> For all Hugo default fields, `camelCase` is used.
> For all custom Trigo theme naming and fields, `snake_case` is used instead to help distinguish from official Hugo syntax.
> CSS classes and IDs use hyphens like `custom-class`.

| Field name | Value type | Example |
|---|---|---|
| `author` | string | Alice |
| `category` | string (options) | Event |
| `cover` | map | {"image": "img.webp", "caption": None} |
| `date` | date | 2020-01-02 |
| `description` | string | How to write great articles. |
| `draft` | bool | False |
| `icon` | string | puzzle |
| `icon_cms` | string | bolt |
| `lastmod` | date | 2021-02-03 |
| `layout` | string | archives |
| `linkTitle` | string | Admin |
| `redirect` | string | auto |
| `tags` | list[string] | [code, python] (can be inline or block array) |
| `title` | string | A great title |
| `versions` | list[string] | ["1.0", "1.1"] (can be inline or block array) |
| `weight` | int | 1 |

## YAML syntax

| Case | Example | Quote? | Comment |
|:-----|---------|--------|---------|
| Simple string | `title: My Blog` | ❌ No | Safe plain string |
| String with colon + space | `title: "YAML: The Guide"` | ✅ Yes | Key confusion (`YAML: `) |
| String with `#` | `description: "C# basics"` | ✅ Yes | `#` starts comment |
| String starting with `*` | `alias: "*draft"` | ✅ Yes | `*` is YAML alias marker |
| String starting with `&` | `key: "&value"` | ✅ Yes | `&` is YAML anchor |
| URL | `baseURL: https://example.com` | ❌ No | Safe URL (`:` not followed by space) |
| URL with fragment | `url: "https://example.com/page#intro"` | ✅ Yes | `#` starts comment |
| Number | `paginate: 10` | ❌ No | Proper numeric type |
| Leading zero | `id: "00123"` | ✅ Yes | Numeric parsing (leading zeros removed) |
| Date | `date: 2026-03-03` | ❌ No | Proper date object |
| Null value | `field: null` | ❌ No | Proper null |
| Boolean | `draft: true` | ❌ No | Proper boolean |
| Boolean-like word | `title: "On"` | ✅ Yes | `on` is YAML boolean |
| Multiline text | `summary: \|` | ❌ No | `>` is folded and `\|` is literal block scalars |
| Inline array | `tags: [hugo, blog]` | ❌ No | Safe inline list |
| Block array | `- hugo` | ❌ No | Safe block list (more readable than inline) |

### Hugo-Specific Cases

| Case | Example | Quote? | Comment |
|:-----|---------|--------|---------|
| Simple glob pattern | `include: "*.md"` | ✅ Yes | `*` is wildcard |
| Recursive glob pattern | `exclude: "**/*.draft.md"` | ✅ Yes | `**` is super wildcard |
| Glob slice | `matrix: ["! en", "v1.*.*", "{fr, de}"]` | ✅ Yes | Negation, single, list and range |

See [Hugo Glob patterns docs](https://gohugo.io/quick-reference/glob-patterns).


### Sveltia CMS config

| Case | Example | Quote? | Comment |
|:-----|---------|--------|---------|
| Simple string | `label: Blog` | ❌ No | Plain string is safe |
| Folder path | `folder: content/blog` | ❌ No | No special YAML chars |
| Boolean field option | `required: true` | ❌ No | Must remain boolean |
| Boolean mistakenly quoted | `required: "true"` | ❌ No | Becomes string → breaks validation |
| Number field option | `max: 10` | ❌ No | Must remain numeric |
| String that looks boolean | `default: "on"` | ✅ Yes | `on` becomes boolean otherwise |
| Glob pattern | `pattern: "*.md"` | ✅ Yes | `*` is YAML alias symbol |
| Recursive glob | `exclude: "**/*.draft.md"` | ✅ Yes | `*` must be quoted |
| Regex pattern | `pattern: "^[a-z0-9-]+$"` | ✅ Yes | Contains `[]`, `^`, `$`, etc. |
| Template variables | `slug: "{{slug}}"` | ✅ Yes | `{}` should be quoted |
| Preview path template | `preview_path: "blog/{{slug}}"` | ✅ Yes | Prevent parsing issues |
| Value containing `#` | `default: "C#"` | ✅ Yes | `#` starts comment |
| Option list (normal) | `- draft` | ❌ No | Safe string |
| Option list (boolean-like) | `- "on"` | ✅ Yes | Prevent boolean coercion |
| Datetime default | `default: 2026-03-03` | ❌ No | Keeps date type |
| Datetime wrongly quoted | `default: "2026-03-03"` | ⚠️ Avoid | Becomes string, may break widget |

See [Sveltia CMS docs](https://sveltiacms.app/en/docs/config-basics).