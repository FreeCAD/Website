---
title: WIP Wednesday, 4 November 2026
date: 2026-11-04
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---

The FreeCAD team has been eliminating blocking issues in preparation for the v26.3 release. Of the 75 pull requests merged in the last 7 days, 30 have been backports from the main development branch to the dedicated 26.3 release branch. This overview focuses on the work in the main branch only.

## Part and PartDesign

- Ayushjo fixed a regression where Pipe would fail when you pick a section or the profile by clicking an edge of a sketch in the 3D view (PR#33971). They also fixed part builder and box selection picking faces of hidden parts ([PR#33540](https://github.com/FreeCAD/FreeCAD/pull/33971)).
- YashSuthar983 fixed a crash that occurred after creating a shapebinder ([PR#33967](https://github.com/FreeCAD/FreeCAD/pull/33967)).
- maxwxyz patched booleans to recompute after placement changes ([PR#33357](https://github.com/FreeCAD/FreeCAD/pull/33357)).

## CAM

- davidgilkaufman fixed the Adaptive operation in rest machining as part of his work on clipper migration ([PR#33909](https://github.com/FreeCAD/FreeCAD/pull/33909)). He also fixed the final depth pass sometimes missing from Pocket ([PR#33917](https://github.com/FreeCAD/FreeCAD/pull/33917)).
- sliptonic cleaned up postprocessor testing code ([PR#33584](https://github.com/FreeCAD/FreeCAD/pull/33584)).
- tarman3 fixed combineHorizontalFaces ([PR#33784](https://github.com/FreeCAD/FreeCAD/pull/33784)) and incorrect definitions for closed B‑spline edges ([PR#33488](https://github.com/FreeCAD/FreeCAD/pull/33488)).

## BIM

- furgo16 moved NativeIFC unit tests into the BIM test suite, so that CI would run them ([PR#32846](https://github.com/FreeCAD/FreeCAD/pull/32846)).
- Roy-043 added regression tests for TD View window/door floorplan symbols ([PR#34082](https://github.com/FreeCAD/FreeCAD/pull/34082)).
- matthijskooijman fixed the rendering of window/door floorplan symbols ([PR#32672](https://github.com/FreeCAD/FreeCAD/pull/32672)).

## Other changes

- WandererFan fixed section lines being drawn on top of vertices/center marks and thus blocking their selection ([PR#33979](https://github.com/FreeCAD/FreeCAD/pull/33979)).
- marbocub fixed a bug in Sketcher where continuous dragging could trigger CarbonCopy multiple times ([PR#29104](https://github.com/FreeCAD/FreeCAD/pull/29104)).
- x2605 fixed colors not exported to STEP and IGES ([PR#33922](https://github.com/FreeCAD/FreeCAD/pull/33922)).
- PaddleStroke fixed an arcane release blocker ([PR#34000](https://github.com/FreeCAD/FreeCAD/pull/34000)).
- Lokerstrom updated the Measure tool to disqualify unbounded planes from area measurement ([PR#31769](https://github.com/FreeCAD/FreeCAD/pull/31769)).

Additional improvements and fixes were contributed by 3x380V, adrianinsaval, anshurajbisoyi98-ctrl, Ayushjo, chennes, flaviut, furgo16, greggjaskiewicz, gudnimg, ipatch, Lgt2x, maxwxyz, nm2107, PhoneDroid, Prakhar1808, sliptonic, xSetech, and xtemp09.

If you want to test the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.11.04).

## Activity stats

**PR stats**: since the previous report, 75 pull requests have been merged, and 42 new pull requests have been opened.

**Issue stats**: overall, there are 3507 open issues in the tracker, down by 10 from last week. There are currently 2 unresolved blocker issues for v26.3, down by 3 from last week.
