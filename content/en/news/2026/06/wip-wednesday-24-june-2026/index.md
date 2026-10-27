---
title: WIP Wednesday, 24 June 2026
date: 2026-06-24
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

- czarflix patched the Line/Wire tool to stop creating duplicate points with the same coordinates ([PR#29372](https://github.com/FreeCAD/FreeCAD/pull/29372)).
- Roy-043 fixed some task panels not auto-closing on document close ([PR#30894](https://github.com/FreeCAD/FreeCAD/pull/30894)). He also added a new 'Set Point as First' option for wires and B-splines when the wire or B-spline is closed, and the point under the cursor is not the first point of the curve ([PR#30830](https://github.com/FreeCAD/FreeCAD/pull/30830)).

## Sketcher

- jlewin introduced per-sketch geometry creation mode ([PR#30761](https://github.com/FreeCAD/FreeCAD/pull/30761)). Now when you use the construction line mode and switch to a different sketch or document, you only get that mode if you actually last used it there.
- PaddleStroke fixed the updated Polyline tool so that it does not attempt to create an arc where an arc is impossible to make ([PR#30497](https://github.com/FreeCAD/FreeCAD/pull/30497)).
- Reqrefusion iterated on his original patch to improve the length dimension rendering of large arcs and made it handle negative angles ([PR#30503](https://github.com/FreeCAD/FreeCAD/pull/30503)).

## Part and PartDesign

- tritao fixed a regression where selecting a PartDesign Body could render with highlight/preselection behavior instead of committed selection behavior ([PR#30791](https://github.com/FreeCAD/FreeCAD/pull/30791)).
- alfrix fixed cosmetic threads appear in subsequent unthreaded holes ([PR#30005](https://github.com/FreeCAD/FreeCAD/pull/30005)).
- maxwxyz added a custom coordinate system (CS) mode to view and adjust the transform in any picked coordinate system + alignment of the dragger to the selected CS ([PR#30227](https://github.com/FreeCAD/FreeCAD/pull/30227)).
- PaddleStroke fixed a few issues with selection order in patterns ([PR#30548](https://github.com/FreeCAD/FreeCAD/pull/30548)).
- xorza added a unified face maker that replaces the Bullseye+Cheese+BuildFace waterfall with a single algorithm handling all planar and non-planar cases ([PR#28788](https://github.com/FreeCAD/FreeCAD/pull/28788)).

## TechDraw

- fatalwir added Czech (cs) localized ISO 5457 drawing templates ([PR#30888](https://github.com/FreeCAD/FreeCAD/pull/30888)).
- ayyaz20003 fixed the workbench to stop changing the DraftView/ArchView "Page" to "Custom" after you save and reload the document ([PR#30529](https://github.com/FreeCAD/FreeCAD/pull/30529)).

## CAM

- davidgilkaufman added support for fractional percentages for adaptive stepover and UI elements for stepover distance ([PR#30846](https://github.com/FreeCAD/FreeCAD/pull/30846)).
- tarman3 added line enumeration in the editor in the Custom operation ([PR#30566](https://github.com/FreeCAD/FreeCAD/pull/30566)).
- dbtayl added H to the list of default-supported parameters, so tool-length offsets get output if the box in the machine config to utilize them is checked ([PR#30640](https://github.com/FreeCAD/FreeCAD/pull/30640)).

## FEM

marioalexis84 added support for 2D geometries to the Transform constraint and Cylindrical transform support for shell elements ([PR#30946](https://github.com/FreeCAD/FreeCAD/pull/30946)). He also added an electrostatic spark gap example ([PR#30928](https://github.com/FreeCAD/FreeCAD/pull/30928)), set pipeline filters as visible by default ([PR#30936](https://github.com/FreeCAD/FreeCAD/pull/30936)), and introduced a few more quick improvements ([PR#30665](https://github.com/FreeCAD/FreeCAD/pull/30665) and [PR#30653](https://github.com/FreeCAD/FreeCAD/pull/30653)).

## Other changes

- maxwxyz addex statusbar input hints to BIM ([PR#30511](https://github.com/FreeCAD/FreeCAD/pull/30511)).
- tritao reduced unnecessary repaint work while zooming in the 3D view by throttling updates to the status bar dimension pane ([PR#30822](https://github.com/FreeCAD/FreeCAD/pull/30822)) and improved the Navicube rendering and home navigation ([PR#30703](https://github.com/FreeCAD/FreeCAD/pull/30703)).
- wmayer implemented an automatic preselection check to improve the rendering times ([PR#29978](https://github.com/FreeCAD/FreeCAD/pull/29978)), cherry-picked by maxwxyz) and improved annotation label dragging ([PR#29953](https://github.com/FreeCAD/FreeCAD/pull/29953), cherry-picked by maxwxyz).
- pieterhijma introduced fine-grained recomputes in FreeCAD ([PR#25603](https://github.com/FreeCAD/FreeCAD/pull/25603)). These are recomputes based on dependencies between properties instead of based on objects, as is the case in FreeCAD currently.

Additional improvements and fixes were contributed by awgrover, chennes, ItSaulGoodMan, maxwxyz, moench-tegeder, Roy_043, ryankembrey, simonfrechette-dev, sliptonic, tarman3, tritao, and xtemp09.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.06.24).

## Activity stats

**PR stats**: since the previous report, 64 pull requests have been merged, and 37 new pull requests have been opened.

**Issue stats**: overall, there are 3478 open issues in the tracker, down by 15 from last week.
