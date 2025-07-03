---
title: 'New Grants approved: Variant Parts, debugging with CLion and VSCode, Homebrew build update'
date: 2024-09-24
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

The FPA general assembly approved the funding of three more grants.

**Pieter Hijma** will be working on research for variant parts. There's a number of FreeCAD features that require inserting copy-on-change links, such as referencing external geometry in a body for which SubShapeBinders are used in Part Design. The architecture behind the current implementation involves hidden parts and temporary files and is fragile. The workflow imposed by this architecture isn't great either. Another domain where a better implementation is required are assemblies where you might want inserting a variation of a linked part.

Pieter will begin the project by elaborating on the current state of affairs in the forum for developers, then propose patches targeting three aspects of the current implementation: how parent documents refer to properties of child documents, how shapes are computed from a base part, and how variants are created. Please see the [proposal](https://github.com/FreeCAD/FPA-grant-proposals/issues/10) for more details. He was awarded a grant of EUR 8,000 for the entire project. Work starts in September and is expected to be done by the end of this year.

**Brad McLean** will write documented procedures and/or code for supporting debugging FreeCAD C++ and Python from CLion and VSCode. The project is expected to take approximately 2 weeks. Brad was [awarded](https://github.com/FreeCAD/FPA-grant-proposals/issues/13) a grant of USD $1,500 for the project.

**Chris Jones** will continue his work on homebrew builds of FreeCAD. This time, he will update the homebrew-freecad tap to link against Python v3.12 and Qt v6 when creating the build. The project is expected to take a few weeks to complete. Chris was [awarded](https://github.com/FreeCAD/FPA-grant-proposals/issues/11) a grant of USD $2,000 for the project.

If you are interested in improving FreeCAD one way or another, you can[ apply](https://fpa.freecad.org/programs/fpadf-announcement) for an out-of-program grant any time.