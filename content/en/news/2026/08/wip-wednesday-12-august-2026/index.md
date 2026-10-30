---
title: WIP Wednesday, 12 August 2026
date: 2026-08-12
author: prokoudine
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

## Sketcher

- matthiasdanner simplified the entry of negative numbers in constraints, which now doesn't require pressing Enter twice ([PR#30587](https://github.com/FreeCAD/FreeCAD/pull/30587)).
- Reqrefusion added point-on-object constraint support for arcs (all types), circles, and ellipses ([PR#31295](https://github.com/FreeCAD/FreeCAD/pull/31295)).
- maxwxyz added a 400ms delay for drag autoconstraints to evaluate and show the proposal ([PR#31725](https://github.com/FreeCAD/FreeCAD/pull/31725)).

## Part and PartDesign

- maxwxyz added a new Offset mode for the start position of Pad and Pocket, with an interactive start control (PR#31688 and [PR#31839](https://github.com/FreeCAD/FreeCAD/pull/31839)). He also added a MidPlane attachment mode between two planar faces ([PR#31574](https://github.com/FreeCAD/FreeCAD/pull/31574)) and removed the limitation where a PartDesign body and its BaseFeature had to live inside the exact same Part container ([PR#31763](https://github.com/FreeCAD/FreeCAD/pull/31763), with another improvement in [PR#31767](https://github.com/FreeCAD/FreeCAD/pull/31767)).
- Syres916 fixed a bug where FreeCAD would crash when opening files with faulty geometry ([PR#31812](https://github.com/FreeCAD/FreeCAD/pull/31812)).

## Assembly

- PaddleStroke added numeric editing of movements in exploded views ([PR#30955](https://github.com/FreeCAD/FreeCAD/pull/30955)): you can quickly edit them in the task panel or right-click and open the Placement dialog for advanced editing.
- slendidev added a new, Fusion-like Rigid Group joint type - a fixed joint between all selected components that makes them fixed relative to one another ([PR#29605](https://github.com/FreeCAD/FreeCAD/pull/29605)).

## TechDraw

- WandererFan fixed a bug that prevented surface finish symbols from being placed precisely ([PR#31635](https://github.com/FreeCAD/FreeCAD/pull/31635)). He also fixed the display of leading signs for zero tolerance values ([PR#31226](https://github.com/FreeCAD/FreeCAD/pull/31226)).
- eleknader unhardcoded center line colors to follow user preferences for horizontal center lines and vertical center lines ([PR#31847](https://github.com/FreeCAD/FreeCAD/pull/31847)).

## CAM

Numerous patches by tarman3, including but not limited to these:

- Removed the dependency of Start Depth from Step Down ([PR#31282](https://github.com/FreeCAD/FreeCAD/pull/31282)).
- Improved Helix by adding a Start Cone From Bottom property that allows processing cone helices from bottom to top ([PR#30975](https://github.com/FreeCAD/FreeCAD/pull/30975)).
- Improved Helix some more by allowing selection of the outer side of cylindrical shapes ([PR#30977](https://github.com/FreeCAD/FreeCAD/pull/30977)).
- Moved the LeadInOut logic to Generator and Extend In and Extend Out to the task panel ([PR#31069](https://github.com/FreeCAD/FreeCAD/pull/31069)).
- Improved Pocket Shape: allowed using Use Outline with edges and vertical faces and added the Close Open Paths property, which allows processing open wires and vertical faces ([PR#29675](https://github.com/FreeCAD/FreeCAD/pull/29675)).

## BIM

- maxwxyz fixed several issues in the Views panel ([PR#31791](https://github.com/FreeCAD/FreeCAD/pull/31791) and [PR#31813](https://github.com/FreeCAD/FreeCAD/pull/31813)).
- mozman fixed incorrect face orientation on IFC exports ([PR#31867](https://github.com/FreeCAD/FreeCAD/pull/31867)).
- Roy-043 added Survey to the Report Tools group in the toolbar and Unclone to the Cloning Tools group ([PR#31547](https://github.com/FreeCAD/FreeCAD/pull/31547)). He also fixed an index error for pipe T-connectors ([PR#31911](https://github.com/FreeCAD/FreeCAD/pull/31911)).

## FEM

marioalexis84 added boundary conditions to magnetic 2D examples ([PR#31690](https://github.com/FreeCAD/FreeCAD/pull/31690)) and a magnetization 3D example for Elmer ([PR#31856](https://github.com/FreeCAD/FreeCAD/pull/31856)). He also made it possible to save Elmer eigen analysis as multiframes ([PR#31851](https://github.com/FreeCAD/FreeCAD/pull/31851)).

## Other changes

- pieterhijma added a core feature to move properties from one object to another ([PR#23841](https://github.com/FreeCAD/FreeCAD/pull/23841)).
- maxwxyz added more mouse action hints to the hint status bar section ([PR#31570](https://github.com/FreeCAD/FreeCAD/pull/31570)). He also improved the Measure tool to use the mass property to calculate inertia around any given straight edge ([PR#31157](https://github.com/FreeCAD/FreeCAD/pull/31157)).

Additional improvements and fixes were contributed by adrianinsaval, arkadesOrg, aw-engineer, chennes, codeotaku, darkdi, davidgilkaufman, jlewin, kkchemboli, Lokestrom, marioalexis84, matthiasdanner, offbynull, oliveroxtoby, PaddleStroke, rehan-ahmed-aix, Roy-043, theosib, weslord, and wmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.08.12).

## Activity stats

**PR stats**: since the previous report, 77 pull requests have been merged, and 51 new pull requests have been opened.

**Issue stats**: overall, there are 3512 open issues in the tracker, up by 4 from last week.
