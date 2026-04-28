---
title: WIP Wednesday, 28 May 2025
date: 2025-05-28
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

**Draft**:

- yorikvanhavre added a "Recenter" shortcut to move the working plane to be centered on the current snap position.
- Roy_043 reimplemented closing task panels when the relevant document is closed.
- B0cho implements an "Align to face" checkbox in the Hatch task panel. This controls whether the pattern aligns with the base object or the global coordinate system.

**Sketcher**: jffmichi fixed a bug where FreeCAD would show the "Wire is not closed" error message when external edges are used in the sketch.

**PartDesign**: alfrix fixed a few issues in the Hole tool, including one where ISO metric regular standardized head cuts were not working.

**TechDraw**:

- benj5378 fixed an issue where vertical dimensions overlap the arrows if the dimension line is shorter than the dimension.
- WandererFan fixed an issue where it was impossible to mark very small angles.
- PaddleStroke fixed an issue where rich text annotation was rendered white by default in the dark theme.

**BIM**:

- furgo16 contributed numerous improvements:
  - Refactored the Arch module to improve code readability and documentation, and added 37 automated tests. This is part 1 of a multi-part project.
  - Enabled the Arch_Remove command to remove windows or doors from walls.
  - Allowed deleting locked IFC properties when needed.
  - Enabled B-spline support in structures and fixed structure area calculation.
  - tetektoza added support for deactivating active objects to the BIM Views Tree. They also added missing IFC attributes for both Pipe and Rebar tools.
  - rhabacker added support for importing lines from OBJ files.

Among other changes:

- chennes, mosfet80, and jffmichi contributed various fixes to CAM.
- davesrocketshop did further external interface refinements in Materials.
- pieterhijma contributed new functionality to rename dynamic properties.

Additional improvements and fixes were contributed by Roy_043, longrackslabs, tetektoza, paullee0, sasobadovinac, FC-FBXL5, alfrix, Syres916, ipatch, oursland, and luzpaz.

**PR stats**: since the previous report, 48 pull requests have been merged, and 37 new pull requests have been opened.

**Issue stats**: overall, there are 2905 open issues in the tracker, up by 9 from last week.