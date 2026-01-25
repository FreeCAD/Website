---
title: 'New in 0.20: Improved OpenSCAD compatibility'
date: 2022-12-14
authors: Chris Hennes
draft: false
categories: feature
tags:
- OpenSCAD
cover:
  image:
  caption:
---

FreeCAD has supported importing *.scad and *.csg files from [OpenSCAD ](http://openscad.org/)for several years, but supporting the full range of features provided by OpenSCAD is an ongoing project. The FreeCAD 0.20 release brings improved compatibility with several more commands, as well as bug fixes to several existing commands.

### Low-poly modeling

OpenSCAD and FreeCAD have different modeling strategies: OpenSCAD is fundamentally discrete, whereas FreeCAD typically maintains mathematically-precise object definitions without surface discretization (unless explicitly told to discretize using the Mesh workbench, etc.). Most of the time when importing from OpenSCAD, the discretized object is replaced by its equivalent "exact" FreeCAD object: however, this is not always the OpenSCAD geometry designer's intent. For example, sometimes a cylinder with only eight sides (i.e. `$fn=8` in OpenSCAD) is really intended to have an octagonal cross-section which is _not_ intended to be a perfect circle. FreeCAD 0.20 improves support for this modeling strategy to include low-`$fn` sweeps and revolutions.

### Surfaces from data

When creating a surface from a set of 2D data points and some arbitrary data value at those points, previous versions of FreeCAD "un-discretized" that surface and created a Bezier surface representation. However, this conflicted with OpenSCAD's fully-discrete geometry representation and often resulted in extreme spikes in the splined surface. FreeCAD now remains faithful to the original discrete surface geometry and gives results more akin to what would be seen directly in OpenSCAD.

### Improved extrusions

FreeCAD now fully supports tapered and twisted extrusions, in both low-`$fn` and non-discretized versions.

### Improved Snap/AppImage support

For users with the latest version of OpenSCAD installed (2021.01) FreeCAD now supports the new pipe-based data transmission method. The upshot of this new method is that even if FreeCAD and OpenSCAD are installed as Snap or AppImage packages (precluding communication using files in `/tmp` because the different packages will be prevented from accessing each other's temp files), they can still exchange data. As a fallback for older versions of OpenSCAD, users can now explicitly set the transfer directory to someplace where both programs can access files (for example, the user's home directory).