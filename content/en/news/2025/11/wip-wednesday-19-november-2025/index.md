---
title: WIP Wednesday, 19 November 2025
date: 2025-11-19
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Quick disclaimer: maintainers have created a branch for the upcoming v1.1 release and started reviewing and merging patches for v1.2. They have also been backporting some of the fixes to the v1.1 branch where possible - 36 backports in the past 7 days. The list of changes in this recap applies to the main development branch.

This week in FreeCAD development:

**Sketcher**:

- PaddleStroke improved selection efficiency in terms of how many transactions FreeCAD performs ([PR#25254](https://github.com/FreeCAD/FreeCAD/pull/25254) and [PR#25255](https://github.com/FreeCAD/FreeCAD/pull/25255)).
- theo-vt improved the constraint solver ([PR#25318](https://github.com/FreeCAD/FreeCAD/pull/25318)) and fixed Fillet/Chamfer when selecting vertices that contain construction geometry as a third line ([PR#25319](https://github.com/FreeCAD/FreeCAD/pull/25319)).
- ipatch fixed a big where points would get repositioned after snapping ([PR#25219](https://github.com/FreeCAD/FreeCAD/pull/25219))
- Logstor and revaarathore11 fixed tooltips ([PR#PR#24839](https://github.com/FreeCAD/FreeCAD/pull/24839) and [PR#PR#24825](https://github.com/FreeCAD/FreeCAD/pull/24825)).

**Part and PartDesign**:

- captain0xff fix the interactive controls for Revolution and Groove commands in PD ([PR#25202](https://github.com/FreeCAD/FreeCAD/pull/25202)).
- ipatch fixed a regression in Part where a file created with an earlier version of FreeCAD would not load correctly, if there was a slice of a slice in the project ([PR#25293](https://github.com/FreeCAD/FreeCAD/pull/25293)).

**Assembly**: PaddleStroke fixed 8 issues, including incorrect exploded views in TD ([PR#25426](https://github.com/FreeCAD/FreeCAD/pull/25426)), the handling of partially loaded documents when inserting links ([PR#25275](https://github.com/FreeCAD/FreeCAD/pull/25275)), a crash on moving unconnected parts ([PR#25433](https://github.com/FreeCAD/FreeCAD/pull/25433)), and more ([PR#25270](https://github.com/FreeCAD/FreeCAD/pull/25270), [PR#25277](https://github.com/FreeCAD/FreeCAD/pull/25277), [PR#25279](https://github.com/FreeCAD/FreeCAD/pull/25279), [PR#25396](https://github.com/FreeCAD/FreeCAD/pull/25396), [PR#25393](https://github.com/FreeCAD/FreeCAD/pull/25393)).

**TechDraw**:

- WandererFan fixed several issues related to Vertex and Center Mark display and selection ([PR#25044](https://github.com/FreeCAD/FreeCAD/pull/25044)).
- FlachyJoe fixed a bug where the workbench would remove trailing zeroes from the "%.0w" format spec ([PR#25367](https://github.com/FreeCAD/FreeCAD/pull/25367)).

**BIM**:

- furgo16 made it possible to remove a wall's base object and retain the wall's location and parametric nature ([PR#24550](https://github.com/FreeCAD/FreeCAD/pull/24550)) and updated the search box text in the BIM Material Manager ([PR#24754](https://github.com/FreeCAD/FreeCAD/pull/24754)).
- paullee0 disabled the 'At each corner' property for Landings, since it's not implemented yet ([PR#25278](https://github.com/FreeCAD/FreeCAD/pull/25278)).
- PhoneDroid refactored a function in the BIM Project Manager ([PR#25140](https://github.com/FreeCAD/FreeCAD/pull/25140)).
- Roy_043 fixed a bug where it was impossible to create walls with Building US unit system selected ([PR#25288](https://github.com/FreeCAD/FreeCAD/pull/25288)).

**CAM**:

- 10 patches from tarman3, mainly in LeadInOut, Slot, Engrave, and SelectLoop ([PR#25371](https://github.com/FreeCAD/FreeCAD/pull/25371), [PR#24829](https://github.com/FreeCAD/FreeCAD/pull/24829), [PR#25087](https://github.com/FreeCAD/FreeCAD/pull/25087), [PR#25212](https://github.com/FreeCAD/FreeCAD/pull/25212), [PR#24185](https://github.com/FreeCAD/FreeCAD/pull/24185), [PR#25215](https://github.com/FreeCAD/FreeCAD/pull/25215), [PR#24852](https://github.com/FreeCAD/FreeCAD/pull/24852), [PR#25074](https://github.com/FreeCAD/FreeCAD/pull/25074), [PR#22764](https://github.com/FreeCAD/FreeCAD/pull/22764), [PR#25101](https://github.com/FreeCAD/FreeCAD/pull/25101)).
- 3 patches by Connor: rigid tapping in the linuxcnc post processor using Path Command Annotations feature ([PR#24676](https://github.com/FreeCAD/FreeCAD/pull/24676)), Path command annotations ([PR#24675](https://github.com/FreeCAD/FreeCAD/pull/24675)), and a fix for a crash ([PR#25346](https://github.com/FreeCAD/FreeCAD/pull/25346)).
- 2 patches by davidgilkaufman: ramp and lead in/out feed rates to the tool controller ([PR#23285](https://github.com/FreeCAD/FreeCAD/pull/23285)) and improved Adaptive operation to successfully generate for small stepover ([PR#24044](https://github.com/FreeCAD/FreeCAD/pull/24044)), both part of his grant work.
- pmarcelll fixed model centering when HiDPI scaling is active ([PR#25241](https://github.com/FreeCAD/FreeCAD/pull/25241)).
- sliptonic did some postprocessors renaming and cleanup ([PR#24771](https://github.com/FreeCAD/FreeCAD/pull/24771)).
- emmanuel-ferdman fixed the array dressup test ([PR#22598](https://github.com/FreeCAD/FreeCAD/pull/22598)).

**GUI**:

- kadet1090 patched the GUI code to save the default layout after the first launch ([PR#25457](https://github.com/FreeCAD/FreeCAD/pull/25457)) and fixed the stylesheet loading order ([PR#25468](https://github.com/FreeCAD/FreeCAD/pull/25468)).
- tetektoza differentiated completion activation modes in Expression Editor ([PR#25244](https://github.com/FreeCAD/FreeCAD/pull/25244)).

**Other changes**:

- Roy_043 patched user-visible messages all around the GUI in numerous commits.
- ryankembrey made some sketch-related user-visible messages consistent ([PR#24278](https://github.com/FreeCAD/FreeCAD/pull/24278)).
- pieterhijma improved the documentation of transactions ([PR#21494](https://github.com/FreeCAD/FreeCAD/pull/21494)).
- davesrocketshop fixed an issue in materials where assigning a material without appearance settings would override appearance settings ([PR#24916](https://github.com/FreeCAD/FreeCAD/pull/24916)).
- ipatch fixed a regression in STEP exporting ([PR#25042](https://github.com/FreeCAD/FreeCAD/pull/25042)).

Additional improvements and fixes were contributed by Mr-Rahul-Paul, Roy-043, FEA-eng, chennes, luzpaz, rehan-ahmed-aix, StephanTLavavej, furgo16, aqeel13932, pinkavaj, Connor, galou, and kadet1090.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.11.20).

**PR stats**: since the previous report, 117 pull requests have been merged, and 43 new pull requests have been opened.

**Issue stats**: overall, there are 3047 open issues in the tracker, down by 2 from last week. There are 2 release blockers for v1.1 currently, down by 3 from last week.