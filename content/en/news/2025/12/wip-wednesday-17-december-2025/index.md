---
title: WIP Wednesday, 17 December 2025
date: 2025-12-17
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 22 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**Sketcher**:

- AjinkyaDahale fixed the removal of the angle constraint when trimming edges ([PR#25914](https://github.com/FreeCAD/FreeCAD/pull/25914)).
- theo-vt patched the code to prevent autoscaling from happening when there are blocked geometries ([PR#26117](https://github.com/FreeCAD/FreeCAD/pull/26117)). This was a release blocker.

**Part and PartDesign**:

- saksham-malhotra-27 moved the Allow Compound property from experimental to base now that this feature is not considered experimental anymore ([PR#26180](https://github.com/FreeCAD/FreeCAD/pull/26180)).
- kadet1090 fixed some cases where the preview was stale and not recomputed after changes done via code ([PR#25989](https://github.com/FreeCAD/FreeCAD/pull/25989)).
- alfrix changed a translation bug in Hole where the head type dropdown would change to English when a different option is chosen ([PR#25932](https://github.com/FreeCAD/FreeCAD/pull/25932)).
- chennes fixed the incorrect reporting of a datum plane as being part of another body when it really isn't ([PR#26036](https://github.com/FreeCAD/FreeCAD/pull/26036)). He also fixed a midplane warning on document load ([PR#26071](https://github.com/FreeCAD/FreeCAD/pull/26071)).

**Assembly**:

- PaddleStroke fixed the drag mode for Ball joints ([PR#26222](https://github.com/FreeCAD/FreeCAD/pull/26222)) and made it possible to delete non-valid references ([PR#26055](https://github.com/FreeCAD/FreeCAD/pull/26055)).

**CAM**:

- Tarman3 removed unused code ([PR#25826](https://github.com/FreeCAD/FreeCAD/pull/25826) and [PR#25285](https://github.com/FreeCAD/FreeCAD/pull/25285)), allows multiple selections for SimpleCopy ([PR#24297](https://github.com/FreeCAD/FreeCAD/pull/24297)), did some preparations for upcoming Slot improvements ([PR#25839](https://github.com/FreeCAD/FreeCAD/pull/25839)), and made various minor code fixes ([PR#25218](https://github.com/FreeCAD/FreeCAD/pull/25218), [PR#25827](https://github.com/FreeCAD/FreeCAD/pull/25827), and [PR#26008](https://github.com/FreeCAD/FreeCAD/pull/26008)).
- Connor added a TSP tunnel solver ([PR#24726](https://github.com/FreeCAD/FreeCAD/pull/24726)) and then updated it ([PR#26205](https://github.com/FreeCAD/FreeCAD/pull/26205)) to match revised Python logic, including improved early exit, open-ended route handling, and performance tweaks. He also:
  - added units (metric/imperial) property to ToolBit ([PR#25783](https://github.com/FreeCAD/FreeCAD/pull/25783)),
  - added annotations support to Command constructor and Python bindings ([PR#25938](https://github.com/FreeCAD/FreeCAD/pull/25938)) and comprehensive tests ([PR#26123](https://github.com/FreeCAD/FreeCAD/pull/26123)),
  - added rigid Tapping back to legacy LinuxCNC postprocessor ([PR#257860](https://github.com/FreeCAD/FreeCAD/pull/257860)),
  - refactored stock used as a boundary to be distinct from regular stock ([PR#25960](https://github.com/FreeCAD/FreeCAD/pull/25960)).
- sliptonic patched the code to stop ignoring raised protrusions (bosses) when pocketing ([PR#24723](https://github.com/FreeCAD/FreeCAD/pull/24723)).
- petterreinholdtsen made the Fanuc post-processor compatible with FreeCAD 1.1 ([PR#25850](https://github.com/FreeCAD/FreeCAD/pull/25850)).

**BIM**:

- Roy_043 fixed the Lightweight reference mode ([PR#26068](https://github.com/FreeCAD/FreeCAD/pull/26068)) and the handling of old and new Diffuse Color options in ArchReference ([PR#26067](https://github.com/FreeCAD/FreeCAD/pull/26067)). He also fixed Arch CutVolume and CutPlane to work with pipes correctly ([PR#25952](https://github.com/FreeCAD/FreeCAD/pull/25952)).
- furgo16 added a new BIM Report command to extract data and generate schedules from a model using an SQL-like query language ([PR#24078](https://github.com/FreeCAD/FreeCAD/pull/24078)). It is an alternative to the ArchSchedule command, offering a different method to select, filter, and aggregate data.

**GUI**:

- Kadet1090 improved transform UI responsiveness ([PR#26029](https://github.com/FreeCAD/FreeCAD/pull/26029)), fixed a segfault in the Safe mode ([PR#26206](https://github.com/FreeCAD/FreeCAD/pull/26206)), the inability to use a larger marker size in Sketcher ([PR#26136](https://github.com/FreeCAD/FreeCAD/pull/26136)), and a stylesheet issue for the "Close without Saving" button text ([PR#25993](https://github.com/FreeCAD/FreeCAD/pull/25993)).
- chennes fixed UTF-8 support for property names ([PR#26121](https://github.com/FreeCAD/FreeCAD/pull/26121)).
- xtemp 09 renamed the Cancel in the Add Property dialog to Close ([PR#26016](https://github.com/FreeCAD/FreeCAD/pull/26016)).
- timpieces added proper tooltips for Material properties ([PR#25509](https://github.com/FreeCAD/FreeCAD/pull/25509)).

**Other changes**:

- ipatch fixed part of the issue in FEM where the Show Results slider would ignore the max value ([PR#25642](https://github.com/FreeCAD/FreeCAD/pull/25642)).
- Roy_043 fixed a lag when snapping to face intersections in Draft ([PR#26089](https://github.com/FreeCAD/FreeCAD/pull/26089)).
- drwho495 fixed a regression in the toponaming code ([PR#26019](https://github.com/FreeCAD/FreeCAD/pull/26019)).
- kadet1090 added a code quality problem report form ([PR#26204](https://github.com/FreeCAD/FreeCAD/pull/26204)), and furgo16 updated the problem report template for improved previews ([PR#26236](https://github.com/FreeCAD/FreeCAD/pull/26236)).

Roy_043, PaddleStroke, luzpaz, and YashSuthar983 contributed additional improvements and fixes.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.12.17).

**PR stats**: since the previous report, 67 pull requests have been merged (including backports to the v1.1 branch), and 48 new pull requests have been opened.

**Issue stats**: overall, there are 3092 open issues in the tracker, up by 43 from last week. There are 19 release blockers for v1.1 currently, down by 10 from last week.