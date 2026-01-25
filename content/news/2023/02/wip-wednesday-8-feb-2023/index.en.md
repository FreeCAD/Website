---
title: 'WIP Wednesday: 8 Feb 2023'
date: 2023-02-08
authors: Chris Hennes
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

As everyone makes their way back home from FreeCAD Day 2023, we still have a few things going on in the FreeCAD development world:

- @uwestoehr has worked to clean up the rendering of the navigation cube ([PR #8266](https://github.com/FreeCAD/FreeCAD/pull/8266)) and is working to extend the SectionCutting feature for intersecting objects ([PR #8252](https://github.com/FreeCAD/FreeCAD/pull/8252)).

- @abdullah submitted PRs with two pre-requisites to the new NotificationArea ([PR #8350](https://github.com/FreeCAD/FreeCAD/pull/8350) and [#8352](https://github.com/FreeCAD/FreeCAD/pull/8352)). He plans to respond to feedback on that front to try to get them merged. One of them introduces a new external library libfmt, which can be header-only or pre-compiled. In parallel, he has started to fix the [sketcher grid tool PR](https://github.com/FreeCAD/FreeCAD/pull/7754).

**PR stats:** In the week from Tuesday, 1 Jan to Tuesday, 7 Jan there were 55 pull requests submitted and 47 merged, with a total codebase change of +6,155 / ‑3,681 lines (not counting translation changes). That's an average merged PR size of +131 / ‑78.