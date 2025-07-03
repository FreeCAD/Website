---
title: 'WIP Wednesday: 15 Feb 2023'
date: 2023-02-15
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

This past week was a very busy one for code merges, with almost 80 pull requests completed. Developers plan on continuing the high pace this next week:

- @JohnD/[Ondsel](https://ondsel.com) is surveying the [toponaming branch](https://github.com/FreeCAD/FreeCAD/tree/development/toponaming) and consolidating a list of affected classes and intent.

- @wandererfan began work this week on the problem of dimensions losing their reference geometry after recomputes or save/restore.

- @openBrain is improving CI reporting on GitHub.

- @jnxd is now working for Ondsel, and will be continuing his spline enhancements.

- @uwestoehr has merged the section cutting feature, and is now working on [new electrodynamics capabilities](https://forum.freecad.org/viewtopic.php?t=75888) in the FEM Workbench sponsored by the [Open Toolchain Foundation](https://opentoolchain.org).

- @jonasb is doing some cleanup of the PartDesign involute gear code and then hopefully adding profile shifting.

- I (@chennes) am starting to merge in the refactored Addon Manager code to support speeding up the AM, reducing its network load, and probably most importantly, get it under test for our automated CI.

**PR stats:** In the week from Tuesday, 7 Jan to Tuesday, 14 Jan there were 79 pull requests merged, with a total codebase change of +17,382 / ‑7,809 lines (not counting translation changes). That's an average merged PR size of +220/ ‑99.