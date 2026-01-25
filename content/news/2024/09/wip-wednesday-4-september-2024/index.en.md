---
title: 'WIP Wednesday: 4 September 2024'
date: 2024-09-04
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

- PaddleStroke fixed a bug with geometry copy-pasting and another bug where on-view parameters would use numeric input for the wrong constraint in certain scenarios.

- AjinkyaDahale fixed another bug that would prevent users from escaping the autosnapping of circles with autoconstraint enabled.

**TechDraw**:

- benj5378 fixed the centering of dimension labels and improved the UI of surface finish labels.

- WandererFan submitted several fixes, including ones for sections snapping, project group detection, and PDF output with correct margins.

**CAM**: shaise fixed 5 bugs in the new milling simulator in one pull request.

**Assembly**: PaddleStroke fixed several bugs, including one where the workbench would fail to create a joint coordinate system for a linked object created with multiple "Elements" count.

**Measure**: hlorus fixed two bugs including one where unsaved measure was considered a document modification; the measurement tool now only add the measure object to the document when it is saved.

**GUI**: kadet1090 fixed a couple of UI issues in Sketcher and Preferences, and qewer33 added a random splashscreen selector.

![Image](image.png "Image")

Among other changes:

- bgbsww and CalligaroV fixed several bugs in the toponaming code, including correct element map support in Revolution.

- marioalexis84 and NewJoker fixed several bugs in FEM.

- Syres916 fixed a bug where the user directory for materials couldn't be set in Preferences.

- More fixes all around from wmayer as usual.

**PR stats**: since the previous report, 49 pull requests have been merged, 23 new pull requests have been opened.

**Issue stats**: overall, there are 1945 open issues in the tracker, up by 64 from last week. 9 of them are v1.0 release blockers, down by 5 from last week.