---
title: 'WIP Wednesday: 2 October 2024'
date: 2024-10-02
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

**Part and PartDesign**:

- AIRCAP fixed another Loft issue and then a blocker where Pocket's up-to-face option would work differently (and incorrectly at that) from v0.21.2.

- mwganson fixed a bug where you wouldn't be able to run CheckGeometry on an X-axis object when the "Too small edge" option is enabled, after expanding origin object in Part Design.

**Measure**: hlorus fixed 3 bugs including one release blocker where measurements wouldn't disappear when reset was used in the task panel.

**Assembly**: PaddleStroke fixed a lag that would occur when dragging parts in an assembly with a lot of fixed parts.

**FEM**: marioalexis84 fixed another issue where flickering would occur between faces and wireframe in FEM mesh view, it was more noticeable on curved surfaces and using flat color for the wireframe.

**TechDraw**: WandererFan fixed 7 minor issues (1 of them not reported to the tracker).

**CAM**: shaise dropped the previous code for Screen Space Ambient Occlusion shaders in favor of one that is under the MIT license for license compatibility's sake.

**GUI**: Syres916 added a workaround for Qt6 and its OpenGL widget's misbehavior, and hyarion contributed a fix towards eliminating another blocker where the application would crash on macOS.

Further BIM and core fixes came from NomAnor, oursland, hyarion, bgbsww, and wwmayer.

**PR stats**: since the previous report, 21 pull requests have been merged, 33 new pull requests have been opened.

**Issue stats**: overall, there are 2136 open issues in the tracker, up by 48 from last week. 12 of them are v1.0 release blockers, up by 6 from last week.