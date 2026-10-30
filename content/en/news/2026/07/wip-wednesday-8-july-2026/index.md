---
title: WIP Wednesday, 8 July 2026
date: 2026-07-08
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

## Sketcher

- PaddleStroke fixed a crash that occurred when selecting external edges ([PR#30816](https://github.com/FreeCAD/FreeCAD/pull/30816)), an incorrect calculation of angle inputs in the OVP ([PR#30468](https://github.com/FreeCAD/FreeCAD/pull/30468)), and backported various bounding box improvements from RealThunder's fork ([PR#26291](https://github.com/FreeCAD/FreeCAD/pull/26291)).
- tritao improved the way Sketcher deals with invalid view projections ([PR#31073](https://github.com/FreeCAD/FreeCAD/pull/31073)).
- maxwxyz fixed the Dimension tool's imprecise hint when applying it to concentric circles ([PR#30944](https://github.com/FreeCAD/FreeCAD/pull/30944)).

## Part and PartDesign

- PaddleStroke contributed a couple of improvements to the pattern tools ([PR#31167](https://github.com/FreeCAD/FreeCAD/pull/31167) and [PR#31100](https://github.com/FreeCAD/FreeCAD/pull/31100)).
- maxwxyz patched the code to allow projecting internal sketch faces onto surfaces ([PR#30425](https://github.com/FreeCAD/FreeCAD/pull/30425)) and made bodies inside booleans visible if they are active ([PR#30002](https://github.com/FreeCAD/FreeCAD/pull/30002)).
- xorza fixed a regression with subshapebinders ([PR#31049](https://github.com/FreeCAD/FreeCAD/pull/31049)).

## Assembly

PaddleStroke added snapshots that allow saving multiple versions of the current state of an assembly (visible parts, positions, etc.) and switching between them in the project tree ([PR#25384](https://github.com/FreeCAD/FreeCAD/pull/25384)).

## CAM

- Connor changed the way the task panel is packed with widgets to better display available options ([PR#31158](https://github.com/FreeCAD/FreeCAD/pull/31158)) and improved the Holding Tags panel layout and coordinate display ([PR#30655](https://github.com/FreeCAD/FreeCAD/pull/30655)).
- awgrover fixed the annotations support in the Array dressup ([PR#31014](https://github.com/FreeCAD/FreeCAD/pull/31014)).
- tarmans3 fixed options visibility in the Helix op ([PR#31034](https://github.com/FreeCAD/FreeCAD/pull/31034)).

## FEM

NewJoker added two new example files: one with cavity (surface-to-surface) radiation ([PR#31175](https://github.com/FreeCAD/FreeCAD/pull/31175)) and one for heat conduction with radiation to ambient ([PR#31171](https://github.com/FreeCAD/FreeCAD/pull/31171)).

## BIM

Roy-043 fixed a bug where ArchView wouldn't auto-update after changes to the model ([PR#29404](https://github.com/FreeCAD/FreeCAD/pull/29404)) and another bug where the width and height of rectangle tubes were reversed ([PR#31168](https://github.com/FreeCAD/FreeCAD/pull/31168)).

## Other changes

- tritao patched the build system to make Coin and Pivy available as git submodules ([PR#30920](https://github.com/FreeCAD/FreeCAD/pull/30920)) and updated the bundled Coin version ([PR#31111](https://github.com/FreeCAD/FreeCAD/pull/31111)).
- kevenwyld fixed an issue where the auto-task view would not correctly hide and unhide the task panel when the transparent overlay was active ([PR#30561](https://github.com/FreeCAD/FreeCAD/pull/30561)).
- maxwxyz improved preselection colors ([PR#31050](https://github.com/FreeCAD/FreeCAD/pull/31050)) and added support for object selection in the tree view for the custom dragger ([PR#30943](https://github.com/FreeCAD/FreeCAD/pull/30943)).

Additional improvements and fixes were contributed by chennes, ElementW, jffmichi, kimimgo, kkchemboli, Lokestrom, maxwxyz, mnesarco, and tarithj.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.07.08).

## Activity stats

**PR stats**: since the previous report, 45 pull requests have been merged, and 62 new pull requests have been opened.

**Issue stats**: overall, there are 3495 open issues in the tracker, same as last week.

## Elsewhere in the community

Aleksander Sadowski got FreeCAD to show up in the [EU Open Source Solutions Catalogue](https://interoperable-europe.ec.europa.eu/eu-oss-catalogue/solutions/freecad).
