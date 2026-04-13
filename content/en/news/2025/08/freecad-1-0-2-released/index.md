---
title: FreeCAD 1.0.2 released
date: 2025-08-06
authors: Aleksandr Prokudin
draft: false
categories: announcement
tags:
  - release
versions: "1.0"
cover:
  image:
  caption:
---


We've just released an update with over 30 bugfixes and small improvements, [go get it here](https://www.freecad.org/downloads.php). As a reminder, these 1.0.X releases bring added stability to version 1.0 of FreeCAD, whereas new features in development will be released in version 1.1. Here are the main changes in v1.0.2:

**Draft**: Roy_043 fixed a bug where a dimension would show up with inward-pointing arrows, whereas all others would have outward-pointing arrows.

**Assembly**: PaddleStroke fixed a crash ([#20614](https://github.com/FreeCAD/FreeCAD/issues/20614)) that would sometimes occur when dragging a part with the fixed joint.

**TechDraw**:

- bguest fixed a dimension alignment issue.
- Syres916 updated FillTemplateFields.csv to work with newer templates.

**CAM**: The workbench now writes post files in the UTF-8 encoding (fixes [#18698](https://github.com/FreeCAD/FreeCAD/issues/18698)) and removes a redundant move after drilling. Patches contributed by Syres916 and jffmichi.

**BIM**: Roy_043 fixed several bugs where...

- BIM_Leader would create a wire with fewer than 2 points.
- BIM_WPView did not work properly due to a faulty import.
- Roof would not auto-limit run length ([#21796](https://github.com/FreeCAD/FreeCAD/issues/21796))
- Collapsing Building container with Level inside would fail in Strict IFC mode ([#21912](https://github.com/FreeCAD/FreeCAD/issues/21912)).
- Arch_Level and Arch_Wall would disappear during the conversion to the Strict IFC mode ([#21400](https://github.com/FreeCAD/FreeCAD/issues/21400)).

**GUI**: Syres916 and xtemp09 removed the dark fringe around letters and fixed some issues when building FreeCAD against Qt6.

The code also received fixes and improvements for the build system, unit tests, and Python bindings. For the full list of changes, please [see here](https://github.com/FreeCAD/FreeCAD/compare/1.0.1...1.0.2).