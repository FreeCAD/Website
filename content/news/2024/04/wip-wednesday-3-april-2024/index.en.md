---
title: 'WIP Wednesday: 3 April 2024'
date: 2024-04-03
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

This week in FreeCAD development, the most actively worked-on parts of FreeCAD have been the toponaming project, Sketcher, FEM, and UI/UX.

Toponaming:

- **CalligaroV** imported and improved the WireJoiner class.

- **bgbsww** fixed a few issues, made minor improvements, and added Python implementations for CompSolid, Face, Shell, Solid, as well as missing entries in TopoShape.

Sketcher:

- **Roy-043** renamed "Map sketch to face..." in the main menu to "Attach sketch..." for clarity.

- **PaddleStroke** implemented a midpoint autoconstraint, fixed a bug in Chamfer tool code, as well as a bug with a B-Spline icon in construction line mode.

- **FlachyJoe** added an arc length constraint.

FEM:

- **marioalexis84** improved post-processing object style.

- **NewJoker** changed 2D element thickness from 20 to 1 by default.

- **lyphrowny** fixed and typo in FEM code and removed calculix from solvers tab in examples.

- **davesrocketshop** added the property 'Thermal Expansion Reference Temperature' to the Thermal properties in the new materials editor.

UI/UX:

- **Roy-043** made "View Left" the last option in the "Individual views" toolbar.

- **maxwxyz** updated FEM and Part Design icons for better consistency and added a missing "View Top" option. He also added missing commands to the tree context menu.

- **PaddleStroke** added an opt-in Tab-Bar workbench selector (enabled in Preferences). He also fixed the toggling of objects' transparency in some scenarios and improved the double-click behavior for spreadsheet objects to switch to the Spreadsheet WB.

- **NomAnor** made it possible to allow adding transformations to MultiTransform if there is no active Body.

Among other changes:

- **wwmayer** fixed a lot of bugs and developed a new function to approximate B-Spline from points.

- **Roy-043** added a new Fuse property to patharray and pathtwistedarray in Draft. This fixes a problem when applying union/intersect to a point array and other objects.

- **tomate44** enabled multi-threading to _distToShape_ following a change in OCCT (starting with v7.6.0). This brings an ×3 to ×6 performance boost on a rather complex 20MB STEP file.

- **adrianinsaval** fixed building new material code on Windows with debugging enabled.

- **NomAnor** patched FreeCAD to ignore suppressed features in patterns (Part Design).

- **furgo16** fixed WebGL exporting

- **paullee0** made a few fixes and improvements in Arch.

- **jamwaffles** added feed retract option to drilling op settings for reaming/boring heads in CAM.

- **yorikvanhavre** made it possible to unset modified state with Python code.

- **chennes** fixed some minor bugs.

- **WandererFan** fixed a failure on corrupt dimension reference in TechDraw.

**PR stats:** In the week from Wednesday, 27 March to Wednesday, 3 April there were 70 pull requests merged, with a total codebase change of +9,316 / ‑1,737 (excluding updated translations and icons). We had an average merged PR size of +133 / ‑25. 17 new pull requests were opened.

**Issue stats:** we closed 47 issues, and 37 new issues were opened. Overall, 1,392 issues are currently open.