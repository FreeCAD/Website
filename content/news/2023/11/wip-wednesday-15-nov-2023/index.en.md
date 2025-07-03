---
title: 'WIP Wednesday: 15 Nov 2023'
date: 2023-11-16
author: Chris Hennes
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

- The new Assembly solver, [OndselSolver](https://github.com/Ondsel-Development/OndselSolver/), was added as a git submodule. This is a major step towards having a working version of an integrated assembly workbench.

- **@wwmayer** applied clang-format to the Base section of the code, taking one step further towards standardizing our code formatting.

- **@paddle** continued his work on the Sketcher DrawSketchHandler (DSH) system, merging the new Arc Slot tool.

- **@adrianinsaval** is putting the finishing touches on the release of 0.21.2

- I (**@chennes**) am working on the Toponaming merge, working on the caching methods in TopoShape.

**PR stats:** In the week from Wednesday, 8 Nov to Wednesday, 15 Nov there were 53 pull requests merged, with a total codebase change of +22,174 / ‑16,030 lines (not counting translation updates). We had an average merged PR size of +426 / ‑308. We closed 26 Issues, and 21 new Issues were opened.