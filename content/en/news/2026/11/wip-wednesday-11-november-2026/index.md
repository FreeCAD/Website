---
title: WIP Wednesday, 11 November 2026
date: 2026-11-11
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---

The FreeCAD team has been eliminating blocking issues ahead of the v26.3 release. Of the 119 pull requests merged in the last 7 days, 42 have been backports from the main development branch to the dedicated 26.3 release branch. This overview focuses on the work in the main branch only.

## Sketcher

- UnKabaraQuiDev patched the Perpendicular Constraint tool to support arcs ([PR#31824](https://github.com/FreeCAD/FreeCAD/pull/31824)).
- flaviut improved the text dialog’s user interface ([PR#32735](https://github.com/FreeCAD/FreeCAD/pull/32735)).
- VishalRamKN added a user-visible explanation why the fillet/chamfer vertex selection is blocked for curves ([PR#32759](https://github.com/FreeCAD/FreeCAD/pull/32759)).
- chennes removed the code that forbids creating redundant constraints ([PR#34123](https://github.com/FreeCAD/FreeCAD/pull/34123)).
- PaddleStroke fixed several issues in the B‑Spline-to-NURBS converter ([PR#32504](https://github.com/FreeCAD/FreeCAD/pull/32504)).
- Ayushjo fixed the handling of internal geometry when splitting ([PR#33592](https://github.com/FreeCAD/FreeCAD/pull/33592)).

## Assembly

- Rchiemstra fixed the joint offset on link-array elements ([PR#34146](https://github.com/FreeCAD/FreeCAD/pull/34146)).
- maxwxyz updated the Revolute joint’s angle to allow angle limits up to +/-360 degrees ([PR#34182](https://github.com/FreeCAD/FreeCAD/pull/34182)).
- GeeBee2 fixed the exploded lines ([PR#33936](https://github.com/FreeCAD/FreeCAD/pull/33936)).

## TechDraw

- WandererFan fixed curved splines displayed as straight ([PR#34137](https://github.com/FreeCAD/FreeCAD/pull/34137)).
- Ayushjo fixed a crash that occurred after removing a cosmetic edge vertex or centerline ([PR#34222](https://github.com/FreeCAD/FreeCAD/pull/34222)) and another crash on canceling in-line decoration ([PR#34171](https://github.com/FreeCAD/FreeCAD/pull/34171)).
- fatalwir fixed composite hit shapes of Balloon Annotations and Leader Lines ([PR#34007](https://github.com/FreeCAD/FreeCAD/pull/34007)).

## CAM

- Connor fixed a bug where Helix would take a counterbore and the hole under it for one hole, as they share a center, and drop the smaller one, so the bore was oversized or left uncut ([PR#34027](https://github.com/FreeCAD/FreeCAD/pull/34027)). He also fixed Z positioning on simulator helix arcs ([PR#34026](https://github.com/FreeCAD/FreeCAD/pull/34026)).
- davidgilkaufman ported the Adaptive operation to clipper2 ([PR#33739](https://github.com/FreeCAD/FreeCAD/pull/33739)).
- tarman3 updated task panels of Profile and PocketShape ([PR#33100](https://github.com/FreeCAD/FreeCAD/pull/33100)).

## Other changes

- Point after closing a document with another workbench active ([PR#34125](https://github.com/FreeCAD/FreeCAD/pull/34125)).
- flaviut optimized the thread generation code in PartDesign to work faster ([PR#34132](https://github.com/FreeCAD/FreeCAD/pull/34132)).
- Kirmy34 patched the Measure tool to attach the length label to the edge midpoint ([PR#33144](https://github.com/FreeCAD/FreeCAD/pull/33144)).

Additional improvements and fixes were contributed by 3x380V, adrianinsaval, alfrix, Ayushjo, chennes, Connor, GeeBee2, kanginXD, marioalexis84, maxwxyz, PhoneDroid, pieterhijma, relikd, sliptonic, sosakubito-cyber, and YashSuthar983.

If you want to test the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.11.11).

## Activity stats

**PR stats**: since the previous report, 119 pull requests have been merged, and 45 new pull requests have been opened.

**Issue stats**: overall, there are 3514 open issues in the tracker, up by 7 from last week. There is currently 1 unresolved blocker issue for v26.3, down by 1 from last week.