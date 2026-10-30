---
title: WIP Wednesday, 22 July 2026
date: 2026-07-22
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

- Bojan9597 fixed precision loss in the Dimension tool ([PR#30157](https://github.com/FreeCAD/FreeCAD/pull/30157)).
- PaddleStroke fixed a confusing behavior when entering angle values in the Polyline's on-view parameter boxes ([PR#30479](https://github.com/FreeCAD/FreeCAD/pull/30479)).
- matthiasdanner added on-view parameter resetting on clicking in the Polyline and BSpline tools when creating a new segment ([PR#31209](https://github.com/FreeCAD/FreeCAD/pull/31209)).
- maxwxyz fixed a bug that would interrupt creating a sequence of tangentially connected arcs with the Polyline tool in certain scenarios ([PR#31139](https://github.com/FreeCAD/FreeCAD/pull/31139)).
- Lokestrom fixed a bug where minor and major radius would get swapped when sketching ellipse arcs ([PR#31343](https://github.com/FreeCAD/FreeCAD/pull/31343)).

## Part and PartDesign

- PaddleStroke fixed a bug that made all subtractive tools use the same icon and name in the task panel ([PR#31045](https://github.com/FreeCAD/FreeCAD/pull/31045)). He also partially fixed performance issues with pattern tools by removing an extra recompute of multitransforms ([PR#30872](https://github.com/FreeCAD/FreeCAD/pull/30872)).
- drwho495 fixed a toponaming-related issue where FreeCAD would often remove perfectly valid geometry when an element loses reference in a fillet or chamfer operation ([PR#31411](https://github.com/FreeCAD/FreeCAD/pull/31411)).

## CAM

tarman3 patched Probe to use the bounding box rather than the volume of the selected shape to define probe area ([PR#30609](https://github.com/FreeCAD/FreeCAD/pull/30609)), fixed cycle time for dress-ups ([PR#31110](https://github.com/FreeCAD/FreeCAD/pull/31110)). He also contributed the first step towards making helix ramp an option in Profile and Pocket to make this feature more discoverable ([PR#26957](https://github.com/FreeCAD/FreeCAD/pull/26957)).

## TechDraw

- WandererFan fixed using a custom section line color ([PR#31386](https://github.com/FreeCAD/FreeCAD/pull/31386)) and balloon positioning ([PR#30895](https://github.com/FreeCAD/FreeCAD/pull/30895)).
- wwmayer fixed a crash that occurred when opening a drawing created in 0.21 ([PR#31186](https://github.com/FreeCAD/FreeCAD/pull/31186), cherry-picked by maxwxyz).

## BIM

Roy-043 fixed deactivation of spatial objects like levels and buildings ([PR#31064](https://github.com/FreeCAD/FreeCAD/pull/31064)) and the cloning of stairs ([PR#30960](https://github.com/FreeCAD/FreeCAD/pull/30960)). He also added support for different pipe diameter values in the T-connector ([PR#29504](https://github.com/FreeCAD/FreeCAD/pull/29504)).

## Other changes

- marioalexis84 added options to reverse master and slave references for Contact and Tie constraints in FEM ([PR#31055](https://github.com/FreeCAD/FreeCAD/pull/31055)).
- tritao contributed a patch that prepares the codebase for the new renderer ([PR#31187](https://github.com/FreeCAD/FreeCAD/pull/31187)). Scene construction, screen-space geometry, mesh render data, framebuffer capture, and teardown are made more explicit, deterministic, and reusable while preserving the existing rendering path.
- ElementW boosted the loading of workbench resources multifold ([PR#29904](https://github.com/FreeCAD/FreeCAD/pull/29904)).

Additional improvements and fixes were contributed by adrianinsaval, chennes, greg19, ItSaulGoodMan, j-hewett, KKTHEGREAT07, Lgt2x, maxwxyz, Roy-043, TravisThomp, tritao, and wwmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.07.22).

## Activity stats

**PR stats**: since the previous report, 67 pull requests have been merged, and 35 new pull requests have been opened.

**Issue stats**: overall, there are 3508 open issues in the tracker, up by 4 from last week.

## Elsewhere in the community

KiCad developers recently [announced](https://fosstodon.org/@kicad/116964415817525125) they will be using FreeCAD's PlaneGCS constraint solver in v11. The feature is already available in [nightly builds](https://downloads.kicad.org/kicad/).
