---
title: 'WIP Wednesday: 7 August 2024'
date: 2024-08-07
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

**Toponaming**: bgbsww added more missing TNP code and fixed several bugs including one blocker.

**Assembly**: PaddleStroke fixed the migration script to correctly load older files with assemblies.

**BIM**: Roy_043 fixed the calculation of wall blocks and yorikvanhavre fixed the loading of psets in IFC files (produced by SolidWorks).

**FEM**: marioalexis84 fixed warnings about materials, element geometry, and mesh elements when meshing, and NewJoker repaired example files.

**UI**: MisterMakerNL fixed at least three bugs by improving stylesheets (including the new dark theme).

Among other changes:

- chennes and luzpaz updated the build system; additionally, chennes and oursland updated CI scripts.

- bgbsww added a command line option to keep FreeCAD open after running tests.

**PR stats**: since the previous report, 26 pull requests have been merged, 28 new pull requests have been opened.

**Issue stats**: overall, there are 1866 open issues in the tracker, up by 27 from last week. 40 of them are v1.0 release blockers, up by 5 from last week.

There have been more interesting things happening in and around FreeCAD.

Following some conversations in the developers community, Shai Seger (Fasteners, SheetMetal WB) [started hacking](https://forum.freecad.org/viewtopic.php?t=89424) on ground shadows and ambient occlusion using custom shaders in Coin3D. Here is the most recent demo:

{{< youtube id=jaRh9DgtSxg title="YouTube video" loading=lazy >}}

Pierre-Louis Boyer is exploring the topic of flexible assemblies:

{{< youtube id=OO0-X_uDMDA title="YouTube video" loading=lazy >}}

There's also a [thread in the forum](https://forum.freecad.org/viewtopic.php?t=89650) about it.