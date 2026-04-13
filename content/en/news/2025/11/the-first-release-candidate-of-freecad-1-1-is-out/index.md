---
title: The first release candidate of FreeCAD 1.1 is out
date: 2025-11-26
authors: Aleksandr Prokudin
draft: false
categories: announcement
tags:
  - release
  - RC
versions: "1.1"
cover:
  image:
  caption:
---


The team has just published builds of the first candidate of FreeCAD 1.1, you can download them [on GitHub](https://github.com/FreeCAD/FreeCAD/releases/tag/1.1rc1). Here is what it means and what's going to happen next.

The release candidates are basically preliminary builds of the final version. They are aimed at a particular demographic: people who want to help the team make a final check for major regressions before the final release can be published. If you are one of those people, please download a build for your operating system, test it, and [report](https://github.com/FreeCAD/FreeCAD/issues) any new issues you run into.

We are currently down to [5 critical bugs](https://github.com/FreeCAD/FreeCAD/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Blocker%22) that block the v1.1 release (we call them release blockers). The number of blockers can temporarily go up, if a lot of people download RC1 and report major issues, and that's great. It means that the final official release will be more polished.

If you are a developer willing to contribute bugfixes, come look at the list of reports, pick an issue that seems trivial to resolve, write a fix, and submit a pull request. We have weekly [merge meetings](https://www.freecad.org/events.php) on Mondays to discuss submitted patches. You are welcome to join!