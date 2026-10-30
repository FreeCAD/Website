---
title: WIP Wednesday, 30 September 2026
date: 2026-09-30
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

- chennes fixed the Fit All command so that it can zoom in, not just zoom out ([PR#33080](https://github.com/FreeCAD/FreeCAD/pull/33080)) and patched the code to retain constraint names on auto-scale ([PR#32947](https://github.com/FreeCAD/FreeCAD/pull/32947)).
- alfrix fixed two crashes ([PR#32804](https://github.com/FreeCAD/FreeCAD/pull/32804) and [PR#32989](https://github.com/FreeCAD/FreeCAD/pull/32989)).
- flaviut improved fonts discovery on Linux and Windows ([PR#32729](https://github.com/FreeCAD/FreeCAD/pull/32729)).

## Part and PartDesign

- PaddleStroke exposed recently added circular, path, and point pattern tools in the user interface ([PR#33072](https://github.com/FreeCAD/FreeCAD/pull/33072)). He also added interactive pattern suppression controls ([PR#33071](https://github.com/FreeCAD/FreeCAD/pull/33071)).
- UnKabaraQuiDev added a control to Thickness to control how the dressup is applied: full inside, fully outside, or somewhere in between ([PR#32935](https://github.com/FreeCAD/FreeCAD/pull/32935)).
- maxwxyz implemented axis projection for Revolution and Groove ([PR#32747](https://github.com/FreeCAD/FreeCAD/pull/32747)).

## Assembly

PaddleStroke fixed a rack-and-pinion bug ([PR#32922](https://github.com/FreeCAD/FreeCAD/pull/32922)) and the inability to delete an orphaned group of joints after an assembly has been deleted ([PR#32924](https://github.com/FreeCAD/FreeCAD/pull/32924)).

## CAM

29 PRs merged this past week, ladies and gents. Here are some of the patches:

- tarman3 patched profile to combine connected faces ([PR#31074](https://github.com/FreeCAD/FreeCAD/pull/31074)), added Spiral Circular pattern to MillFacing ([PR#31887](https://github.com/FreeCAD/FreeCAD/pull/31887)), and added a talk panel for SimpleCopy ([PR#32450](https://github.com/FreeCAD/FreeCAD/pull/32450)). He also patched Toolbit shape to allow using the Transform tool ([PR#32818](https://github.com/FreeCAD/FreeCAD/pull/32818)).
- sliptonic pushed the next step towards workplace handling for multi-axis ([PR#32903](https://github.com/FreeCAD/FreeCAD/pull/32903)) and added a machine-based postprocessor for Fanuc ([PR#33069](https://github.com/FreeCAD/FreeCAD/pull/33069)).
- jffmichi added a new ramp method without backtracking to improve the cut quality ([PR#32838](https://github.com/FreeCAD/FreeCAD/pull/32838)).

## BIM

- furgo16 added tooltips for the most common BIM objects' task panel boxes ([PR#32904](https://github.com/FreeCAD/FreeCAD/pull/32904)).
- yangyu0330 patched the workbench to be able to use external defining sketch geometry ([PR#30086](https://github.com/FreeCAD/FreeCAD/pull/30086)).

## TechDraw

- WandererFan prevented failures on equal projected points ([PR#32880](https://github.com/FreeCAD/FreeCAD/pull/32880)) and improved templates to conform to Finnish standards ([PR#32701](https://github.com/FreeCAD/FreeCAD/pull/32701)).
- PaddleStroke restored dynamic properties of rich annotations ([PR#32915](https://github.com/FreeCAD/FreeCAD/pull/32915)).
- pavltom added a new algorithm to improve face finding by handling voids and islands ([PR#28046](https://github.com/FreeCAD/FreeCAD/pull/28046)).

## Other changes

- ILoveBuns patched Draft to use global coordinates for Trimex so that it works inside translated Parts ([PR#31995](https://github.com/FreeCAD/FreeCAD/pull/31995)).
- pieterhijma adapted Part code to support the future OCCT 8.1 release ([PR#33062](https://github.com/FreeCAD/FreeCAD/pull/33062)).
- maxwxyz added a fuzzy matcher for expression autocompletion ([PR#30531](https://github.com/FreeCAD/FreeCAD/pull/30531)).
- marioalexis84 added moment of inertia of area unit and properties for mass and area moment of inertia ([PR#31972](https://github.com/FreeCAD/FreeCAD/pull/31972)).

Additional improvements and fixes were contributed by 007stevendigar-lgtm, 3x380V, alfrix, awgrover, chennes, Connor, davidgilkaufman, Dimitris75, ElementW, flaviut, jffmichi, jlewin, ipatch, kazan417, kevenwyld, Lgt2x, M3mL34k, maxwxyz, mnesarco, novalis, oursland, PaddleStroke, ryneeverett, sean-de-courcy, SeaPickle754, sliptonic, tarman3, tritao, UnKabaraQuiDev, and wwmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.09.30).

## Activity stats

**PR stats**: since the previous report, 103 pull requests have been merged, and 60 new pull requests have been opened.

**Issue stats**: overall, there are 3437 open issues in the tracker, down by 9 from last week.
