---
title: WIP Wednesday, 29 October 2025
date: 2025-10-29
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

**BIM**:

- Roy_043 fixed several minor issues ([PR#24805](https://github.com/FreeCAD/FreeCAD/pull/24805), [PR#24847](https://github.com/FreeCAD/FreeCAD/pull/24847), [PR#24846](https://github.com/FreeCAD/FreeCAD/pull/24846), [PR#24806](https://github.com/FreeCAD/FreeCAD/pull/24806)).
- tetektoza fixed beam rotation when the Base property is cleared ([PR#24831](https://github.com/FreeCAD/FreeCAD/pull/24831)).
- paullee0 fixed a bug in ArchStairs where the height would be wrong when toSlabThickness & Landings AtCenter were set ([PR#24864](https://github.com/FreeCAD/FreeCAD/pull/24864)).

**CAM:**
- Connor fixed the expression editor so that widgets refresh after closing ([PR#24837](https://github.com/FreeCAD/FreeCAD/pull/24837)) and refactored the LeadInOut task panel to use QuantitySpinBox ([PR#24818](https://github.com/FreeCAD/FreeCAD/pull/24818)).
- Tarman3 fixed several issues in the LeadInOut dress-up ([PR#24810](https://github.com/FreeCAD/FreeCAD/pull/24810), [PR#24666](https://github.com/FreeCAD/FreeCAD/pull/24666), [PR#24471](https://github.com/FreeCAD/FreeCAD/pull/24471)).
- sebastianohl fixed the KineticNCBeamicon2 postprocessor to eliminate one of the two M-commands in one line ([PR#24809](https://github.com/FreeCAD/FreeCAD/pull/24809)) to please the Zero-4 machine controller.

**TechDraw**:

- WandererFan fixed a view border size issue ([PR#23623](https://github.com/FreeCAD/FreeCAD/pull/23623)).
- Syres916 fixed the way Preferences, Property dock, and the task panel reference the first angle and the third angle so that live update works again ([PR#24762](https://github.com/FreeCAD/FreeCAD/pull/24762)).
- tetektoza fixed an offset of centerlines and cosmetic edges on DXF exports ([PR#24858](https://github.com/FreeCAD/FreeCAD/pull/24858)).

**GUI**:

- ryankembrey cherry-picked a patch by wwmayer that adds new behavior: now when the Esc key is pressed after interacting with the 3D view, the pending changes are correctly reverted instead of being accepted ([PR#24277](https://github.com/FreeCAD/FreeCAD/pull/24277)).
- hyarion moved the task panel to the right side of the window by default ([PR#23471](https://github.com/FreeCAD/FreeCAD/pull/23471)).

**Other changes**:

- Roy_043 fixed a relative path issue when double-clicking a hatch in the Tree View in Draft ([PR#24883](https://github.com/FreeCAD/FreeCAD/pull/24883)).
- theo-vt fixed a virtual space issue in Sketcher ([PR#24398](https://github.com/FreeCAD/FreeCAD/pull/24398)).
- FlachyJoe changed the default error policy for Refine feature so it only warns on failure ([PR#23486](https://github.com/FreeCAD/FreeCAD/pull/23486)).
- PaddleStroke fixed two issues in Assembly: the renaming of joints ([PR#24686](https://github.com/FreeCAD/FreeCAD/pull/24686)) and the isolation issue when the object and the link are both in the assembly ([PR#24781](https://github.com/FreeCAD/FreeCAD/pull/24781)).
- tetektoza fixed the height of imported TEXT and MTEXT entities in the new (C++) DXF importer ([PR#24859](http://github.com/FreeCAD/FreeCAD/pull/24859)).
- NepEgor added the missing constraint on vertical orientation to the Turntable orbit style ([PR#24861](https://github.com/FreeCAD/FreeCAD/pull/24861)).
- filippor added RPM building to CI ([PR#21063](https://github.com/FreeCAD/FreeCAD/pull/21063)).

Additional improvements and fixes were contributed by chennes and pyro9.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.10.29) (currently broken due to CI issues).

**PR stats**: since the previous report, 31 pull requests have been merged, and 38 new pull requests have been opened.

**Issue stats**: overall, there are 2990 open issues in the tracker, up by 11 from last week. There are 13 release blockers currently, down by 1 from last week.

The team postponed creating v1.1 release branch due to broken CI. Once that is fixed, they will create a branch and start preparing the first release candidate.