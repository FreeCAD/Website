---
title: 'WIP Wednesday: 27 November 2024'
date: 2024-11-27
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

**Sketcher**:

- FlachyJoe made axes scale dependent on the viewport size so that they always appear infinite.

- PaddleStroke enhanced the offset tool and the transform tools to use external geometries as input.

**GUI**:

- wwmayer implemented support for Freedesktop's [Thumbnail Management Standard](https://specifications.freedesktop.org/thumbnail-spec/0.8.0/) v0.8.0 in the Start page.

- Various minor tweaks arrived from 3x380V, ein-shved, wwmayer, bdieterm, luzpaz, and pieterhijma.

**FEM**: marioalexis84 added local refinement and second-order linear for Netgen meshing, as well as other improvements and fixes in the FEM workbench.

**BIM**: Roy-043 and cjmayo fixed a few issues in the workbench, and yorikvanhavre added support for for additions/subtractions in NativeIFC.

**Materials**: davesrocketship added physical properties that are automatically recalculated when the shape or material changes. These values are accessible from the part data display and as attributes within Python.

**Core**: PaddleStroke's patches for a better datums implementation started landing on the main branch. So far, it's just cosmetic work. Larger patches with refactoring are still in review. The [original PR](https://github.com/FreeCAD/FreeCAD/pull/16675) lists UX/UI issues it's fixing.

Among other changes:

- Syres916, mwganson, and wwmayer fixed some issues in Part and Part Design.

- paullee0 and Roy_043 fixed several issues in Draft.

- PaddleStroke, kadet1090, and H. Tsubota fixed several fixes to Assembly.

**PR stats**: since the previous report, 72 pull requests have been merged, and 32 new pull requests have been opened.

**Issue stats**: overall, there are 2327 open issues in the tracker, up by 25 from last week.

The lager-than-usual number of merged pull requests is the result of more frequent PR merge meetings. Until the number of open PRs goes back to normal, the team will be meeting twice a week. The next meeting will take place [this Friday](https://www.freecad.org/events.php). Some fixes have been ported to the v1.0 branch and will become available in the first bugfix update for 1.0.