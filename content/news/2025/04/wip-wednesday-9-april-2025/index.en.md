---
title: 'WIP Wednesday: 9 April 2025'
date: 2025-04-09
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

**CAM**:

- phaseloop migrated the Array operation to a dressup operation and changed the design of the origin axis to be in line with the LCS indicator.

- bdieterm contributed a minor fix.

**TechDraw**: benj5378 fixed a bug where edges would have the wrong color, and jonzirk76 contributed minor code refactoring.

**Surface**: Shkolik changed the behavior of the Fill Boundary Curves and Sections surface tools: after activating either of the tools, there's no need to click on the "Add edge" button anymore, you can select edges immediately.

**Addon Manager**: chennes moved the code to its own repository and made it a Git submodule. According to chennes, this will ultimately provide the ability for the Addon Manager to update itself even within individual releases of FreeCAD.

**GUI**:

- alfrix fixed the Quantity spinbox margin so that on-view input widgets would render correctly in Sketcher.

- kadet1090 added an optional origin placement indicator in the LCS indicator style.

- vletii fixed the behavior of the Freeze toggle to unfreeze objects down the hierarchy properly.

- pieterhijma patched varsets to make value inputs show units for properties that have units.

Among other changes:

- Fixes in Draft by Roy_043, aprospero, and luzpaz.

- Further work on XML bindings refactoring in Sketcher and Part by tritao.

- Fixes in PartDesign by PaddleStroke.

Additional fixes, small improvements, and code refactoring were contributed by pieterhijma, mosfet80, tritao, hyarion, MisterMakerNL, Frankleklek, captain0xff, furgo16, marcuspollio, pskowronskiTDx, kpemartin, xtemp09, runzh-crypto, kadet1090, drwho495, chennes, 3x380V, and oursland.

**PR stats**: since the previous report, 52 pull requests have been merged, and 29 new pull requests have been opened.

**Issue stats**: overall, there are 2789 open issues in the tracker, up by 34 from last week.