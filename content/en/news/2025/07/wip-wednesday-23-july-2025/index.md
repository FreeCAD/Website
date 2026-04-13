---
title: WIP Wednesday, 23 July 2025
date: 2025-07-23
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

- hyarion added support for constraints with more than three points.
- wwmayer fixed a crash in Sketcher (cherry-picked by PaddleStroke).
- PaddleStroke fixed several bugs, including one where a contextual dimension would overlap with the cursor in UI.
- matthiasdanner fixed a bug and added a second arc helper to the diameter constraint, useful if the second side of the diameter arrow doesn't point directly to the arc.
- kadet1090 refactored tool hints to remove code repeats.
- FlachyJoe fixed a bug causing negative measures on circles.

**Part**:

- maxwxyz added alignment to selection for a single non-planar face selection.
- tomate44 fixed a bug where Part_Offset2D would wrongly produce a partial offset.
- kadet1090 patched the Attacher so that the normals would always point outside of the shape, because with the transform dialog, it was the other way 'round for some faces.

**Assembly**:

- PaddleStroke fixed several bugs related to flexible assemblies and another one where unconnected joints always touched after a recompute.
- OnesAndZer0s fixed two bugs related to adding subassemblies.

**BIM**:

- yorikvanhavre fixed a bug that would result in opening several Layer Managers and another one where Arch_Stairs would not hide its base object upon creation.
- Roy_043 made length, width, and height inputs consistent with the X, Y, and Z inputs to make them check for in-command shortcuts and select only the numerical portion of the text on focus change.

**FEM: **NewJoker added two new properties to FEM heat flux load to support an advanced type of radiation interaction: cavity (surface-to-surface) radiation and cavity name (required to specify which heat flux loads form the cavity). He also added a new Hard Contact property that, when enabled, changes the default linear contact to hard contact.

**GUI**:

- MisterMakerNL updated the dark theme's tree color and tab bar background to improve the UI readability.
- Rexbas narrowed down the reason why FreeCAD would sometimes crash after being idle to an invalid NaviCube frame buffer and then (hopefully) fixed the bug.
- xtemp09 added a **Clear Recent Files** command to the list of recent files in the menu.
- wwmayer fixed a crash when deleting a binder after deleting the binder's source (cherry-picked by 3x380V).

**I/O**:

- Syres916 added e57 to import file extensions. This file format stores 3D point cloud data, images, and associated metadata.
- PaddleStroke fixed a crash that occurred when exporting a STEP file from a project with an assembly.

Among other changes:

- PaddleStroke fixed a crash in PartDesign on cancelling a sketch without selecting a plane.
- chennes and mosfet80 contributed a couple of fixes to TechDraw.
- jffmichi, dbtayl, chennes, and z0r0 contributed several fixes to CAM.
- Roy_043 fixed a hang on snapping to large point cloud in Draft.

Additional improvements and fixes were contributed by PaddleStroke, theo-vt, pieterhijma, MisterMakerNL, luzpaz, oursland, z0r0, chennes, and mosfet80.

Please note that maintainers are currently _not_ merging any new features or improvements to CAM. For the weeks to follow, only fixes for regressions will be approved. This is because Brad Collette is working on a roadmap for the workbench to help better plan future development to make it sustainable. Please see [this discussion page](https://github.com/FreeCAD/FreeCAD/discussions/22536) for the rationale.

**PR stats**: since the previous report, 62 pull requests have been merged, and 37 new pull requests have been opened.

**Issue stats**: overall, there are 2938 open issues in the tracker, up by 32 from last week.

Since a few recent patches touch the point cloud functionality, here is a new video by Tomas Polak explaining the basics of using point clouds in FreeCAD:

{{< youtube id=LLW7OiDOSKk title="Import Point Cloud to FreeCAD" loading=lazy >}}

Elsewhere in the world, a [new add-on](https://robodk.com/doc/en/Plugin-FreeCAD.html) is now available that enables loading 3D models, curves, and points directly from FreeCAD to [RoboDK](https://robodk.com/), a proprietary application for simulating and programming robot arms. Here is a quick demonstration:

{{< youtube id=TtZ6EWdK68U title="RoboDK Add-In for FreeCAD" loading=lazy >}}