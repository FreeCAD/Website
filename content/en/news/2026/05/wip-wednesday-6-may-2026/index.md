---
title: WIP Wednesday, 6 May 2026
date: 2026-05-06
author: Aleksandr Prokudin
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

## Draft

Roy_043 fixed a regression where clones would not receive the correct Diffuse color ([PR#29725](https://github.com/FreeCAD/FreeCAD/pull/29725)), added statusbar hints for annotation tools ([PR#29649](https://github.com/FreeCAD/FreeCAD/pull/29649)), and fixed a bug where the XYZ would be overridden by the cursor position when creating a shapestring ([PR#29762](https://github.com/FreeCAD/FreeCAD/pull/29762)).

## Sketcher

- marbocub fixed constraint remapping in the Merge Sketches command and extended it in two ways: added support for importing external geometry and changed the behavior to create the merged sketch inside the body when all sources share the same body ([PR#29497](https://github.com/FreeCAD/FreeCAD/pull/29497)).
- alfrix changed the way the on-view parameters mechanism switches between editing the numbers and moving the view ([PR#29477](https://github.com/FreeCAD/FreeCAD/pull/29477)). Instead of using a timer, it now detects events: if you start inserting numbers, period, comma, minus, delete, backspace, or use Ctrl+V, it will switch to the edit mode. Pressing Enter or Tab will switch the mode to camera controls again.

## Part and PartDesign

- Bojan9597 fixed a bug in the attachment editor ([PR#29195](https://github.com/FreeCAD/FreeCAD/pull/29195)).
- FlachyJoe fixed the UpToShape extrusion where padding doesn't work with a specified shape ([PR#29686](https://github.com/FreeCAD/FreeCAD/pull/29686)).

## TechDraw

- nishendra3 fixed the insertion of incorrect dimensions for straight bsplines ([PR#29400](https://github.com/FreeCAD/FreeCAD/pull/29400)).
- Syres916 fixed icon colors for the Balloon task panel ([PR#29349](https://github.com/FreeCAD/FreeCAD/pull/29349)).
- WandererFan fixed a crash ([PR#29557](https://github.com/FreeCAD/FreeCAD/pull/29557)).
- maxwxyz fixed involuntary maximization of the TechDraw page ([PR#29081](https://github.com/FreeCAD/FreeCAD/pull/29081)).

## CAM

- tarman3 added the possibility to automatically place tags for several closed paths in Holding Tags ([PR#22468](https://github.com/FreeCAD/FreeCAD/pull/22468)), completed his work on getting identical names and behavior of helix ramp entry in Helix and Adaptive operations ([PR#22357](https://github.com/FreeCAD/FreeCAD/pull/22357)), added Pattern property with Directional and Bidirectional options in Engrave ([PR#22226](https://github.com/FreeCAD/FreeCAD/pull/22226)), added rottion jitter to all patterns in Array ([PR#26326](https://github.com/FreeCAD/FreeCAD/pull/26326)), and fixed retraction for G84 in the new simulator ([PR#29691](https://github.com/FreeCAD/FreeCAD/pull/29691)).
- soruh fixed the scaling for tags with many edges in Holding Tags ([PR#29094](https://github.com/FreeCAD/FreeCAD/pull/29094))
- sliptonic fixed toolpath rendering for multi-revolution rotary moves ([PR#29707](https://github.com/FreeCAD/FreeCAD/pull/29707)).

## FEM

- marioalexis84 fixed an exception in data extraction with an empty pipeline ([PR#29739](https://github.com/FreeCAD/FreeCAD/pull/29739)).
- NewJoker added two CCX 2D examples - plane stress and axisymmetric ([PR#29711](https://github.com/FreeCAD/FreeCAD/pull/29711)).

## BIM

- Roy_043 fixed the "Wall has no solid" error when subtracting roofs ([PR#29472](https://github.com/FreeCAD/FreeCAD/pull/29472)) and incorrect detection of windows and doors in curtain walls and roofs ([PR#27873](https://github.com/FreeCAD/FreeCAD/pull/27873)).
- PaddleStroke removed duplicate transform actions from the context menu ([PR#29604](https://github.com/FreeCAD/FreeCAD/pull/29604)).

## Measurement

Lokestrom allowed angle measurement for discs ([PR#29803](https://github.com/FreeCAD/FreeCAD/pull/29803)) and added disc face measuring to QuickMeasure ([PR#29385](https://github.com/FreeCAD/FreeCAD/pull/29385)). He also allowed the measuring of internal sketch faces ([PR#29551](https://github.com/FreeCAD/FreeCAD/pull/29551)).

## Other changes

- Maik-0000FF fixed the periodic input polling that resulted in 2% CPU use for FreeCAD when it was idle ([PR#29331](https://github.com/FreeCAD/FreeCAD/pull/29331)).
- BurksEngineering added a visual indication in the project tree that a document is opened in read-only mode ([PR#26702](https://github.com/FreeCAD/FreeCAD/pull/26702)).

Additional improvements and fixes were contributed by 3x380V, antoinecellerier, Bojan9597, czarflix, ElementW, furgo16, ipatch, Iskaban10, luzpaz, maxwxyz, sliptonic, tarman3, Thovthe, tritao, and xtemp09.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.05.06).

## Activity stats

**PR stats**: since the previous report, 55 pull requests have been merged, and 46 new pull requests have been opened.

**Issue stats**: overall, there are 3436 open issues in the tracker, up by 54 from last week.
