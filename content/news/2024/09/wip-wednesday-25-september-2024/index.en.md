---
title: 'WIP Wednesday: 25 September 2024'
date: 2024-09-25
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

**Measurement**: hlorus and AIRCAP fixed several issues including one release blocker, and PaddleStroke fixed Quick Measure to work on bodies in assemblies correctly.

**Draft**: Roy_043 fixed a minor issue, and Syres916 improved the color activation and added an ability to change the size of the snap text (in code).

**Part Design**:

- FlachyJoe fixed several issues where the padding operation would fail in some scenarios when applied with _Up to Face_ and _Up to Shape_ options (that's another release blocker down).

- AIRCAP fixed additive loft for cases when the selected shape is not a vertex in the sketch.

- theosib fixed Part Design to no longer allow part planes and axes as options for Sweep and Loft.

**DXF**: kpemartin fixed two regressions related to the importing of layers and layer names, and increased the importing speed.

Among other changes:

- davesrocketshop fixed several issues in the new materials system, including one release blocker.

- WandererFan fixed 6 issues in TechDraw, including 2 crashes.

- Syres916, yorikvanhavre, and pinkavaj fixed several issues in BIM.

- marioalexis84 contributed several improvements and fixes to FEM.

- bgbsww fixed several toponaming issues including one blocker where FreeCAD would crash after accepting toponaming recompute dialog in a file with multiple links.

- Rexbas fixed a blocker issue in the align to selection tool.

- xtemp09 improved the Light Sources page of Preferences to move the zoom button to the left so that XYZ axes would be visible in the lower right corner.

- shaise fixed a minor occlusion in the Ambient Occlusion code in the new CAM simulator.

**PR stats**: since the previous report, 61 pull requests have been merged, 18 new pull requests have been opened.

**Issue stats**: overall, there are 2088 open issues in the tracker, up by 37 from last week. 6 of them are v1.0 release blockers, down by 5 from last week.