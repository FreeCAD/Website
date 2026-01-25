---
title: 'WIP Wednesday: 13 March 2024'
date: 2024-03-13
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

- **bgbsww** and **chennes** made further progress towards mitigating the toponaming issue.

- **wwmayer** fixed MinGW builds, added a class for reading metadata from project files and a test function to write to file stream, and fixed the context menu for the expression editing input box.

- **pavltom** reimplemented parent linking for weld symbols in TechDraw.

- **edi271** fixed a scaling issue in TechDraw's AxoLengthDimension.

- **prrvchr** fixed an issue with filling template fields in TechDraw when importing an Arch section plan.

- **yorikvanhavre** introduced a new "Mouse delay" preference in "Edit -> Preferences -> Draft -> Grid and Snapping" for suppressing mouse events in numeric inputs for coordinates in Draft and Arch.

- **chennes** fixed several i18n bugs in PartDesign, Sketcher, and the task panel. He also convert GTest to a git submodule and made more improvements in the Addon Manager.

- **FlachyJoe** fixed the issue where dimensions in Sketcher would have an unselectable area.

- **Roy-043** corrected the position of ConstrainLock and ConstrainRadiam in Sketcher.

- **sliptonic** renamed the Path workbench to CAM (additional fixes for that from maxwxyz and chennes), for rationale please see [this post](https://ondsel.com/blog/path-wb-going-away/). He also fixed an edge case with missing toolshapes.

- **davesrocketshop** enhanced the new materials system with data models to support elasticity. This will allow FEM to expand support for more material types.

- **FEA-eng** added a new CalculiX property OutputFrequency that defines output frequency for the whole step in numbers of increments. He also added support for quad8 elements in 2D analyses and fixed Elmer FEM 2D flow examples.

- **marioalexis84** implemented partial support for hexahedral elements meshing and submitted a partial transparency fix in FemPostObject display modes.

- **NomAnor** added an additional visibility icon for features in groups.

- **Ovalelephant35** improved API documentation.

- **mpfusion** improved ISO 286 (geometrical product specifications) conformance.

- **xtemp09** fixed two crashes.

**PR stats:** In the week from Wednesday, 6 March to Wednesday, 13 March there were 55 pull requests merged, with a total codebase change of +6,554 / ‑3,909 (additional loss of 108K+ lines of code is due to GTest devendoring in favor of a git submodule). We had an average merged PR size of +119 / ‑71. 24 new pull requests were opened.

**Issue stats:** we closed 37 issues, and 66 new issues were opened. Overall, 1,354 issues are currently open.