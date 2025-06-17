---
title: Translating FreeCAD
date: 2022-09-21
author: Chris Hennes
draft: false
categories: feature
tags:
- UI
cover:
  image:
  caption:
  alt:
---

FreeCAD is an international project featuring contributors from dozens of countries, and users around the globe. One way we work to improve the usefulness of FreeCAD is by making it available in many different user-interface languages using the crowd-sourced translation platform [CrowdIn](http://crowdin.com/project/freecad).

![Language Support Aug 2022](LanguageSupportAug2022.png "Language Support Aug 2022")

The process begins with individual developers marking user-visible strings in their code as needing translation. Once or twice per month an extraction process is run on FreeCAD's source code to extract those strings and send them to the CrowdIn platform, at which point volunteer translators take over, examining each string and its context and translating it into the many languages FreeCAD supports. In the next cycle, those new translations are downloaded from CrowdIn and incorporated into FreeCAD's builds, and the process repeats with the new strings added in the meantime.

As of this writing, FreeCAD has support for over two dozen languages: of course, in most cases there are still some missing translations! If you use FreeCAD in a language other than English and notice an untranslated string, or one whose translation you believe is incorrect, consider joining the project at [CrowdIn](https://crowdin.com/project/freecad) and helping us improve the user experience for others using your language. You can also post about the missing string in either the [FreeCAD Forum](https://forum.freecadweb.org) or in the [GitHub repository for translations](https://github.com/FreeCAD/FreeCAD-translations/issues/). With your help we can continue to improve FreeCAD for users everywhere.