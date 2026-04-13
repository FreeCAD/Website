---
title: WIP Wednesday, 2 July 2025
date: 2025-07-02
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

- Roy-043 fixed an issue where, on document load, TechDraw would ask Draft for SVG before the Draft objects are fully restored.
- tetektoza removed redundant group boxes in task panels of several tools.

**Sketcher**: karliss fixed an issue where the state of the "Esc can leave sketch edit mode" setting would not refresh after changes and required a restart for the change to take effect.

**PartDesign**: mosfet80 removed some deprecated and unused functions.

**BIM**: Roy-043 fixed an issue where a subtracted roof would be hidden when the base wall was copied.

**TechDraw**: ryankembrey updated the name of the command for inserting active views and added a tooltip.

**GUI**: maxwxyz improved the consistency of some user-visible messages (mostly things like "doesn't" vs "does not" and the right Unicode character for ellipsis).

**I/O**:

- furgo16 added a console DXF statistics reporter for the FreeCAD C++ importer, which reports details such as DXF file metadata, import time, total entities read, etc. [See here](https://github.com/FreeCAD/FreeCAD/pull/21985) for the full list.
- galou improved DAE exporting by using the object labels rather than the object names.

Among other changes:

- Syres916 fixed a small regression in BIM, Draft, and CAM.
- NewJoker fixed a couple of typos in FEM.
- pieterhijma added undo/redo support for renaming properties in VarSets.
- davesrocketshop added support for file types other than PNG to embedded images in materials.
- Rexbas contributed a patch that instructs the upcoming version of Coin to use EGL when running on Wayland.
- kadet1090 added another [requirement](https://github.com/FreeCAD/FreeCAD/commit/536775188bca2ee202cc4a960aada04d6b51d77d) for contributors: new PRs need to contain proper attribution in description and commits if they were made by non-author.

Additional improvements and fixes were contributed by chennes, knipknap, luzpaz, lahwaacz, and mosfet80.

**PR stats**: since the previous report, 34 pull requests have been merged, and 40 new pull requests have been opened.

**Issue stats**: overall, there are 2921 open issues in the tracker, up by 14 from last week.

In other news, Pieter Hijma [got an NLnet grant](https://pieterhijma.net/blog.html#nlnet-grant-accepted) to improve the Integration between FreeCAD and [Lens](https://github.com/FreeCAD/Ondsel-Server), a free PDM system originally developed by Ondsel. He will resume his work on the [Lens addon](https://github.com/FreeCAD/Ondsel-Lens-Addon) that-just like Lens itself-has now been moved to the FreeCAD organization.

Some of the possible changes Pieter outlined in an [earlier blog post](https://pieterhijma.net/blog.html#ondsel-onward-for-osh) are UX improvements, support for Git-based workspaces (with support for visual version differences), and a notification system. He will also update the addon to provide easy support for self-hosted Lens instances.