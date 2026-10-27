---
title: WIP Wednesday, 15 April 2026
date: 2026-04-15
author: Aleksandr Prokudin
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

## Draft

- czarflix fixed SVG exporting for faces with islands and circular edges ([PR#29347](https://github.com/FreeCAD/FreeCAD/pull/29347)) and patched the code to honor overshoot settings in angular dimensions ([PR#29298](https://github.com/FreeCAD/FreeCAD/pull/29298)).
- Syres916 fixed the importing of SVG field with UTF-16 encoded text ([PR#29244](https://github.com/FreeCAD/FreeCAD/pull/29244)).
- Bojan9597 fixed a crash when deleting an object while in edit mode ([PR#29040](https://github.com/FreeCAD/FreeCAD/pull/29040)).

## Sketcher

- theo-vt removed superfluous solves to cut down the CPU use ([PR#28652](https://github.com/FreeCAD/FreeCAD/pull/28652)).
- wwmayer fixed rounding errors in the code that recomputes FreeCAD 1.0.x files ([PR#28650](https://github.com/FreeCAD/FreeCAD/pull/28650), cherry-picked by maxwxyz).
- xorza fixed internal faces for self-intersecting BSplines and dangling edges ([PR#28964](https://github.com/FreeCAD/FreeCAD/pull/28964)).
  - tritao fixed depth layering for face-attached sketches in the edit mode ([PR#29280](https://github.com/FreeCAD/FreeCAD/pull/29280)).

## Part and PartDesign

- PaddleStroke fixed a bug where the "XY Parallel to Plane" attachment mode wouldn't work when directly selecting origin planes rather than the origin object ([PR#28958](https://github.com/FreeCAD/FreeCAD/pull/28958)).
- Bojan9597 fixed a bug where newer versions of FreeCAD would swap Length and Length2 properties of Pads on older files ([PR#29247](https://github.com/FreeCAD/FreeCAD/pull/29247)) and another bug where Part_EditAttachment couldn't handle Std_Group in Std_Part properly ([PR#29218](https://github.com/FreeCAD/FreeCAD/pull/29218)).

## TechDraw

- Roy-043 fixed the projection direction of hidden geometry in TechDraw_ArchView ([PR#28801](https://github.com/FreeCAD/FreeCAD/pull/28801)).
- Syres916 restored the correct color of symbols in dark themes/stylesheets ([PR#29217](https://github.com/FreeCAD/FreeCAD/pull/29217)).
- ryankembrey polished the Balloon task panel user interface ([PR#28101](https://github.com/FreeCAD/FreeCAD/pull/28101)).

## CAM

- tarman3 added approximation of Ellipse, Hyperbola, Parabola, BezierCurve, and BSplineCurve edges to arcs and lines for SVG importing ([PR#29142](https://github.com/FreeCAD/FreeCAD/pull/29142)), re-added the extend feature to the LeadInOut dressup ([PR#29061](https://github.com/FreeCAD/FreeCAD/pull/29061)), and fixed several bugs related to open wires ([PR#27203](https://github.com/FreeCAD/FreeCAD/pull/27203)).
- sliptonic refactored the machine editor template selector to use addon metadata ([PR#29150](https://github.com/FreeCAD/FreeCAD/pull/29150)) and fixed two bugs in millfacing ([PR#29231](https://github.com/FreeCAD/FreeCAD/pull/29231), [PR#29189](https://github.com/FreeCAD/FreeCAD/pull/29189)).
- jffmichi fixed a bug where operations would use the wrong parent as job and model ([PR#28100](https://github.com/FreeCAD/FreeCAD/pull/28100)).
- glsys fixed a bug where some circular faces and edges would not be selectable for drilling or tapping ([PR#29051](https://github.com/FreeCAD/FreeCAD/pull/29051)).

## BIM

- Roy-043 fixed the double-click visibility behavior of views in the Views Manager ([PR#28749](https://github.com/FreeCAD/FreeCAD/pull/28749)).
- Bojan9597 fixed MultiMaterial thickness input ignoring user unit system ([PR#29295](https://github.com/FreeCAD/FreeCAD/pull/29295)) and the baseless wall ignoring Offset property ([PR#29264](https://github.com/FreeCAD/FreeCAD/pull/29264)). He also fixed a bug where using Std_Part and BIM materials would pull materials inside the Part in the Tree View ([PR#29262](https://github.com/FreeCAD/FreeCAD/pull/29262)).
- caio-venancio fixed the handling of the missing identification attribute for IFC2X3 compatibility ([PR#29152](https://github.com/FreeCAD/FreeCAD/pull/29152)).
- tritao added the graceful handling of missing IfcOpenShell ([PR#29192](https://github.com/FreeCAD/FreeCAD/pull/29192)).
- jgenunez fixed the bug where Arch_Stairs handrail visibility does not respect the visibility of the parent object ([PR#29173](https://github.com/FreeCAD/FreeCAD/pull/29173)).

## FEM

- ickby added advanced meshing features to Gmsh: boundary layer fix, switched to use gmsh size fields for standard mesh refinements, added size field-based refinements like distance threshold and ball/box fields, manual transfinite meshing tools, and the switch to vtk files for mesh transfer to allow the use of 3D structured meshes ([PR#24792](https://github.com/FreeCAD/FreeCAD/pull/24792)).
- NewJoker added general support for CalculiX's reduced integration elements ([PR#29223](https://github.com/FreeCAD/FreeCAD/pull/29223)) and field parameters to CalculiX's solver controls ([PR#29227](https://github.com/FreeCAD/FreeCAD/pull/29227)).
- marioalexis84 fixed pressure for Z88 plane stress ([PR#29377](https://github.com/FreeCAD/FreeCAD/pull/29377)), made it possible to assign different cross sections to truss elements ([PR#29379](https://github.com/FreeCAD/FreeCAD/pull/29379)), added Z88 section print support ([PR#29188](https://github.com/FreeCAD/FreeCAD/pull/29188)), and patched the code to use material and elements without references as the default value for Z88 ([PR#29185](https://github.com/FreeCAD/FreeCAD/pull/29185)).

## Other changes

- alfrix fixed text input in the on-view parameters in Sketcher ([PR#29287](https://github.com/FreeCAD/FreeCAD/pull/29287)).
- YashSuthar983 improved label dragging for the Measure tool ([PR#29228](https://github.com/FreeCAD/FreeCAD/pull/29228)).
- PaddleStroke fixed a bug in Assembly where dragging would work incorrectly with modified assembly placement ([PR#28093](https://github.com/FreeCAD/FreeCAD/pull/28093)).
- czarflix added missing ImperialBuilding density (lb/ft\^3) and pressure (psi) schema entries ([PR#29278](https://github.com/FreeCAD/FreeCAD/pull/29278)).
- ElementW made FCStd info & thumbnail fetching async to speed up the program startup ([PR#29175](https://github.com/FreeCAD/FreeCAD/pull/29175)). She also improved the performance of reading document metadata ([PR#29178](https://github.com/FreeCAD/FreeCAD/pull/29178)).
- andershol fixed startup window placement to handle multiple monitors and provide a nicer first run ([PR#28807](https://github.com/FreeCAD/FreeCAD/pull/28807)).

Additional improvements and fixes were contributed by Bojan9597, ElementW, FEA-eng, Lgt2x, PaddleStroke, Roy-043, Syres916, WandererFan, YashSuthar983, adrianinsaval, alfrix, andershol, asukiaaa, awgrover, ayushishuklaME, caio-venancio, chennes, czarflix, dependabot\[bot\], freecad-ci-runner, freecad-gh-actions-translation-bot, glsys, ickby, ipatch, jffmichi, jgenunez, marioalexis84, maxwxyz, pieterhijma, pre-commit-ci\[bot\], ryankembrey, sliptonic, tarman3, theo-vt, tritao, xorza.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.04.16).

## Activity stats

**PR stats**: since the previous report, 89 pull requests have been merged, and 71 new pull requests have been opened.\
**Issue stats**: overall, there are 3384 open issues in the tracker, up by 14 from last week.
