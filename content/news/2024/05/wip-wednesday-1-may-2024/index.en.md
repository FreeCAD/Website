---
title: 'WIP Wednesday: 1 May 2024'
date: 2024-05-01
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

This week in FreeCAD development:

**Toponaming:** most work porting RT's patches is now done except just one piece of code that was mysteriously overlooked. Both CalligaroV, chennes, and bgbsww contributed to the TNP effort last week. bgbsww also started looking into performance regressions due to toponaming changes and found surprisingly few issues.

**Draft:** Roy-043 reverted some of the recent material system changes related to Draft for a better implementation in the future, and cjmayo fixed a bug related to QImage objects.

**FEM:** marioalexis84 added radiation heat transfer for CalculiX, and then he, Syres916, FlachyJoe, and wwmayer fixed several bugs in other parts of the FEM workbench.

**UI:**

- The unified measurement tool by hlorus (GSoC2023 student) was finally merged. There is more work to be done in the future: 20 bug reports and features requests have already been submitted against the new tool.

- chennes continued working on the new Start page: he implemented a first start section and fixed card size calculation.

- maxwxyz updated the context menu with a toggle for suppress and updated the icon for assembly's recompute command.

- PaddleStroke did a small reorganization of toolbars in Sketcher, fixed an issue with the TabBar workspace switcher, and removed "Project Shape" from TechDraw's toolbar.

- MisterMakerNL contributed an overlay fix for default windows style and various light themes.

- kadet1090 fixed issues with wrong color for preference page tooltips.

**DXF support:** Roy-043 fixed a bug with polylines importing in the newer importer, as well as a couple of bugs in the legacy DXF importer.

Some of the other changes:

- Nexusnui fixed a scaling parameter bug in importCSG (OpenSCAD).

- wwmayer made the Validate Sketch feature scriptable and fixed several bugs in various parts of FreeCAD's code.

- 0penBrain and oursland fixed bugs in the build system and CI.

**PR stats:** In the week from Wednesday, 24 April to Wednesday, 1 May there were 51 pull requests merged. 29 new pull requests were opened.

**Issue stats:** we closed 28 issues, and 62 new issues were opened. Overall, 1,566 issues are currently open.