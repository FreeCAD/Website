---
title: WIP Wednesday, 20 May 2026
date: 2026-05-20
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

## Draft

- Roy_043 fixed a regression ([PR#30061](https://github.com/FreeCAD/FreeCAD/pull/30061)) and an incorrect Autoupdate icon ([PR#30063](https://github.com/FreeCAD/FreeCAD/pull/30063)).
- ItSaulGoodMan fixed a bug where Trimex would not write the trim/extend result back to the opened sketch ([PR#29845](https://github.com/FreeCAD/FreeCAD/pull/29845)).

## Sketcher

- pavltom made the font face used in Sketcher labels configurable in Preferences ([PR#26600](https://github.com/FreeCAD/FreeCAD/pull/26600)).
- Reqrefusion improved the default angle placement for arcs ([PR#29630](https://github.com/FreeCAD/FreeCAD/pull/29630)).
- Bojan9597 fixed a bug where AutoColor would not update colors immediately when enabled ([PR#30185](https://github.com/FreeCAD/FreeCAD/pull/30185)).
- ElementW fixed empty line style dropdown lists in Preferences ([PR#30151](https://github.com/FreeCAD/FreeCAD/pull/30151)).
- andershol fixed a bug where a constrained element would not be updated post partial constraint removal ([PR#29812](https://github.com/FreeCAD/FreeCAD/pull/29812)).
- PaddleStroke updated the Polyline tool to accept on-view parameters as you sketch ([PR#29336](https://github.com/FreeCAD/FreeCAD/pull/29336)).

{{< youtube id=18WdpAEWxRg title="Sketcher: New polyline tool" loading=lazy >}}

## Part and PartDesign

- caio-venancio fixed a bug where creating boolean inside Std_Group would result in an "Out of allowed scope" error ([PR#29534](https://github.com/FreeCAD/FreeCAD/pull/29534)).
- wwmayer fixed a toponaming issue in Loft ([PR#29982](https://github.com/FreeCAD/FreeCAD/pull/29982)) and added a FuzzyTolerance property ([PR#29984](https://github.com/FreeCAD/FreeCAD/pull/29984)). Both patches were cherry-picked by maxwxyz.
- drwho495 fixed Additive and Subtractive Pipes not generating ElementMaps ([PR#23265](https://github.com/FreeCAD/FreeCAD/pull/23265)).
- maxwxyz fixed body toggling with the Spacebar ([PR#30231](https://github.com/FreeCAD/FreeCAD/pull/30231)).

## Assembly

- Lgt2x made simulation playback buttons bigger and more distinguishable ([PR#30257](https://github.com/FreeCAD/FreeCAD/pull/30257)).
- spontarelliam added a Joint Rotate button that adds 90° to the rotation spinbox ([PR#29717](https://github.com/FreeCAD/FreeCAD/pull/29717)).
- PaddleSroke fixed a bug where right-clicking on a sub-assembly item in the tree or deleting it in the 3D view would crash FreeCAD ([PR#29887](https://github.com/FreeCAD/FreeCAD/pull/29887)).

## TechDraw

- WandererFan patched the code to prioritize X/Y position over snapping and added new preferences for dimension snapping ([PR#30154](https://github.com/FreeCAD/FreeCAD/pull/30154)). He also fixed a build bug ([PR#30223](https://github.com/FreeCAD/FreeCAD/pull/30223)).
- ayyaz20003 prevented edge deletion on torus and similar concentric-arc shapes ([PR#29637](https://github.com/FreeCAD/FreeCAD/pull/29637)).

## CAM

- tarman3 improved the time it takes to recompute when linking ([PR#29983](https://github.com/FreeCAD/FreeCAD/pull/29983)).
- tarman3 patched SelectLoop to allow it to select several horizontal wires when two or more selected edges are not part of one wire ([PR#27497](https://github.com/FreeCAD/FreeCAD/pull/27497)) and select all edges from the shape if no subelements are selected ([PR#29523](https://github.com/FreeCAD/FreeCAD/pull/29523)).
- tarman3 patched Profile to allow selecting vertical faces ([PR#27236](https://github.com/FreeCAD/FreeCAD/pull/27236)).
- tarman3 improved Slot in various ways and added the ability to create slots from non-horizontal arcs and any straight edges ([PR#25090](https://github.com/FreeCAD/FreeCAD/pull/25090)).
- tarman3 added approximation to Engrave for smoother, complex curves ([PR#29528](https://github.com/FreeCAD/FreeCAD/pull/29528)).
- davidgilkaufman fixed a bug in generating Adaptive lead-ins where the stepover would not be respected ([PR#29971](https://github.com/FreeCAD/FreeCAD/pull/29971)). He also continued porting code from Clipper1 to Clipper2 as part of his FPA grant project ([PR#29535](https://github.com/FreeCAD/FreeCAD/pull/29535)).

## BIM

- Roy_043 fixed restoring the working plane after recentering ([PR#28836](https://github.com/FreeCAD/FreeCAD/pull/28836)) and an Arch_CutPlane error ([PR#29699](https://github.com/FreeCAD/FreeCAD/pull/29699)).
- tritao reduced toponaming noise from BIM horizontal area analysis ([PR#29066](https://github.com/FreeCAD/FreeCAD/pull/29066)).
- semhustej updated the BIM Classification Download URL ([PR#30247](https://github.com/FreeCAD/FreeCAD/pull/30247)) and changed DrawingView LineWidth of Cut Lines object to 2x the default thickness ([PR#30149](https://github.com/FreeCAD/FreeCAD/pull/30149)).
- paullee0 fixed ArchWall unsupported base not managed properly ([PR#29810](https://github.com/FreeCAD/FreeCAD/pull/29810)).
- ItSaulGoodMan fixed the IFC import hanging when multi-core is set to 0 ([PR#30201](https://github.com/FreeCAD/FreeCAD/pull/30201)).

## Other changes

- wwmayer fixed DXF importing on Windows ([PR#30125](https://github.com/FreeCAD/FreeCAD/pull/30125)); cherry-picked by maxwxyz.
- pieterhijma adapted FreeCAD to OpenCascade 8 ([PR#25502](https://github.com/FreeCAD/FreeCAD/pull/25502)).
- YashSuthar983 implemented on-the-fly unit changes ([PR#29157](https://github.com/FreeCAD/FreeCAD/pull/29157)).
- marioalexis84 updated analysis type and eigenmode limits properties for old projects in FEM ([PR#30198](https://github.com/FreeCAD/FreeCAD/pull/30198)).

Additional improvements and fixes were contributed by alecGraves, andershol, awgrover, Bojan9597, chennes, davidosterberg, drwho495, ElementW, ItSaulGoodMan, kadet1090, Lgt2x, maxwxyz, mosfet80, pjcreath, tarman3, and tritao.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.05.20).

## Activity stats

**PR stats**: since the previous report, 83 pull requests have been merged, and 51 new pull requests have been opened.

**Issue stats**: overall, there are 3442 open issues in the tracker, up by 1 from last week.
