---
title: 'WIP Wednesday: 26 March 2025'
date: 2025-03-26
author: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

**Draft**: Roy_043 contributed several improvements and bugfixes including one for the bug where Near Snap would not obey the Always Snap setting.

**Sketcher**: PaddleStroke improved the way length is enforced in Line and Slot tools when an angle is set.

**Part and PartDesign**:

- PaddleStroke added missing tooltips to Clone and Subshapebinder tools.

- tritao converted Part's XML-based Python APIs to the newly introduced Python-based bindings code model.

**Assembly**:

- PaddleStroke patched the workbench to show an error when a joint is missing a reference.

- JoaoMartins99 fixed a bug where it would be impossible to repeatedly deactivate an assembly.

**TechDraw**:

- PaddleStroke, benj5378, and WandererFan fixed several bugs.

- j-hap replaced the annotation edit dialog with QPlainTextEdit widget, so now you get to have a simpler dialog and annotations in multiple lines.

**CAM**:

- phaseloop fixed a bug in the estlcam postprocessor.

- LarryWoestman refactored postprocessors to use shared code.

**FEM**: ickby extended the VTK post-processing functionality to handle multi-frame results in a single post-processing object.

**BIM**:

- furgo16 contributed new unit tests and refactored some of the existing ones.

- semhustej improved UI text.

- yorikvanhavre fixed a bug where saving a project setup preset would fail.

- paullee0 contributed [ArchSketch](https://github.com/paullee0/FreeCAD_SketchArch) support.

**Materials**: davesrocketshop started working on support for external data sources such as databases or web services.

Additional fixes were contributed by aprospero, J-Dunn, Roy-043, chennes, karliss, Roy-043, kadet1090, mosfet80, tritao, pieterhijma, adrianinsaval, 3x380V, xtemp09, Syres916, alfrix, furgo16, thyssentishman, hasecilu, FlachyJoe, hyarion, bofdahof.

**PR stats**: since the previous report, 93 pull requests have been merged, and 44 new pull requests have been opened.

**Issue stats**: overall, there are 2735 open issues in the tracker, up by 20 from last week.

A word of warning: our weekly builds for Windows are severely behind our Linux and macOS for technical reasons. We are working on resolving the issue. The fix is all but trivial, so please bear with us.