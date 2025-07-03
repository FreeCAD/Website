---
title: 'WIP Wednesday: 9 August 2023'
date: 2023-08-09
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

Welcome back to WIP Wednesday! After a short hiatus while we prepared for the [0.21.0 release](https://blog.freecad.org/2023/08/02/freecad-0-21-released/), we're back out of the feature freeze, and FreeCAD development continues apace. Actually, it's accelerating, and fast! We're still working through the PR backlog that built up over the freeze, but expect to make major progress during the [FreeCAD Hackathon this Friday-Sunday](https://blog.freecad.org/2023/07/27/freecad-hackathon-discord/).

Please note that we expect the master development branch to experience some slowdowns, increased memory consumption, and probably some other temporary regressions going forward. This is due in part to the plans for integrating the Topological Naming Problem (TNP) mitigation strategy into master, but also in part to the accelerated pace of development. If you choose to use a daily or weekly development build, _**please**_ **back up your data regularly**.

Over the past weeks:

- **wwmayer** has been working on some C++ code modernization

- **PaddleStroke** reorganized the preference page folder structure

- **ConnorWarrell** optimized the QuantitySpinBox regular expressions

- I (**chennes**) worked on getting the Snap updated to Ubuntu 22.04, and developing a new LibPack for Windows based on Qt6.5 and Python 3.11.

- Plus hundreds of other items: check the [Pulse](https://github.com/FreeCAD/FreeCAD/pulse) for details!

**PR stats:** In the week from Wednesday, 2 Aug to Wednesday, 9 Aug there were 55 pull requests merged, with a total codebase change of +14,550 / ‑13,172 lines (not counting translation changes). That's an average merged PR size of +269 / ‑244. We closed 16 Issues, and 47 new Issues were opened.