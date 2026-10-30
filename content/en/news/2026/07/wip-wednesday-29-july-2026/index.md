---
title: WIP Wednesday, 29 July 2026
date: 2026-07-29
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

- maxwxyz added statusbar hints to pattern tools ([PR#31536](https://github.com/FreeCAD/FreeCAD/pull/31536)) and increased the contrast of the default face color ([PR#31369](https://github.com/FreeCAD/FreeCAD/pull/31369)).
- PaddleStroke fixed the Polyline parallel/perpendicular helper disappearing after an arc segment ([PR#31588](https://github.com/FreeCAD/FreeCAD/pull/31588)), a Polyline snapping bug ([PR#30579](https://github.com/FreeCAD/FreeCAD/pull/30579)), and another bug where the Move/Array transform tool would break constraints ([PR#30507](https://github.com/FreeCAD/FreeCAD/pull/30507)). He also added a symmetric mode to the Rotate tool ([PR#30747](https://github.com/FreeCAD/FreeCAD/pull/30747)).
- xorza fixed a regression related to preserving legacy internal face naming in older documents ([PR#31117](https://github.com/FreeCAD/FreeCAD/pull/31117)).
- ipatch fixed a bug where constraints could be lost when splitting an edge ([PR#31216](https://github.com/FreeCAD/FreeCAD/pull/31216)).

## Part and PartDesign

- alfrix fixed the M26 thread missing from Hole parameters ([PR#30770](https://github.com/FreeCAD/FreeCAD/pull/30770)).
- PaddleStroke fixed several bug in pattern tools ([PR#30851](https://github.com/FreeCAD/FreeCAD/pull/30851) and [PR#31496](https://github.com/FreeCAD/FreeCAD/pull/31496)).
- maxwxyz fixed two issues with boolean placement preservation ([PR#30575](https://github.com/FreeCAD/FreeCAD/pull/30575)).

## TechDraw

ryankembrey improved the selection of leader lines ([PR#30986](https://github.com/FreeCAD/FreeCAD/pull/30986)) and made it possible to open the task panel by double-clicking on a view or a projection group in the page ([PR#30797](https://github.com/FreeCAD/FreeCAD/pull/30797)).

## BIM

- maxwxyz fixed a regression where changing elevation in BIM Views Panel wouldn't change the level position ([PR#31433](https://github.com/FreeCAD/FreeCAD/pull/31433)). He also added the Draft_Edit command to the BIM WB menu and toolbar to the 2D modify tools, so that it's possible to edit baseless walls and other base objects without the need to switch workbenches ([PR#31538](https://github.com/FreeCAD/FreeCAD/pull/31538)).

## Other changes

- tritao made it possible to set save grid settings as document properties, so that reopening a design on another computer will preserve the intended grid context ([PR#30696](https://github.com/FreeCAD/FreeCAD/pull/30696)).
- tarman3 fixed a bug where the Inspector would not open in certain circumstances ([PR#30897](https://github.com/FreeCAD/FreeCAD/pull/30897)).
- marioalexis84 fixed Elmer mechanical equations for 2D cases ([PR#31610](https://github.com/FreeCAD/FreeCAD/pull/31610)).
- pieterhijma added a workaround for STEP export regression in OpenCascade 8 ([PR#31067](https://github.com/FreeCAD/FreeCAD/pull/31067)).
- tsaaristo improved image calibration by allowing image rotation to align the calibration line to the nearest 45° ([PR#30755](https://github.com/FreeCAD/FreeCAD/pull/30755)).

Additional improvements and fixes were contributed by chennes, ElementW, graelo, HonakerM, ipatch, j-hewett, Lgt2x, maxwxyz, mosfet80, NewJoker, PaddleStroke, tritao, and wmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.07.29).

## Activity stats

**PR stats**: since the previous report, 51 pull requests have been merged, and 49 new pull requests have been opened.

**Issue stats**: overall, there are 3502 open issues in the tracker, down by 6 from last week.
