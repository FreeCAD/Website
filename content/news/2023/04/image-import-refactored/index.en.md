---
title: Image Import Refactored
date: 2023-04-24
authors: Chris Hennes
draft: false
categories: feature
tags:
- image
- UI
cover:
  image:
  caption:
---

Over the course of a few different PRs, developers @wwmayer and @PaddleStroke have re-imagined image import into FreeCAD. Gone is the old "Image Workbench" -- images are now first-class citizens in FreeCAD, with their import integrated into the core as a normal File->Open or File->Import. And this week @PaddleStroke implemented a new (and much more intuitive) user interface for setting the scale of an imported image. This is critical since the most common use of imported images is to match new CAD geometry to the scale in that image.

If you are running a recent developer build, give the new Image handling a try and let us know what you think!