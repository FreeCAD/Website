---
title: 'WIP Wednesday: 9 October 2024'
date: 2024-10-09
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

- PaddleStroke fixed the bug where double-clicking to select connected wires wouldn't work.

- Benj5378 fixed the automatic constraint tool to do distance to origin when origin is selected.

- AjinkyaDahale fixed a bug where it would be impossible to create an ellipse by center if a point meets an axis.

**PartDesign**: FlachyJoe fixed several bugs including one in Helix (seems to be a popular minefield), and mwganson fixed "Allow Compound" to recompute features and not just the body.

**Assembly**:

- PaddleStroke fixed the script for migration of older files with assembly objects.

- furgo16 fixed to bugs in the BOM generator.

- bgbsww fixed a TNP issue where adding a chamfer to the sketch of one of the bodies connected with a joint would break the assembly.

**Materials**:

- shaise improved the loading of materials (now takes a fraction of a second rather than a couple of seconds).

- davesrocketshop fixed a bug where diffuse color would ignore transparency.

**FEM**: marioalexis84 added an option in Preferences to use the old Netgen mesher implementation, because the new implementation has dependencies that are hard to resolve on some older systems, He also fixed a bug where quantity spin boxes in the mesher settings in the task panel are cropped.

**GUI**:

- Rexbas fixed a regression where entering edit mode for a sketch with TouchPad navigation style enabled would result in camera rotation when the <kbd>Shift</kbd> button is pressed.

- Benj5378 fixed font size scaling in the Pythion console by using <kbd>Ctrl</kbd> + mouse scrolling.

Among other changes:

- Various core fixes from wmayer, bgbsww, pieterhijma, and PaddleStroke.

- WandererFan fixed a bug where adding measurements would not work between lines and circle center line anymore.

- Roy_043 fixed several bugs including one crasher in BIM and Draft.

- AIRCAP, PaddleStroke, and hyarion fixed a couple of bugs in Quick Measurement.

- Various other commits by maxwxyz, Unl0gic, kriswilk, chennes, NomAnor, pinkavaj.

There are still nine unmerged pull requests from Bradley "bgbsww" McLean who unfortunately [passed away](https://blog.freecad.org/2024/10/08/rip-bradley-bgbsww-mclean/) last week. Five of them are open and another four are in draft. All nine are scheduled for review after v1.0 is released. Brad's family also gave access to Brad's laptop to one of his friends who is trying to figure out if there's any code he has not pushed to any public or private git repository online. We will do our very best to make sure that his legacy will be preserved and put to a good use.

**PR stats**: since the previous report, 46 pull requests have been merged, 42 new pull requests have been opened.

**Issue stats**: overall, there are 2157 open issues in the tracker, up by 21 from last week. 20 of them are v1.0 release blockers, up by 8 from last week.