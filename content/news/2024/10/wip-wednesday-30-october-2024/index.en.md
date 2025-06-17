---
title: 'WIP Wednesday: 30 October 2024'
date: 2024-10-30
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

**Sketcher**: PaddleStroke fixed several bugs, including one release blocker, all related to constraints and transformations / arrays.

**PartDesign**:

- mwganson applied minor fixes to _Groove_ and _Revolution_ task panels.

- PaddleStroke fixed a release blocker in which creating a body in an existing document raised the request to migrate it, and then creating another body would segfault FreeCAD.

- kadet1090 fixed an issue occurring when changing _Pad_ from _Dimension_ to _Two Dimensions_.

**Assembly**: PaddleStroke fixed a bug where _Insert Component_ would show items hidden in the Tree view. He also added support for flexible subassemblies that create links to separate parts of subassemblies rather than to the entire assemblies. This preserves existing joints in subassemblies and allows controlling the position of those parts from a parent assembly, even if links to the same parts already exist in the parent assembly.

**GUI**:

- pieterhijma made the VarSets dialog modal and fixed an issue with the _Tooltip_ property.

- benj5378 fixed the legibility of start page example files with the _Dark_ theme.

- Rexbas continued his work fixing issues related to incorrect camera rotation with some navigation styles.

Among other changes:

- yorikvanhavre and Roy_043 fixed several issues in Draft.

- davesrocketshop patched the new materials system to change the appearance of a body when switching materials only if the appearance hasn't been set explicitly.

- PaddleStroke fixed a release blocker where closing a Sketcher tab with a task running would crash FreeCAD. The fix was to associate task dialogs with views, so now when a view is closed, the task is closed too.

- WandererFan fixed several issues in TechDraw, including two release blockers.

- AIRCAP patched Tolerance to restrict maximum tolerance and repair shapes optionally.

- marioalexis84 fixed two minor issues in FEM.

- hoshengwei and yorikvanhavre fixed several bugs in BIM.

- wwmayer fixed a bug in the measure tool to use the center points as a reference when measuring the distance between circles.

More fixes arrived from wwmayer, adrianinsaval, mwganson.

**PR stats**: since the previous report, 47 pull requests have been merged, 27 new pull requests have been opened. We've been steadily accumulating patches scheduled for review once v1.0 is out, there are now 236 such pull requests.

**Issue stats**: overall, there are 2194 open issues in the tracker, up by 14 from last week. 4 of them are v1.0 release blockers, down by 3 from last week.