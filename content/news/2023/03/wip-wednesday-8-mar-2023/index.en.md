---
title: 'WIP Wednesday: 8 Mar 2023'
date: 2023-03-08
authors: Chris Hennes
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

During this past week work continued on getting FreeCAD ready for Qt6, plus some bug fixes to OpenSCAD file import, UI tweaks to the Workbenches preferences page, and the File and Clipboard toolbars were split to improve customization. In the upcoming week:

- From @sliptonic: "[Toponaming](https://github.com/FreeCAD/FreeCAD/issues/8432) is moving forward. First four units of work (cards) have been created. Remember, this isn't an Ondsel project. It's a FreeCAD project. We'll be looking for help on each of these, including unit test code. Please get involved."

- @wandererfan is chasing TechDraw bugs that appear in some versions but not others.

- I (@chennes) am bug hunting in the Addon Manager's macro installation code, and continuing the refactoring work for better testability.

**PR stats:** In the week from Tuesday, 28 Feb to Tuesday, 7 Mar there were 34 pull requests merged, with a total codebase change of +6,306 / ‑5,630 lines (not counting translation changes). That's an average merged PR size of +185 / ‑166.