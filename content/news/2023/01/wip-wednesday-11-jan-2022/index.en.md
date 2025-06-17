---
title: 'WIP Wednesday: 11 Jan 2023'
date: 2023-01-11
author: Chris Hennes
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week we're introducing a new blog feature: "WIP Wednesday". I'm collecting input from anyone currently working on any kind of FreeCAD development, and letting all of you know what they are working on _right now_, so you can stay abreast of the very latest developments in the FreeCAD world. Of course, a lot of this is pretty mundane (I've been working on unit tests for the Addon Manager, for example), but sometimes it's pretty exciting stuff (for example @wmayer has been working on getting FreeCAD working with Qt6). Developers: if you are working on anything you'd like featured here, drop me a line at [chennes@freecad.org](mailto:chennes@freecad.org), or on the [FreeCAD Forum](https://forum.freecadweb.org/viewtopic.php?f=10&t=75141).

So, for the week of 11 Jan 2023, we have a few in-progress tasks from various developers:

- @sliptonic (maintainer of the Path CNC workbench) is working on coaching @luvtofish on adding a tapping operation in [PR 8069](https://github.com/FreeCAD/FreeCAD/pull/8069).

- He's also working on a PR for [bug 7855](https://github.com/FreeCAD/FreeCAD/issues/7855) (threadmill collision) and another for [bug 7600](https://github.com/FreeCAD/FreeCAD/issues/7600) (adaptive task panel controls).

- @openBrain is working on our continuous integration (CI) system so that we have better automated testing of incoming code.

- @wandererfan is working on various TechDraw projects: easier 3d dimensions ([issue 7830](https://github.com/FreeCAD/FreeCAD/issues/7830)), light on dark mode ([8062](https://github.com/FreeCAD/FreeCAD/issues/8062) & [8093](https://github.com/FreeCAD/FreeCAD/issues/8093)), ANSI Y14.5 compatible text, and investigating panning anomalies with zoom at cursor.

- @Roy_043 is working on some Draft WB bugs: an Undo problem that only affects Windows users ([issue 8044](https://github.com/FreeCAD/FreeCAD/issues/8044)), and some [annotation style problems](https://forum.freecadweb.org/viewtopic.php?f=3&t=73222).

- @jonasb is working on exposing the addednum and dedenum coefficients of Part Design's involute gear profile. This will allow modification of the tooth height and thus use the profile for things other than full-depth systems.

- I (@chennes) am working on refactoring the Addon Manager to improve its unit test coverage, in anticipation of adding support for a "Last updated" field in the user interface. I'm also chasing down a couple of bugs related to the Addon Manager not properly installing addons.