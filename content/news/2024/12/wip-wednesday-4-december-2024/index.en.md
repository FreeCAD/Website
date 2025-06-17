---
title: 'WIP Wednesday: 4 December 2024'
date: 2024-12-04
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

- AjinkyaDahale's work on refactoring the workbench code to make it more manageable started landing on the main branch. This work is being on on FPA's grant issued earlier this year.

- PaddleStroke continued his work on making use of external geometry. The latest patch fixes an issue where external geometry can't be converted to normal geometry, and another one where there is no way to add intersection geometry. To aid that effort, maxwxyz updated Sketcher icons accordingly.

**Assembly**:

- The work by aiksiongkoh and PaddleStroke on simulations has finally landed in the main repository. The new Assembly workbench tool allows adding motion to joints and creating animations. There are limitations in what it can do (e.g. what joint types are supported), so expect further refinement. This was one of the two missing changes by Ondsel that were scheduled for upstreaming.

- PaddleStroke implemented an "Insert A New Part" command to allow selecting a feature in the geometry of an existing part's, then insert a new body with a sketch referencing that selected feature. So these are humble beginnings of the top-down design approach implementation.

- hyarion did some code cleanup.

**Part Design**: FlachyJoe fixed a design issue where switching the Refine property would trigger a recompute of the shape, this is going to be useful for e.g. helix.

**BIM**:

- yorikvanhavre added support for property sets in Native IFC. This means any property added by the user becomes an IFC property, and the BIM properties manager tool now also supports native IFC objects.

- He also added NativeIFC support to Add/Remove tools.

Various other fixes and improvements arrived from Roy_043, wwmayer, WandererFan, maxxyz, VincidaB, effere79, Roy_043 and others.

**PR stats**: since the previous report, 74 pull requests have been merged, and 29 new pull requests have been opened.

**Issue stats**: overall, there are 2352 open issues in the tracker, up by 25 from last week.