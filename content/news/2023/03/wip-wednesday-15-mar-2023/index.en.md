---
title: 'WIP Wednesday: 15 Mar 2023'
date: 2023-03-15
authors: Chris Hennes
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

I am hopelessly biased, but as far as I am concerned the big news this week is the merge of the first piece of the puzzle to mitigating the Topological Naming Problem, with the merge of [PR 8776](https://github.com/FreeCAD/FreeCAD/pull/8776). It's not a large or complicated piece of code, but it forms the very innermost core of the TNP solution created by FreeCAD developer @**realthunder**, and it's now in the main FreeCAD codebase 🎉. No user-visible changes yet, but you eat an elephant one bite at a time!

The past week also saw merges of new notification functionality from Abdullah (the maintainer of the Sketcher workbench), plus many small usability improvements and bug fixes. In the upcoming week:

- @wandererfan is working on an annoying fail when creating a projection group on some Windows builds.

- He's also working on the first steps in fixing the "lesser topo naming problem" - autocorrect dimension references when they become invalid after a recompute.

- @jonasb is working on [Profile Shift](https://github.com/FreeCAD/FreeCAD/issues/5618) -- this time for real.

- I (@chennes) am starting in on the next chunk of the Topological Naming Problem merge, as well as fixing a bug in the Addon Manager that prevented Addon installation after running Update All.

**PR stats:** In the week from Tuesday, 7 Feb to Tuesday, 14 Mar there were 75 pull requests merged, with a total codebase change of +16,880 / ‑11,672 lines (not counting translation changes). That's an average merged PR size of +225 / ‑156.