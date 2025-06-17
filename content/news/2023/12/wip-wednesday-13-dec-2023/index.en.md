---
title: 'WIP Wednesday: 13 Dec 2023'
date: 2023-12-13
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

- **@davesrocketshop** pushed an update to the new materials system adding new data types (in particular, for the Render workbench), a new appearance preview UI based on the Coin library, and changes in the array data types.

- **@edi271**, **@Syres916**, and **@WandererFan** pushed numerous fixes and improvements to the TechDraw workbench, including the collection of document info for filling template fields.

- **@Roy-043** introduced the `DefaultAnnoScaleMultiplier` parameter to replace `DraftAnnotationScale`, and a new `get_param` function to help having all defaults in one place to avoid inconsistencies.

- **@abdullahtahiriyo** improved the notification area behavior by grouping the same error messages and appending the instance count next to it.

- **@oursland** added support for macOS builds and Windows C++ unit tests on Conda; package dependency builds for Ubuntu 22.04 and Windows are now Conda-based as well.

**PR stats:** In the week from Wednesday, 6 Dec to Wednesday, 13 Dec there were 30 pull requests merged, with a total codebase change of +8,464 / ‑2,707 lines (not counting translation updates). We had an average merged PR size of +285 / ‑93. 10 new pull requests were opened.

**Issue stats:** we closed 13 issues, and 22 new issues were opened. Overall, 1,095 issues are currently open.

The FreeCAD project association's general assembly approved several new grants in November:

- Amulya Paritosh and Harshita Saraswat will continue this year's GSoC project to create the component library, both the server-side and client-side functionality.

- Kurt Kremitzki will improve FreeCAD's infrastructure performance and maintenance.

- Ajinkya Dahale will improve curve geometry: general tangency with B-splines, B-splines preview, Bezier curves, curvature constraint etc.'

For more information, please see the [Development Fund](https://fpa.freecad.org/programs/fpadf-announcement) page.