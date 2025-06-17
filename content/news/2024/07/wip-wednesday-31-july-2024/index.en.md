---
title: 'WIP Wednesday: 31 July 2024'
date: 2024-07-31
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

**Toponaming**: bgbsww finished transferring the code to solve the save/restore errors with objects with element maps, this did away with 3 release blockers.

**BIM**: hasecilu, Roy_043, paullee0, and cjmayo fixed several bugs, including one blocker.

**FEM**: marioalexis84 fixed a bug where the workbench would spill red ink into the Report View about linked objects when meshing, and fandaL fixed a bug where the FemMesh2Mesh tool didn't work with quad elements.

**Assembly**: PaddleStroke made it possible to edit joints by double-clicking them in the 3D view. He also reworked assembly properties to store the full path to objects so that two identical objects could be differentiated; this resolves another release blocker.

**Materials**: davesrocketshop fixed two blockers related to setting custom color to objects.

**GUI**:

- 3x380V added a workaround for missing custom cursors on Wayland when building FreeCAD with Qt6.

- Syres916 synced 'Preferences > Display > UI' page with actual defaults for new users: some checkboxes had incorrect states, one checkbox was missing.

- kadet1090 fixed various small cosmetic issues with the Preferences dialog, such as incorrect padding, inconsistent alignment, horizontal scrollbars that should not be present etc.

**Among other changes**:

- NewJoker added a missing 2D meshing algorithm, Quasi-structured Quad, to the Gmsh mesher in the Mesh WB.

- WandererFan fixed a loop in Techdraw during the calculation of the automatic scale.

- Roy_043 fixed a snap-at-intersection bug that would cause the infinite hanging of the program.

- pieterhijma fixed the use of the '--single-instance' command line argument on Windows so that new files would always be opened in the already running instance of FreeCAD.

**PR stats**: since the previous report, 33 pull requests have been merged, 14 new pull requests have been opened.

**Issue stats**: 1839 issues are currently open, 20 issues up from last week. Of those, 35 issues still block the v1.0 release - 4 up from last week.