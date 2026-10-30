---
title: WIP Wednesday, 15 July 2026
date: 2026-07-15
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

## Draft

- Roy-043 increased the center point tolerance for angular dimensions, or else endpoints that are (almost) equal to the center would be disregarded ([PR#31172](https://github.com/FreeCAD/FreeCAD/pull/31172)).
- maxwxyz fixed Draft input locking so command shortcuts like X and E do not accidentally lock the focused coordinate field ([PR#31256](https://github.com/FreeCAD/FreeCAD/pull/31256)).

## Sketcher

- Reqrefusion fixed a regression where dragging elements would overconstrain the sketch ([PR#30877](https://github.com/FreeCAD/FreeCAD/pull/30877)).
- tritao fixed Sketcher preselection conflicts where constraint datum labels or dimension presentation lines could take precedence over overlapping sketch geometry, making points, curves, or axes difficult to select ([PR#30792](https://github.com/FreeCAD/FreeCAD/pull/30792)).
- theo-vt fixed an issue where you couldn't perform some operations on a sketch opened in one document if another sketch was opened and closed in a second document ([PR#31302](https://github.com/FreeCAD/FreeCAD/pull/31302)).

## CAM

- sliptonic pushed some helper Feeds & Speeds code in preparation for the real F&S code ([PR#30078](https://github.com/FreeCAD/FreeCAD/pull/30078)).
- jffmichi fixed a crash in Assembly by fixing a bug in CAM ([PR#31214](https://github.com/FreeCAD/FreeCAD/pull/31214)).
- tarman3 fixed a precision error ([PR#28519](https://github.com/FreeCAD/FreeCAD/pull/28519)) and an incorrect initial stock selection in DressupPathBoundary ([PR#31116](https://github.com/FreeCAD/FreeCAD/pull/31116)).
- awgrover allowed non-supported/non-conforming G-code in the Custom operation ([PR#31022](https://github.com/FreeCAD/FreeCAD/pull/31022)) and removed the generation of the F parameter in G0 ([PR#31150](https://github.com/FreeCAD/FreeCAD/pull/31150)).

## TechDraw

- kevinsmia1939 fixed a crash that occurred when activating the Circle Centerlines tool with a stale selection ([PR#28772](https://github.com/FreeCAD/FreeCAD/pull/28772)).
- WandererFan fixed the conversion of a "circle-like" bspline to actual circle geometry ([PR#30530](https://github.com/FreeCAD/FreeCAD/pull/30530)).

## Other changes

- wmayer fixed a regression where the shape builder's "Face from edges" option would create a face on the wrong plane ([PR#31141](https://github.com/FreeCAD/FreeCAD/pull/31141), cherry-picked by maxwxyz).
- georgee26 patched the user interface to ask just once with an "Apply to all" checkbox when deleting multiple non-empty groups instead of asking the question multiple times ([PR#30586](https://github.com/FreeCAD/FreeCAD/pull/30586)).

Additional improvements and fixes were contributed by AngelGalindo7, Bojan9597, chennes, Connor, ElementW, greg19, j-hewett, Krrish777, Lgt2x, matthiasdanner, maxwxyz, Roy-043, tarman3, theo-vt, tritao, and wmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.07.15).

## Activity stats

**PR stats**: since the previous report, 70 pull requests have been merged, and 47 new pull requests have been opened.

**Issue stats**: overall, there are 3504 open issues in the tracker, up by 9 from last week.
