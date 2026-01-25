---
title: 'WIP Wednesday: 28 February 2024'
date: 2024-02-28
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

- **bgbsww**, **CalligaroV**, and **chennes** made a lot more progress towards mitigating the toponaming issue.

- **chennes** contributed more changes to the addon manager: fixes and support for sorting addons by several criteria (alphabetical, last update time, creation date, GitHub stars), as well as support for custom scores for addons.

- **pavltom** added the Insert Repetition Count command to TechDraw and reimplemented Rich Annotation parent linking.

- **wwmayer** improved the materials editor to use integers for shininess and transparency in a certain value range, submitted a few fixes to Sketcher.

- **edwilliams16** improved the calculation of the 'b' parameter of the hyperbolic arc in Sketcher.

- **Roy-043** improved some wording in Sketcher for better consistency.

- **PaddleStroke** made it possible to sort items in the project tree by dragging and dropping them. He also changed the behavior of line DSH length/width mode so that it behaves like the rectangle length/width DSH in Sketcher.

- **LemonBoy** made datum points highlightable/selectable in the viewport.

- **NomAnor** added an optional visibility toggle to the project tree with the "classic" eye icon. He also refactored the task panel code for PartDesign's patterns.

- **FlachyJoe** improved Helix in PartDesign to use the wires of the computed face instead of the selected ones. He also made suppressed objects distinguishable in the project tree.

- **adrianinsaval** added a new template to the Start page to easily create a new assembly.

- **FEA-eng** added a new property, BeamReducedIntegration, to the CalculiX solver in FEM. He also made several minor improvements in the workbench.

- **marioalexis84** submitted more fixes to the FEM workbench, including mesh generation for check type analysis in CalculiX.

- **Rexbas** fixed a regression in the Blender, CAD, and Revit navigation styles.

- **mosfet80** removed a deprecated function in core and two workbenches.

- **3x380V** fixed a few bugs.

**PR stats:** In the week from Wednesday, 21 February to Wednesday, 28 Feb there were 58 pull requests merged, with a total codebase change of +9,585 / ‑4,489 (not counting translation updates). We had an average merged PR size of +165 / ‑77. 22 new pull requests were opened.

**Issue stats:** we closed 42 issues, and 48 new issues were opened. Overall, 1,266 issues are currently open.