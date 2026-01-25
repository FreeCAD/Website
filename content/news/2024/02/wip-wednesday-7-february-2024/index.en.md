---
title: 'WIP Wednesday: 7 February 2024'
date: 2024-02-07
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

- **CalligaroV**, **bgbsww**, and **chennes** made further changes towards mitigating the toponaming issue.

- **marioalexis84** submitted a quick fix to the new materials system, and **daverocketshop** made further improvements: better compatibility when using the legacy material editor, fixes, reduced verbosity of console messages.

- **chennes** added support for codeberg.org git repositories to the Addon Manager.

- **PaddleStroke** improved Sketcher: added arrowheads to angles and a new tool for scaling geometry.

- **Roy-043** added creating empty wall openings to the Arch workbench and made several minor improvements to the Draft workbench.

- **kpemartin** contributed a fixes to remove excessively verbose output from certain operations in the Draft workbench. He also patched DXF importer (the C++ one) to properly handle combinations of grouping/layers/colors.

- **Syres916** fixed a possible segmantation fault in Draft and Arch workbenches.

- **Neumann-A** made the use of SMESH version API unconditional in the FEM workbench.

**PR stats:** In the week from Wednesday, 31 Jan to Wednesday, 7 Feb there were 27 pull requests merged, with a total codebase change of +5,002 / ‑1,182. We had an average merged PR size of +185 / ‑44. 20 new pull requests were opened.

**Issue stats:** we closed 13 issues, and 22 new issues were opened. Overall, 1,212 issues are currently open.