---
title: 'WIP Wednesday: 8 May 2024'
date: 2024-05-08
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

**Toponaming:** bgbsww added some missing code (there will be more to add, it seems) and started performance testing. So far, things don't look bad at all performance-wise.

**Sketcher:**

- PaddleStroke: added arc length to the Dimension tool and fixed the placing of the on-view parameter inputs.

- maxwxyz updated the Sketcher toolbar to list and group all arc tools (incl. hyperbola and parabola).

- FlachyJoe fixed a point where FreeCAD would ask for information about a point of a curve which doesn't exist.

**Assembly:** PaddleStroke merged the vast majority of newer Ondsel code: new joints types (Rack and Pinion, Screw, Gears, Belt), limits, Exploded View tool, special drag mode for the distance joint, and various fixes. Some of the features (explosion, new joint types) are considered experimental and require adding 'ExperimentalFeatures' boolean parameter added via 'Tools > Edit parameters...' (BaseApp > Preferences > Mod > Assembly).

**TechDraw:**

- WandererFan did a quick fix for the missing fallback default template issue. He also fixed a bug where autocorrect was not handling scaled and rotated reference geometry properly.

- pavltom implemented the user-requested splitting of "sheet" field in the "X / Y" form (X for page ordinal number, Y for total count of pages) into two separate values.

- HowThatWorks added page size to ISO 5457 template borders, replaced page size data fields, and added blank owner data fields.

**CAM:**

- sliptonic refactored sanity reports to make the logic more modular and further separate it from GUI. He also significantly changed how post-processing is done: not any existing post-processors, but the way they are called; this sets the stage for refactoring the individual postprocessors to have less duplicated code.

- LarryWoestman added tests for A, B, and C parameters to the linuxcnc post.

**Materials:** davesrocketshop updated material models to separate Hardness from LinearElastic model, added UUID definitions for FEM-dependent models, and updated unit tests. He also expanded the Python API to allow for material creation.

Some of the other changes:

- PaddleStroke introduced QuickMeasure - a status bar area that displays useful measurements for selected geometry features: length, radius, angles etc.

- maxwxyz changed default colors of the new Measure tool for better contrast.

- furgo16 adapted Arch materials to the new Materials path scheme.

- realthunder backported support for toolbar drag-and-drop to status bar and menu bar.

- Roy-043 and paullee0 fixed a few bugs in Arch.

- wwmayer fixed several bugs.

- WandererFan added a privacy policy.

**PR stats:** In the week from Wednesday, 1 May to Wednesday, 8 May there were 56 pull requests merged. 26 new pull requests were opened.

**Issue stats:** we closed 73 issues, and 51 new issues were opened. Overall, 1,559 issues are currently open.