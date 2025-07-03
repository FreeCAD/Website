---
title: 'WIP Wednesday: 21 Mar 2023'
date: 2023-03-22
author: Chris Hennes
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
  alt:
---

There have been a number of exciting changes to FreeCAD in the past week, most notably the merge of a new notification system from Sketcher developer @abdullah. It's still a work-in-progress, so expect to see significant refinement of this feature in the coming weeks. The FreeCAD Project Association also released its first [Annual Report](https://fpa.freecad.org/reports/2022), so big kudos to the team that worked on that document (especially @wandererfan and @yorik), and to the whole FPA for an amazing inaugural year.

In this upcoming week:

- @wandererfan expects phase 1 of the dimension reference error detection and correction to get merged this week.

- @wmayer is working on eliminating the Image workbench and integrating image import into the core of FreeCAD.

- @jnxd is shepherding another PR in the Topological Naming Problem (TNP) series into merge readiness.

- I (@chennes) merged a fix for a bug in the Addon Manager that prevented Addon installation after running Update All, and am working on prepping the remaining first-phase TNP pull request, completing the first set of code merges that set the stage for implementing the actual TNP mitigation algorithms.

**PR stats:** In the week from Tuesday, 14 Feb to Tuesday, 21 Mar there were 58 pull requests merged, with a total codebase change of +9,759 / ‑6,030 lines (not counting translation changes). That's an average merged PR size of +168 / ‑104.