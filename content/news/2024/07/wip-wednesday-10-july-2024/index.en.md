---
title: 'WIP Wednesday: 10 July 2024'
date: 2024-07-10
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

This week in FreeCAD development there has been more bugfixing in preparation for FreeCAD v1.0 release later this summer. Disclaimer: this report's data is offset by 1 day due to traveling.

**Toponaming**: bgbsww commented out console warnings triggered by external geometry, added more missing TNP code, and improved the testing framework.

**Sketcher** got the most fixes: NewJoker increased the default width of dashed lines to improve their visibility above the grid, PaddleStroke fixed scale/rotation warnings, two issues with the Dimension tool, and two crashes with the BSpline tool, wwmayer and chennes submitted various other Sketcher fixes.

**BIM**: yorikvanhavre pushed 8 fixes for various issues, including an elusive bug where dragging and dropping IFC project tree items would result in an access violation error message. Overall, he fixed the remaining reported issues caused by the NativeIFC merge and three of the v1.0 blockers.

**Assembly**: PaddleStroke fixed errors on undoing a fixed joint creation, made it possible for the Insert Component taskbox to grow with the number of items, and fixed a typo in the Preferences dialog.

**PartDesign**: NewJoker removed the obsolete Migrate tool from the UI (tool code will be removed in a separate pull request), wwmayer removed dead code from workbench class and refactored thickness parameter to remove hard-coded maximum.

**FEM**: lyphrowny and NewJoker updated CI and fixed a few minor issues, marioalexis84 fixed a crash.

**TechDraw**: Reqrefusion improved Page Template and Geometric Hatch icons, PaddleStroke fixed the Dimension tool not working for measuring area when used the first time, maxwxyz fixed a bug with the autofilling of templates that was introduced by recent icon changes, WandererFan fixed several issues including a bug with the display of spreadsheet cells with no horizontal alignment.

More fixes arrived from wwmayer, chennes (mostly in the addon manager), NewJoker, hasecilu, luzpaz, and others.

**PR stats**: we merged 70 pull requests, 43 new pull requests were opened.

**Issue stats:** overall, 1,816 issues are currently open. Currently, 41 of all issues are blockers preventing the team from releasing v1.0, their number has been going down from over 50 last week so far though.