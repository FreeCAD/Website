---
title: 'WIP Wednesday: 5 February 2025'
date: 2025-02-05
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

This week in FreeCAD development:

**Draft**:

- redonwhite added several new path array features: a setting to reverse path, an align mode that uses rotations instead of tangent vectors, a "Fixed spacing" mode, and an ability to use spacing patterns.

- Roy_043 added [improvements to groups handling](https://github.com/FreeCAD/FreeCAD/pull/19312) and fixed several bugs.

**BIM**:

- furgo16 patched the BIM Schedule command to detect and expand array elements, so that they can be further processed (these elements used to be ignored prior to that) and fixed a couple of bugs.

- Tritao improved the checking for IfcOpenShell installation.

- je-cook upgraded the bundled copy of Three.js to its latest release.

**CAM**: dubstar-04 contributed several quality-of-life improvements for using the Tool Bit Library.

**FEM**: two fixes from marioalexis84 and NewJoker.

**TechDraw**: WandererFan fixed a couple of bugs and added two small features: you can now show/hide units on individual dimensions rather than set it at the Preferences level; similarly, you can now control legacy scaling in symbols, spreadsheets, and draft views at the view level.

Among other changes:

- benj5378 made axis colors user-definable.

- panintended fixed Quick Measure to display the angle between edges in correct units.

- chennes contributed a few improvements to the Addon Manager.

- pmjdebruijn patched the PDF exporter to write proper PDF creator metadata.

- hyarion updated the Ondsel Solver submodule to get the latest community-contributed fixes.

Additional fixes arrived from paullee0, alfrix, pskowronskiTDx, totake0224, mwganson, Roy-043, xtemp09, Syres916, furgo16, Rexbas, tritao.

**PR stats**: since the previous report, 38 pull requests have been merged, and 28 new pull requests have been opened.

**Issue stats**: overall, there are 2553 open issues in the tracker, up by 26 from last week.