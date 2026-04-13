---
title: WIP Wednesday, 11 June 2025
date: 2025-06-11
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

**Draft**: tetektoza implemented a 1-axis mode in Ortho Array to modify only one axis at a time.

**Sketcher**:

- tetektoza made it possible to reset an on-view parameter's state by pressing backspace.
- theo-vt contributed sketch autoscaling that triggers a scale action when there is a single-dimension constraint in a sketch and its datum is edited to avoid breaking the overall shape of the sketch.
- Various other fixes and smaller improvements contributed by longrackslabs and tetektoza.

**PartDesign**: maxwxyz improved the new Transform task panel to allow limiting the transform to translation only, rotation only, or specifying a combination of all individual components. This allows to align an object to a target, without moving or rotating it, or lock movement in certain axes.

**FEM**: rhabacker added a button and a context menu entry to clear all references in all constraints dialogs.

**BIM**:

- Roy-043 fixed an issue where a roof object would not correctly end at the top and continue further. He also improved unit handling in the Roof task panel.
- Fixes and smaller improvements by Syres916, furgo16, and paullee0.

**CAM**:

- Harvie added the 3.175mm milling bit to the default tool library.
- knipknap contributed several fixes.

**GUI**:

- kadet1090 improved the grouping of settings on the Selection page in Preferences.
- Rexbas improved the orthographic camera rotation stability so that the rotation center wouldn't move while rotating.
- wwmayer contributed a Siemens NX navigation style.
- Various fixes by dzid26, alfrix, maxwxyz, kadet1090, 3x380V.

**I/O**:

- rhabacker patched the OBJ importer to insert imported objects into a new group in the top level of the project tree to avoid flooding it.
- totake0224 fixed several SVG importing bugs.

Among other changes:

- WandererFan fixed several issues in TechDraw.
- wwmayer added a task dialog for the blend curve in the Surface workbench.
- wwmayer and godiard fixed several issues in Spreadsheet.

Additional improvements and fixes were contributed by Roy-043, luzpaz, maxwxyz, wwmayer, chennes, 3x380V, oursland, furgo16, tritao, Syres916, sasobadovinac, zbynekwinkler, and mosfet80.

**PR stats**: since the previous report, 57 pull requests have been merged, and 45 new pull requests have been opened.

**Issue stats**: overall, there are 2928 open issues in the tracker, up by 18 from last week.