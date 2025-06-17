---
title: 'WIP Wednesday: 17 July 2024'
date: 2024-07-17
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

Last week in FreeCAD development:

**Toponaming**: bgbsww added more missing TNP code (this time, to PartDesign::Body) and fixed a couple of issues, shaise contributed a partial fix for long TNP names still visible in the 'Subelement' column of the Properties panel.

**BIM**: yorikvanhavre and Roy_043 fixed several bugs, including a v1.0 blocker.

**Sketcher**: PaddleStroke and chennes fixed several bugs (including a crash) and made a few quality-of-life improvements such as undo now working properly for external geometry creation.

**Assembly**: PaddleStroke fixed several issues, including the one where the transform dragger would not show up for the assembly object. He also updated the example assembly project shipped with FreeCAD to work with the latest assembly code.

**FEM**: hyx0329 fixed a regression when searching for 3rd-party binaries in system path, NewJoker improved the Frequency Analysis and Erase Elements icons, and fixed a blocker bug related to custom material cards.

**TechDraw**: Reqrefusion improved new decimal icons, WandererFan fixed i18n for line style preferences.

**Measuring**: hlorus added back the ability to display the X, and Z components of a measured distance in the new Measure tool, wwmayer fixed a memory leak in MeasureDistanceInfo, and PaddleStroke disabled the Quick Measure feature for sketches in edit mode (sketch edges do not get updated until you leave the edit mode, so the wrong information would be displayed anyway).

**GUI**: various smaller fixes to different parts of the user interface arrived from Syres916, kadet1090, chennes, pieterhijma, Roy-043. In particular, kadet1090 fixed a bug where system icons would be invisible with some Qt themes, and made the on-view transform widget smaller (and configurable, though in code only).

**Addon Manager**: chennes addressed the issue the team has with hitting GitHub's requests limits by reducing fetches from the Addon Manager and using a remote cache stored on FreeCAD's servers instead. He also fixed a couple of bugs in the manager's code.

Among other changes:

- PaddleStroke fixed Sketcher and TechDraw to reset dimension tool settings correctly.

- wwmayer fixed the Delete key not working on macOS in various parts of the program.

- davesrocketshop fixed several minor issues in the new materials system.

**PR stats**: 78 PRs have been merged and 19 pull requests have been opened since last report.

**Issue stats**: 1809 issues are currently open, that's 7 issues down from last week. Of those, 33 issues still block the v1.0 release - 8 down from last week, but we expect the number to regrow to some extent when we start making beta releases and release candidates.