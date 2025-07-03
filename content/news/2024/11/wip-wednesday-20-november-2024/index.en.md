---
title: 'WIP Wednesday: 20 November 2024'
date: 2024-11-20
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

This week in FreeCAD development:

**BIM**: yorikvanhavre fixed several issues and added a new ArchDetail example file compatible with modern FreeCAD and tools.

**Draft**: Roy_043 and fra589 fixed several issues, cjmayo made Draft and BIM mutually independent build options, and yorikvanhavre implemented SVG text rotation (this fixes vertical text when placing some BIM views on a TechDraw page).

**FEM**: mosfet80 cleaned dead code in FemMesh.cpp, and marioalexis84 applied several minor fixes.

**Spreadsheet**:

- hyarion implemented double-clicking on separator/handle to resize the column to content.

- snow-faerie added <kbd>Ctrl</kbd> + {B,I,U} shortcuts for cell formatting to Spreadsheet. Since <kbd>Ctrl</kbd> + </kbd>I</kbd> was taken by File/Import, they also remapped that command to <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>.

**Addon Manager**: hasecilu patched the dialog to show the repository URL if it exists in the metadata; and now when you switch to a different branch of an addon, the Addon Manager will show you the names of both involved branches.

**GUI**: benj5378 centered the method icon in calltips vertically, and snow-faerie mapped the Preferences dialog to the <kbd>Ctrl</kbd> + <kbd>;</kbd> shortcut by default.

Among other changes:

- pinkavaj and Syres916 fixed a couple of issues in Sketcher.

- PaddleStroke, Jiri-Macha, and furgo16 fixed a few issues in Assembly.

- benj5378, hasecilu, and WandererFan contributed minor fixes to TechDraw.

- Another patch by bgbsww, helper files for CLion debugging, was merged posthumously (this was code from his last grant project).

Other merged fixes arrived from wwmayer, Syres916, mosfet80, KrisSlyka, luzpaz, OfficialKris, furgo16, cjmayo, and NewJoker.

**PR stats**: since the previous report, 47 pull requests have been merged, and 30 new pull requests have been opened.

**Issue stats**: overall, there are 2302 open issues in the tracker, up by 55 from last week. It will be a while before we start counting release blockers again, yay!

Because over 200 pull requests have accumulated while the team was busy getting v1.0 out the door, we now have two merge meetings a week, the next one will happen [this Friday](https://www.freecad.org/events.php). This is a temporary measure. We will keep doing it until we burn through the backlog of PRs back to where we were in June, just before the feature freeze.