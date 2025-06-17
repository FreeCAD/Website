---
title: 'WIP Wednesday: 5 June 2024'
date: 2024-06-05
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week, FreeCAD has entered feature freeze for upcoming v1.0. This means no new patches adding features will be merged until the new version is released.

Major changes this week:

**Sketcher**:

- @kadet1090 fixed a bug where colors of sketches wouldn't get updated when a user changed theme preferences.

- @howie-j added a preference toggle for choosing the preferred method of constraining circles with on-view parameters (the new floating input widgets): automatically, by diameter, or by radius.

- @wwmayer refactored the Sketch Analysis code.

**BIM**: @Syres916 and @yorikvanhavre continued cleaning up the combined Arch/BIM/NativeIFC workbench.

**Materials**: @davesrocketshop improved the use of the ShapeAppearance property for the Part workbench, as well as UI elements for setting object appearance. He also laid the foundation for future texture support and added API for inheriting a material.

**CAM**: @sliptonic added machinability material model, a couple of materials, and a button in the job dialog to assign a material. So when you try to assign a material in the CAM workbench now, you will get a list of only machinable materials. The sanity report has been updated to display the surface speed for assigned materials. This is the bare minimum of support for the new materials system in CAM.

**VarSets** got two patches by @pieterhijma. The first one provides a GUI command to create variable sets and it presents you with a dialog to add properties. The second one allows users to directly add properties to variable sets from within the expression input dialog.

Among other changes:

- @bgbsww did further cleanup in the new toponaming code.

- @PaddleStroke fixed several bugs in new snapping and smart dimensions code.

- @maxwxyz contributed small UI improvements.

PR stats: In the week from Wednesday, 29 May to Wednesday, 5 June there were 53 pull requests merged. 46 new pull requests were opened.

Issue stats: we closed 44 issues, and 55 new issues were opened. Overall, 1,681 issues are currently open.