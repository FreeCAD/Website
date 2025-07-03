---
title: 'WIP Wednesday: 27 March 2024'
date: 2024-03-27
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

This week in FreeCAD development, the four most actively worked-on parts of FreeCAD have been the toponaming project, TechDraw, Sketcher, and FEM.

Toponaming: **bgbsww** and **chennes** are now actively adding history support. Think extrusion, feature mirroring and offset. And tests - that's really important too.

TechDraw:

- **pavltom** contributed an initial implementation of automatic filling of basic editable fields in TechDraw templates. [See here](https://github.com/FreeCAD/FreeCAD/pull/13005) for details.

- **WandererFan** fixed a crash occuring when deleting a centerline followed by undo, as well as some other issues in TechDraw. He also fixed a problem with the initial painting of PAT hatches on section views.

- **PaddleStroke** removed "cosmetic eraser" from TechDraw's toolbar (it can already be done by selecting and pressing the Del key anyway) and fixed several issues.

- **mpfusion** added leading plus (+) in hole/shaft fit limit.

- **guenthereder** fixed a bug occuring when added a BIM section plane into a TechDraw page.

Sketcher: **PaddleStroke** created a new Chamfer tool, reworked the Fillet tool (angle preservation is now an option), and reworked the Symmetry tool (now supports previewing and creating symmetry constraints). He also fixed a regression where floating input widget wouldn't get focus after a user tweaks settings in the Task panel.

FEM:

- **NewJoker** added minimum and maximum time increment properties for CalculiX solver settings.

- **marioalexis84** implemented the exporting of post-processing data to VTK.

- **chennes** fixed a small bug in FEM.

Among other changes:

- **yorikvanhavre** fixed an bug in the WebGL exporter in Arch and made it possible to write IFC objects without owner history. On top of that, he added a color button to the task panel in Draft, that appears when pressing the Draft working plane button, that allows to change the grid color. And he registered interactive Arch tools to Draft, so that additional Draft mechanisms such as the grid turning automatically on/off would apply.

- **Roy-043** fixed several issues in Draft and improved the logic of Draft_Label texts.

- **wwmayer** did minor refactoring in the code for creating task dialogs, made Part_ProjectionOnSurface in the Part WB parametric, added an 'MSAA 6x' viewport rendering option, and fixed several issues.

- **qewer33** rearranged 'New File' buttons on the Start page and renamed the 'Standard Part' button to 'Parametric Part'.

- **FlachyJoe** fixed a helix bug in Part Design. He also contributed a patch to allow creating an ExpLineEdit widget with Python code.

- **Ovalelephant35** added missing API documentation and updated existing one for for various files.

**PR stats:** In the week from Wednesday, 20 March to Wednesday, 27 March there were 50 pull requests merged, with a total codebase change of +7,670 / ‑3,140. We had an average merged PR size of +153 / ‑63. 19 new pull requests were opened.

**Issue stats:** we closed 39 issues, and 55 new issues were opened. Overall, 1,390 issues are currently open.