---
title: WIP Wednesday, 8 April 2026
date: 2026-04-08
author: Aleksandr Prokudin
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


*It looks like the original post didn't show up on Wed/Thu here on the blog, but* [*was posted on the forum*](https://forum.freecad.org/viewtopic.php?p=882798#p882798)*. Not sure what the glitch was, but here is the post in its entirety on the blog as well, backdated for accuracy.*

Now that FreeCAD 1.1 is out, maintainers will keep backporting some changes from the main development branch to the 1.1 branch for future bugfix releases. There have been 12 such backports these last 7 days.

This week in FreeCAD development:

## Sketcher

- Bojan9597 fixed a blocker bug where adding external geometry would break sketch editing ([PR#29046](https://github.com/FreeCAD/FreeCAD/pull/29046)).
- theo-vt fixed a regression where a tangent constraint between circle/arc and line would always resolve to the same placement and ignore initial placement ([PR#29015](https://github.com/FreeCAD/FreeCAD/pull/29015)).
- PaddleStroke fixed a bug where ungrouped dimensions would move in the opposite direction of the mouse pointer movement ([PR#28294](https://github.com/FreeCAD/FreeCAD/pull/28294)).
- drwho495 fixed a toponaming regression where sketch internal faces would have unstable names ([PR#29043](https://github.com/FreeCAD/FreeCAD/pull/29043)).

## Part & PartDesign

- Bojan9597 fixed a bug where the attachment editor list item selection would get stuck on the wrong item ([PR#29010](https://github.com/FreeCAD/FreeCAD/pull/29010)).
- ipatch fixed an UX issue where pressing Esc on a Fillet popup would close the task panel, and the user would lose the selection ([PR#28131](https://github.com/FreeCAD/FreeCAD/pull/28131)).
- flaviut sped up text sketch extrusion by \~37% ([PR#28344](https://github.com/FreeCAD/FreeCAD/pull/28344)).
- wwmayer moved the common code of Revolution and Groove to a base class ([PR#25607](https://github.com/FreeCAD/FreeCAD/pull/25607), cherry-picked by 3x380V).
- rehan-ahmed-aix fixed Polar Pattern task panel labels ([PR#28960](https://github.com/FreeCAD/FreeCAD/pull/28960)).
- YashSuthar983 fixed a regression where Part Design boolean operations on two bodies inside a part container would fail ([PR#28955](https://github.com/FreeCAD/FreeCAD/pull/28955)).

## TechDraw

- maxwxyz added a Toggle Grid command to the right-click menu of the active TD page ([PR#29083](https://github.com/FreeCAD/FreeCAD/pull/29083)).
- ryankembrey patched the way vertices work: they now never show on "off", always show on "on", and respect toolbar command Toggle View Frames ([PR#28733](https://github.com/FreeCAD/FreeCAD/pull/28733)).
- ghatoleaakruti patched preferences to allow negative values for LineSpacingFactorISO, which can now go as low as -10.0 ([PR#28711](https://github.com/FreeCAD/FreeCAD/pull/28711)).

## Assembly

PaddleStroke added MP4 video exporting to the simulation feature, currently with the active viewport; there may be a PNG sequence with transparent background option further down the road ([PR#25307](https://github.com/FreeCAD/FreeCAD/pull/25307)). He also fixed a regression in the migration script that would result in fixed joints made in v1.1 having different results in v1.2 ([PR#29141](https://github.com/FreeCAD/FreeCAD/pull/29141)).

## CAM

- sliptonic fixed a bug where the new post-processing dialog would show for legacy post-processors as well ([PR#29065](https://github.com/FreeCAD/FreeCAD/pull/29065). He also added a guard against invalid or deprecated post-processor names in job templates ([PR#28870](https://github.com/FreeCAD/FreeCAD/pull/28870)).
- tarman3 added a RestMachining property to the Boundary dressup to allow skipping areas excluded by the boundary path ([PR#22994](https://github.com/FreeCAD/FreeCAD/pull/22994)). He also refactored the context menu for geometry, jobs, and profiles in the project tree to show more relevant options depending on what is selected ([PR#26492](https://github.com/FreeCAD/FreeCAD/pull/26492)).
- davidgilkaufman made the pocket offset stepover adaptive as needed to ensure it fully clears the region ([PR#28707](https://github.com/FreeCAD/FreeCAD/pull/28707)).

## BIM

- czarflix fixed a bug where native IFC objects would have a limited list of available IfcClass options ([PR#28994](https://github.com/FreeCAD/FreeCAD/pull/28994)).
- Roy-043 fixed invalid generation of BimLibrary URLs on Windows ([PR#28875](https://github.com/FreeCAD/FreeCAD/pull/28875) and renamed OutDiameter to OutsideDiameter and the Draft property group to Profile in ArchProfile ([PR#27856](https://github.com/FreeCAD/FreeCAD/pull/27856)).
- furgo16 contributed several changes:
  - Migrated ArchStructure API functions to the Arch module for consistency with the rest of objects ([PR#28893](https://github.com/FreeCAD/FreeCAD/pull/28893)).
  - Fixed Beam task panel crash when changing category after the first point ([PR#29050](https://github.com/FreeCAD/FreeCAD/pull/29050)). -Fixed MakeBlocks not working for baseless walls ([PR#28720](https://github.com/FreeCAD/FreeCAD/pull/28720)).
  - Improved the Site task panel's UX ([PR#28504](https://github.com/FreeCAD/FreeCAD/pull/28504)).
  - Decouple Beam and Column parameters ([PR#28896](https://github.com/FreeCAD/FreeCAD/pull/28896)).

## FEM

marioalexis84 contributed several changes:

- Updateed SolverCalculiX object created with an old FreeCAD version ([PR#29102](https://github.com/FreeCAD/FreeCAD/pull/29102)).
- Refactored the Z88 solver object, which now supports almost all elements, constraints, and loads available in the open source version of Z88 ([PR#28944](https://github.com/FreeCAD/FreeCAD/pull/28944)).
- Fixed the CalculiX constraint for plane and truss elements ([PR#28986](https://github.com/FreeCAD/FreeCAD/pull/28986)).

## Other changes

- slendidev added configurable snapping for gizmos ([PR#28384](https://github.com/FreeCAD/FreeCAD/pull/28384)).
- czarflix restored live size updates in Image Plane settings ([PR#28820](https://github.com/FreeCAD/FreeCAD/pull/28820)).
- tritao recently resumed his work on the rendering system; some of the results are: the NaviCube now works correctly on factional scaling ([PR#29128](https://github.com/FreeCAD/FreeCAD/pull/29128) and is now isolated and excluded from scene captures such as thumbnail generation ([PR#28943](https://github.com/FreeCAD/FreeCAD/pull/28943).
- ElementW fixed the file type filters in Open/Save dialog being too long ([PR#23209](https://github.com/FreeCAD/FreeCAD/pull/23209)).
- andershol patched the task panel to drop background transparency ([PR#29018](https://github.com/FreeCAD/FreeCAD/pull/29018)).

Additional improvements and fixes were contributed by 3x380V, Bojan9597, ElementW, Maik-0000FF, PaddleStroke, Roy-043, YashSuthar983, adrianinsaval, andershol, ayyaz20003, chennes, coldtobi, czarflix, davidgilkaufman, dependabot\[bot\], drwho495, filippor, flaviut, freecad-ci-runner, furgo16, ghatoleaakruti, greggjaskiewicz, ipatch, kadet1090, marioalexis84, maxwxyz, rehan-ahmed-aix, ryankembrey, slendidev, sliptonic, tarman3, theo-vt, tritao, wuhkuh.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.04.01).

## Activity stats

**PR stats**: since the previous report, 84 pull requests have been merged, and 113 new pull requests have been opened.

**Issue stats**: overall, there are 3370 open issues in the tracker, up by 19 from last week.
