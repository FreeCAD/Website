---
title: 'WIP Wednesday: 29 May 2024'
date: 2024-05-29
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

This week in FreeCAD development, major changes have been in Assembly, CAM, and TechDraw workbenches, as well as in the new materials system.

**Assembly** got three new joint types: 'Angle', 'Perpendicular', and 'Parallel', all added by PaddleStroke.

**CAM**:

- sliptonic took a first step towards a better CAM tool system. This has been discussed at length with the design working group, more changes will follow.

- phaseloop reworked the VCarve operation to include features that are mostly available in commercial software: step down, finishing, pass, and head movement optimization. They drastically improve carved surface quality while decreasing the carving time by up to 50%. See [this discussion](https://forum.freecad.org/viewtopic.php?t=87475) for details and photo examples.

**TechDraw**: PaddleStroke contributed snapping of view to views and dimensions to dimensions, he also added snapping of value to centers of dimensions, WandererFan contributed various fixes.

**Materials**: davesrocketshop made further improvements to the new materials system:

- New inspectors for the Appearance and Material properties of an object have been added. They are intended for debugging Appearance and Material issues in models.

- Editor's UI has been enhanced: you can now set a default color to be used when creating a new material, plus the name of the material Properties tab has been changed to Physical for improved consistency in the user interface.

- New Material Filter API is now available, developers can use to e.g. request a list of all machinable materials in the CAM workbench.

**BIM**: yorikvanhavre did further post-merge cleanup, and paullee0 added a new 'Offset per Edge' feature in ArchWall.

**UI/UX**:

- Developers started using new logo in various bits of the program.

- Icon updates were contributed by maxwxyz and marcuspollio.

- Additionally, task panels cleanup for Sketcher and Part Design was contributed by marcuspollio.

Among other changes:

- Further toponaming patches by bgbsww and yorikvanhavre (in Draft).

- Draft WB got fixes and partial new materials system support, thanks to Roy-043.

- Addon Manager: pieterhijma added supporting for starting the Addon Manager for a specific addon (e.g. to update the addon).

- New Measure tool has been improved: hlorus made the initial measurement placement scale with viewport zoom.

- Fixes to FEM by marioalexis84 and NewJoker.

- Fixes and new tests in Sketcher, by wwmayer and PaddleStroke.

- Headlight intensity value is now decreased when entering Edit mode in Sketcher. This has been patched by Syres916, but the community keeps discussing better ways to make editing sketches easier to do, when you create a sketch from a face.

- Various core fixes by pieterhijma and wwmayer.

- GUI fixes by 0penBrain.

- Unused code removal in Mesh by mosfet80

PR stats: In the week from Wednesday, 22 May to Wednesday, 29 May there were 75 pull requests merged. 36 new pull requests were opened.

Issue stats: we closed 49 issues, and 50 new issues were opened. Overall, 1,659 issues are currently open.