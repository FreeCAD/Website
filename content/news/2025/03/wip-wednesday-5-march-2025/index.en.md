---
title: 'WIP wednesday: 5 March 2025'
date: 2025-03-05
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

**Draft**: Roy_043 fixed numerous issues and regressions, including ones where the Trimex command would change the visibility of an object or extend to the wrong face.

**BIM**: galou, mosfet80, furgo16, and paullee0 cleaned up the code and fixed several issues including ones where Shape2DCut would not cut and where the Door generator would punch holes in an adjacent wall segment.

**Sketcher**: Shkolik fixed two bugs, including one where creating external projection geometry would not work with datum objects

**TechDraw**:

- WandererFan changed the scaling default for Draft & BIM views and fixed an issue with broken views not collapsing.

- aurelienpascal fixed a bug where Draft's hatching patterns would be displayed in a wrong way.

- benj5378 continued his refactoring effort

**FEM**:

- marioalexis84 added support for Elmer static current solver, improved current density boundary condition, changed the direction of the static current symbol, and fixed a crash in the Cut filter.

- NewJoker added Joule heating to FEM Examples.

**Start page**:

- furgo16 added a Preferences section for the Start page with the following options:

- Displaying the contents of the examples folder

    - Displaying the contents of a custom folder

    - Closing the Start page after loading

- alfrix fixed scrollbars in the Start page itself.

**Addon Manager**: thanks to chennes, the Update All report now displays previously installed version of the addon and the newly installed version.

**Among other changes**:

- Various build system and CI improvements by schiele, tritao, mosfet80, maxmosk, and changes.

- Tweaks in GUI code by Syres916, Roy_043, kadet1090, tritao, chennes, tringenbach, oursland.

Additional fixes and improvements were contributed by chennes, hyarion, kadet1090, tritao, PaddleStroke, mosfet80, and totake0224.

**PR stats**: since the previous report, 64 pull requests have been merged, and 37 new pull requests have been opened.

**Issue stats**: overall, there are 2657 open issues in the tracker, up by 23 from last week.