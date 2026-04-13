---
title: WIP Wednesday, 30 July 2025
date: 2025-07-30
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

- Roy_043 added a dotted line tracker in Trimex extrude mode. This tracker connects the center of mass of the face with the picked point.
- He also fixed a bug in MouseDelay handling and implemented EditTrackers for Draft Labels so that the Draft Edit command works.

**Sketcher**:

- matthiasdanner patched the arc angle and length constraints to show up beyond the center point.
- AjinkyaDahale fixed a crash that would occur when using the Trim tool in certain scenarios.
- Syres916 fixed the bug where the reference constraints weren't read-only in the property view.

**Assembly**:

- PaddleStroke fixed 11 reported bugs, including undeletable flexible sub-assemblies, incorrectly positioned flexible sub-assemblies, and more.
- One of the fixes also replaces the "Deactivated" property of joints by the core "suppressed" property mechanism.

**BIM**:

- Roy_043 fixed profile rotation of elbow pipe connector and patched Arch_Stairs to hide the base of the railings upon creation.
- furgo16 changed sun path diagram scale from 1 mm to 20 m radius, which is better suited to BIM magnitudes.

**CAM**: Various fixes and improvements by adrianinsaval, Syres916, knipknap, z0r0, chennes, and tarman3.

**I/O**: furgo16 redesigned the DXF import UI to streamline the options, added a Part primitives import mode as a middle ground between performance and import fidelity, and added a Draft objects import mode to get closer to feature parity with the legacy importer. The plan is to bring the new importer on par with the legacy one and then remove the latter.

Among other changes:

- jwueller, theo-vt, and chennes fixed various issues in Sketcher.
- WandererFan fixed several issues in TechDraw.
- furgo16 added a context menu item for groups ("Select group contents") so that you can select their contents at once.
- pieterhijma patched the VarSets dialog to allow for the use of expressions.
- jffmichi made it possible to undock all MDI windows and toggle the fullscreen mode for them. This applies to Spreadsheet, TechDraw, Dependency Graph, Start Page, and others.

Additional improvements and fixes were contributed by chennes, oursland, z0r0, leematos, theo-vt, PaddleStroke, kadet1090, luzpaz, and Syres916.

**PR stats**: since the previous report, 58 pull requests have been merged, and 42 new pull requests have been opened.

**Issue stats**: overall, there are 2938 open issues in the tracker, same as last week.