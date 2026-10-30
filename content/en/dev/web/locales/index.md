---
title: Translations and languages
description: Translate content and configure locales for the website.
weight: 7
---


The FreeCAD website and the Trigo theme support multiple languages using Hugo's [multilingual mode](https://gohugo.io/content-management/multilingual/).


## Enable multi-language

To make the Hugo project multi-language, configure the supported languages:

```yaml {file="hugo.yaml"}
defaultContentLanguage: en
languages:
  en:
    label: English
    weight: 1
  fr:
    label: Français
    weight: 2
  ja:
    label: 日本語
    weight: 3
```

> [!NOTE]
> Before a new language is enabled, the main sections and navigation pages (Homepage, Features, Download, News, Community, Documentation and Donate) and the Theme strings must be translated.
>
> Want to add a new language? Please use the provided [feature issue](https://github.com/FreeCAD/Website/issues) template indicating who will translate and proof-read/review.

## Manage content translations

Hugo supports multiple approaches to managing translations. The FreeCAD website currently uses the [translation by content directory](https://gohugo.io/content-management/multilingual/#translation-by-content-directory).

### Translation by content directory

Each locale has its own content directory as configured by their `contentDir` parameter.

The current FreeCAD website configuration defined separate root content directories for each locale:

{{< tree >}}
  {{< branch label="/content" >}}
    {{< branch label="en" state="open" >}}
      {{< leaf label="_index.md  ← / (English homepage)" >}}
      {{< branch label="docs" state="open" >}}
        {{< leaf label="_index.md  ← /docs/ (English docs section)" >}}
      {{< /branch >}}
    {{< /branch >}}
    {{< branch label="fr" state="open" >}}
      {{< leaf label="_index.md  ← / (French homepage)" >}}
      {{< branch label="docs" state="open" >}}
        {{< leaf label="_index.md  ← /docs/ (French docs section)" >}}
      {{< /branch >}}
    {{< /branch >}}
    {{< branch label="ja" state="open" >}}
      {{< leaf label="_index.md  ← / (Japanese homepage)" >}}
      {{< branch label="docs" state="open" >}}
        {{< leaf label="_index.md  ← /docs/ (Japanese docs section)" >}}
      {{< /branch >}}
    {{< /branch >}}
  {{< /branch >}}
{{< /tree >}}

This allows to use content mounts in the project configuration, where missing translated content uses the default language site as fallback (i.e. `en` for English).

### Translation by filename

Hugo also supports managing translations by filename. With a file `content/docs/_index.en.md` in English, the file `content/docs/_index.fr.md` contains the French translation. This approach is currently not used for the FreeCAD website.

{{< tree >}}
  {{< branch label="/content" >}}
    {{< leaf label="_index.en.md  ← / (English homepage)" >}}
    {{< leaf label="_index.fr.md  ← / (French homepage)" >}}
    {{< leaf label="_index.ja.md  ← / (Japanese homepage)" >}}
    {{< branch label="docs" state="open" >}}
      {{< leaf label="_index.en.md  ← /docs/ (English docs section)" >}}
      {{< leaf label="_index.fr.md  ← /docs/ (French docs section)" >}}
      {{< leaf label="_index.ja.md  ← /docs/ (Japanese docs section)" >}}
    {{< /branch >}}
  {{< /branch >}}
{{< /tree >}}


## Theme strings translations

To translate theme strings, i18n translation tables are used. YAML data files for each locale are stored in the `i18n` directory and define the string identifier and the translated value.

```yaml {file="i18n/fr.yaml"}
- id: title
  translation: "Titre"
```


## Reference

- [Hugo Multilingual Mode](https://gohugo.io/content-management/multilingual/)
- [Hugo Multilingual Part 1: Content translation](https://www.regisphilibert.com/blog/2018/08/hugo-multilingual-part-1-managing-content-translation/)
- [Hugo Multilingual Part 2: Strings localization](https://www.regisphilibert.com/blog/2018/08/hugo-multilingual-part-2-i18n-string-localization/)