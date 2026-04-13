---
title: WIP Wednesday, 24 September 2025
date: 2025-09-24
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

- theo-vt fixed a blocker where FreeCAD would crash when trimming arcs and lines. She also fixed another bug where splitting an edge would work incorrectly.
- PaddleStroke improved circle constraint positioning, fixed a crash on constraint selection, and fixed a blocker where arc offset dimension constraint wouldn't work properly.
- matthiasdanner fixed the "Display only filtered constraints" option, as well as a bug where sketches with only external geometry would be considered empty.

**Part Design**:

- PaddleStroke fixed a bug that prevented datums and sketches from being reordered in the tree by dragging and dropping them.
- alfrix fixed two bugs in Hole.
- Further fixes arrived from xtemp09, Roy-043, NomAnor, theo-vt, and jffmichi.

**TechDraw**:

- ryankembrey disallowed double-dragging in Projection Groups.
- pmjdebrujn reorganized templates by splitting them into ISO and ASME folders.
- WandererFan fixed two minor issues, including one where an auto-balloon would be placed on any mouse click.

**CAM**:

- sliptonic fixed two minor issues and a release blocker. The latter required reverting early loading of CAM preference pages: this needs an overall architecture improvement first, so CAM will be patched accordingly later on.
- lagnat fixed the Dragknife dress-up to avoid making unnecessary maneuvers.
- pmjdebrujn fixed two issues in PocketShape's Offset Patterns. He also changed the default value of StepOver in Pocket to 50%.
- dbtayl fixed the incorrect processing of extensions in the Adaptive operation.
- tarman3 fixed stock creation for flat objects and a minor issue in LeadInOut.
- Connor fixed an issue with the Group drop-down list in PropertyBag (when you create a new property).
- papaathome fixed a bug that would create a difference between rotational paths generated for X/A and Y/B axis.
- itsharrie renamed Offset Pattern to Clearance Pattern in Pocket Shape / Data pane to improve the terminology.
- davidgilkaufman fixed two bugs, including one regression, and reordered job tabs to put Setup first.

**GUI**:

- pieterhijma fixed [several issues](https://github.com/FreeCAD/FreeCAD/pull/23648) related to using expressions and varsets. He also fixed a crash in the Property Link dialog and improved the UX for expanding and collapsing Property View.
- captain0xff fixed an issue with the on-view draggers.
- chennes improved the UX of migrating settings from older to newer versions of FreeCAD.
- kadet1090 added the handling of an edge case where base features are dragged out of a Body object. He also fixed a regression where elements of a link cannot be moved individually with a Transform.

**Other changes**:

- Roy-043 fixed lags in the snapper code in Draft and the handling of materials in Arch_Equipment.
- paullee0 fixed Regression Curve support in BIM/Arch.
- PaddleStroke fixed five issues in Assembly, including two crashers, and several linking-related issues.
- marioalexis84 fixed several issues in FEM.
- drwho495 fixed another toponaming issue.

Additional improvements and fixes were contributed by furgo16, PaddleStroke, luzpaz, chennes, matt-taylor-git, and MisterMakerNL.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.09.24).

**PR stats**: since the previous report, 74 pull requests have been merged, and 48 new pull requests have been opened.

**Issue stats**: overall, there are 2997 open issues in the tracker, up by 27 from last week. 45 known release blockers remain unfixed for v1.1, down by 4 from last week.