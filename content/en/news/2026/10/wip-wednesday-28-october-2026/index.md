---
title: WIP Wednesday, 28 October 2026
date: 2026-10-28
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


The FreeCAD team has been eliminating blocking issues in preparation for the v26.3 release.

Of 44 pull requests merged in the last 7 days, 15 were backports from the main development branch to the dedicated 26.3 release branch. This overview focuses on the work in the main branch only.

## Part and PartDesign

UnKabaraQuiDev fixed three path pattern issues in PartDesign ([PR#33865](https://github.com/FreeCAD/FreeCAD/pull/33865) and [PR#33822](https://github.com/FreeCAD/FreeCAD/pull/33822)).

## Assembly

- GeeBee2 fixed a bug where a subshape binder surface couldn’t be used for mating correctly ([PR#33835](https://github.com/FreeCAD/FreeCAD/pull/33835)).
- Ayushjo fixed a bug where double-clicking an exploded view tree node would apply explosion to the normal drawing in a certain scenario ([PR#32497](https://github.com/FreeCAD/FreeCAD/pull/32497)).

## TechDraw

WandererFan fixed a bug where it was impossible to create an angle dimension on a chamfer of a cylinder ([PR#33820](https://github.com/FreeCAD/FreeCAD/pull/33820)). He also fixed an unwanted rotation of detail geometry in axonometric view ([PR#33833](https://github.com/FreeCAD/FreeCAD/pull/33833)) and two issues related to cosmetic object deletion ([PR#33880](https://github.com/FreeCAD/FreeCAD/pull/33880)).


## Other changes

- DesignWeaver3D fixed a Trimex issue in Draft ([PR#33619](https://github.com/FreeCAD/FreeCAD/pull/33619)).
- Connor fixed a bug with a round stock in the Adaptive command in CAM ([PR#33705](https://github.com/FreeCAD/FreeCAD/pull/33705)).
- tritao fixed Spreadsheet numeric values changing after saving and reopening a document ([PR#32464](https://github.com/FreeCAD/FreeCAD/pull/32464)).

Additional improvements and fixes were contributed by 3x380V, Ayushjo, chennes, flaviut, gudnimg, MortenVajhoj, PhoneDroid, xSetech, and xtemp09.

If you want to test the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.10.28).

## Activity stats

**PR stats**: since the previous report, 44 pull requests have been merged, and 39 new pull requests have been opened.

**Issue stats**: overall, there are 3517 open issues in the tracker, up by 22 from last week (normal when release candidates start getting tested). There are currently 5 unresolved blocker issues for v26.3.
