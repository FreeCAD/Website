---
title: 'WIP Wednesday: 21 August 2024'
date: 2024-08-21
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

**CAM**:

- shaise updated the new CAM simulator: there's code refactoring, bug fixes, and a couple of minor new features (not expected at this stage, but bugfixes outweighed the danger of new features).

- sliptonic fixed a bug where the G85 command would be issued without feed rate. He also fixed the G-Code importing.

- Additional minor fixes arrived from alexfacciorusso and Syres916.

**Materials**: jbaehr extended initial work by sliptonic on machining properties in materials and added complete machining model data for various classes of metals. The information comes from the German standard work "Tabellenbuch Zerspantechnik" and is not subject to copyright as per German law.

Among other changes:

- bgbsww fixed a release blocker, and CalligaroV added a missing test in toponaming code.

- WandererFan fixed 3 bugs including one crasher in TechDraw.

- hlorus fixed two issues in the new measurement tool, both related to annotation placement.

- oursland improved Conda builds on Windows.

- Roy_043 fixed a BIM bug preventing the program from exporting IFC in certain scenarios.

- wwmayer did the usual cleanup and bugfixing magic all over FreeCAD.

**PR stats**: since the previous report, 27 pull requests have been merged, 29 new pull requests have been opened.

**Issue stats**: overall, there are 1865 open issues in the tracker, up by 13 from last week. 18 of them are v1.0 release blockers, down by 8 from last week.