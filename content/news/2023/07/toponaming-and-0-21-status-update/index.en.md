---
title: Toponaming and 0.21 Status Update
date: 2023-07-14
author: Chris Hennes
draft: false
categories: announcement
tags:
- roadmap
- TNP
cover:
  image:
  caption:
  alt:
---

It's been a while since I posted a status update! Developers have been meeting regularly to make sure we are still making progress towards releasing 0.21 (you can see the [release status page here](https://github.com/orgs/FreeCAD/projects/4)). The main things we're waiting on are two Topological Naming Problem (TNP) pull requests, [PR 9780](https://github.com/FreeCAD/FreeCAD/pull/9780) (closes [issue 9116](https://github.com/FreeCAD/FreeCAD/issues/9116): TopoNaming Phase 2 card 3 of 5 - ComplexGeoData dressing) and [PR 9696](https://github.com/FreeCAD/FreeCAD/pull/9696) (closes [issue 9119](https://github.com/FreeCAD/FreeCAD/issues/9119): TopoNaming Phase 2 card 4 of 5 - SketchObject dressing).

Both of those PRs are in active development, with an initial suite of tests written, and the code from the original TNP pull request incorporated into the two classes being looked at in those issues. If you are interested in helping out, there are many more tests to write, either before or after the PRs are merged! Drop me a message if you are interested and I'll bring you up to speed ([chennes@freecad.org](mailto:chennes@freecad.org)). You don't need to have a deep understanding of the TNP or the classes involved, though some experience with C++ development will be helpful. There are several of us working on the problem who can help you learn the ropes as you go.

Once these two classes are merged into FreeCAD's main codebase, we will make a 0.21 release of FreeCAD. The TNP will still be a problem in that release, but the groundwork for solving it will have been laid (and you'll get access to all of the amazing things developers have been doing for the last year!). After that release, we will begin activating the new TNP mitigation code, which will likely result in some temporary slowdowns and stability issues in the daily and weekly development builds. We are going to encourage most people to use 0.21 as your "daily driver" and only use the development builds to help test the new TNP code (and be aware that things might break -- back up those models!).