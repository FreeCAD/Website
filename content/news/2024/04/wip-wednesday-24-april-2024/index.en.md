---
title: 'WIP Wednesday: 24 April 2024'
date: 2024-04-24
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

TechDraw:

- **PaddleStroke** unified Insert View tools (View, ProjGroup, Sheet, Arch, SVG, Image). He also made App::Links of views work in TechDraw, this also removes 'Share Views' from the toolbar.

- **WandererFan** fixed several bugs and added two new Python methods, for getting visible and hidden vertices.

- **farleyrunkel** refactored a minor part of TechDraw code.

Sketcher:

- **Roy-043** made constraints and geometry menu texts more consistent and improved GUI texts in Sketcher settings.

- **PaddleStroke** joined Line and Polyline in a command group in the toolbar and fixed the midpoint autoconstraint to work with polylines.

FEM:

- **NewJoker** fixed several bugs.

- **marioalexis84** extended the ABAQUS writer to select the element types available in CalculiX. He also fixed a bug where the size of the FEM feature symbols couldn't be changed.

- **chennes** fixed the compilation of FEM on MSVC.

Materials:

- **davesrocketshop** brought major improvements to the material tree widget:

- Filters are now lsist and allow a variety of filtering options.

    - User preferences allow the inclusion/exclusion of favorites and recents.

    - Widget state such as expansion, tree expansions, etc. are saved and restored.

    - The current appearance material is now displayed whehn editing.

    - There's now a Python interface.

- **wwmayer** added support for customizing all material colors and fixed further material issues.

Draft:

- **Roy-043** fixed several bugs in the workbench.

- **yorikvanhavre** removed hardcoded axis colors (red, green, blue) and made the workbench use FreeCAD-wide axis colors.

Start:

- **chennes** recreated the _Start_ workbench/page as a QtWidgets-based app.

- Several more people contributed further fixes and improvements: **Rexbas** fixed the migration script, **wwmayer** made the new Start page look more like the old one, and **cjmayo** made it possible to use Microsoft GSL on the Start page.

Some of the other changes are:

- **wwmayer** fixed several other bugs.

- **mosfet80** removed more dead and unused code.

- **dzid26** fixed a bug where a Save window would remain in the background if FreeCAD is closed by the operating system.

- **tomate44** fixed shape projection of complex BSpline curves.

- **jwueller** fixed a bug in OpenSCAD where CSG computations would start too early.

- **farleyrunkel** fixed a bug where searching a model tree wouldn't work for numbers.

- **PaddleStroke** moved the '+' tab of the TabBar workbench selector to the left so that it wouldn't be hidden by default with many workbenches enabled.

- **realthunder** fixed a problem with incorrect referencing of App::Part child object's CopyOnChangeGroup.

- **cjmayo** fixed several bugs in the code.

**PR stats:** In the week from Wednesday, 17 April to Wednesday, 24 April there were 54 pull requests merged. 23 new pull requests were opened.

**Issue stats:** we closed 32 issues, and 60 new issues were opened. Overall, 1,517 issues are currently open.