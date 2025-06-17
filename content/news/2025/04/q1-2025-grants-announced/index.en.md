---
title: Q1 2025 grants announced
date: 2025-04-07
author: Aleksandr Prokudin
draft: false
categories: announcement
tags:
- FPA
- grant
cover:
  image:
  caption:
  alt:
---

The FPA General Assembly has finalized the list of approved grant applications for the first quarter of 2025.

**Ajinkya Dahale** (AjinkyaDahale) will develop [two new types of curves](https://github.com/FreeCAD/FPA-grant-proposals/issues/33) in Sketcher: restricted and offset curves. Restricted curves are useful when we only need a portion of an external curve that can change. Offset curves are dependent on a parent curve to allow offset for a larger set of curves (independent offset curves already exist in FreeCAD, this is different). Ajinkya was awarded a grant of EUR 2000 for the project.

**Mario Passaglia** (@marioalexis84) will continue his [work on the FEM workbench](https://github.com/FreeCAD/FPA-grant-proposals/issues/34). He will fix bugs, maintain and reorganize the code, and take care of various shortcomings in the mesh object, such as the impossibility of handling multiple meshes, time-consuming algorithms to search mesh elements, and the lack of mesh quality checking. Mario was awarded a grant of USD 3000 for the project.

**João Matos** (@tritao) and **Benjamin Nauck** (@hyarion) will [modernize](https://github.com/FreeCAD/FPA-grant-proposals/issues/35) FreeCAD's rendering and selection systems to fix various performance issues on large projects. They will decouple the selection picking and selection rendering system, abstract the raw legacy OpenGL calls into a rendering abstraction layer, and add a modern renderer to Coin. João and Benjamin were awarded a grant of EUR 4000.

**João** and **Benjamin** got another grant approved: [multithreading architecture improvements](https://github.com/FreeCAD/FPA-grant-proposals/issues/36) in FreeCAD. They will focus on enhancing the base infrastructure to enable asynchronous operations and deliver asynchronous recomputation of the document and its objects, a multi-threaded signal system, Python async support, and UI enhancements to manage modal or background tasks. They were awarded a grant of EUR 2000 for this project.

**Chris Jones** (@ipatch) will [fix building FreeCAD on macOS](https://github.com/FreeCAD/FPA-grant-proposals/issues/28) with Homebrew. Chris was awarded a grant of USD 1000 for the project.

**Amritpal Singh** (@amrit3701) will resume his work on Ondsel Lens, a FreeCAD-centered online PDM system developed by Ondsel. He will [decouple](https://github.com/FreeCAD/FPA-grant-proposals/issues/29) it from Amazon S3 and Lambda to make it self-hosted on any infrastructure. Amritpal was awarded a grant of USD 6500 out of the [Ondsel Onward fund](https://blog.freecad.org/2025/02/14/the-ondsel-onwards-fund/) contributed by an anonymous sponsor.