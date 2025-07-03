---
title: 'WIP Wednesday: 24 July 2024'
date: 2024-07-24
author: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

**Toponaming**: bgbsww fixed a blocker bug in the toponaming code, refactored all element name pairs into clearer struct names, and contributed several patches transferring RealThunder's code to solve the save/restore errors with objects with element maps.

**Assembly**: PaddleStroke fixed two bugs in the new Bill of Materials tool and resolved a shortcut conflict between the Exploded View tool and multiple other global shortcuts.

**FEM**: marioalexis84 fixed several issues in the workbench and added support for exporting FEM mesh 1D elements to VTK and importing VTK files as FEM mesh.

**CAM**: sliptonic fixed several "red ink" issues (cryptic messages shown in the Report View console rather than human-readable messages in regular GUI.

**Part Design**: wwmayer took out two v1.0 blockers, and chennes improved more code for Qt6 compatibility.

**GUI**: Syres916 fixed a couple of minor issues, and MisterMakerNL updated the stylesheet and fixed a bug where buttons in the Start page wouldn't work with an overlay.

**Measure**: Syres916 fixed a blocker bug, and hlorus fixed an issue where trying to measure distance or angle between two bodies in an assembly would provide an incorrect result.

Among other changes:

- WandererFan fixed an issue in TechDraw where the initial point of a leader added to a rotated view was misplaced.

- yorikvanhavre and Roy_043 fixed two issues in the BIM workbench.

- wwmayer added tests for MeshPart and contributed various fixes.

**PR stats**: 39 PRs have been merged and 22 new pull requests have been opened since last report. We also keep accumulating pull requests that will be reviewed once v1.0 is out, there's currently 90 of those (out of 124 overall).

**Issue stats**: 1819 issues are currently open, 10 issues up from last week. Of those, 31 issues still block the v1.0 release - 2 down from last week.