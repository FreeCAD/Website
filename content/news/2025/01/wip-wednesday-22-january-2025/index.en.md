---
title: 'WIP Wednesday: 22 January 2025'
date: 2025-01-22
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

**Sketcher**:

- Beep6581 patched the workbench to automatically scroll to the constraint in the list view when you click on that constraint in the 3D view.

- AjinkyaDahale's second refactoring patch landed. No new features, it's just cleaner code with tests.

- chennes and Jonezzzzz fixed a couple of bugs.

**PartDesign**:

- PaddleStroke added a new Preferences option: when enabled, the Create New Sketch command opens the attachment dialog instead of the 'feature pick' dialog. Once the attachment dialog becomes more useful, this could become the default option (undecided yet). He also replaced Part Design datum commands by the core ones.

- alfrix updated the Hole task panel to show drill point options based on the selected type of the drill point. There is ongoing work by the Design Working Group to improve that task panel, you can find the latest mockup [here](https://www.figma.com/proto/nDkUKcH1YgriUSRG2EInYj/FreeCAD-Dialogs?node-id=247-3465&node-type=canvas&t=PXunFHu2h93heWMQ-1&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=247%3A3465&show-proto-sidebar=1).

**Draft**: Roy_043 made move, rotate, and scale commands link-aware, made the DXF exporter preserve text alignment, improved some tooltips, and made Fillet remember the last used settings.

**BIM**: Roy_043 and yorikvanhavre fixed several bugs.

**FEM**: marioalexis84 patched the Reinforced material tool to use the new material editor and made more minor improvements.

**GUI**:

- Rexbas fixed a navigation glitch where camera position would shift when starting viewport rotation.

- benj5378 made autocompletion global and available in all TextEdit objects.

- hasecilu added units to some spinboxes on Preferences pages.

- kadet1090 fixed the render order of datum planes and added an option to show the plane that a sketch is based on.

![Image 1](image-1.png "Image 1")

**Importing**: wwmayer fixed a transparency issue when loading STEP files made by FreeCAD 0.21 and VariCAD, and rostskadat made miscellaneous improvements in the SH3D importing code.

Other changes arrived from: davesrocketshop, tritao, kadet1090, xtemp09, toastedcrumpets, and BootsSiR.

**PR stats**: since the previous report, 56 pull requests have been merged, and 25 new pull requests have been opened.

**Issue stats**: overall, there are 2512 open issues in the tracker, up by 3 from last week.

Meanwhile, Yorik van Havre posted an [update](https://yorik.uncreated.net/blog/2025/001-freecad-news-28) about his work on the BIM workbench. The post covers new features, such as support for the Type property in native IFC objects, and support for classification systems and quantities.

![Image 2](image-2.png "Image 2")