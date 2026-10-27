---
title: WIP Wednesday, 7 October 2026
date: 2026-10-07
author: Aleksandr Prokudin
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


The FreeCAD team has switched to preparing for the release of FreeCAD 26.3, the first one under the new versioning scheme. They are now focused on polishing the release branch and preparing the first release candidate. There will be a separate announcement about that.

Out of 93 pull requests merged in the last 7 days, 36 have been backports from the main development branch to the dedicated 26.3 release branch. This overview focuses on the work in the main branch only,

## Sketcher

- Reqrefusion fixed a bug where moving a sketch point slightly would snap it back to the previous position ([PR#32614](https://github.com/FreeCAD/FreeCAD/pull/32614)).
- theo-vt fixed occasionally disappearing icons in the toolbar ([PR#32530](https://github.com/FreeCAD/FreeCAD/pull/32530)).
- 3x380V fixed a segmentation fault ([PR#33177](https://github.com/FreeCAD/FreeCAD/pull/33177)).

## Part and PartDesign

- maxwxyz added datum commands to the Create menu ([PR#33207](https://github.com/FreeCAD/FreeCAD/pull/33207)) and fixed a regression where for dressup features, the entire solid would be rendered in magenta preview color ([PR#33197](https://github.com/FreeCAD/FreeCAD/pull/33197)).
- oursland fixed a crash in setting a preview color ([PR#33163](https://github.com/FreeCAD/FreeCAD/pull/33163)).
- PaddleStroke added interactive pattern suppression controls ([PR#33071](https://github.com/FreeCAD/FreeCAD/pull/33071)) and exposed circular, path, and point pattern tools in PD commands, menus, toolbars, and view providers ([PR#33072](https://github.com/FreeCAD/FreeCAD/pull/33072)).

## CAM

- Rimas2200 added geometry verification for each cutting pass ([PR#33113](https://github.com/FreeCAD/FreeCAD/pull/33113)).
- Dimitris75 patched Planar Surfaces to fix the 'Avoid faces boundary' offset for Safe STL ([PR#33053](https://github.com/FreeCAD/FreeCAD/pull/33053)).
- davidgilkaufman fixed Clipper arc fitting ([PR#33049](https://github.com/FreeCAD/FreeCAD/pull/33049)).

## Other changes

- Roy-043 made the new Draft_UpdateShape2DView command available from the Draft menu ([PR#33121](https://github.com/FreeCAD/FreeCAD/pull/33121)).
- MortenVajhoj fixed screen mode exports throughout the workbench ([PR#32949](https://github.com/FreeCAD/FreeCAD/pull/32949)).
- Ads9115 fixed the overlay panel remaining visible over the Start page ([PR#33297](https://github.com/FreeCAD/FreeCAD/pull/33297)).

Additional improvements and fixes were contributed by andershol, Ayushjo, chennes, davidgilkaufman, flaviut, Lgt2x, Lihis, Maik-0000FF, marioalexis84, maxwxyz, MortenVajhoj, n3orma, obelisk79, oursland, PaddleStroke, rblenis, UnKabaraQuiDev, and WandererFan.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.10.07).

## Activity stats

**PR stats**: since the previous report, 93 pull requests have been merged, and 58 new pull requests have been opened.

**Issue stats**: overall, there are 3442 open issues in the tracker, up by 5 from last week.
