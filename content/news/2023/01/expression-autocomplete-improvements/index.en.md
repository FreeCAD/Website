---
title: Expression Autocomplete Improvements
date: 2023-01-30
authors: Chris Hennes
draft: false
categories: feature
tags:
- expression
cover:
  image:
  caption:
---

A longstanding bug in FreeCAD was recently tackled by new contributor Adrian Popescu ([@acpopescu](https://github.com/acpopescu)). In [PR 8228](https://github.com/FreeCAD/FreeCAD/pull/8228) and a series of follow-up commits, he has addressed some of the major shortcomings in the expression auto-complete function.

{{< video "expressioncompleter.mp4" >}}

AutoCompleter demonstration using data from a spreadsheet.

The improved autocompleter works anywhere you enter expression data in FreeCAD, and can pull data from all of the sources you'd expect. If searches inside variable names, so you don't have to remember whether you called your entry `widget_height` or `height_of_widget` -- start typing `height` and it will show up, whichever option you chose.

There are still some issues with the new completer (for example, the "Constraints" object in Assembly4 blocks autocomplete of local constraints!), but those are being worked on as I type this, and even the first batch of improvements here makes a big difference in the day-to-day use of expressions. If you are using a beta of the current development version give it a try and let us know what you think.