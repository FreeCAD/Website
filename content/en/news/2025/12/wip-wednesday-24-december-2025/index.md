---
title: WIP Wednesday, 24 December 2025
date: 2025-12-24
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 45 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**Sketcher**:

- ipatch fixed three issues: polygon distortion when repositioning or constraining ([PR#26258](https://github.com/FreeCAD/FreeCAD/pull/26258)), lack of live preview of sketch placement ([PR#26033](https://github.com/FreeCAD/FreeCAD/pull/26033)), and not being able to keep snapped position when releasing the mouse for updated sketch points ([PR#26102](https://github.com/FreeCAD/FreeCAD/pull/26102)).
- marbocub added reverse mapping correction to Carbon Copy so that the orientation of geometry is as expected ([PR#25745](https://github.com/FreeCAD/FreeCAD/pull/25745)).

**Part:**

- Roy-043 fixed an issue where the attachment would not remember local coordinates (attachment offset) on first launch ([PR#25923](https://github.com/FreeCAD/FreeCAD/pull/25923)). He also fixed a release blocker where part attachment would work incorrectly in some cases ([PR#26298](https://github.com/FreeCAD/FreeCAD/pull/26298)).
- Lgt2x improved preview performance ([PR#26363](https://github.com/FreeCAD/FreeCAD/pull/26363)).
- YashSuthar983 fixed a regression where files created with 1.0.x would fail to recompute in 1.2dev ([PR#26253](https://github.com/FreeCAD/FreeCAD/pull/26253)).

**PartDesign**:

- ipatch fixed a release blocker where sketches based on subshapebinder external references would not update ([PR#26212](https://github.com/FreeCAD/FreeCAD/pull/26212)). He also fixed a bug where selected references would be displayed without subelements in the task panel ([PR#26227](https://github.com/FreeCAD/FreeCAD/pull/26227)).
- alfrix fixed Hole clearance and thread depth not appearing in the task panel ([PR#26289](https://github.com/FreeCAD/FreeCAD/pull/26289) and [PR#26290](https://github.com/FreeCAD/FreeCAD/pull/26290)).
- chennes fixed a release blocker where the macOS build would crash when applying the Hole command ([PR#26369](https://github.com/FreeCAD/FreeCAD/pull/26369)).
- kadet1090 fixed two release blockers where newer versions of FreeCAD would fail to process v0.21 files correctly ([PR#26137](https://github.com/FreeCAD/FreeCAD/pull/26137) and [PR#26141](https://github.com/FreeCAD/FreeCAD/pull/26141)).

**CAM**:

- MTronics contributed a patch towards fixing the issue where the task panel in CAM ignores selected stock ([PR#26413](https://github.com/FreeCAD/FreeCAD/pull/26413)).
- sliptonic fixed pure vertical linking move in the new MillFacing command ([PR#26195](https://github.com/FreeCAD/FreeCAD/pull/26195)) and a tolerance issue with hole detection in Pocket ([PR#26404](https://github.com/FreeCAD/FreeCAD/pull/26404)).
- Dimitris75 incorporated the OCL Adaptive algorithm into the Waterline operation to provide a significant speed advantage over the OCL Drop-Cutter algorithm ([PR#23149](https://github.com/FreeCAD/FreeCAD/pull/23149)).
- phaseloop improved VCarve routing by introducing virtual edge backtracking ([PR#25049](https://github.com/FreeCAD/FreeCAD/pull/25049)).
- tarman3 contributes several fixes and improvements:
  - Made it possible to select multiple shapes in the task panel, e.g., for the Profile command ([PR#22304](https://github.com/FreeCAD/FreeCAD/pull/22304)).
  - Patched the OperationCopy command to allow for all operations and copy dressups recursively ([PR#24819](https://github.com/FreeCAD/FreeCAD/pull/24819)).
  - Fixed the Active icon state for MillFacing and Arraw ([PR#26316](https://github.com/FreeCAD/FreeCAD/pull/26316) and [PR#26217](https://github.com/FreeCAD/FreeCAD/pull/26217)).
  - Fixed toggling items in Job and Operations groups ([PR#24872](https://github.com/FreeCAD/FreeCAD/pull/24872)).
- Connor improved path optimization when the ending point is flexible by adding open-route optimizations to the recently added point-based TSP solver ([PR#26260](https://github.com/FreeCAD/FreeCAD/pull/26260)). He also added migration for toolbit metrici/imperial units ([PR#26409](https://github.com/FreeCAD/FreeCAD/pull/26409)).

**BIM**:

- Roy-043 fixed the handling of IfcGridAxis ([PR#26225](https://github.com/FreeCAD/FreeCAD/pull/26225)) and two release blockers: snapping to object without Base when placing window results in AttributeError ([PR#26424](https://github.com/FreeCAD/FreeCAD/pull/26424)) and being unable to delete native IfcBuilding and IfcLevel objects ([PR#26219](https://github.com/FreeCAD/FreeCAD/pull/26219)).
- furgo16 started reducing visual clutter in BIM ([PR#25147](https://github.com/FreeCAD/FreeCAD/pull/25147)), fixed an error when adding custom windows ([PR#26336](https://github.com/FreeCAD/FreeCAD/pull/26336)) and the lock removal of Sill property ([PR#26333](https://github.com/FreeCAD/FreeCAD/pull/26333)). He also renamed ArchWindow's Sill property to SillHeight and handled one-way migration of properties from older projects ([PR#26277](https://github.com/FreeCAD/FreeCAD/pull/26277)).

**TechDraw**:

- WandererFan fixed the page rectangle tearing when panning ([PR#26021](https://github.com/FreeCAD/FreeCAD/pull/26021)) and another issue where printing and PDF export do not work correctly with custom paper sizes ([PR#26124](https://github.com/FreeCAD/FreeCAD/pull/26124)).
- FlachyJoe fixed the %r format spec ([PR#26133](https://github.com/FreeCAD/FreeCAD/pull/26133)).

**GUI**:

- VM4Dim fixed the bug where group names would not be displayed correctly if they were not in Latin ([PR#26285](https://github.com/FreeCAD/FreeCAD/pull/26285)).
- YashSuthar983 made it possible to select all instances of an object in the tree ([PR#26096](https://github.com/FreeCAD/FreeCAD/pull/26096)).
- kadet1090 contributed several fixes and improvements:
  - Fixed a bug where numeric input fields would not evaluate arithmetic expressions (e.g., "10+10mm") and revert to the previous value ([PR#26358](https://github.com/FreeCAD/FreeCAD/pull/26358)).
  - Removed shortcuts for overlay toggles to avoid changing the layout of FreeCAD irreversibly and unpredictably ([PR#26376](https://github.com/FreeCAD/FreeCAD/pull/26376)).
  - Fix the separators` appearance ([PR#26278](https://github.com/FreeCAD/FreeCAD/pull/26278)).

**Other changes**:

- PaddleStroke fixed a release blocker in Assembly to make it possible to edit joint references ([PR#26054](https://github.com/FreeCAD/FreeCAD/pull/26054)).
- Roy-043 patch Draft to make OrthoArray work with the Building US unit system ([PR#26280](https://github.com/FreeCAD/FreeCAD/pull/26280)).
- rodrigo-olaya fixed an RGB rounding bug in the material appearance editor ([PR#26134](https://github.com/FreeCAD/FreeCAD/pull/26134)).
- Lgt2x improved SVG exporting performance ([PR#26149](https://github.com/FreeCAD/FreeCAD/pull/26149)).
- marbocub fixed rotation expression errors by adding unit handling and angle range validation ([PR#26058](https://github.com/FreeCAD/FreeCAD/pull/26058)).
- timpieces improved user experience on macOS by disabling actions while file dialogs are open ([PR#26171](https://github.com/FreeCAD/FreeCAD/pull/26171)) and blocking shortcuts from overriding text input ([PR#26170](https://github.com/FreeCAD/FreeCAD/pull/26170)).

Syres916, kadet1090, moench-tegeder, PaddleStroke, and chennes contributed additional improvements and fixes.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.12.24).

**PR stats**: since the previous report, 102 pull requests have been merged (including backports to the v1.1 branch), and 36 new pull requests have been opened.

**Issue stats**: overall, there are 3121 open issues in the tracker, up by 29 from last week. There are 8 release blockers for v1.1 currently, down by 11 from last week.

Two other notable news:

- David Carter recently updated his [proposal for the material editor improvements](https://github.com/FreeCAD/FreeCAD-Enhancement-Proposals/blob/da8ee42ec39d086aff491902993deb3feec3c162/FEPs/FEP-0006-materials-editor/README.md) and [started working](https://github.com/FreeCAD/FreeCAD/pull/26434) on a tag widget. [See here](https://github.com/FreeCAD/FreeCAD-Enhancement-Proposals/discussions/33) for the discussion of the overall proposal.
- Pieter Hijma's [enhancement proposal for variant parts](https://github.com/FreeCAD/FreeCAD-Enhancement-Proposals/blob/master/FEPs/FEP-0010-variant-parts/README.md) has been accepted. He created a pull request that implements [fine-grained recomputes](https://github.com/FreeCAD/FreeCAD/pull/25603)(phase 1 of the implementation) and is now moving to the second phase of the implementation, which is adding variant links.

Happy holidays, everyone!