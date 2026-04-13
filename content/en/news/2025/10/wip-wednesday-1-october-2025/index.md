---
title: WIP Wednesday, 1 October 2025
date: 2025-10-01
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

**Sketcher**:

- PaddleStroke fixed one release blocker, two regressions, and a few more bugs.
- theo-vt fixed a crash in the Scale tool; it should now better handle a dimension of a single line.
- longrackslabs patched all constraint tools to provide context-aware hints that remember user selections and guide them through the correct workflow.
- kadet1090 fixed Sketcher to not enforce visibility of planes on edit.
- tetektoza fixed a bug where on-view parameters would disregard 0 as a valid input.

**Part Design**:

- PaddleStroke fixed two blockers and two regressions, including one that made some properties in Pocket uneditable.
- kadet1090 fixed a crash that would occur in rare cases where features were placed outside the body container. He also fixed the occasional incorrect rendering of transparent profile previews.
- 3x380V fixed GCC warning, and marioalexis84 fixed a bug where the AllowCompound parameter would not be enabled by default for indirectly created bodies despite the preference being checked.

**Assembly**:

- PaddleStroke fixed a crash when activating flexible sub-assemblies by implementing support for Link groups in sub-assemblies. He also fixed a release blocker where adding the limits for the joints would break the joints.
- furgo16 fixed a bug that prevented any joints from being created in certain scenarios.

**TechDraw**:

- WandererFan fixed several bugs, including a release blocker where an area annotation would cause a crash if multiple faces were selected.
- ryankembrey fixed a bug where the view frame would not reset with a click.

**CAM**:

- sliptonic fixed the size of the direction marker for high-resolution displays.
- Connor fixed the base template substitution and the style of the CAM Sanity Report. He also fixed changing the spindle direction or material in the tool library editor and converted the tapping operation to an experimental feature (and applied several fixes and improvements to it).

**BIM**:

- furgo16 refactored parts of the Arch module and introduced quite a handful of improvements to the section plane task panel (see [PR#23826](https://github.com/FreeCAD/FreeCAD/pull/23826) for the full list).
- galou fixed a regression in DAE import and restored support for non-triangular faces.
- Roy_043 fixed several bugs.

**GUI**:

- marcuspollio updated group icons in Draft.
- furgo16 brought back visual feedback on toolbar button press and hover.
- Tiago-Almeida007 slightly reorganized tree view preferences.

**Other changes**:

- B0cho, NewJoker, and marioalexis84 fixes various minor issues and a few memory leaks in FEM.
- tetektoza patched the core to allow deleting objects inside a group recursively.
- sliedes fixed displaying objects in the 3D view on Wayland with native and proprietary Nvidia drivers (see [PR#23768](https://github.com/FreeCAD/FreeCAD/pull/23768) for details).

Additional improvements and fixes were contributed by Roy-043, chennes, marioalexis84, matt-taylor-git, ipatch, wwmayer, 3x380V, PaddleStroke, kadet1090, mrpilot2, mnesarco, tetektoza, luzpaz, Rexbas, captain0xff, Mikestriken, and FlachyJoe.

For translators, some translatable text issues have been fixed, and translation updates have been merged from Crowdin.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.10.01).

**PR stats**: since the previous report, 80 pull requests have been merged, and 38 new pull requests have been opened.

**Issue stats**: overall, there are 2954 open issues in the tracker, down by 43 from last week. 30 known release blockers remain unfixed for v1.1, down by 15 from last week.