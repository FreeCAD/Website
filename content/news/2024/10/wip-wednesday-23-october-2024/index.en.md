---
title: 'WIP Wednesday: 23 October 2024'
date: 2024-10-23
author: Aleksandr Prokudin
draft: false
categories: announcement
tags: []
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

**Part and PartDesign**: the unsung hero this week was AIRCAP who single-handedly wrestled with a huge amount of bugs and came out on top:

- Fixed 7 bugs and regressions in the boolean operations code, alleviated another regression, and provided a workaround for yet another issue operations - all that in just one pull request.

- Added features to investigate and debug the effect of Tolerance on FreeCAD features - and the effect of FreeCAD features on tolerance.

- Disabled the tesselation limit in Part to prevent large parts from freezing FreeCAD.

**GUI/UX**: various fixes arrived from Rexbas, NewStorm, and hyarion.

Among other changes:

- Roy-043 further improved the fix for dragging and dropping layers in Draft.

- yorikvanhavre and Roy-043 fixed a couple of bugs in BIM.

- PaddleStroke fixed two regressions in the Assembly workbench.

- WandererFan fixed a bug in TechDraw to restore leader line style handling, i.e. setting the leader line to dash, dot, dash and dot.

- marioalexis84 contributed two fixes and improvements to meshing in FEM.

- davesrocketshop fixed a bug where inheriting the material from the parent object would fail in certain scenarios.

As usual, more fixes arrived from wwmayer, yorikvanhavre, PaddleStroke, Roy-043, and FlachyJoe. Additional fixes arrived from mwganson, cjmayo, adrianinsaval, and pieterhijma.

Last but not least, yorikvanhavre added a dedication of FreeCAD 1.0 to the late Brad "bgbsww" McLean to the About screen.

**PR stats**: since the previous report, 39 pull requests have been merged, 34 new pull requests have been opened.

**Issue stats**: overall, there are 2180 open issues in the tracker, down by 2 from last week. 7 of them are v1.0 release blockers, down by 8 from last week.