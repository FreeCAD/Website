---
title: 'WIP Wednesday: 14 February 2024'
date: 2024-02-14
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

- **bgbsww**, **CalligaroV**, and **chennes** made more progress with mitigating the toponaming issue.

- The latest work by **paddle** on integrated assembly workbench has been merged: linking and grounding parts, functional joints (Fixed, Revolute, Cylindrical, Slider, Ball, Distance), dragging support for Slider and Revolute joints.

- **paddle** patched the parallel constraint code to ignore points and non-line geometries. He also added Translate tool that also works as a replacement for Rectangular Array / Move / Copy / Clone.

- **AjinkyaDahale** implemented general tangency with B-splines in Sketcher.

- **Rexbas** contributed a patch fixing rotation for some navigation styles in Sketcher.

- **maxwxyz** further improved contextual right-click menu in Sketcher: preselection and external geometry are now taken into consideration, Fillet and Trim commands have been removed (they can't work with a selection), Cut/Copy/Paste commands have been added.

- **FlachyJoe** added a "Passthrough" boolean property in PartDesign so that it would be possible to disable a feature without removing it. He also made it possible to use equal radii in Part and PartDesign cones and implemented 1D intersection for attachments.

- **LemonBoy** added an option to dim the navigation cube when it's not in the focus. He also fixed the extrusion behavior when the height is zero.

- **Zolko-123** improved the LCS representation in the  window to make it easier to select the point/vertex on which the LCS is attached.

- **marioalexis84** made further improvements in the FEM workbench: added support for cyclic symmetry and fixed several issues.

- **chennes** and **rostskadat** made various improvements in the Addon Manager code.

- **Roy-043** made several fixes and small improvements in Draft and Arch, he also fixed the path for off-line documentation.

- **mark-dev** added subvolume property for roofs based on a solid shape in Arch.

- **pavltom** implemented adding "Owner" property to all Symbols in TechDraw.

- **kadet1090** made axis label color configurable for better theming capabilities.

- **wwmayer** fixed 3MF exporting with clones, contributed to the Python 3.12 port, improved the port to OpenCascade 7.8.0, and contributed more fixes.

**PR stats:** In the week from Wednesday, 7 February to Wednesday, 14 Feb there were 66 pull requests merged, with a total codebase change of +15,543 / ‑3,626 (not counting translation updates). We had an average merged PR size of +235 / ‑55. 36 new pull requests were opened.

**Issue stats:** we closed 52 issues, and 47 new issues were opened. Overall, 1,216 issues are currently open.