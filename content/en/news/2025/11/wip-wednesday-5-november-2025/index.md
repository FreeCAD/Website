---
title: WIP Wednesday, 5 November 2025
date: 2025-11-05
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

**Sketcher**:

- AjinkyaDahale fixed a regression where trimming would break polygons ([PR#25054](https://github.com/FreeCAD/FreeCAD/pull/25054)).
- PaddleStroke fixed a bug where Offset would not select an open loop correctly ([PR#25091](https://github.com/FreeCAD/FreeCAD/pull/25091)). He also improved constraint rendering ([PR#24534](https://github.com/FreeCAD/FreeCAD/pull/24534), [PR#25055](https://github.com/FreeCAD/FreeCAD/pull/25055)).
- tetektoza patched the code to make it remember the cursor angle for on-view parameters (OVP) after an OVP has been set ([PR#24904](https://github.com/FreeCAD/FreeCAD/pull/24904)).

**BIM/Draft**:

- Roy_043 fixed the broken Continue mode ([PR#24993](https://github.com/FreeCAD/FreeCAD/pull/24993)), fixed paths to example files ([PR#24878](https://github.com/FreeCAD/FreeCAD/pull/24878)), and eliminated warnings when switching the Render mode to Solid ([PR#24978](https://github.com/FreeCAD/FreeCAD/pull/24978)).
- paullee0 largely fixed the incorrect Window opening ([PR#25001](https://github.com/FreeCAD/FreeCAD/pull/25001)) and the incorrect Stairs structure ([PR#24917](https://github.com/FreeCAD/FreeCAD/pull/24917)).
- furgo16 moved the BIM Project command from the toolbar to the Utils menu ([PR#25086](https://github.com/FreeCAD/FreeCAD/pull/25086)).

**FEM:**

- marioalexis84 fixed magnetodynamic2D boundary condition ([PR#25017](https://github.com/FreeCAD/FreeCAD/pull/25017)), fixed CalculiX body heat source writer for 2D cases ([PR#25079](https://github.com/FreeCAD/FreeCAD/pull/25079)), and reworked the Elmer solver object and task panel, which fixes two bugs, including one release blocker ([PR#24912](https://github.com/FreeCAD/FreeCAD/pull/24912)).
- chennes tweaked a couple of unit tests ([PR#24936](https://github.com/FreeCAD/FreeCAD/pull/24936)).

**GUI**:

- tetektoza patched the code to force the expression completer to display a drop-down list when an item is clicked ([PR#25011](https://github.com/FreeCAD/FreeCAD/pull/25011)). He also fixed the window restoration after Edit->Alignment completion ([PR#24651](https://github.com/FreeCAD/FreeCAD/pull/24651)).
- pieterhijma fixed supporting xlinks in the Add Property dialog ([PR#25052](https://github.com/FreeCAD/FreeCAD/pull/25052)).
- maxwxyz fixed the width of the status bar buttons ([PR#24972](https://github.com/FreeCAD/FreeCAD/pull/24972)).

**Other changes**:

- tetektoza fixed a bug in Draft where geometry would be imported from DXF with the Make Face property set to the last used option ([PR#24857](https://github.com/FreeCAD/FreeCAD/pull/24857)). He fixed another bug where enabling the "Treat ellipses and splines as polylines" option in DXF export preferences would still result in exporting stove primitives ([PR#24856](https://github.com/FreeCAD/FreeCAD/pull/24856)).
- WandererFan fixed the angle dimming in the detail view in TechDraw ([PR#25062](https://github.com/FreeCAD/FreeCAD/pull/25062)).
- PaddleStroke fixed isolation rendering in Assembly when double-clicking a joint for editing ([/PR#24942](https://github.com/FreeCAD/FreeCAD/issues/24942)). He also fixed the rendering of exploded views in TechDraw ([PR#24769](https://github.com/FreeCAD/FreeCAD/pull/24769)).
- tarman3 fixed a minor dress-up UI issue ([PR#24732](https://github.com/FreeCAD/FreeCAD/pull/24732)) and added a more straightforward UI for selecting either the new or the legacy CAM simulator ([PR#24875](https://github.com/FreeCAD/FreeCAD/pull/24875)).
- wwmayer fixed a release blocker where toggling transparency would reset colors in PartDesign ([PR#24970](https://github.com/FreeCAD/FreeCAD/pull/24970), cherry-picked by maxwxyz).
- PhoneDroid added many more missing SPDX license identifiers to boilerplates of source code files ([PR#25070](https://github.com/FreeCAD/FreeCAD/pull/25070) and counting).

Additional improvements and fixes were contributed by chennes, tritao, oursland, leoheck, mosfet80, adrianinsaval, and kpemartin.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2025.11.05). Builds for macOS are temporarily unavailable.

**PR stats**: since the previous report, 67 pull requests have been merged, and 29 new pull requests have been opened.

**Issue stats**: overall, there are 3032 open issues in the tracker, up by 42 from last week. There are 9 release blockers currently, down by 4 from last week. The list of blockers is revisited and updated on Monday merge meetings.

The first release candidate of FreeCAD 1.1 is currently expected later this week.