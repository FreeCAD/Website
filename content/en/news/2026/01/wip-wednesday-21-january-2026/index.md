---
title: WIP Wednesday, 21 January 2026
date: 2026-01-21
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 18 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**Draft**: Roy-043 fixed snapping to geometry when the object under the cursor is not snappable, e.g., an image ([PR#26966](https://github.com/FreeCAD/FreeCAD/pull/26966)). He also fixed incorrect geometry saving when exporting DXF ([PR#26953](https://github.com/FreeCAD/FreeCAD/pull/26953)).

**Sketcher**:

- wmayer fixed a bug where trying to transform a sketch activates sketch edit mode instead of the transform dialog (cherry-picked by PaddleStroke, [PR#27063](https://github.com/FreeCAD/FreeCAD/pull/27063)).
- PaddleStroke fixed a box selection regression ([PR#26869](https://github.com/FreeCAD/FreeCAD/pull/26869))
- Syres916 fixed objects not rendered in the 3D viewport ([PR#27004](https://github.com/FreeCAD/FreeCAD/pull/27004)) and the setting of vertex size for new sketches ([PR#26908](https://github.com/FreeCAD/FreeCAD/pull/26908)).
- YashSuthar983 fixed a bug where external geometry couldn't be created from local coordinate systems ([PR#26946](https://github.com/FreeCAD/FreeCAD/pull/26946)).
- [PR#27033](https://github.com/FreeCAD/FreeCAD/pull/27033)

**Part and PartDesign:**
- kadet1090 fixed a regression so that the visuals wouldn't be recomputed when shapes don't change ([PR#26992](https://github.com/FreeCAD/FreeCAD/pull/26992)) and a release blocker where FreeCAD would produce invalid geometry from a file that works in v1.0.2 ([PR#27016](https://github.com/FreeCAD/FreeCAD/pull/27016)).
- PaddleStroke enabled LCS in **Move Feature After** ([PR#27022](https://github.com/FreeCAD/FreeCAD/pull/27022)).

**CAM**:

- Connor fixed the installation and packaging of the newly added machine editor ([PR#26940](https://github.com/FreeCAD/FreeCAD/pull/26940)) and added a tapered ball nose toolbit/shape asset ([PR#26988](https://github.com/FreeCAD/FreeCAD/pull/26988) and [PR#26989](https://github.com/FreeCAD/FreeCAD/pull/26989)).
- tarman3 fixed a regression in the Drilling operation ([PR#26827](https://github.com/FreeCAD/FreeCAD/pull/26827)).

**BIM/Arch**:

- Roy-043 fixed a crash that occurred when choosing the **Array tools** command ([PR#27060](https://github.com/FreeCAD/FreeCAD/pull/27060)), an incorrect placement of external referenced objects ([PR#26984](https://github.com/FreeCAD/FreeCAD/pull/26984)), and another placement issue in BIM_View ([PR#27015](https://github.com/FreeCAD/FreeCAD/pull/27015)).
- furgo16 added unit tests for vertical area calculation in Arch Component objects ([PR#26874](https://github.com/FreeCAD/FreeCAD/pull/26874)).

**Other changes**:

- PaddleStroke fixed a crash in Assembly ([PR#26949](https://github.com/FreeCAD/FreeCAD/pull/26949)).
- Lgt2x added compatibility with VTK 9.6, which is about to be released ([PR#25825](https://github.com/FreeCAD/FreeCAD/pull/25825)).
- graelo added QuickLook extensions for FCStd files on macOS, so that users can preview these files directly in Finder ([PR#25239](https://github.com/FreeCAD/FreeCAD/pull/25239)).
- WandererFan fixed frame and vertex behaviour in TechDraw ([PR#27009](https://github.com/FreeCAD/FreeCAD/pull/27009)).

YashSuthar983, maxwxyz, petterreinholdtsen, PaddleStroke, ipatch, and mnesarco contributed additional improvements and fixes.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.01.21).

**PR stats**: since the previous report, 50 pull requests have been merged (including backports to the v1.1 branch), and 36 new pull requests have been opened.

**Issue stats**: overall, there are 3178 open issues in the tracker, up by 14 from last week. There are 10 release blockers for v1.1 currently, up by 4 from last week.