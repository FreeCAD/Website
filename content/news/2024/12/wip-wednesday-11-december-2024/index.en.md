---
title: 'WIP Wednesday: 11 December 2024'
date: 2024-12-11
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

**Sketcher**:

- PadleStroke implemented group dragging of geometries.

- FlachyJoe improved the look of arc length for when the arc length is higher than half diameter.

**Draft**: Roy_043 improved the Trimex tool and fixed a couple of bugs.

**BIM**: yorikvanhavre implemented support for 2D objects in NativeIFC: linework, texts, dimensions, hatches, section planes, axes. The BIM views dialog got a second panel that includes 2D views, and BIM annotation tools got a "Create 2D Drawing" tool. He also added a [Type](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcTypeProduct.htm) property to all IFC objects and updated NativeIFC unit tests.

**Measurements**: Murmele implemented the functionality to autosave the current measurement and restart a new measurement automatically.

**TechDraw**: WandererFan added a tool for support and debugging to work around the hidden line removal algorithm's issues handling geometry errors.

**CAM**: luvtofish implemented support for the G84/G74 Tapping Operation.

**FEM**:

- marioalexis84 added box and elliptical beam section types, implemented a tool to delete all results objects including pipelines and filters, added an option to save geometry IDs in ElmerFEM,

- NewJoker fixed CalculiX ties constraints to support shell surfaces.

**Toponaming**: CalligaroV completed another patch that was the legacy of Brad McLean who passed away earlier this year. The patch adds a plane matching based heuristic to TNP mitigation. According to Brad, this should address the common remaining TNPs arising from edge changes in a sketch.

**Core**: The main PR for the core datum by PaddleStroke has landed. No way to create the new LCS objects yet, the only visible change is the origin appearance. The latter is being discussed by the design working group at the moment and will likely be improved.

Various other fixes and improvements arrived from Roy_043, paullee0, wwmayer, FlachyJoe, and others.

**PR stats**: since the previous report, 75 pull requests have been merged, and 21 new pull requests have been opened.

**Issue stats**: overall, there are 2328 open issues in the tracker, down by 24 from last week.