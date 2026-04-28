---
title: WIP Wednesday, 10 September 2025
date: 2025-09-10
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

- theo-vt fixes four bugs, including one release blocker, two crashers, and one regression (the Scale tool would crash or cause excessive constraints in the presence of non-scalable geometry).
- PaddleStroke and NewJoker contributed two minor UI fixes.

**Part**:

- PaddleStroke fixed a release blocker where FreeCAD would change the color and transparency of solids generated based on sketches.
- maxwxyz patched the dragger to attach to the midpoint / axis for circular edges and faces.

**Part Design**:

- kadet1090 rearranged UI elements in the Hole task panel in a more logical manner.
- PaddleStroke fixes two release blockers and a regression (a feature couldn't be added to an existing Polar Pattern).

**TechDraw**:

- WandererFan fixed a bug where the check for horizontal/vertical dimensions would give the wrong result in some cases.
- chennes finished the removal of Link and Landmark from GUI.

**CAM**:

- davidgilkaufman and tarman3 contributed various new features and improvements to the LeadInOut functionality: customizing line and arc angles, new entrance/exit styles, offsetting entrance/exit location, and more ([see here](https://github.com/FreeCAD/FreeCAD/pull/22669) for details).
- davidgilkaufman also fixed a release blocker where changing TC with the same tool number but different spindle speed wouldn't produce correct G-code.
- tarman3 patched the Dogbone dressup to be able to process more complicated cases, such as multiple passes and an excluded inner path.
- Dimitrios2 fixed a G0 regression in drilling (patch prepared by J-Dunn).
- zophon fixed KineticNCBeamicon2 postprocessor to separate M05 and M09 G-code as beamicon2-basic doesn't like having both M-code on the same line.

**BIM**:

- marcuspollio updated various icons, including the Views Panel and Status Bar ones.
- furgo16 fixed sun ray creation in Arch Site solar study.
- Roy-043 fixed a bug where the Arch_Reference object would not display colors of a referenced object. He also fixed another bug where doors and windows would become transparent when multimaterial was assigned to them.

**FEM**:

- NewJoker:
  - Added amplitude support to the Final Temperature field.
  - Added a new property, DisablePastixMixedPrecision (true by default), that disables the PaStiX mixed precision for the ccx solver.
  - Set better defaults for mesh export ([see here](https://github.com/FreeCAD/FreeCAD/pull/23553) for details).
- marioalexis84:
  - Added support for 2D geometries to Centrif constraint.
  - Patched the code not to override user-defined time increment values ​​when running steady state thermo-mechanical analyses.
  - Simplified meshing with Netgen by using Netgen bindings entirely in an external program.
  - Added the Offset property to the old ElementGeometry2D object.
  - Improved the code by allowing the refactored ccx solver to be added with the Analysis containers.

**GUI**:

- B0cho improved the expression editor's input and resize behavior.
- kadet1090 fixed transparent preview rendering issues. He also updated the appearence of planes to react to mouse-over and enlarge for a better visual clue of selection.
- maxwxyz changed hardcoded pixelated bitmap navigation cursors in the 3D view to DPR-aware SVG cursors.
- captain0xff add theming abilities to interactive gizmos merged last week.
- tetektoza added a context menu to select obstructed items; the code has been backported from RealThunder's fork.

{{< video "obstructed-objects-selection.mp4" >}}

**Other changes**:

- Roy-043 fixed several bugs in Draft.
- schmidtw fixed a toponaming bug happening on models made with FreeCAD 0.7.
- drwho495 fixed another toponaming bug that would cause FreeCAD to slow down with some files after a recent patch.
- 3x380V fixed two regressions (one of them also a release blocker) related to units.
- wwmayer and 3x380V modernized FileInfo code.
- PaddleStroke added (back) an icon for the angular motion in Assembly.

Additional improvements and fixes were contributed by NewJoker, adrianinsaval, luzpaz, PaddleStroke, paullee0, z0r0, and kadet1090.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.09.10).

Translators: your recent changes have been merged from Crowdin again.

**PR stats**: since the previous report, 75 pull requests have been merged, and 63 new pull requests have been opened.

**Issue stats**: overall, there are 2972 open issues in the tracker, up by 27 from last week. 46 known release blockers remain unfixed for v1.1.

The soft feature freeze is now on, so starting next Wednesday, weekly updates will be a lot more boring for the next few months. No fancy new features, just bugfixes.