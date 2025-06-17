---
title: 'WIP Wednesday: 24 January 2024'
date: 2024-01-24
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

- **Roy-043** fixed a few bugs in the Arch workbench, improved layer functions and made further improvements in Draft.

- **WandererFan** fixed several bugs in TechDraw.

- **Paddle** added copy/cut/paste commands for geometry, as well as arc angle render improvements and distance arc helpers to Sketcher. He also added a 'Properties' action to the contextual menu to open the property dialog. Moreover, he introduced customization for edges pattern and width by type; this allows to render dashed lines for construction curves.

- **kadet1090** introduced styling to elements and constraints lists in Sketcher.

- **AjinkyaDahale** implemented B-Spline visualization in edit mode.

- **maxwxyz** continued his work on making the contextual (right-click) menu in Sketcher more useful and added BSpline-specific commands.

- **bdieterm** added explicit transparency specification in several parts of the user interface.

- **bgbsww** improved tests for new toponaming code.

- **chennes** committed more toponaming changes - the comparison method for mapped elements. This is original code by **RealThunder** with some modifications. Further changes come from **bgbsww**.

- **sliptonic** fixed a bug with the split output option in Path.

- **marioalexis84** improved the self-weight constraint in FEM and made further small improvements. He also began contributing to the new materials system by Dave Carter.

- **3x380V** improved the code quality in base classes.

- **hasecilu** fixed a bug that would prevent offset property in Part Design linear patterns from being updated.

- **CalligaroV** modernized some of the Preferences dialog code.

**PR stats:** In the week from Wednesday, 17 Jan to Wednesday, 24 Jan there were 47 pull requests merged, with a total codebase change of +6,747 / ‑3,894. We had an average merged PR size of +144 / ‑83. 19 new pull requests were opened.

**Issue stats:** we closed 20 issues, and 24 new issues were opened. Overall, 1,164 issues are currently open.