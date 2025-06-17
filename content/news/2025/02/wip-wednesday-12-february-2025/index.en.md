---
title: 'WIP wednesday: 12 February 2025'
date: 2025-02-12
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

**Sketcher**:

- AjinkyaDahale contributed round 3 of the refactoring project.

- mosfet80 cleaned up another part of Sketcher's code.

- webnard fixed a bug preventing FreeCAD from filtering named constraints.

**PartDesign**:

- alfrix [redesigned](https://github.com/FreeCAD/FreeCAD/pull/19167) the hole cut panel and implemented the auto finding of the closest size when changing thread standards from Metric to Metric-Fine.

- jffmichi fixed a crash where FreeCAD would crash when opening a file with a metric hole.

**Draft**: Roy_043 introduced a uniform scaling option for Clone scaling, made arrays explodable, implemented an "Add to layer" command (and grouped all three "Add" commands in the menu), and fixed a couple of bugs.

**BIM**:

- yorikvanhavre upgraded the BIM Project Manager tool to support Native IFC projects.

- Roy_043, furgo16, and Syres916 fixed various bugs.

**TechDraw**: benj5378 implemented a new feature that allows users to align the vertical/horizontal axis of a view to match an edge.

**FEM**: colinRawlings implemented a new feature for working with mesh group solids; now when the selected face or edge belongs to multiple solids, FreeCAD will show a popup to allow the user to select which solid they wish to add.

Among other changes:

- michaesc added the polycarbonate material physical property to the new materials system.

- LarryWoestman converted refactored postprocessors to a new, more object-oriented API.

- Flast improved DXF import performance by reducing calls of transcode (up to 5% gain on certain projects).

- karliss introduced a workaround for transparency issues on Wayland.

- xtemp09 fixed a crash in Assembly.

Additional fixes were contributed by herbkoni, tritao, benj5378, hyarion, chennes, PhoneDroid, GS-GOAT, Syres916, oursland, mwganson, mosfet80.

**PR stats**: since the previous report, 50 pull requests have been merged, and 32 new pull requests have been opened.

**Issue stats**: overall, there are 2568 open issues in the tracker, up by 15 from last week.