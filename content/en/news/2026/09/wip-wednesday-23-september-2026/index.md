---
title: WIP Wednesday, 23 September 2026
date: 2026-09-23
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

- chennes made it possible to mark specific commands as Stable, Experimental, or Development to control their visibility in the UI based on how mature the code is ([PR#32740](https://github.com/FreeCAD/FreeCAD/pull/32740)). Group constraints are "Development", Text geometry is "Experimental". UI for selecting what's visible will follow.
- alfrix fixed a regression where pressing Tab before entering a dimension would cause focus to move after the first digit ([PR#32709](https://github.com/FreeCAD/FreeCAD/pull/32709)).

## Part and PartDesign

- shubhrai23 fixed a bug where create a clone of a project would place the clone in the root of the project instead as a child object of the select dpart ([PR#31978](https://github.com/FreeCAD/FreeCAD/pull/31978)).
- PaddleStroke added point patterns as part of work on arrays in ([PR#32763](https://github.com/FreeCAD/FreeCAD/pull/32763)).
- alfrix fixed a bug where the Hole Parameter window would not show the custom head value after project save and reopen ([PR#32889](https://github.com/FreeCAD/FreeCAD/pull/32889)).
- maxwxyz fixed a regression where dressup previews would be rendered in the wrong color ([PR#32748](https://github.com/FreeCAD/FreeCAD/pull/32748)).
- greggjaskiewicz patched the Part code to preserve seam edges during face refinement to maintain closed wires ([PR#32730](https://github.com/FreeCAD/FreeCAD/pull/32730)).
- aw-engineer made it possible to use SubShapeBinders as Profile in FeaturePipe ([PR#31786](https://github.com/FreeCAD/FreeCAD/pull/31786)).

## Assembly

PaddleStroke added commands and the shared task panel for LinkArray tools ([PR#32688](https://github.com/FreeCAD/FreeCAD/pull/32688)) and integrated the tools into Assembly ([PR#32762](https://github.com/FreeCAD/FreeCAD/pull/32762)).

## CAM

This workbench continues to be probably the most actively developed one these days. 19 pull requests were merged, including these patches:

- sliptonic made the first step towards support for tilted workplanes and made it possible to have shared workplanes held by the Job and manage them ([PR#32722](https://github.com/FreeCAD/FreeCAD/pull/32722)). He also added a Machine-based postprocessor for Heidenhain ([PR#32863](https://github.com/FreeCAD/FreeCAD/pull/32863)), and fixed several bugs ([PR#32043](https://github.com/FreeCAD/FreeCAD/pull/32043), [PR#32513](https://github.com/FreeCAD/FreeCAD/pull/32513), [PR#32615](https://github.com/FreeCAD/FreeCAD/pull/32615), [PR#32366](https://github.com/FreeCAD/FreeCAD/pull/32366)).
- tarman3 added depth parameters checks to Pocket Shape ([PR#32573](https://github.com/FreeCAD/FreeCAD/pull/32573)), made LeadInOut skip zero length plunge moves ([PR#32257](https://github.com/FreeCAD/FreeCAD/pull/32257)), exposed a bunch of new properties in the Helix task panel ([PR#31620](https://github.com/FreeCAD/FreeCAD/pull/31620)), and fixed the processing of vertical faces in Profile in certain scenarios ([PR#31259](https://github.com/FreeCAD/FreeCAD/pull/31259)).
- Dimitris75 fixed several bugs in the planar surfaces code ([PR#32766](https://github.com/FreeCAD/FreeCAD/pull/32766)).
- Connor added the wire EDM toolhead type ([PR#32485](https://github.com/FreeCAD/FreeCAD/pull/32485)).
- davidgilkaufman fixed an flipped arc bug in OffsetWire ([PR#32703](https://github.com/FreeCAD/FreeCAD/pull/32703)) and fixed incorrect cycle time estimates on long, shallow horizontal-speed ramp entrances ([PR#32170](https://github.com/FreeCAD/FreeCAD/pull/32170)).

## FEM

- marioalexis84 fixed the usability of the FEM unit scheme and added the momentum unit *N⋅mm* ([PR#31013](https://github.com/FreeCAD/FreeCAD/pull/31013)).
- oursland fixed a crash ([PR#32871](https://github.com/FreeCAD/FreeCAD/pull/32871)).

## BIM

Roy-043 prevented the conversion of temporary Draft objects in Native IFC ([PR#31592](https://github.com/FreeCAD/FreeCAD/pull/31592)), fixed the flipping of the default structure extrusion direction ([PR#32244](https://github.com/FreeCAD/FreeCAD/pull/32244)), several IFC import issues ([PR#31940](https://github.com/FreeCAD/FreeCAD/pull/31940), [PR#31801](https://github.com/FreeCAD/FreeCAD/pull/31801)), and a few more bugs. He also made it possible for walls based on lines or sketches to handle expressions for the Length property ([PR#32806](https://github.com/FreeCAD/FreeCAD/pull/32806)).

## TechDraw

- WandererFan fixed section cut shape positioning ([PR#31921](https://github.com/FreeCAD/FreeCAD/pull/31921)) and PAT hatches and color changes not rendering on the page ([PR#32791](https://github.com/FreeCAD/FreeCAD/pull/32791)).
- mohamed-khairy-swe fixed centering in balloon rectangular shape with separators ([PR#31591](https://github.com/FreeCAD/FreeCAD/pull/31591)).
- MortenVajhoj added a Screen mode to help deal with situations where you zoom in on complex models, and bits of geometry start obstructing other bits of geometry ([PR#32180](https://github.com/FreeCAD/FreeCAD/pull/32180)). He also made it possible to move view TD view captions around (with snapping) and edit them directly on the page ([PR#32216](https://github.com/FreeCAD/FreeCAD/pull/32216)):

{{< video src="td-captions-snapping-and-editing.mp4" >}}

## Other changes

- For people who don't use the toolbar all that much, maxwxyz added a Create group under Tools with commands for creating a new part, part datums, a new group, and other items ([PR#31435](https://github.com/FreeCAD/FreeCAD/pull/31435)).
- pavliha added support for the pinch gesture and two-finger scroll panning on Apple trackpads ([PR#32030](https://github.com/FreeCAD/FreeCAD/pull/32030)).
- Lgt2x started preparing the code for dropping Qt5 compatibility ([PR#29470](https://github.com/FreeCAD/FreeCAD/pull/29470)).

Additional improvements and fixes were contributed by 007stevendigar-lgtm, 3x380V, AjinkyaDahale, alfrix, awgrover, chennes, Connor, davesrocketshop, davidgilkaufman, ElementW, jffmichi, Irvinwop, kadet1090, Kuzma30, Lgt2x, Lokestrom, maxwxyz, mnesarco, oursland, PaddleStroke, shubhrai23, tritao, WandererFan, and wmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.09.23).

## Activity stats

**PR stats**: since the previous report, 98 pull requests have been merged, and 53 new pull requests have been opened.

**Issue stats**: overall, there are 3446 open issues in the tracker, down by 47 from last week.
