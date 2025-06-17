---
title: 'WIP Wednesday: 29 January 2025'
date: 2025-01-29
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

**Draft**: Roy-043 fixed several bugs and changed the Draft_Layer icon to look different from the LayerContainer one.

**Sketcher**:

- jffmichi fixed a segfault that occurred when loading sketches with redundant constraints.
- Jonezzzzz fixed a mapping error when creating a sketch inside a group.
**BIM/Arch**: paullee0 fixed a regression preventing the workbench from performing wall length calculations properly.

**FEM**:

- NewJoker patched the CalculiX code to use thermal expansion reference temperature from material properties (new in FreeCAD v1.0).

- akapelrud added a Neumann-style boundary condition (Electric Flux) to the electrostatic potential constraint; additional fixes to the new code came from marioalexis84.

**TechDraw**:

- WandererFan, marcuspollio, and dbtayl fixed several bugs.

- bguest fixed an issue with dimensions alignment.

- pmjdebruijn fixed an issue with autofill scaling in templates.

**CAM:**

- ShamanTcler contributed a postprocessor for the Masso G3 CNC controller.

- shaise fixed an OpenGL compatibility issue in the new CAM simulator on Linux.
- Various additional fixes from phaseloop, hyarion, LarryWoestman, dbtayl, and st68.


**Misc**: pskowronskiTDx updated the 3DConnexion code to work on macOS now with newer drivers.

Additional fixes arrived from hasecilu, xtemp09, ovo-Tim, and others.

**PR stats**: since the previous report, 46 pull requests have been merged, and 25 new pull requests have been opened.

**Issue stats**: overall, there are 2527 open issues in the tracker, up by 15 from last week.