---
title: 'WIP Wednesday: 31 January 2024'
date: 2024-01-31
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

- **bgbsww**, **chennes**, and **CalligaroV** ported and further improved various changes from **RealThunder**'s branch towards mitigating the toponaming problem.

- **Roy-043** fixed several scale widget related bugs in the Draft workbench, a few bugs in the Arch workbench, a couple of minor issues in Sketcher and in the Preferences dialog, and then tweaked Arch's preferences layout to follow recent changes in Draft's preferences.

- **WandererFan** fixed several issues in the TechDraw workbench.

- **marioalexis84** improved contact and tie constraints in FEM. He also contributed several fixes to the new materials system.

- **LemonBoy** fixed a bug where color assignment to a body would not be undoable.

- **chennes** tweaked the Addon Manager to remove excess macros information that can't be rendered properly and fixed git detection on macOS. He also made it possible to allow primary branch name change in `package.xml`.

- **PaddleStroke** fixed a bug with copying single geometry items and a bug that broke building the main development branch.

- **oursland** fixed a Conda-related build issue on Windows.

- **3x380V** submitted further fixes towards Qt6 support.

**PR stats:** In the week from Wednesday, 24 Jan to Wednesday, 31 Jan there were 31 pull requests merged, with a total codebase change of +4,138 / ‑1,902. We had an average merged PR size of +133 / ‑61. 24 new pull requests were opened.

**Issue stats:** we closed 28 issues, and 53 new issues were opened. Overall, 1,196 issues are currently open.