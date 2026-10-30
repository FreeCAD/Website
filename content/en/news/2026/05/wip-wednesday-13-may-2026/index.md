---
title: WIP Wednesday, 13 May 2026
date: 2026-05-13
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

## Part and PartDesign

- wwmayer fixed a bug where Part would accept an invalid attachment, leading to Sketcher creating empty sketches ([PR#29958](https://github.com/FreeCAD/FreeCAD/pull/29958)), a crash when adding fillets ([PR#29932](https://github.com/FreeCAD/FreeCAD/pull/29932)), and another bug where FreeCAD would crash whenever linear pattern iterations reached 10 ([PR#29935](https://github.com/FreeCAD/FreeCAD/pull/29935)). All these fixes (and at least half a dozen of others, also by wwmayer) were cherry-picked by maxwxyz.
- semedooo patched the material library widget to update when the face selection changes ([PR#28734](https://github.com/FreeCAD/FreeCAD/pull/28734)).
- xorza fixed the code to make subshapebinders work correctly on overlapping geometry ([PR#29249](https://github.com/FreeCAD/FreeCAD/pull/29249)).
- ItSaulGoodMan fixed a crash that occurred when changing the Pad type to Up To Face ([PR#30022](https://github.com/FreeCAD/FreeCAD/pull/30022)) and a bug where WireJoiner would abort on non-closed traversal paths ([PR#29640](https://github.com/FreeCAD/FreeCAD/pull/29640)).
- PaddleStroke added on-view parameters to the Pattern tool for overriding the spacing defined in the task panel ([PR#23997](https://github.com/FreeCAD/FreeCAD/pull/23997)).
- maxwxyz added statusbar hints for draggers for ([PR#29631](https://github.com/FreeCAD/FreeCAD/pull/29631)). He also changed the program's behavior to toggle the visibility of the parent body instead of the last visible feature with the spacebar ([PR#29110](https://github.com/FreeCAD/FreeCAD/pull/29110)).

## CAM

- sliptonic added several usability improvements ([PR#29861](https://github.com/FreeCAD/FreeCAD/pull/29861)) and a dedicated rotary surface operation ([PR#29751](https://github.com/FreeCAD/FreeCAD/pull/29751)). The new op is intended for 4th-axis surfacing, but the underlying path generators may be useful for lathe operations later on.
- awgrover contributed fixes to tests ([PR#29880](https://github.com/FreeCAD/FreeCAD/pull/29880) and [PR#29886](https://github.com/FreeCAD/FreeCAD/pull/29886)), added a return mode to drill commands ([PR#29892](https://github.com/FreeCAD/FreeCAD/pull/29892)), and improved DrillCycleExpander ([PR#30112](https://github.com/FreeCAD/FreeCAD/pull/30112)).
- tarman3 fixed the trimming in path approximation ([PR#29525](https://github.com/FreeCAD/FreeCAD/pull/29525)), a precision error in Engrave ([PR#29897](https://github.com/FreeCAD/FreeCAD/pull/29897)), and a bug in copying tags in DressupTag ([PR#29877](https://github.com/FreeCAD/FreeCAD/pull/29877)).
- soruh made CAM leaner and eating fewer system resources when capturing backtraces ([PR#29092](https://github.com/FreeCAD/FreeCAD/pull/29092)).

## Other changes

- PaddleStroke fixed a bug in Assembly where grounded objects could still be moved ([PR#28087](https://github.com/FreeCAD/FreeCAD/pull/28087)).
- tritao fixed a bug in the core where selection filters would block selection instead of trying to pick the nearby entities ([PR#29705](https://github.com/FreeCAD/FreeCAD/pull/29705)).
- vovodroid fixed the orientation of datum labels when the view is rotated in Sketcher ([PR#29569](https://github.com/FreeCAD/FreeCAD/pull/29569)).
- WandererFan added warnings about incorrect geometry to TechDraw ([PR#29255](https://github.com/FreeCAD/FreeCAD/pull/29255)).
- NewJoker improved the readability of CalculiX preferences in FEM ([PR#30099](https://github.com/FreeCAD/FreeCAD/pull/30099)).
- greg19 redesigned the Keyboard Shortcuts user interface and moved it to the General section of the Preferences dialog ([PR#27725](https://github.com/FreeCAD/FreeCAD/pull/27725)).
- MortenVajhoj added on-view icons for the center of gravity and the center of volume for the Measure tool ([PR#29288](https://github.com/FreeCAD/FreeCAD/pull/29288)).
- triatao added rubberband selection to the 3D view ([PR#29547](https://github.com/FreeCAD/FreeCAD/pull/29547)).

{{< video src="3d-view-rubberband-selection.mp4" >}}

Additional improvements and fixes were contributed by 3x380V, alfrix, andershol, boomskats, chennes, coldtobi, danieljimol, ElementW, ItSaulGoodMan, Maik-0000FF, maxwxyz, rehan-ahmed-aix, Roy_043, tarman3, tritao, wwmayer, and z0r0.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.05.13).

## Activity stats

**PR stats**: since the previous report, 81 pull requests have been merged, and 76 new pull requests have been opened.

**Issue stats**: overall, there are 3441 open issues in the tracker, up by 5 from last week.
