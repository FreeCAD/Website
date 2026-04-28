---
title: WIP Wednesday, 20 August 2025
date: 2025-08-20
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

- matthiasdanner removed the **Edit Value** option from the right-click menu of non-dimensional constraints, as it only works for dimensional constraints like length or angle.
- valir fixed a crash that would happen when modifying a datum line right after modifying a sketch.

**Part**:

- hyarion fixed WireJoiner error handling (the remnant of a patch backport from RT's fork).
- kadet1090 fixed a crash that would occur because of an uncaught exception in Cross Sections computation.

**Part Design**:

- maxwxyz enabled the support for multiple bodies by default. This was considered an experimental option earlier.
- hyarion continued working on support for sketches as neutral planes in PD's Draft.
- theo-vt fixed a regression where it would be impossible to create a hole from a SubShapeBinder. He also removed the transform tool option from the Hole's context menu to align it with other PartDesign features.

**TechDraw**:

- theo-vt fixed balloon annotation unlinking after undo-redo. He also added the missing transaction code to the remaining TD commands that were missing it, so now all commands in TechDraw should support undo-redo.
- ryankembrey patched the cosmetic circles code to bring all the commands into one unified dropdown in the toolbar and the same submenu. Here is a quick video:

{{< youtube id=lFys3EEsqjY title="TechDraw Cosmetic Circle Tools UI Improvements - FreeCAD" loading=lazy >}}

**FEM**:

- NewJoker added support for CalculiX membrane elements. He also added Amplitude support for rigid body constraints.
- marioalexis84:
  - Changed the priority of the Elmer equations to be set based on the order of definition, starting with a sufficiently high number (255 is max) and decreasing the values as the equations are defined.
  - Fixed a regression where CalculiX output wouldn't be created from `.dat` files after a recent refactoring effort.
  - Added a new boolean **Glue** option to create conformal meshes from Netgen.
  - ickby contributed several bug fixes, including one that makes the Branch filter Python object work well with the data extraction code.

**GUI**:

- tetektoza fixed a small UI bug in Preferences.
- captain0xff fixed the cropping of some Sketcher icons on HiDPI displays.

**Other changes**:

- Roy_043 fixed several issues with the mouse delay in Draft.
- drwho495 fixed several toponaming issues in part ([PR#23151](https://github.com/FreeCAD/FreeCAD/pull/23151), [PR#22785](https://github.com/FreeCAD/FreeCAD/pull/22785)).
- WandererFan fixed measurement visibility after a reload.
- wwmayer fixed a crash in Sheet (patch cherry-picked by hyarion).

Additional improvements and fixes were contributed by marioalexis84, Roy_043, kadet1090, NewJoker, chennes, luzpaz, and corpix.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.08.20). Please note that weekly builds are now only available from the main git repository's [Tags](https://github.com/FreeCAD/FreeCAD/tags) section. You can find earlier builds there as well, e.g., if you need to bisect a bug. FreeCAD-Bundle is not used for weekly builds anymore.

**PR stats**: since the previous report, 50 pull requests have been merged, and 57 new pull requests have been opened.

**Issue stats**: overall, there are 2958 open issues in the tracker, up by 15 from last week.