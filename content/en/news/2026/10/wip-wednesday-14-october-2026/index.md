---
title: WIP Wednesday, 14 October 2026
date: 2026-10-14
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


The FreeCAD team has switched to preparing for the release of FreeCAD 26.3, the first one under the new versioning scheme. They are now focused on polishing the release branch and preparing the second release candidate. There will be a separate announcement about that.

Out of 123 pull requests merged in the last 7 days, 59 have been backports from the main development branch to the dedicated 26.3 release branch. This overview focuses on the work in the main branch only.

## Draft

- DesignWeaver3D fix undo not restoring the shape after Trimex ([PR#33458](https://github.com/FreeCAD/FreeCAD/pull/33458)).
- Roy-043 fixed numerous buglets in Draft.

## Sketcher

- alfrix fixed a bug where a polyline would lose the last point after fillet trimmed its segments ([PR#32430](https://github.com/FreeCAD/FreeCAD/pull/32430)).
- UnKabaraQuiDev fixed a bug where chamfer would faik in Sketcher ([PR#33402](https://github.com/FreeCAD/FreeCAD/pull/33402)).

## Part and PartDesign

- maxwxyz removed redundant feature nesting when selecting a sketch as attachment support within a body ([PR#33315](https://github.com/FreeCAD/FreeCAD/pull/33315)). He also fixed a regression where dress-up bases would be out of sync when inserting new features ([PR#33376](https://github.com/FreeCAD/FreeCAD/pull/33376)) and patched PartDesign to preserve external body references when creating sketches ([PR#33222](https://github.com/FreeCAD/FreeCAD/pull/33222)).
- UnKabaraQuiDev fixed a bug where the first instance of a circular link pattern would always be missing ([PR#33537](https://github.com/FreeCAD/FreeCAD/pull/33537)) and a warning when trying to remove the first (identity) transformation in point and circular patterns ([PR#33444](https://github.com/FreeCAD/FreeCAD/pull/33444)).
- novalis increased box selection speed ([PR#32963](https://github.com/FreeCAD/FreeCAD/pull/32963)).
- PaddleStroke fixed a bug where Loft Section selection would not display updated names ([PR#33023](https://github.com/FreeCAD/FreeCAD/pull/33023)).

## TechDraw

- rblenis fixed a bug where the document was unnecessarily marked as modified and required saving ([PR#33150](https://github.com/FreeCAD/FreeCAD/pull/33150)).
- WandererFan fixed a bug where Dimension Repair would fail when when a dimension reference would not point to valid geometry after a model update ([PR#32151](https://github.com/FreeCAD/FreeCAD/pull/32151)) and fixed the positioning of locked view on loading ([PR#32552](https://github.com/FreeCAD/FreeCAD/pull/32552)).

## CAM

- davidosterberg patched the Mach3_Mach4 postprocessor to work with the new machine-based architecture ([PR#33406](https://github.com/FreeCAD/FreeCAD/pull/33406)).
- Dimitris75 continued working on Planar Surface: added inner holes preservation in boundary masks, cleaned up API, and fixed error messages ([PR#33165](https://github.com/FreeCAD/FreeCAD/pull/33165)).
- sliptonic added preliminary support for tilted workplanes to the LinuxCNC postprocessor ([PR#33254](https://github.com/FreeCAD/FreeCAD/pull/33254)). He also moved Planar Surface and Rotary Surface out of the list of experimental features and fixed a handful of bugs all around ([PR#33264](https://github.com/FreeCAD/FreeCAD/pull/33264)).
- faecorrigan fixed the template feature of the machine editor not populating the machine info correctly ([PR#33255](https://github.com/FreeCAD/FreeCAD/pull/33255)).
- jffmichi fixed a bug in the new simulator that would complain when links to dress-ups are used ([PR#33106](https://github.com/FreeCAD/FreeCAD/pull/33106)). He also fixed unintended diagonal moves in ramp method 4 ([PR#33109](https://github.com/FreeCAD/FreeCAD/pull/33109)).
- tarman3 fixed the ZigZag start point in OpArea ([PR#33087](https://github.com/FreeCAD/FreeCAD/pull/33087)).
- Connor fixed operations' start points not following WCS or model changes ([PR#33319](https://github.com/FreeCAD/FreeCAD/pull/33319)).

## Other changes

- chennes fixed two distinctive bugs related to showing and hiding linked objects in the project tree ([PR#33289](https://github.com/FreeCAD/FreeCAD/pull/33289)).
- pieterhijma fixed fine-grained recomputes in spreadsheets ([PR#33515](https://github.com/FreeCAD/FreeCAD/pull/33515)).
- marioalexis84 fixed the magnetodynamic writer for current density body force ([PR#33159](https://github.com/FreeCAD/FreeCAD/pull/33159)).
- MortenVajhoj fixed a density error in mass properties in the Measure tool ([PR#33380](https://github.com/FreeCAD/FreeCAD/pull/33380)).
- maxwxyz added support for group links and link arrays to Transform and Placement ([PR#33353](https://github.com/FreeCAD/FreeCAD/pull/33353)).
- GeeBee2 fixed rotation order in Assembly ([PR#33290](https://github.com/FreeCAD/FreeCAD/pull/33290)).
- Ayushjo group Extrude and Extrude Face on the toolbar in BIM ([PR#33512](https://github.com/FreeCAD/FreeCAD/pull/33512)).

Additional improvements and fixes were contributed by 3x380V, adrianinsaval, Ads9115, chennes, Connor, flaviut, ipatch, kkchemboli, Lgt2x, maxwxyz, mnesarco, oursland, Reqrefusion, Roy-043, tarman3, and WandererFan.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.10.14).

## Activity stats

**PR stats**: since the previous report, 123 pull requests have been merged, and 48 new pull requests have been opened.

**Issue stats**: overall, there are 3478 open issues in the tracker, up by 36 from last week (normal when release candidates start getting tested).
