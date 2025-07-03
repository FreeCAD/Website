---
title: 'WIP Wednesday: 11 September 2024'
date: 2024-09-11
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

**BIM**: furgo16 and Roy_043 fixed several bugs including incorrect profile creation, color issues in ArchFence, and incorrect transparency of glass panels in windows and doors.

**Assembly**: PaddleStroke replaced Offset and Rotation properties in several joint types with Offset1 and Offset2 placement properties internally. This will provide full control over both JCS positions using FreeCAD's standard attachment offset functionality. However, the UI for that is too late for inclusion into v1.0 (the code is in a [draft PR](https://github.com/FreeCAD/FreeCAD/pull/16317), there's a video there if you are interested).

**Sketcher**: kadet1090, Morimiue, and PaddleStroke fixed several issues including two crashers. MisterMakerNL updated selection colors to be better visible.

**TechDraw**: WandererFan and benj5378 fixed two bugs in balloons code, one for incorrect initial balloon placement on rotated view, the other ­- for uncentered balloon labels.

**FEM**: marioalexis84 fixed two bugs related to [Elmer](https://github.com/ElmerCSC/elmerfem) solver code, and NewJoker fixed several issues with fluid material properties.

**Spreadsheet**: Syres916 fixed a CSV importing bug, and hyarion fixed XSLX importing issues.

**Materials**: davesrocketshop added missing UI elements to support per-face transparencies. Transparency information is now also displayed in the appearance inspector, and alpha channel is exposed in the color selector dialog.

**Measuring**: Murmele patched the new Measure tool to show the delta option in the interactive mode (before you could only see it if you saved the measurement as an object). Syres916 disabled Quick Measure in TechDraw, Spreadsheet, Part Container and Origin objects, because the feature doesn't make a lot of sense there while using system resources.

**GUI**:

- xtemp09 did some fine-tuning in the Light Sources page in Preferences.

- Rexbas fixed two bugs related to the orthographic camera.

- benj5378 added style, theme and qtstyle info to clipboard about info to help investigating UI issues.

Among other changes:

- CalligaroV fixed another bug in the toponaming code.

- Roy_043 fixed snapping to endpoints of dimension lines in Draft - a regression introduced in v0.19.

- FlachyJoe fixed incorrect helix placement in PartDesign.

- pieterhijma deduplicated file extensions on exporting.

- spanner888 fixed a bug where the CAM's toolbit library wouldn't always be saved.

**PR stats**: since the previous report, 45 pull requests have been merged, 36 new pull requests have been opened.

**Issue stats**: overall, there are 1998 open issues in the tracker, up by 53 from last week. 7 of them are v1.0 release blockers, down by 2 from last week.