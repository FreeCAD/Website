---
title: 'WIP Wednesday: 3 July 2024'
date: 2024-07-03
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

**Assembly** got support for the new toponaming routines and per-limit checkboxes when setting joints. Moreover, when a checkbox for a limit is disabled, the value is still updated as you drag or rotate a part. This makes it easy to visually set limits: drag a part to a position where the min value should be, enable the checkbox, repeat for the max value. Both patches were contributed by PaddleStroke. He also fixed a crash that was occurring when using Gear, Belt, and Rack/Pinion joints.

**FEM**: marioalexis84 and lyphrowny and contributed various fixes, and NewJoker added a new Elmer solver icon.

**Sketcher** got new carbon copy icons by NewJoker.

**TechDraw** got a revamp of icons by Reqrefusion, bringing them closer to the new guidelines; further tweaks are expected. WandererFan contributed several fixes, including a fix for the display of autofill value in templates.

**BIM** got fixes and a new example model from yorikvanhavre, as well as icon updates by marcuspollio.

**Overall UI changes**: kadet1090 implemented dragging support for toolbars placed in custom toolbar areas, reorganized UI and Theme pages in Display group of the Preferences dialog, and made some further improvements. Other minor UI improvements were contributed by MisterMakerNL and hlorus.

**Addon Manager** got several Qt6-related fixes by chennes. On a related note, this Sunday, one of the topics for the [online developers meetup](https://www.freecad.org/events.php) is potentially building v1.0 against Qt6.

**Further fixes** arrived from Roy_043 (Draft), bgbsww (toponaming), and wwmayer (virtually everywhere).

**PR stats**: In the week from Wednesday, 27 June to Wednesday, 3 July there were 68 pull requests merged. 55 new pull requests were opened.

**Issue stats**: we closed 90 issues, and 86 new issues were opened. Overall, 1,789 issues are currently open.

The user interface freeze is now on, if you're interested in contributing to translations of the program into your native language, it's a good time to [get started](https://wiki.freecad.org/Localisation).