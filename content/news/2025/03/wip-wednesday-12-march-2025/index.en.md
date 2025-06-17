---
title: 'WIP wednesday: 12 March 2025'
date: 2025-03-12
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

**Draft**: Roy_043 fixed several bugs, including Draft's fillet not working the first time you try it, as well as incorrect snapping behavior. He also implemented a new Dim Auto Flip Text option to disable automatic text orientation based on where you click first.

**BIM**:

- Syres916 fixed two cosmetic bugs in the UI code.

- furgo16 re-enabled adding Arch Space boundaries.

**Sketcher**: Shkolik fixed the projection of B-Splines from parallel planes by reusing LinkStage3 code with minor modifications.

**Part/PartDesign**: j-hap and captain0xff contributed a couple of fixes, and WandererFan updated some properties and spinboxes to use newer properties such as PropertyDirection and spinboxes such as QuantitySpinBox.

**FEM**:

- marioalexis84 improved the Magnetization, the Heat Flux, and the Gmsh task panels. He also used disambiguation for solid references in Elmer equation task panels.

- NewJoker added a new FEM example: rigid body constraint with CalculiX.

**Assembly**: PaddleStroke made it possible to select LCS elements when the LCS is in a body. He also fixed the use of datum axes in joints.

**User interface**:

- tringenbach fixed the NaviCube scale on HiDPI / Retina displays.

- alfrix cleaned up the general task panel code to unify its look across operating systems and make the styling apply faster.

**Among other changes**:

- furgo16 brought back the ability to specify multiple custom folders whose contents will be shown as a combined set of files in the "Custom Folder" file card on the Start page. This was a v0.21 feature.

- kpemartin fixed a bug where the Measure tool crash the application if you measured the same amount twice.

Additional fixes were contributed by hyarion, chennes, clsergent, alfrix, PaddleStroke, bofdahof, tritao, benj5378, mosfet80, and 3x380V.

**PR stats**: since the previous report, 46 pull requests have been merged, and 33 new pull requests have been opened.

**Issue stats**: overall, there are 2670 open issues in the tracker, up by 13 from last week.