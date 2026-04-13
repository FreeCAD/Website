---
title: WIP Wednesday, 10 December 2025
date: 2025-12-10
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 14 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**Sketcher**: PaddleStroke fixed incorrect creation of an offset when sketch directions differ ([PR#25941](https://github.com/FreeCAD/FreeCAD/pull/25941)) and invalid subname errors when clicking on any vertex outside of a sketch edit mode ([PR#25953](https://github.com/FreeCAD/FreeCAD/pull/25953)).

**Part and PartDesign**:

- PaddleStroke fixed a toponaming issue related to links ([PR#25913](https://github.com/FreeCAD/FreeCAD/pull/25913)).
- chennes fixed a release blocker where symmetric padding was not working ([PR#26037](https://github.com/FreeCAD/FreeCAD/pull/26037)).

**TechDraw**:

- WandererFan fixed a crash on adding cosmetic features before geometry is created ([PR#25903](https://github.com/FreeCAD/FreeCAD/pull/25903)).
- 3x380V Syntax errors, missing dimensions, and templates (upon opening a model from a previous FC version ([PR#25853](https://github.com/FreeCAD/FreeCAD/pull/25853)).

**GUI**:

- kadet1090 fixed toolbar button size changing ([PR#26063](https://github.com/FreeCAD/FreeCAD/pull/26063)).
- Syres916 fixed the incorrect position of the main window on first run and Safe Mode on Windows and Wayland ([PR#25809](https://github.com/FreeCAD/FreeCAD/pull/25809)).
- tetektoza fixed preferences search popup positioning on Wayland ([PR#25675](https://github.com/FreeCAD/FreeCAD/pull/25675)).

**Other changes**:

- marioalexis84 fixed and undefined variable issue in FEM ([PR#25935](https://github.com/FreeCAD/FreeCAD/pull/25935)).
- jffmichi reverted an accidental icon name change in CAM ([PR#26038](https://github.com/FreeCAD/FreeCAD/pull/26038)).
- PaddleStroke added getPlacementOf, a better alternative to getGlobalPlacement ([PR#26059](https://github.com/FreeCAD/FreeCAD/pull/26059)). This enables link arrays to give their global placement properly.

YashSuthar983, maxwxyz, adrianinsaval, mnesarco, and ryanthara contributed additional improvements and fixes.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.12.10).

**PR stats**: since the previous report, 35 pull requests have been merged (including backports to the v1.1 branch), and 42 new pull requests have been opened.

**Issue stats**: overall, there are 3049 open issues in the tracker, up by 12 from last week. There are 29 release blockers for v1.1 currently, up by 21 from last week. This is likely because release candidate news doesn't travel all that fast, so there's an increase of people testing it.