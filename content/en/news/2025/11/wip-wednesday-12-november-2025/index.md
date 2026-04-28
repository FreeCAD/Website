---
title: WIP Wednesday, 12 November 2025
date: 2025-11-12
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

**Sketcher**:

- Rexbas fixed a crash by removing unused UI icons ([PR#25162](https://github.com/FreeCAD/FreeCAD/pull/25162)).
- tetektoza fixed a bug that resulted in deleting hidden elements ([PR#25010](https://github.com/FreeCAD/FreeCAD/pull/25010)).
- PaddleStroke fixed the origin axis and planes indicator shown when editing sketches ([PR#20727](https://github.com/FreeCAD/FreeCAD/issues/20727)).

**TechDraw**:

- theo-vt patched the code to ensure the autodistribute parameter is consistent when going from a projection group to a view and back to a projection group in TaskProjGroup ([PR#25103](https://github.com/FreeCAD/FreeCAD/pull/25103)).
- Rexbas fixed TechDraw ignoring the "Zoom at Cursor" setting in Preferences ([PR#25160](https://github.com/FreeCAD/FreeCAD/pull/25160)).

**BIM/Draft**:

- Roy-043 fixed the bug where an empty human figure (for scale) would be created ([PR#25186](https://github.com/FreeCAD/FreeCAD/pull/25186)).
- Paullee0 fixed an issue in ArchStairs ([PR#25167](https://github.com/FreeCAD/FreeCAD/pull/25167)).

**FEM:**

- NewJoker changed categories of two FEM examples ([PR#25246](https://github.com/FreeCAD/FreeCAD/pull/25246)) and added a ccx capacitance two spheres example ([PR#25117](https://github.com/FreeCAD/FreeCAD/pull/25117)).
- marioalexis84 fixed CapacitanceBody default value ([PR#25148](https://github.com/FreeCAD/FreeCAD/pull/25148)).

**CAM**:

- Connor fixed a crash when the toolbit object has been deleted or is missing ([PR#25228](https://github.com/FreeCAD/FreeCAD/pull/25228)). He also fixed an infinite recompute loop when ToolBit properties use expressions ([PR#25039](https://github.com/FreeCAD/FreeCAD/pull/25039)).
- freckletonj wrote a preliminary patch for a bug that affected CAM jobs ([PR#25034](https://github.com/FreeCAD/FreeCAD/pull/25034)).
- tarman3 fixed the Slot task panel.

**Other changes**:

- Various small GUI fixes, crash fixes, and improvements by kadet1090 and chennes.
- depthoffocus fixed a release blocker where FreeCAD was not offering to save modified files on quitting the program ([PR#24876](https://github.com/FreeCAD/FreeCAD/issues/24876)).
- pjcreath fixed a few crashes in the measuring tool after an undo (F[PR#35129](https://github.com/FreeCAD/FreeCAD/pull/25129)).

Additional improvements and fixes were contributed by FlachyJoe, kadet1090, PaddleSgtroke, marbocub, ipatch, pyro9, chennes, marioalexis84, and NewJoker.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.11.12).

**PR stats**: since the previous report, 35 pull requests have been merged, and 47 new pull requests have been opened.

**Issue stats**: overall, there are 3049 open issues in the tracker, up by 17 from last week. There are 5 release blockers currently, down by 4 from last week. The list of blockers is revisited and updated on Monday merge meetings.

We merged a substantially large patch that reformats the source code. So we are waiting to see what bugs it spawns before cutting the release candidate