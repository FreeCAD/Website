---
title: WIP Wednesday, 17 June 2026
date: 2026-06-17
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

## Sketcher

- wwmayer posted the first part of a fix for a crash that occurs when copying constraints ([PR#30749](https://github.com/FreeCAD/FreeCAD/pull/30749), cherry-picked by maxwxyz).
- Reqrefusion implemented autoconstraints that apply when you drag points of lines or centers of circles/ellipses ([PR#29771](https://github.com/FreeCAD/FreeCAD/pull/29771)).
- matthiasdanner made it possible to rename constraints ([PR#29894](https://github.com/FreeCAD/FreeCAD/pull/29894)).
- PaddleStroke fixed a reintroduced misbehavior where pressing Esc would cancel the sketch edit ([PR#30745](https://github.com/FreeCAD/FreeCAD/pull/30745)).

## TechDraw

- ryankembrey rearranged the UI of the New Detail View task panel to group related features together ([PR#29362](https://github.com/FreeCAD/FreeCAD/pull/29362)). He also patched the user interface for seven more task panels ([PR#29807](https://github.com/FreeCAD/FreeCAD/pull/29807)).
- ItSaulGoodMan fixed a bug that prevented cosmetic elements from being deleted in the safe mode ([PR#30046](https://github.com/FreeCAD/FreeCAD/pull/30046)).

## CAM

- tarman3 added an option to reverse the order of the array in the Array op ([PR#30378](https://github.com/FreeCAD/FreeCAD/pull/30378)), added automatic sorting in Engrave to select the optimal starting point from an open wire ([PR#23489](https://github.com/FreeCAD/FreeCAD/pull/23489), based on code by PaxTux), a G-Code source selector in the Custom op ([PR#30562](https://github.com/FreeCAD/FreeCAD/pull/30562)), selection of multiple objects in SelectLoop ([PR#30547](https://github.com/FreeCAD/FreeCAD/pull/30547)), removed a limitation that bottom wires should be closed in DressupTags ([PR#30289](https://github.com/FreeCAD/FreeCAD/pull/30289)), and fixed a few more bugs.
- awgrover added probe handling to the OpenSBP post-processor ([PR#30673](https://github.com/FreeCAD/FreeCAD/pull/30673)).
- Connor a C++ based TSP Solver for pairs that takes a list of pairs and reorders them to create an efficient route for the router ([PR#30214](https://github.com/FreeCAD/FreeCAD/pull/30214)).

## BIM

- czarflix fixed a bug where levels would lose Height, Elevation, and Placement data when switching to strict IFC ([PR#29492](https://github.com/FreeCAD/FreeCAD/pull/29492)).
- maxwxyz implemented fields locking on manual input in Draft/BIM tasks ([PR#30448](https://github.com/FreeCAD/FreeCAD/pull/30448)).
- Roy_043 fixed several bugs, including one where Techdraw_Archview wouldn't render space labels ([PR#30722](https://github.com/FreeCAD/FreeCAD/pull/30722)).

## Other changes

- ipatch fixed a bug in the Measurement tool where measuring a 0° angle would result in an error message ([PR#29718](https://github.com/FreeCAD/FreeCAD/pull/29718)), while Lokestrom fixed a division-by-zero bug in the same tool ([PR#30331](https://github.com/FreeCAD/FreeCAD/pull/30331)).
- PaddleStroke fixed a bug in Part where selected bodies and parts would not be moved to a newly created part ([PR#30040](https://github.com/FreeCAD/FreeCAD/pull/30040)).
- maxwxyz added edge snapping to start and end points in the Transform tool ([PR#30213](https://github.com/FreeCAD/FreeCAD/pull/30213)).
- andershol reduced compile times by removing unnecessary includes in source files ([PR#29108](https://github.com/FreeCAD/FreeCAD/pull/29108)).

Additional improvements and fixes were contributed by Bojan9597, Lokestrom, PaddleStroke, tritao, ypsvlq, and zhyifei.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.06.17).

## Activity stats

**PR stats**: since the previous report, 41 pull requests have been merged, and 58 new pull requests have been opened.

**Issue stats**: overall, there are 3493 open issues in the tracker, up by 23 from last week.
