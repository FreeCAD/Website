---
title: 'WIP Wednesday: 20 March 2024'
date: 2024-03-20
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

- **bgbsww** and **chennes** made further progress towards mitigating the toponaming issue. More RealThunder's code has been ported and improved. A C++ testing framework was added for PartDesign and ShapeBinder.

- **marioalexis84** committed fixes to the FEM workbench.

- **NewJoker** fixed bugs in FEM and updated FEM examples on the Start page.

- **lyphrowny** fixed 1D beam cross section orientation in FEM.

- **hoshengwei** contributed a fix to the Arch workbench.

- **sliptonic** fixed an i18n error in CAM.

- **WandererFan** fixed several bugs in TechDraw.

- **pavltom** contributed further fixes for parent linking in TechDraw, this time for Unify Projection Group.

- **edi271** fixed several bugs in TechDraw.

- **davesrocketshop** fixed bugs in the new materials system.

- **wwmayer** fixed various bugs including some crashers, added a test for mesh export, ported FreeCAD's QtDesigner plugin to Qt6.

- **maxwxyz** made the main window title display the current active document's name. He also created a toolbar command group for view presets (top, bottom, etc.), this is used by default and can be disabled. Additionally, he added the command for the perpendicular constraint to the context menu in Sketcher, if a line and a conic are selected. Moreover, with feedback from the design working group, he updated some of the Assembly icons to look not too similar to each other.

- **PaddleStroke** added missing view menu entries to the navicube button. He also introduced a basic Chamfer tool and reworked the Fillet tool to make the "preserve corner" option a Tasks panel checkbox; both tools now have default shortcuts.

- **yorikvanhavre** fixed IFC export of arrays and improved the IFC exporter in Arch so that it would be able to append objects to an IFC file instead of creating a file from scratch. He also updated Draft to recognize NativeIFC objects.

- **oscarale-camorlinga** updated the Text attribute in ArchSpace to support _Description_ and _Long Name_ IFC attributes.

- **NomAnor** fixed a regression in pattern reference selection in PartDesign.

- **FlachyJoe** fixed a crash occurring when using variable links.

- **luzpaz** contributed minor fixes.

**PR stats:** In the week from Wednesday, 13 March to Wednesday, 20 March there were 49 pull requests merged, with a total codebase change of +7,919 / ‑3,833. We had an average merged PR size of +162 / ‑78. 29 new pull requests were opened.

**Issue stats:** we closed 51 issues, and 46 new issues were opened. Overall, 1,367 issues are currently open.