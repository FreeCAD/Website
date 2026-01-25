---
title: 'WIP Wednesday: 13 November 2024'
date: 2024-11-13
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

**Assembly**: PaddleStroke fixed a handful of Exploded View bugs, improved the offset UI for joints, and fixed a few more bugs. Another fix to the workbench was contributed by wwmayer.

**FEM**: for material panels, marioalexis84 replaced the combo box with the material tree widget; this is a quick solution until the workbench completely migrates to the new materials system sometime after the 1.0 release.

**Measure tools**: PaddleStroke fixed another bug in the Quick Measure code.

**GUI**: 3x380V refactored the code of the splash screen and the About dialog, benj5378 fixed the vertical centering of the expressions icon in input widgets, and PaddleStroke made a few cosmetic fixes in the Placement dialog.

Among other changes:

- wwmayer and hasecilu fixed two bugs in the core.

- paullee0 fixed two bugs with walls in BIM.

- Roy_043 fixed several bugs in Draft.

- jbaehr reimplemented the fix for correct terminology in CAM (the original one messed a few things up).

- wwmayer, alfrix, FlachyJoe, and AIRCAP fixed several bugs in Part and Part Design.

**PR stats**: since the previous report, 31 pull requests have been merged, and 16 new pull requests have been opened.

**Issue stats**: overall, there are 2247 open issues in the tracker, up by 27 from last week. One issue is a v1.0 release blocker, same as last week.

While we did tag release candidate 3 recently, we discovered a serious regression in one of the builds. We will fix it and announce RC4 instead.