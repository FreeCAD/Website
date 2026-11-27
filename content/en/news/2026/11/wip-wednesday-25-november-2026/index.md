---
title: WIP Wednesday, 25 November 2026
date: 2026-11-25
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---

The FreeCAD team has been eliminating blocking issues in preparation for the v26.3 release. Of the 61 pull requests merged in the last 7 days, 20 have been backports from the main development branch to the dedicated 26.3 release branch. This overview focuses on the work in the main branch only.

## Part

pieterhijma ensured that FreeCAD builds with upcoming OpenCascade 8.1 that will feature long-anticipated fillet/chamfer fixes, among other things [(PR#33062)](https://github.com/FreeCAD/FreeCAD/pull/33062).

## CAM

Almost a third of patches these past 7 days were for the CAM workbench.

- tarman3 added automatic tags generation while recomputing [(PR#31760)](https://github.com/FreeCAD/FreeCAD/pull/31760), fixed an incorrect post-processing warning [(PR#34372)](https://github.com/FreeCAD/FreeCAD/pull/34372), fixed Helix producing negative feedrates [(PR#33993)](https://github.com/FreeCAD/FreeCAD/pull/33993), and applied a few improvements to Sanity [(PR#32576)](https://github.com/FreeCAD/FreeCAD/pull/32576).
- sliptonic removed support for CAMotics simulation because there hasn’t been a proper release of CAMotics since 2019, and simulation in FreeCAD is going in a different direction [(PR#34461)](https://github.com/FreeCAD/FreeCAD/pull/34461). He also fixed the position of the bCNC block headers in machine-based post-processing [(PR#34417)](https://github.com/FreeCAD/FreeCAD/pull/34417).
- davidosterberg patched Adaptive to use RampFeed for helix entry, so that the feed rate is lower or higher depending on where the toolbit is with regard to the stepdown level [(PR#33938)](https://github.com/FreeCAD/FreeCAD/pull/33938).
- Ayushjo fixed spiral facing adjustment [(PR#33954)](https://github.com/FreeCAD/FreeCAD/pull/33954).
- davidgilkaufman fixed operations getting marked as dirty after getClearedArea is called [(PR#34410)](https://github.com/FreeCAD/FreeCAD/pull/34410) and failures in the test suite [(PR#34330)](https://github.com/FreeCAD/FreeCAD/pull/34330).
- Connor fixed bugs in machine file editing [(PR#34506)](https://github.com/FreeCAD/FreeCAD/pull/34506) and failing to open a job’s task panel [(PR#34518)](https://github.com/FreeCAD/FreeCAD/pull/34518).

## BIM

- Roy-043 fixed the IFC exports of Part compounds [(PR#31616)](https://github.com/FreeCAD/FreeCAD/pull/31616).
- Ayushjo fixed BIM views showing only the first material of a multi-material [(PR#34473)](https://github.com/FreeCAD/FreeCAD/pull/34473).

## Other changes

- TheBhowmik fixed a fatal runtime exception and UI crash in the Sketcher module when a user applies a redundant or conflicting dimensional constraint [(PR#32348)](https://github.com/FreeCAD/FreeCAD/pull/32348).
- pieterhijma fixed various issues with quantity expressions [(PR#34068)](https://github.com/FreeCAD/FreeCAD/pull/34068). He also contributed a patch that synchronizes the expression operator precedence with the precedence defined in the parser to prevent precedence issues with power and units [(PR#33728)](https://github.com/FreeCAD/FreeCAD/pull/33728).

Additional improvements and fixes were contributed by 28arnab, 3x380V, Ayushjo, chennes, davidosterberg, flaviut, ipatch, pieterhijma, tarman3, and TheBhowmik.

If you want to test the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.11.25).

## Activity stats

**PR stats**: since the previous report, 61 pull requests have been merged, and 40 new pull requests have been opened.

**Issue stats**: overall, there are 3535 open issues in the tracker, up by 21 from two weeks ago. There is currently 2 unresolved blocker issues for v26.3, up by 1 from two weeks ago.