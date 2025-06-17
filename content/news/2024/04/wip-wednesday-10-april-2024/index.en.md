---
title: 'WIP Wednesday: 10 April 2024'
date: 2024-04-10
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

In the _toponaming project_, **bgbsww** added more tests and updated existing ones, and **CalligaroV** fixed two bugs.

In _Arch_, **yorikvanhavre** upgraded the reference tool, so that it could work with DXF and IFC files ([NativeIFC](https://github.com/yorikvanhavre/FreeCAD-NativeIFC) is required for the latter), and **paullee0** fixed a regression that occured when making a block from a DraftWire.

In _Sketcher_, **PaddleStroke** [changed the rendering](https://github.com/FreeCAD/FreeCAD/pull/13098) of points' colors (after a discussion with the design working group) and fixed a bug in the Translate tool (horizontal and vertical constraints disappeared after translating).

In _TechDraw_, **WandererFan** implemented the so-called [broken view](https://github.com/FreeCAD/FreeCAD/issues/5694) - a way to render very large objects on a page by cutting a segment from the middle and juxtaposing them. He also fixed a problem with template autofilling where the total number of sheets in a document would always be equal to 1.

In _FEM_, **FlachyJoe** implemented a way to suppress the constraints: a suppressed constraint is no more written in the solver's input file and thus not taken into account for analysis. Meanwhile **lyphrowny** migrated calculix tests to ccxtools tests and attempted to resolve two issues by implementing float comparison for FEM tests.

Thanks to **davesrocketshop**, FreeCAD now uses the new _material system_ for body appearance. A new widget is now available to allow the user to select materials in a consistent fashion. It can also launch the material editor with its more advanced capabilities. Quickly after that, wwmayer fixed some of the regressions that were introduced with this patch.

Several more general fixes were contributed by **mosfet80**.

**PR stats:** In the week from Wednesday, 3 April to Wednesday, 10 April there were 28 pull requests merged, with a total codebase change of +9,853 / ‑2,310 (excluding updated translations and icons). We had an average merged PR size of +352 / -83. 20 new pull requests were opened.

**Issue stats:** we closed 23 issues, and 65 new issues were opened. Overall, 1,439 issues are currently open.