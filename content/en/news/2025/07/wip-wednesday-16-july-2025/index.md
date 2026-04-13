---
title: WIP Wednesday, 16 July 2025
date: 2025-07-16
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

- PaddleStroke created a ConstraintLineByAngle helper.
- FlachyJoe cleaned up planegcs/Geo code.
- theo-vt patched the workbench to update multiple geometry IDs at a time rather than just one when scaling is applied.

**PartDesign**: theo-vt patched the code to allow open wires for profile normal detection. This fixes a bug where holes from arcs would have the wrong orientation.

**TechDraw**:

- WandererFan fixed a regression that caused v1.1 files to become unreadable in v1.0.
- Syres916 fixed the automatic sizing of the TaskFillTemplate's dialog and a [regression](https://forum.freecad.org/viewtopic.php?t=98341) where equal tolerances would display an additional incorrect symbol.

**FEM: **NewJoker added two new properties to FEM Constraint contact: one to enable thermal contact and one to define its properties-a list of gap conductance values optionally paired with contact pressure and temperature. He also added a unitless Offset property to shell sections.

**GUI**:

- Rexbas increased the focal distance in the orthographic view as a workaround for the missing clipping offset in the Coin library (he also [contributed](https://github.com/coin3d/coin/pull/577) the real fix to Coin, review is pending).
- kadet1090 and MisterMakerNL contributed numerous fixes to the default stylesheet.

**I/O**:

- baidakovil contributed a [patch](https://github.com/FreeCAD/FreeCAD/pull/21695) that allows users to customize WebGL exports with their own templates.
- furgo16 [updated](https://github.com/FreeCAD/FreeCAD/pull/22045) the DXF C++ importer to support nested block definitions and allow users to choose parametric or flattened importing of blocks and assemblies.

Among other changes:

- Roy-043 and paullee0 contributed several fixes to BIM and Draft.
- theo-vt fixed a regression in Part code that affected Assembly and TechDraw.
- captain0xff refactored SoRotationDragger as part of his GSoC work on implementing interactive controls in the 3D View.
- z0r0 fixed the Fanuc post-processor (in CAM), which will now search for tool attributes that actually exist.

Additional improvements and fixes were contributed by chennes, oursland, mosfet80, Syres916, hyarion, and theo-vt.

**PR stats**: since the previous report, 31 pull requests have been merged, and 39 new pull requests have been opened.

**Issue stats**: overall, there are 2906 open issues in the tracker, down by 2 from last week.

Elsewhere in the community, Federico Rosa began working on a new workbench called [Solar](https://github.com/Francisco-Rosa/Solar), which uses [LadyBug](https://www.ladybug.tools/) tools for solar positioning and animating it over a specified period.

{{< youtube id=nT1_mGFQwXE title="FreeCAD 1.0 and FreeCAD-Link - Sun path tool" loading=lazy >}}

Alex Sadowski will be representing FreeCAD at [FrOSCon](https://froscon.org) in Sankt Augustin (Germany) this August, with a talk and a stand.