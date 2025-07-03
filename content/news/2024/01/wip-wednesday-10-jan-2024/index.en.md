---
title: 'WIP Wednesday: 10 Jan 2024'
date: 2024-01-10
author: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
  alt:
---

The team accelerated after the winter holidays and did a serious PR queue cleanup:

- **@Roy-043** merged some improvements to Draft and fixed several bugs in Arch.

- **@Berberic2** contributed German ISO 7200 templates for TechDraw.

- **@kadet1090** added an optional horizontal scrollbar to the Preferences dialog so that the minimum width could be smaller to make it fit on smaller displays.

- **@maxwxyz** improved the auto-dimension tool in Sketcher to dimension distances between arc-point, arc-circle, arc-arc. He also changed the respective tool descriptions of the rotate and the polygon tool to hint users to modify with U and J keys.

- **@PaddleStroke** fixed a bug in Sketcher, that made the auto-constraint operation crash when interrupted by undo. He also hid the useless headers of the property view panel.

- **@FlachyJoe** added a fix to Sketcher for [#11826](https://github.com/FreeCAD/FreeCAD/issues/11826).

- **@Rexbas** fixed several right-click context menu issues in the OpenSCAD workbench, and **@maxwxyz** added a context-sensitive right-click menu to Sketcher (selecting a geometric object and right-clicking now displays a list of applicable constraints).

- **@davesrocketshop** contributed further Material editor enhancements: support for embedded SVG files, ability to filter materials in the editor when called from code, new models and materials supporting patterns such as used by the TechDraw workbench.

- **@bgbsww** added support for OCCT 7.8.0 (which is the latest release) and contributed tests for new toponaming code.

- **@leviathanch** added a missing Qt version check to make the program compile with Qt6.

**PR stats:** In the week from Wednesday, 3 Jan to Wednesday, 10 Jan there were 48 pull requests merged, with a total codebase change of +8,461 / -3,054. We had an average merged PR size of +176 / ‑64. 14 new pull requests were opened.

**Issue stats:** we closed 23 issues, and 23 new issues were opened. Overall, 1,143 issues are currently open.