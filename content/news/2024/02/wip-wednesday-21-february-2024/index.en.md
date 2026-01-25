---
title: 'WIP Wednesday: 21 February 2024'
date: 2024-02-21
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

- **bgbsww**, **CalligaroV**, and **chennes** made further progress towards mitigating the toponaming issue.

- **pieterhijma** contributed the first code towards a new custom data elements (custom properties) system, [see here](https://github.com/FreeCAD/FreeCAD/pull/12135) for technical details.

- **maxwxyz** adjusted the default material appearance to better display the objects shape (surfaces and contours) with specular highlights and a low ambient color. He also added the recently merged commands for translating and scaling geometries to the context menu in Sketcher.

- **czinehuba** updated icons for the command that toggles contruction lines mode in Sketcher.

- **Rexbas** fixed disappearing element handles in Sketcher.

- **Roy-043** made several improvements in Draft.

- **yorikvanhavre** fixed an old suboptimal design solution related to IFC.

- **WandererFan** fixed a few issues in TechDraw.

- **marioalexis84** fixed several bugs in FEM.

- **FEA-eng** added new matrix solver types (PaStiX and Pardiso) to FEM.

- **mosfet80** did some refactoring in the UI code

- **3x380V** cleaned up PythonWrapper (more likely to follow).

- **Andrei-Pozolotin** fixed a bug in the expression engine.

- **LemonBoy** fixed a bug that prevented FreeCAD from preserving objects order when moving them in the project tree.

**PR stats:** In the week from Wednesday, 14 February to Wednesday, 21 Feb there were 57 pull requests merged, with a total codebase change of +24,587 / ‑4,685 (not counting translation updates). We had an average merged PR size of +431 / ‑82. 28 new pull requests were opened.

**Issue stats:** we closed 34 issues, and 59 new issues were opened. Overall, 1,247 issues are currently open.