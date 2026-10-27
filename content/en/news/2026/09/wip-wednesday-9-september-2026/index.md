---
title: WIP Wednesday, 9 September 2026
date: 2026-09-09
author: Aleksandr Prokudin
draft: false
category: update
tags:
  - WIP
cover:
  image:
  caption:
---


This week in FreeCAD development:

## Draft

Roy-043 fixed an issue where SVG faces were transformed into B-Spline faces rather than planar faces when imported ([PR#32410](https://github.com/FreeCAD/FreeCAD/pull/32410) and [PR#32410](https://github.com/FreeCAD/FreeCAD/pull/32410)). He fixed another bug where Shape2View would generate extra lines ([PR#28354](https://github.com/FreeCAD/FreeCAD/pull/28354)) and a midpoint snap bug in hyperbola ([PR#32499](https://github.com/FreeCAD/FreeCAD/pull/32499)).

## Sketcher

- UnKabaraQuiDev fixed another trimming issue ([PR#32355](https://github.com/FreeCAD/FreeCAD/pull/32355)).
- PaddleStroke fixed the constraint coincident tool giving errors when applying two points on the same line ([PR#32459](https://github.com/FreeCAD/FreeCAD/pull/32459)), fixed the offset tool creating underconstrained construction lines ([PR#32472](https://github.com/FreeCAD/FreeCAD/pull/32472)), fixed construction lines that B-Spline tools leave when you cancel them ([PR#32457](https://github.com/FreeCAD/FreeCAD/pull/32457)), and several other issues ([PR#32468](https://github.com/FreeCAD/FreeCAD/pull/32468), [PR#32459](https://github.com/FreeCAD/FreeCAD/pull/32459), [PR#32458](https://github.com/FreeCAD/FreeCAD/pull/32458), [PR#32452](https://github.com/FreeCAD/FreeCAD/pull/32452), [PR#32473](https://github.com/FreeCAD/FreeCAD/pull/32473), [PR#32469](https://github.com/FreeCAD/FreeCAD/pull/32469), [PR#32453](https://github.com/FreeCAD/FreeCAD/pull/32453), [PR#32470](https://github.com/FreeCAD/FreeCAD/pull/32470), [PR#32478](https://github.com/FreeCAD/FreeCAD/pull/32478)).
- tritao fixed two Sketcher dimensional-constraint rendering problems ([PR#31922](https://github.com/FreeCAD/FreeCAD/pull/31922)).

## Part and PartDesign

- maxwxyz patched the code to preserve taper direction for multi-sided pockets ([PR#32295](https://github.com/FreeCAD/FreeCAD/pull/32295)), fixed the incorrect transform order that lead to wrong profile shape for rotated profiles when the sketch InternalFace is used ([PR#32388](https://github.com/FreeCAD/FreeCAD/pull/32388)), fixed the display of the wrong edge radius in Quick Measure ([PR#32511](https://github.com/FreeCAD/FreeCAD/pull/32511)), and improved the way FreeCAD handles situations where none of the adjacent faces of an edge has a valid polygon for it (FIXME)
- codeotaku implemented the missing "recto verso" mode for the Thickness tool ([PR#32333](https://github.com/FreeCAD/FreeCAD/pull/32333)).
- FlachyJoe added a common boolean operation to subtractive features ([PR#29650](https://github.com/FreeCAD/FreeCAD/pull/29650)).

{{< video src="boolean-operation.mp4" >}}

## TechDraw

PaddleStroke implemented a parametric spreadsheet view ([PR#31595](https://github.com/FreeCAD/FreeCAD/pull/31595)):

{{< youtube id=B3NANI9FEds title="TechDraw Spreadsheet views coming to FreeCAD" loading=lazy >}}

## CAM

- Connor fixed G-code generation issues where modal deduplication was dropping or misplacing command words, and the LinuxCNC blend command was appended directly to the preamble ([PR#32251](https://github.com/FreeCAD/FreeCAD/pull/32251)). he also improved the Toolbit dialog user interface ([PR#32371](https://github.com/FreeCAD/FreeCAD/pull/32371)).
- sliptonic added a validator for machine definitions ([PR#32367](https://github.com/FreeCAD/FreeCAD/pull/32367)) and restored default pre-/post-amble in the KineticNCBeamicon2 legacy postprocessor ([PR#32343](https://github.com/FreeCAD/FreeCAD/pull/32343)).
- tarman3 produces numerous patches:
  - Allowing users to select axis to align a cylindric stock with a model ([PR#31208](https://github.com/FreeCAD/FreeCAD/pull/31208)).
  - Replacing G0 with G1 for plunge moves in MillFacing ([PR#31744](https://github.com/FreeCAD/FreeCAD/pull/31744)).
  - Patched Helix to use the StartPoint property instead of (0,0) to define orientation of the first helix ([PR#32166](https://github.com/FreeCAD/FreeCAD/pull/32166)).
  - Patched Inspector to allow using units like mm/min and in/min rather than mm/s ([PR#31938](https://github.com/FreeCAD/FreeCAD/pull/31938)).

## BIM

- EdgarJRobles fixed the direction of the TSLOT beam profile extrusion ([PR#32283](https://github.com/FreeCAD/FreeCAD/pull/32283)).
- paulcakeface updated the BIM array menu so that Path Array and Point Array now use the existing Link Array versions ([PR#32325](https://github.com/FreeCAD/FreeCAD/pull/32325)).
- Roy-043 fixed an error when opening BIM Views Manager in old files ([PR#32325](https://github.com/FreeCAD/FreeCAD/pull/32325)), made BIM_Diff work for imported IFC files ([PR#30796](https://github.com/FreeCAD/FreeCAD/pull/30796)), and added a "Force update" command to Shape2DView ([PR#30130](https://github.com/FreeCAD/FreeCAD/pull/30130)),
- maxwxyz fixed a regression where an error would be displayed after Slab is run and no planar obejct is selected ([PR#31671](https://github.com/FreeCAD/FreeCAD/pull/31671)).

## Other changes

- Krrish777 added support for cylinder and cone axes in angle measurements in the Measure tool ([PR#31905](https://github.com/FreeCAD/FreeCAD/pull/31905)).
- Ayushjo added .3mf to the list of supported file formats when importing mesh ([PR#32476](https://github.com/FreeCAD/FreeCAD/pull/32476)).

Additional improvements and fixes were contributed by 007stevendigar-lgtm, andershol, awgrover, Ayushjo, Bojan9597, bountyforge-lab, chennes, Connor, ElementW, Gebert81, ipatch, Lgt2x, maxwxyz, PaddleStroke, tarman3, TD-4242, tritao, and wmayer.

If you are interested in testing the latest weekly build, you can grab it [here](https://github.com/FreeCAD/FreeCAD/releases/tag/weekly-2026.09.09).

## Activity stats

**PR stats**: since the previous report, 76 pull requests have been merged, and 63 new pull requests have been opened.

**Issue stats**: overall, there are 3511 open issues in the tracker, down by 19 from last week.
