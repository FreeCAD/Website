---
title: WIP Wednesday, 18 February 2026
date: 2026-02-18
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 26 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**Draft**: Roy-043 fixed ghost previews of Arch_SectionPlane and Draft_WorkingPlaneProxy ([PR#27605](https://github.com/FreeCAD/FreeCAD/pull/27605)) and fixed dependency of patharray normal on view direction ([PR#27538](https://github.com/FreeCAD/FreeCAD/pull/27538)).

**Sketcher**:

- Lokestrom fixed the issue where arcs of ellipses would be centered incorrectly due to the 2nd point having the same X coordinate as the 1st one ([PR#27327](https://github.com/FreeCAD/FreeCAD/pull/27327)).
- marbocub added a fourth way to specify the symmetry constraint: an element (line, arc, or open B-spline) and a symmetry line ([PR#25525](https://github.com/FreeCAD/FreeCAD/pull/25525)).
- theo-vt fixed a crash when scaling splines ([PR#27188](https://github.com/FreeCAD/FreeCAD/pull/27188)).
- PaddleStroke added tooltips for Offset options ([PR#26114](https://github.com/FreeCAD/FreeCAD/pull/26114)), fixed an issue where Tab would not work after you move the mouse ([PR#27638](https://github.com/FreeCAD/FreeCAD/pull/27638)), fixed the loss of expression when trimming a shape ([PR#27505](https://github.com/FreeCAD/FreeCAD/pull/27505)), and fixed an error in SketchObject::getHigherElements ([PR#27560](https://github.com/FreeCAD/FreeCAD/pull/27560)).

**Part and PartDesign**:

- chennes returned inversion status by reference ([PR#27435](https://github.com/FreeCAD/FreeCAD/pull/27435)) and improved error handling for RevolMethod::ToFirst ([PR#27457](https://github.com/FreeCAD/FreeCAD/pull/27457)).
- ipatch fixed a release blocker in Part where Mirror would place a copy at the wrong location ([PR#27370](https://github.com/FreeCAD/FreeCAD/pull/27370)).

**Assembly**: PaddleStroke fixed a regression in the BOM generator that stopped grouping items ([PR#27522](https://github.com/FreeCAD/FreeCAD/pull/27522)), fixed link objects becoming permanently non-selectable ([PR#27567](https://github.com/FreeCAD/FreeCAD/pull/27567)), and fixed an issue with isolation of grounded joints ([PR#24952](https://github.com/FreeCAD/FreeCAD/pull/24952)).

**BIM/Arch**:

- Roy-043 fixed a Placement task panel issue for Arch_SectionPlane and Draft_WorkingPlaneProxy ([PR#27101](https://github.com/FreeCAD/FreeCAD/pull/27101)) and ArchReference issues with BuildingPart ([PR#27133](https://github.com/FreeCAD/FreeCAD/pull/27133)).
- furgo16 fixed coordinate normalization and area calculation for generic ArchComponents ([PR#27322](https://github.com/FreeCAD/FreeCAD/pull/27322)), prevented child objects from moving during Arch Wall debasing ([PR#27290](https://github.com/FreeCAD/FreeCAD/pull/27290)), and added a Window options task box ([PR#27381](https://github.com/FreeCAD/FreeCAD/pull/27381)).
- paullee0 fixed a regression in ArchWall ([PR#27676](https://github.com/FreeCAD/FreeCAD/pull/27676)).

**Measurement**:

- Anakin100100 added on-the-fly measurement unit change ([PR#27462](https://github.com/FreeCAD/FreeCAD/pull/27462)).
- Lokestrom fixed a bug that was causing build failures ([PR#27580](https://github.com/FreeCAD/FreeCAD/pull/27580)).
- YashSuthar983 fixed angle measurement for face and edge selection ([PR#27432](https://github.com/FreeCAD/FreeCAD/pull/27432)).

**Other changes**:

- marioalexis84 removed unnecessary code from the Preferences page of FEM ([PR#25538](https://github.com/FreeCAD/FreeCAD/pull/25538)).
- mnesarco fixed a regression introduced during the TNP Integration ([PR#27491](https://github.com/FreeCAD/FreeCAD/pull/27491)).
- 3x380V cherry-picked multiple fixes from wwmayer ([PR#27363](https://github.com/FreeCAD/FreeCAD/pull/27363)).

Syres916, ipatch, chennes, hyarion, Roy-043, bdieterm, greg19, Lgt2x, xtemp09, WandererFan, and pyro9 contributed additional improvements and fixes.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.02.18).

**PR stats**: since the previous report, 76 pull requests have been merged (including backports to the v1.1 branch), and 52 new pull requests have been opened.

**Issue stats**: overall, there are 3266 open issues in the tracker, up by 30 from last week. There are [2 release blockers for v1.1](https://github.com/FreeCAD/FreeCAD/issues?q=state%3Aopen%20label%3ABlocker%20milestone%3A1.1) currently, down by 3 from last week.