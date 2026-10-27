---
title: WIP Wednesday, 2 September 2026
date: 2026-09-02
author: Aleksandr Prokudin
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

- UnKabaraQuiDev patched the Fillet tool to actually preserve corners between two arcs ([PR#31746](https://github.com/FreeCAD/FreeCAD/pull/31746)).
- miakh fixed an inconvenience where switching between the construction line and normal modes would not update the active preview ([PR#32245](https://github.com/FreeCAD/FreeCAD/pull/32245)).
- maxwxyz improved dimension and constraint tools, which are now able to select model edges and vertices while editing a sketch ([PR#31916](https://github.com/FreeCAD/FreeCAD/pull/31916)).

{{< video src="sketcher_external_dimension_relnotes_26.3.mp4" >}}

## Part and PartDesign

- ILoveBuns fixed a bug where sketches would lose their attachment when loading an older file ([PR#31983](https://github.com/FreeCAD/FreeCAD/pull/31983)).
- maxwxyz restored circular axis selection for polar patterns ([PR#32287](https://github.com/FreeCAD/FreeCAD/pull/32287)), added angular start offsets to Revolution and Groove ([PR#32121](https://github.com/FreeCAD/FreeCAD/pull/32121)), fixed a crash when selecting a Body for Boolean operation ([PR#32284](https://github.com/FreeCAD/FreeCAD/pull/32284)), and made the defeaturing command available in PartDesign, as it was already available in the Part workbench ([PR#29616](https://github.com/FreeCAD/FreeCAD/pull/29616)).

{{< video src="partdesign_defeaturing_relnotes_26.3.mp4" >}}

## Assembly

- tsiwt fixed a shortcut conflict between CreateBom and CreateJointRigidGroup ([PR#32222](https://github.com/FreeCAD/FreeCAD/pull/32222)).
- PaddleStroke fixed DoF calculation with bundled fixed joints ([PR#30937](https://github.com/FreeCAD/FreeCAD/pull/30937)) and added a coaxial gear joint ([PR#31155](https://github.com/FreeCAD/FreeCAD/pull/31155)).

## TechDraw

- ryankembrey fixed vertical misalignment of dimension text ([PR#32146](https://github.com/FreeCAD/FreeCAD/pull/32146)).
- MortenVajhoj fixed selection state for face centerline ([PR#32204](https://github.com/FreeCAD/FreeCAD/pull/32204)) and the Keep Label property ([PR#32205](https://github.com/FreeCAD/FreeCAD/pull/32205)).
- PaddleStroke added the missing PDF command ([PR#31523](https://github.com/FreeCAD/FreeCAD/pull/31523)).
- wmayer made it possible to use Bezier or B-spline curves of degree 1 for angle measurement ([PR#32256](https://github.com/FreeCAD/FreeCAD/pull/32256), cherry-picked by maxwxyz).
- WandererFan fixed several issues related to line formats ([PR#29430](https://github.com/FreeCAD/FreeCAD/pull/29430)).

## CAM

- sliptonic fixed the new 3+2 machining not outputting A-axis rotation for workplane aligned with Z ([PR#32082](https://github.com/FreeCAD/FreeCAD/pull/32082)) and added the ability to create a new CAM machine by importing from an MTConnect probe stream ([PR#32081](https://github.com/FreeCAD/FreeCAD/pull/32081)).
- Connor added an All Tools view to the toolbit dialog, so a tool can be picked from any library rather than only the selected one ([PR#32211](https://github.com/FreeCAD/FreeCAD/pull/32211)), made ToolBit shape drawings theme-aware ([PR#32278](https://github.com/FreeCAD/FreeCAD/pull/32278)), and moved toolheads to their own tab in the machine editor ([PR#32250](https://github.com/FreeCAD/FreeCAD/pull/32250)).
- jffmichi fixed the missing initial move to the start location in the Pocket operation ([PR#31491](https://github.com/FreeCAD/FreeCAD/pull/31491)).
- awgrover fixed a bug in drill expansion ([PR#32099](https://github.com/FreeCAD/FreeCAD/pull/32099)).
- tarman3 added the possibility to append CNC-specific G-Code lines in Custom for post-processing ([PR#31720](https://github.com/FreeCAD/FreeCAD/pull/31720)), fixed G85 in simulators ([PR#32087](https://github.com/FreeCAD/FreeCAD/pull/32087)), added more options to the Engrave task panel ([PR#32115](https://github.com/FreeCAD/FreeCAD/pull/32115)), and fixed an open path error for one and two faces ([PR#31882](https://github.com/FreeCAD/FreeCAD/pull/31882)).

## Other changes

- MortenVajhoj applied half a dozen small improvements to the Mass properties tool ([PR#30810](https://github.com/FreeCAD/FreeCAD/pull/30810)).
- chennes fixed several bugs while continuing his work on the new crash reporter ([PR#32137](https://github.com/FreeCAD/FreeCAD/pull/32137)).
- Lgt2x removed outdated Rift/Oculus compatibility code; people willing to work on VR can use OpenXR to build a new compatibility layer ([PR#30652](https://github.com/FreeCAD/FreeCAD/pull/30652)).
- tarman3 made it possible to apply StdCmdSendToPythonConsole to multiple objects ([PR#31096](https://github.com/FreeCAD/FreeCAD/pull/31096)).
- tritao expanded FreeCAD's Python typing coverage in Core, Part, Sketcher, and the Python bootstrap while reducing handwritten stub duplication, and added PySide Qt5/Qt6 compatibility overlays ([PR#32209](https://github.com/FreeCAD/FreeCAD/pull/32209)).

Additional improvements and fixes were contributed by awgrover, chennes, codeotaku, Connor, davesrocketshop, davidgilkaufman, flaviut, FreeCAD-Nut, jffmichi, ILoveBuns, kadet1090, Lgt2x, maxwxyz, mnesarco, pieterhijma, Roy-043, shubham-pawar, sliptonic, tarman3, TD-4242, TheBhowmik, tritao, waynepiekarski and wmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.09.02).

## Activity stats

**PR stats**: since the previous report, 79 pull requests have been merged, and 60 new pull requests have been opened.

**Issue stats**: overall, there are 3530 open issues in the tracker, down by 10 from last week.
