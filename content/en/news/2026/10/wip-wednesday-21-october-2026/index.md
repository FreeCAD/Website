---
title: WIP Wednesday, 21 October 2026
date: 2026-10-21
author: Aleksandr Prokudin
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


The FreeCAD team has been hard at work eliminating blocking issues in preparation for the v26.3 release.

Out of 89 pull requests merged in the last 7 days, 38 have been backports from the main development branch to the dedicated 26.3 release branch. This overview focuses on the work in the main branch only.

## CAM

- sliptonic added a postprocessor for DynaPath control ([PR#33174](https://github.com/FreeCAD/FreeCAD/pull/33174)).
- faecorrigan created a brand new EstlCam postprocessor with more features ([PR#33229](https://github.com/FreeCAD/FreeCAD/pull/33229)).
- Connor fixed the speed readout's invisibility in the simulator ([PR#33633](https://github.com/FreeCAD/FreeCAD/pull/33633)).
- davidgilkaufman fixed Clipping arc fitting ([PR#33284](https://github.com/FreeCAD/FreeCAD/pull/33284)).

## Other changes

- DesignWeaver3D fixed two bugs in Trimex (Draft): start/end points swapping ([PR#33442](https://github.com/FreeCAD/FreeCAD/pull/33442)) and not accounting for Placement rotation when working on arcs ([PR#33463](https://github.com/FreeCAD/FreeCAD/pull/33463)).
- maxwxyz fixed Sketcher toolbars disappearing when switching documents ([PR#33554](https://github.com/FreeCAD/FreeCAD/pull/33554)).
- WandererFan fixed a bug where TechDraw-projected shapes would deviate from the body for curves/splines ([PR#33707](https://github.com/FreeCAD/FreeCAD/pull/33707)).

Additional improvements and fixes were contributed by 28arnab, 3x380V, Chaitanya-970, chennes, Connor, DesignWeaver3D, ElementW, flaviut, gudnimg, Lgt2x, Lokestrom, maxwxyz, mnesarco, relikd, sliptonic, theo-vt, UnKabaraQuiDev, VishalRamKN, WandererFan, wwmayer, and xtemp09.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.10.21).

## Activity stats

**PR stats**: since the previous report, 89 pull requests have been merged, and 29 new pull requests have been opened.

**Issue stats**: overall, there are 3495 open issues in the tracker, up by 17 from last week (normal when release candidates start getting tested). There are currently 5 unresolved blocker issues for v26.3.
