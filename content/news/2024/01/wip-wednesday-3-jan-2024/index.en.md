---
title: 'WIP Wednesday: 3 Jan 2024'
date: 2024-01-03
author: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development wasn't very active due to holidays, and yet:

- **@chennes** added a TopoShapeCache class based on RealThunder's implementation. This is an important step towards the end of Phase 3 of the toponaming project.

- **@Syres916** changed the way the units schema check is done in the Path workbench: it now reads the document-level setting.

- **@WandererFan** fixed several bugs and made a few minor improvements in the TechDraw workbench.

- **@bgbsww** created cpp tests for Part boolean operations.

- **@maxwxyz** patched the Sketcher workbench to always show auto HorVer tool command in the toolbar when the tool is present (with the concise toolbar option enabled).

**PR stats:** In the week from Wednesday, 27 Dec to Wednesday, 3 Jan there were 10 pull requests merged, with a total codebase change of +1772 / -348 (not counting all translation updates). We had an average merged PR size of +197 / ‑39. 14 new pull requests were opened.

**Issue stats:** we closed 7 issues, and 22 new issues were opened. Overall, 1,136 issues are currently open.

In other news: Ondsel is running a [**survey**](https://ondsel.com/blog/survey-engineers-architecture/) to better understand FreeCAD users: who they are, what kind of work they do professionally or as hobby, what their main challenges with FreeCAD are etc. Results are promised to be made public.