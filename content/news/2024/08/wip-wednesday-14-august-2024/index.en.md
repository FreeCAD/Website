---
title: 'WIP Wednesday: 14 August 2024'
date: 2024-08-14
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

**Toponaming**: mostly bugfixing and code refactoring. 8 pull requests from bgbsww and chennes fixed 9 reported issues including 3 release blockers. The toponaming PRs queue has been largely cleaned up. Currently, there are just 3 PRs from bgbsww and CalligaroV left in draft, that could be completed before v1.0 is out.

**Assembly**: PaddleStroke fixed 4 bugs including one crash that was happening when using the distance joint with zero distance.

**FEM**: NewJoker replaced three different example files with one containing all 3 versions of the cantilever beam analysis in Group containers; he also added a text document with a short description.

**GUI**: qewer33 improved the design of the Start Page fixing 4 bugs in one go, including one blocker. Other GUI improvements arrived from Syres916, MisterMakerNL, maxwxyz, and chennes. Notably, Syres916 improved the contrast in the overlay mode of the tree view, and maxwxyz added a new option to toggle the rendering of FreeCAD's icon in project thumbnails, then regenerated thumbnails of example files for consistency's sake.

Among other changes:

- pieterhijma fixes three minor issues in the core.

- Roy_043 and paullee0 fixed two issues in the Draft workbench.

- PaddleStroke fixed two issues related to dimensions in TechDraw.

- chennes fixed two bugs in the Addon Manager, one of them related to Qt6 compatibility.

**PR stats**: since the previous report, 34 pull requests have been merged, 12 new pull requests have been opened.

**Issue stats**: overall, there are 1852 open issues in the tracker, down by 14 from last week. 26 of them are v1.0 release blockers, down by 14 from last week as well.