---
title: WIP Wednesday, 4 June 2025
date: 2025-06-04
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

- tetektoza fixed the UX issue where moving the mouse while entering in the on-view parameter widget would close that widget.
- matthiasdanner fixed the arrow direction for negative angles, as well as the View Scale Ratio preference.
- longrackslabs implemented context-sensitive input hints for all Sketcher geometry creation tools so that users get clear instructions for each step of the sketching process.
- Additional fixes from PaddleStroke and theo-vt.

**CAM**:

- sliptonic finally merged the [Ondsel SVG postprocessor](https://ondsel.com/blog/ondsel-svg-postprocessor/).
- tarman3 contributed 10 fixes for various issues in the workbench, as well as improvements:
  - New CycleTime property for the Array tool.
  - Dressup context submenu.
  - Support for RetractMode G98/G99 for Drilling in the simulator.
  - knipknap replaced CAM Tool Management with a better alternative developed for the [Better Tool Library](https://github.com/knipknap/better-tool-library/).
  - Various improvements and fixes by dbtayl, chennes, jffmichi, and LarryWoestman.

**GUI**:

- tritao added support for OCCT-style progress reporting and user-abort handling across Base, Part, PartDesign and boolean/shape builders.
- Further fixes and improvements by theo-vt and alfrix.

Among other changes:

- Roy-043 fixed several issues in Draft.
- ryankembrey and mosfet80 fixed several issues in FEM.
- WandererFan, PaddleStroke, and benj5378 fixes several issues in TechDraw.
- Roy-043, furgo16, and paullee0 contributed several improvements to BIM.
- davesrocketshop fixed a few issues in Materials and thermal conductivity units conversion in the core.

Additional improvements and fixes were contributed by wwmayer, Roy-043, luzpaz, alfrix, godiard, tarman3, oursland, 3x380V, sasobadovinac, Reqrefusion, samrg472, julian1, behollister, theo-vt, hyarion, kadet1090, and  maxwxyz.

**PR stats**: since the previous report, 72 pull requests have been merged, and 36 new pull requests have been opened.

**Issue stats**: overall, there are 2910 open issues in the tracker, up by 5 from last week.