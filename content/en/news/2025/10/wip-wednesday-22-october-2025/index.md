---
title: WIP Wednesday, 22 October 2025
date: 2025-10-22
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

- PaddleStroke added code to prevent Polar Pattern and Offset from creating reversed arcs and fixed another bug where Ctrl+A would not select points in the Geometry list.
- sparker0594 fixed a regression where the 3-point arc tool would not retain the final constraint of the 3rd point when it is a tangent constraint.

**Part and PartDesign**:

- kadet1090 fix misplaced preview for the Boolean operation in PD.
- FlachyJoe fixed a bug where applying MultiTransform to PolarPattern would fail.

**CAM:**

- tarman3 fixed a couple of minor UI issues and two bugs in the LeadIn/Out dressup.
- Connor fixed a regression that prevented the Surface operation from v1.0.2 files from working.
- davidgilkaufman fixed a minor UI issue and made the experimental adaptive model awareness feature optional and off by default.
- sliptonic removed the Split Output by Fixture command from UI as it conflicts with the primary use of fixtures in the Job setup.

**Other changes**:

- PaddleStroke fixed a crash that occurred when making a grounded subassembly flexible. He also fixed the bug preventing image data being pasted from the clipboard into the 3D view.
- WandererFan fixed a bug where the area annotation position would be set to (0,0) after dragging the annotation. He also patched Area Dimension to actually use unit schema values.
- Roy_043 and furgo16 fixed a dozen issues in BIM, some of them related to materials and multi-materials.
- theo-vt allowed the Measurement tool and the Quick Measure feature to calculate length for ellipse, hyperbola, and parabola.
- Various GUI fixes by tetektoza, ipatch, Syres916, and kadet1090.

Additional improvements and fixes were contributed by Syres916, LarryWoestman, captain0xff, marcuspollio, chennes, ipatch, ebswift, paullee0, OPGL, pyro9, Roy-043, kpemartin, petterreinholdtsen, and tetektoza.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.10.22).

**PR stats**: since the previous report, 57 pull requests have been merged, and 17 new pull requests have been opened.

**Issue stats**: overall, there are 2979 open issues in the tracker, down by 10 from last week.

The team has reviewed issues, downgraded some of the issues from blockers. We are now down to 14 release blockers. The plan is to create a v1.1 release branch on October 29 and start working on the first release candidate.