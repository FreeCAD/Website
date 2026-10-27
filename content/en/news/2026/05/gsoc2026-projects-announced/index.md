---
title: GSoC2026 projects announced
date: 2026-05-02
author: Aleksandr Prokudin
draft: false
category: feature
tags:
  - GSOC
cover:
  image:
  caption:
---


Google announced the projects that will be part of the Summer of Code 2026 project. Here is what our GSoC students will be working on this year.

Aymi will be adding support for [animated multibody dynamics visualizations](https://forum.freecad.org/viewtopic.php?t=104219). The project will be built on top of the 3rd-party Motion workbench (by Jose Gabriel Egas Ortuño) and the native FEM workbench. It's an extremely challenging project to tackle alone for anyone, but Aymi won't be alone. Her mentors are long-time FEM contributor marioalexis84 and multi-body dynamics expert [Aik-Siong Koh](https://mbdfem.com/).

Morten Vajhøj will be changing the way you annotate geometry in TechDraw. Right now, you need to select an object and then pick the right tool, which is not how the rest of FreeCAD works for the most part. Morten [will revamp](https://forum.freecad.org/viewtopic.php?t=104015) this workflow so that you select an annotation tool and immediately see the applicable geometry to use it on.

[Nishendra Singh's project](https://forum.freecad.org/viewtopic.php?t=103697) follows a [recent discussion](https://forum.freecad.org/viewtopic.php?t=100142) about reviving the abandoned Robot workbench. Nishendra will be replacing CSV/DH file imports with URDF imports, adding the exporting of the joint & trajectory data, and updating the Orocos KDL kinematics library.

Parag Debnath will make it possible to search and apply international classification standards to selected IFC entities by [integrating the buildingSMART Data Dictionary](https://forum.freecad.org/viewtopic.php?t=104041) into the BIM workbench.

YashSuthar983 will add [3D parametric sketching](https://forum.freecad.org/viewtopic.php?t=104125). This work will involve adding new primitives and spatial constraints to the PlaneGCS solver. The plan right now is to create a temporary new workbench as a testbed and then merge it into the unified Sketcher workbench.

We also received multiple applications for improving the Measure tool. This is a great indication of how important this functionality is and how much more work needs to happen there. While neither application made the cut for GSoC this year, we encourage contributors interested in improving the Measure tool to [submit applications for an FPA grant](/news/q2-2026-grant-program/).
