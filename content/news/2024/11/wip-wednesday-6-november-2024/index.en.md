---
title: 'WIP Wednesday: 6 November 2024'
date: 2024-11-06
authors: Aleksandr Prokudin
draft: false
categories: announcement
tags:
- WIP
cover:
  image:
  caption:
---

This week in FreeCAD development:

**Sketcher**: mwganson defractalized the workbench by disallowing a sketch to be attached to itself.

**Assembly**: paddlestroke fixed two bugs including one release blocker. He also fixed the task panel to allow using expressions for joints.

**BIM**:

- yorikvanhavre fixed IfcOpenShell 0.8 compatibility.

- cjmayo fixed Qt6 compatibility in the IFC explorer.

- hoshengwei changed the IFC Spatial Element to have 'Element' for default composition type.

**TechDraw**: WandererFan fixed two bugs related to displaying SVG hatches; this resulted in better handling for short & wide hatch area and in better scaling of large hatch tiles.

**FEM**: marioalexis84 and AIRCAP fixed several bugs including one where it was impossible to assign a material to a compound.

**GUI**: Rexbas, benj5378, and hyarion contributed several improvements, including one where FreeCAD switches to an internal dark theme when it's the operating system's choice on macOS and Windows.

Among other changes:

- wwmayer fixed a crash on exporting STEP files.

- davesrocketshop disabled the right-click menu in the material editor; it doesn't yet do anything useful and the editor functionality needs to be looked at once v1.0 is out.

Various other fixes were submitted by adrianinsaval, wwmayer, JamesHodgkins, Jarno-de-Wit, cjmayo, mwganson, AIRCAP.

**PR stats**: since the previous report, 35 pull requests have been merged, and 21 new pull requests have been opened.

**Issue stats**: overall, there are 2220 open issues in the tracker, up by 26 from last week. One issue is a v1.0 release blocker, down by 3 from last week.