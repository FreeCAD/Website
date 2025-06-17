---
title: 'WIP Wednesday: 26 June 2024'
date: 2024-06-26
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

The development of new features is pretty much done. Some larger changes, such as the BOM tool in Assembly last week, are still landing to the main development branch. But they are simply patches that were submitted prior to feature freeze a few weeks back and finally passed review.

This Monday, maintainers agreed to delay the proposed UI freeze by 1 week. So any _fixes_ that affect the user interface and change translatable strings should be submitted by the time the [next PR merge meeting](https://www.freecad.org/events.php) starts.

This week in FreeCAD development:

**BIM**: Roy-043, yorikvanhavre, and DeniseBryson fixed several bugs, and marcuspollio updated the Glue tool icon.

**Sketcher**: Syres916, maxwxyz, and CalligaroV fixed several bugs, PaddleStroke implemented on-view parameters (OVP) for BSplines, and maxwxyz renamed OVP-related settings in Preferences for clarity's sake.

**Assembly**: PaddleStroke fixed several issues related to inserting subassemblies and linking to them, he also fixed a bug where a model would "explode" during the presolve step, and fixed attempts to drag grounded objects.

Additionally:

- chennes and marioalexis84 fixed several bugs in the FEM workbench.

- sliptonic fixed several "red ink" bugs in CAM (error messages that show up in Report View and are hard to understand by mere mortals) and fixed a bug where users were unable to add a toolbit to a job and to create a new one.

- Roy-043 fixed several bugs in Draft.

**PR stats**: In the week from Wednesday, 19 June to Wednesday, 26 June there were 63 pull requests merged. 42 new pull requests were opened.

**Issue stats**: we closed 56 issues, and 71 new issues were opened. Overall, 1,765 issues are currently open.

You should expect the weekly reports to be similarly "boring" in the coming weeks - and for a good reason!