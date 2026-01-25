---
title: 'WIP Wednesday: 14 May 2025'
date: 2025-05-14
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

**Draft**:

- tetektoza patched the Polygon tool to show a real shape preview rather than a generic circle when adding a polygon to the draft.

- Various fixes from Roy_043, tetektoza, and furgo16.

**CAM**:

- tarman3 made the new CAM simulator to show the document name in the window title. They also added a button to decrease simulation speed, changed the list of speed values from [1, 10, 40] to [1, 5, 10, 25, 40], and improved camera zoom limits.

- Various fixes from jffmichi, dbtayl, LarryWoestman, tarman3, davidgilkaufman, and otwieracz.

**BIM**:

- paullee0 continued adding support for the ArchSketch add-on.

- tetektoza added a button for the BIM Views submenu to activate a working plane of the selected item. He also made it possible to change the Sill parameter once a Window object has already been created.

- Various fixes by furgo16, marcuspollio, Roy_043, tetektoza, and paullee0.

**FEM**:

- marioalexis84 implemented solving electrostatic systems with CalculiX by analogy with the steady-state heat equation.

- NewJoker and ickby fixed several issues.

**TechDraw**:

- chennes fixed a hatch size constraint introduced by an earlier patch.

- WandererFan made it possible for non-shape views (Symbols, DraftView, BIMView, etc.) to have children.

**Materials**: triato and chennes fixed a couple of issues.

Additional improvements and fixes were contributed by theo-vt, RaynoJiang, sasobadovinac, Syres916, chennes, oursland, tritao, filippor, 3x380V, pieterhijma, xtemp09, kadet1090, benj5378, and mosfet80.

**PR stats**: since the previous report, 71 pull requests have been merged, and 34 new pull requests have been opened.

**Issue stats**: overall, there are 2852 open issues in the tracker, up by 12 from last week.