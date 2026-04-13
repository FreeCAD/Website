---
title: WIP Wednesday, 26 November 2025
date: 2025-11-26
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


Maintainers have been backporting some of the fixes to the v1.1 branch where possible - 49 backports in the past 7 days. The list of changes in this recap applies to the main development branch (future v1.2).

This week in FreeCAD development:

**Sketcher**:

- PaddleStroke fixed three bugs:
  - new geometry would always default to construction in certain circumstances ([PR#25390](https://github.com/FreeCAD/FreeCAD/pull/25390));
  - FreeCAD would throw an unhandled exception in case of setting coincidence on both endpoints of a line/arc ([PR#25304](https://github.com/FreeCAD/FreeCAD/pull/25304));
  - Rotate would not copy the distance constraint attached to the edge ([PR#25434](https://github.com/FreeCAD/FreeCAD/pull/25434)).
- pjcreath fixed two blockers related to undo/redo ([PR#25498](https://github.com/FreeCAD/FreeCAD/pull/25498) and [PR#25501](https://github.com/FreeCAD/FreeCAD/pull/25501)).
- Ipatch fixed two issues: updating the state for a sketch's transform ([PR#25478](https://github.com/FreeCAD/FreeCAD/pull/25478)) and allowing grid snapping while hovering the mouse over an axis ([PR#25226](https://github.com/FreeCAD/FreeCAD/pull/25226)).

**PartDesign**:

- kadet1090 fixed boolean positioning ([PR#25580](https://github.com/FreeCAD/FreeCAD/pull/25580)) and ([PR#25579](https://github.com/FreeCAD/FreeCAD/pull/25579)).
- ipatch fixed a crash ([PR#25671](https://github.com/FreeCAD/FreeCAD/pull/25671)) and a regression where a datum plane could not be moved after another object inside a Body ([PR#25287](https://github.com/FreeCAD/FreeCAD/pull/25287)).

**Assembly**:

- PaddleStroke fixed 6 issues: lack of support for negative values in rackpinion and screw joints ([PR#25679](https://github.com/FreeCAD/FreeCAD/pull/25679)), crashes when manually deleting parts ([PR#25651](https://github.com/FreeCAD/FreeCAD/pull/25651)), two BOM issues ([PR#25613](https://github.com/FreeCAD/FreeCAD/pull/25613) and [PR#25421](https://github.com/FreeCAD/FreeCAD/pull/25421)), and two issues with the joint task panel ([PR#25445](https://github.com/FreeCAD/FreeCAD/pull/25445) and [PR#25612](https://github.com/FreeCAD/FreeCAD/pull/25612)).
- furgo16 fixed an issue where exploded views could not be added to TechDraw pages ([PR#25555](https://github.com/FreeCAD/FreeCAD/pull/25555)).

**CAM**:

- LarryWoestman fixed the linuxcnc postprocessor after the recent renaming.
- Connor updated CAM unit tests and LinuxCNC serializer to handle decimal separators consistently ([PR#25480](https://github.com/FreeCAD/FreeCAD/pull/25480)), added a new migration system to handle legacy parameter conversion for ToolBit assets and objects ([PR#25438](https://github.com/FreeCAD/FreeCAD/pull/25438)), and ensured Chipload is restored and displayed with user-preferred units ([PR#25570](https://github.com/FreeCAD/FreeCAD/pull/25570)).
- tarman3 fixed a regression in LeadInOut ([PR#25554](https://github.com/FreeCAD/FreeCAD/pull/25554)), allowed applying Pocket to BSplineSurface (PR#22738), fixed an overtravel in LeadInOut ([PR#25403](https://github.com/FreeCAD/FreeCAD/pull/25403)), and fixed occasional path duplication in Engrave ([PR#25372](https://github.com/FreeCAD/FreeCAD/pull/25372)).
- davidgilkaufman implemented automatic migration of tools in (old) custom working directory to the new tool system ([PR#25106](https://github.com/FreeCAD/FreeCAD/pull/25106)).

**BIM**:

- ezhukov changed the params variable to uppercase PARAMS ([PR#25663](https://github.com/FreeCAD/FreeCAD/pull/25663)).
- Roy_043 fixed the handling of several BIM_Sketch view properties ([PR#25339](https://github.com/FreeCAD/FreeCAD/pull/25339)).
- paullee0 fixed the recomputation of walls with centered multimaterials ([PR#25572](https://github.com/FreeCAD/FreeCAD/pull/25572)).

**FEM**:

- NewJoker added ccx disc ([PR#25268](https://github.com/FreeCAD/FreeCAD/pull/25268)) and ccx 2D pipe examples ([PR#25191](https://github.com/FreeCAD/FreeCAD/pull/25191)).
- chennes fixed two translation issues ([PR#25378](https://github.com/FreeCAD/FreeCAD/pull/25378) and [PR#25407](https://github.com/FreeCAD/FreeCAD/pull/25407)).

**GUI**:

- maxwxyz added a command to create an AnnotationLabel at the picked 3D position ([PR#23673](https://github.com/FreeCAD/FreeCAD/pull/23673)) and an icon for the Clarify Selection tool ([PR#24844](https://github.com/FreeCAD/FreeCAD/pull/24844)).
- tetektoza added support for searching for tooltips, comboboxes, and groups in Preferences ([PR#24283](https://github.com/FreeCAD/FreeCAD/pull/24283)).
- Rexbas fixed the Gesture style context menu segfault ([PR#25548](https://github.com/FreeCAD/FreeCAD/pull/25548)).
- kadet1090 reduced unnecessary rotation around normals for midpoints in the Attacher ([PR#25505](https://github.com/FreeCAD/FreeCAD/pull/25505)).
- xtem09 fixed the handling of ampersands in windowTitle for Windows and macOS ([PR#25424](https://github.com/FreeCAD/FreeCAD/pull/25424)).
- Syres916 fixed string encoding for document, object, and subobject names in PropertyLink, SelectionSearch, PD Sketch Based Tasks, Part Primitives, and Document handling ([PR#25479](https://github.com/FreeCAD/FreeCAD/pull/25479)). He also increased the contrast of menu separators and down arrows in comboboxes ([PR#25526](https://github.com/FreeCAD/FreeCAD/pull/25526)).
- PaddleStroke fixed losing thumbnails when saving partially loaded documents ([PR#25458](https://github.com/FreeCAD/FreeCAD/pull/25458)) and a tooltip ([PR#25693](https://github.com/FreeCAD/FreeCAD/pull/25693)).
- Ipatch fixed the inability to select all instances of an object in the tree ([PR#25503](https://github.com/FreeCAD/FreeCAD/pull/25503)).
- pieterhijma fixed refreshing on boolean property toggle ([PR#25632](https://github.com/FreeCAD/FreeCAD/pull/25632)).

**Other changes**:

- oursland re-enabled the Reverse Engineering workbench that is Qt6-compatible now ([PR#25492](https://github.com/FreeCAD/FreeCAD/pull/25492)).
- BurksEngineering added read-only warnings showing up when users save documents with read-only permissions ([PR#25532](https://github.com/FreeCAD/FreeCAD/pull/25532)).
- Roy_043 fixed number_length for imperial dimensions ([PR#25369](https://github.com/FreeCAD/FreeCAD/pull/25369)).

Additional improvements and fixes were contributed by AjinkyaDahale, chennes, Logstor, adrianinsaval, maxwxyz, ipatch, Lgt2x, and mnesarco.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.11.26).

**PR stats**: since the previous report, 115 pull requests have been merged, and 53 new pull requests have been opened.

**Issue stats**: overall, there are 3037 open issues in the tracker, down by 10 from last week. There are 5 release blockers for v1.1 currently, up by 3 from last week.