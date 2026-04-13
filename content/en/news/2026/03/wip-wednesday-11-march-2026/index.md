---
title: WIP Wednesday, 11 March 2026
date: 2026-03-11
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 5 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**Draft**:

- Roy-043 fixed the error that was causing circular import warnings ([PR#25386](https://github.com/FreeCAD/FreeCAD/pull/25386)), updated user-visible text in Draft_SelectPlane ([PR#28233](https://github.com/FreeCAD/FreeCAD/pull/28233)), and allowed more than 1 character for in-command shortcuts ([PR#26950](https://github.com/FreeCAD/FreeCAD/pull/26950)).
- Bojan9597 patches the workbench so that when a single vertex is pre-selected and the Working Plane command (W, P) is triggered, the working plane now moves its origin to that vertex without changing its orientation ([PR#27979](https://github.com/FreeCAD/FreeCAD/pull/27979)).

**Sketcher**:

- theo-vt improved the 2D solver ([PR#27954](https://github.com/FreeCAD/FreeCAD/pull/27954)).
- mosfet80 cleaned up some dead code in the workbench ( [PR#20509](https://github.com/FreeCAD/FreeCAD/pull/20509)).
- YuraSokolovskyi changed the "Autoconstraints cause redundancy, removing them" error message to mention the sketch name ([PR#27971](https://github.com/FreeCAD/FreeCAD/pull/27971)).
- Multiple patches from PaddleStroke:
  - Two fixes for the Dimension tool ([PR#28242](https://github.com/FreeCAD/FreeCAD/pull/28242) and [PR#27630](https://github.com/FreeCAD/FreeCAD/pull/27630)).
  - A fix for a crash on external deletion ([PR#27717](https://github.com/FreeCAD/FreeCAD/pull/27717)).
  - A fix for the coincidence constraint not set and shown ([PR#28120](https://github.com/FreeCAD/FreeCAD/pull/28120)).
  - Refactoring of removeAxesAlignment ([PR#27451](https://github.com/FreeCAD/FreeCAD/pull/27451)).
  - New parametric Text object controlled by a text constraint ([PR#22217](https://github.com/FreeCAD/FreeCAD/pull/22217)).



{{< youtube id=nmLSNaO1YXE title="Sketcher: Text tool" loading=lazy >}}

**Part and PartDesign**:

- Bojan9597 fixed a chamfer crash on the OCC kernel failure ([PR#28029](https://github.com/FreeCAD/FreeCAD/pull/28029)).
- PaddleStroke fixed the wireframe not working on the external links to the body ([PR#28086](https://github.com/FreeCAD/FreeCAD/pull/28086)).

**Assembly**: PaddleStroke fixed the joint creation not working on draft links ([PR#26085](https://github.com/FreeCAD/FreeCAD/pull/26085)), fixed the inability to go to the linked part if the "part" itself is an assembly ([PR#27531](https://github.com/FreeCAD/FreeCAD/pull/27531)), and fixed the JCS position if an assembly is transformed ([PR#28089](https://github.com/FreeCAD/FreeCAD/pull/28089)).

**BIM/Arch**:

- Roy-043 fixed a bug where a column would get the wrong height when the unit system was set to Imperial ([PR#28020](https://github.com/FreeCAD/FreeCAD/pull/28020)) and three bugs with BIM views in TechDraw ([PR#27511](https://github.com/FreeCAD/FreeCAD/pull/27511)).
- ipatch fixed a crash when creating text with the BIM_Text tool ([PR#28135](https://github.com/FreeCAD/FreeCAD/pull/28135)).

**FEM**:

marioalexis84 contributed numerous improvements and fixes:

- Added a method to create custom arrays in the pipeline ([PR#26076](https://github.com/FreeCAD/FreeCAD/pull/26076)).
- Added a command to the context menu to remove groups from mesh ([PR#27945](https://github.com/FreeCAD/FreeCAD/pull/27945)).
- Added log verbosity preference to the Elmer solver ([PR#28058](https://github.com/FreeCAD/FreeCAD/pull/28058)).
- Removed transparency from equation icons ([PR#28193](https://github.com/FreeCAD/FreeCAD/pull/28193)).
- Grouped all solver commands in the toolbar and the menu bar ([PR#28144](https://github.com/FreeCAD/FreeCAD/pull/28144)).
- Set pipeline frame units for new CalculiX ([PR#27845](https://github.com/FreeCAD/FreeCAD/pull/27845)).
- Fixed a crash in the pipeline ([PR#28171](https://github.com/FreeCAD/FreeCAD/pull/28171)).
- Fixed a bug where coloring couldn't be changed for the "Field: None" mode of the Results pipeline ([PR#28028](https://github.com/FreeCAD/FreeCAD/pull/28028)).
- Fixed a start page example ([PR#28094](https://github.com/FreeCAD/FreeCAD/pull/28094)).

**CAM**:

- The usual batch of improvements and fixes from tarman3:
  - Added dedicated titles to the Inspect and Export windows ([PR#26605](https://github.com/FreeCAD/FreeCAD/pull/26605)) and changed the buttons' captions in the G-Code exporting window to make them more descriptive ([PR#26507](https://github.com/FreeCAD/FreeCAD/pull/26507)).
  - Fixed speed assignment for the vertical feed ([PR#28210](https://github.com/FreeCAD/FreeCAD/pull/28210)).
  - Added the processing of compound objects in the Profile operation ([PR#23747](https://github.com/FreeCAD/FreeCAD/pull/23747)).
  - Patched the code that looks for coinciding points to make it possible to compare points represented by any iterable objects, such as lists and tuples ([PR#26976](https://github.com/FreeCAD/FreeCAD/pull/26976)).
  - Fixed positive overtravel for open profile in LeadInOut ([PR#25482](https://github.com/FreeCAD/FreeCAD/pull/25482)).
- petterreinholdtsen improved the Fanuc post-processor: adjusted the G-Code output to include FreeCAD body and job information, and fixed various small issues ([PR#27960](https://github.com/FreeCAD/FreeCAD/pull/27960)).
- sliptonic consolidates tapping into Drilling as a new strategy ([PR#27506](https://github.com/FreeCAD/FreeCAD/pull/27506)) and made several improvements in the machine code - changed the location of machine files, updated the machine data schema, and made small changes in the machine editor. ([PR#28011](https://github.com/FreeCAD/FreeCAD/pull/28011)).
- filippor fixed tests ([PR#28038](https://github.com/FreeCAD/FreeCAD/pull/28038)).

**TechDraw**:

- WandererFan allowed 3D dimension references to use point objects ([PR#28199](https://github.com/FreeCAD/FreeCAD/pull/28199)), fixed a crash that occurred when dropping dim text on a face face with nested voids ([PR#28097](https://github.com/FreeCAD/FreeCAD/pull/28097)), and another bug with PDF exporting ([PR#25716](https://github.com/FreeCAD/FreeCAD/pull/25716)).
- Bojan9597 fixed a bug where an annotation would stay highlighted in blue in the project tree after editing ([PR#28009](https://github.com/FreeCAD/FreeCAD/pull/28009)).

**Other changes**:

- Reqrefusion updated the contribution guideline to include rules regarding AI-generated patches ([PR#24646](https://github.com/FreeCAD/FreeCAD/pull/24646)). See an upcoming blog post about it for details.
- Krrish777 added status bar hints for modifier keys in the Measure tool ([PR#26568](https://github.com/FreeCAD/FreeCAD/pull/26568)).
- chennes fixed authorship and licensing for the converted materials where this data was missing or incorrect ([PR#28202](https://github.com/FreeCAD/FreeCAD/pull/28202)).
- paragforwork fixed the visibility of bounding boxes ([PR#28123](https://github.com/FreeCAD/FreeCAD/pull/28123)).
- pieterhijma improved the formatting of the doxygen output ([PR#25200](https://github.com/FreeCAD/FreeCAD/pull/25200)).
- Gaurang-2005 fixed the Collada exporter skipping App::Link geometry ([PR#27974](https://github.com/FreeCAD/FreeCAD/pull/27974)).
- TheRobotFox added new quantities to the Standard Unit System, which allow for calculations of light retention in optic paths and through substance transmission ([PR#27944](https://github.com/FreeCAD/FreeCAD/pull/27944)). Adding these quantities makes it possible to to plan optic systems (e.g., the positioning of lens/apertures) right inside a spreadsheet and use the results for the construction of parameterized parts.

3x380V, hyarion, chennes, greg19, PaddleStroke, JonasVgt, marioalexis84, Maik-0000FF, ipatch, mosfet80, dhruvjamwal, hyarion, pieterhijma, krissrex, petterreinholdtsen, kkocdko, and devanshibhatt23 contributed additional improvements and fixes.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.03.11).

**PR stats**: since the previous report, 87 pull requests have been merged (including backports to the v1.1 branch), and 52 new pull requests have been opened.

**Issue stats**: overall, there are 3326 open issues in the tracker, up by 4 from last week. There are [4 release blockers](https://github.com/FreeCAD/FreeCAD/issues?q=state%3Aopen%20label%3ABlocker%20milestone%3A1.1) for v1.1 currently, up by 2 from last week.