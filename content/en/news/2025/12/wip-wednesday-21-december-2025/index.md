---
title: WIP Wednesday, 31 December 2025
date: 2025-12-31
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 21 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**PartDesign**:

- chennes with a release blocker where symmetric padding would not work with MidPlane set to True ([PR#26462](https://github.com/FreeCAD/FreeCAD/pull/26462)).
- PaddleStroke fixed a regression where padding up to face would not worki if filename contained non-ASCII characters ([PR#26514](https://github.com/FreeCAD/FreeCAD/pull/26514)).
- alfrix fixed an issue where feleting a Pattern feature after deleting the source feature would cause the next step to break ([PR#26467](https://github.com/FreeCAD/FreeCAD/pull/26467)).

**CAM**:

- tarman3 fixed the RampEntry dressup generating Path.Log errors ([PR#25398](https://github.com/FreeCAD/FreeCAD/pull/25398)) and adding an unneeded line that causes a CNC to go back to the origin ([PR#22484](https://github.com/FreeCAD/FreeCAD/pull/22484)), refactored a part of the Array command ([PR#26324](https://github.com/FreeCAD/FreeCAD/pull/26324)), fixed a zero deflection issue in Path.Post.Utils.splitArcs() ([PR#26322](https://github.com/FreeCAD/FreeCAD/pull/26322)), improved Slot ([PR#25841](https://github.com/FreeCAD/FreeCAD/pull/25841)), and removed a useless property from Engrave ([PR#25374](https://github.com/FreeCAD/FreeCAD/pull/25374)).
- Dimitris75 fixed Linear and Angular Deflection values in Waterline OCL Adaptive ([PR#26422](https://github.com/FreeCAD/FreeCAD/pull/26422)).

**BIM**: Roy-043 fixed a warning that was displayed when changing wall length ([PR#26254](https://github.com/FreeCAD/FreeCAD/pull/26254)), a crash that occurred when switching BIM_View Render Mode ([PR#26490](https://github.com/FreeCAD/FreeCAD/pull/26490)), and the transparency of the curtain walls in BIMExample.FCStd ([PR#26499](https://github.com/FreeCAD/FreeCAD/pull/26499)).

**Other changes**:

- theo-vt fixed a bug in Sketcher where using the Scale tool when autoscaling would create new scaled constraints but not scale the labels ([PR#26442](https://github.com/FreeCAD/FreeCAD/pull/26442)).
- tetektoza fixed an issue in Part where the visibility of compound child objects would change in a certain scenario ([PR#26509](https://github.com/FreeCAD/FreeCAD/pull/26509)).
- adrianinsaval fixed an issue with NaN formatting in FEM ([PR#26519](https://github.com/FreeCAD/FreeCAD/pull/26519)).
- Mr-Rahul-Paul fixed premature evaluation and recursive updates in the Image Plane Settings dialog ([PR#26390](https://github.com/FreeCAD/FreeCAD/pull/26390)).

YashSuthar983, drwho495, horseDeveloper, chennes, adrianinsaval, tetektoza, and moench-tegeder contributed additional improvements and fixes.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.12.31).

**PR stats**: since the previous report, 49 pull requests have been merged (including backports to the v1.1 branch), and 29 new pull requests have been opened.

**Issue stats**: overall, there are 3146 open issues in the tracker, up by 25 from last week. There are 4 release blockers for v1.1 currently, down by 4 from last week.

Happy New Year, everyone!