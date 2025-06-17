---
title: 'WIP Wednesday: 12 June 2024'
date: 2024-06-12
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

**BIM**: @paullee0 made small improvements in ArchWall, @Roy-043 fixed image plane imports and updated the BIM WP commands to use the new Draft code, @Syres916 added fallback IfcOpenShell installation fix for Python 3.10, 3.11, and 3.12 systems, @furgo16 fixed the Cut Plane command, and @DeniseBryson fixed incorrect computed dimensions in ArchSpace (floor area and perimeter length).

**Sketcher**: @emmanuelobrien improved FreeCAD's performance when selecting a lot of geometry objects, @PaddleStroke fixed a bug where on-view parameters wouldn't use the same color after a user saved unrelated program's preferences.

**Part Design**: @FlachyJoe fixed a bug where FreeCAD couldn't pad a sketch on a datum plane, and @kadet1090 added UI for the _Up to Shape_ feature (supports selecting only one shape and set of faces for now).

**Part**: @mh-dm added a new ParallelPlane attachment/map mode which results in an attachment similar to ObjectXY but with the XY plane translated to pass through a selected vertex, and @NewJoker added a New Sketch command to the workbench's toolbar.

**Assembly**: @PaddleStroke resumed improving the dragging behavior. There's now a Preferences option to generate debug files for dragging, and the workbench now looks for movement of grounded objects before attempting to drag.

**CAM**: @jamwaffles renamed CW/CCW to Climb/Conventional respectively for consistency with regular industry's nomenclature.

**TechDraw**: @PaddleStroke fixed a computation error for areas, @Wandererfan fixed incorrect section lines with expression links, and changed template svg_namespace to www.freecad.org.

**FEM**: @marioalexis84 added body heat source to CalculiX writer, he also cleaned up the _ViewProviderFemConstraint_ class and updated constraint transform.

**UI**: @Rexbas fixed rotation mode in Gesture and MayaGesture navigation styles, @maxwxyz updated several GUI icons, and @Kuzma30 implemented the displaying of internal object names in the project tree view (optional, can be toggled in Preferences).

As usual, @FlachyJoe and @wwmayer fixed a number of bugs in the core.

**PR stats**: In the week from Wednesday, 5 June to Wednesday, 12 June there were 46 pull requests merged. 28 new pull requests were opened.

**Issue stats**: we closed 40 issues, and 63 new issues were opened. Overall, 1,717 issues are currently open.