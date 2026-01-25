---
title: 'WIP Wednesday: 19 March 2025'
date: 2025-03-19
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

- PaddleStroke added an option to combine line and polyline tools and fixed a couple of bugs.

- Shkolik implemented a new configurable color for external defining geometry.

**CAM**:

- clsergent added a postprocessor for the Snapmaker machines with CNC capabilities.

- phaseloop change the default V-bit tip diameter to 0.1mm and added other popular v-bits: 30°, 45°, and 90°.

- LarryWoestman added three command line options to the refactored postprocessors code base.

**Among other changes**:

- PaddleStroke fixed the bug where selecting a datum object would show dragger.

- captain0xff fixed several issues, and benj5378 started another minor refactoring effort in TechDraw.

- furgo 16, semhustej, and yorikvanhavre fixed several bugs in BIM.

- tritao added initial support for frame profiling via the [Tracy](https://github.com/wolfpld/tracy) profiler to look into rendering performance.

Additional fixes were contributed by chennes, pmjdebruijn, mosfet80, jbaehr, bofdahof, tritao, thomasgi1, adrianinsaval, kpemartin (measurements), xtemp09, ljo, yomgui1, thyssentishman, hasecilu, luzpaz, wwmayer, alfrix, benj5378, hyarion, and karliss.

**PR stats**: since the previous report, 54 pull requests have been merged, and 38 new pull requests have been opened.

**Issue stats**: overall, there are 2715 open issues in the tracker, up by 45 from last week.