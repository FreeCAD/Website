---
title: 'WIP Wednesday: 25 December 2024'
date: 2024-12-25
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

**Assembly**: PaddleStroke fixed a bug where an existing part would shift when inserting a new one.

**FEM**: marioalexis84 fixed mesh exporting to vtk formats and introduced a preference for Netgen log verbosity, and NewJoker fixed a typo in an error message.

**TechDraw:** WandererFan fixed several issues including Link Array objects in 3D producing wrong dimensions, and NewJoker fixed a user-visible typo.

**Spreadsheet**: mwganson fixed an alias validation regression he inadvertently introduced in an earlier patch.

**Materials**: davesrocketshop fixed an issue where too low values would be confusingly displayed as zero.

**Addon Manager**: chennes fixed a few issues.

**GUI**: hyarion, wwmayer, and marcuspollio fixed a few issues in the UI code, but most noticeably, Rexbas fixed navigation issues with the <kbd>Shift</kbd> key in Sketcher while using Blender or Revit navigation styles.

**Add-ons**: rostskadat improved the SweetHome 3D importer to import elements such as 'pieceOfFurniture', 'light', 'camera', etc.

More fixes arrived from Roy_043, paullee0, yorikvanhavre, oursland, wwmayer, 3x380V, mosfet80, coldtobi, alfrix, luzpaz, mwganson, chennes, and coldtobi.

**PR stats**: since the previous report, 44 pull requests have been merged, and 21 new pull requests have been opened.

**Issue stats**: overall, there are 2434 open issues in the tracker, up by 26 from last week.