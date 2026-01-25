---
title: 'Addon Spotlight: Assembly Workbenches'
date: 2022-10-19
authors: Chris Hennes
draft: false
categories: feature
tags:
- addon
- assembly
cover:
  image:
  caption:
---

The current 0.20 release of FreeCAD does not include a built-in workbench for assembling individual components into a more complex system: instead, several 3rd-party addons are available through the Addon Manager, allowing individual users to choose the type of assembly procedure they prefer. Three popular options are A2+, Assembly 3, and Assembly 4. This article will briefly overview each. Note that although the names make it sound like one might be the successor of the other, in fact all three are "spiritual successors" to the no-longer-maintained Assembly 2 workbench. The order they are presented here (and in the Addon Manager) is alphabetical, not an indication of popularity or "official" endorsement.

## A2+

![A 2Plus](A2Plus.png "Adding a constraint in A2+")

[A2+ (Assembly 2 Plus)](https://github.com/kbwbe/A2plus), an assembly workbench by "kbwbe", is intended as a direct successor to the original Assembly 2 workbench. It uses the same basic workflow as Assembly 2 so users already familiar with that workbench will be able to get started quickly. Begin by creating your parts in separate FreeCAD files, then create a new empty file and import the part that forms the basis for your assembly. Successively import more FreeCAD files and apply constraints to position them relative to your other parts. As the README puts it:

> The main goal of A2plus is to create a very simple, easy to use, and not over-featured workbench for FreeCAD assemblies. Using the KISS principle: KEEP IT SIMPLE, STUPID

## Assembly 3

![Addon Spotlight: Assembly Workbenches 2](A3.png "An Assembly 3 assembly")

[Assembly 3](https://github.com/realthunder/FreeCAD_assembly3) (a.k.a. ASM3) is an assembly workbench written and maintained by developer realthunder. It also uses a constraint-based approach to refer to existing geometric entities and align them relative to one another. It is often used in conjunction with [realthunder's fork of FreeCAD](https://github.com/realthunder/FreeCAD), which implements techniques to mitigate the so-called "topological naming problem" (TNP). TNP-related issues can otherwise cause problems for a constraint-based approach if the underlying objects change after the assembly has begun. Those techniques are being merged into the main FreeCAD development project during the current development cycle, but as of this writing they are not yet available.

## Assembly 4

![Addon Spotlight: Assembly Workbenches 3](A4.png "Placing a new body in Assembly 4")

[Assembly 4](https://github.com/Zolko-123/FreeCAD_Assembly4), by Zolko-123, uses user-assigned "LCS" (Local Coordinate System) objects to assemble objects relative to one another. This avoids any potential TNP issues by ignoring the underlying geometry itself and using FreeCAD's built-in `Part::Attacher` and `ExpressionEngine`. It completely avoids the idea of "constraints", opting for a simpler (and arguably more reliable) direct-positioning approach.

## How do you choose?

All three of these workbenches are easily installed using the Addon Manager, and all three can be installed at the same time. The best way to determine which one is best for you is to give each of them a test-drive. The user experience for each is very different, and many people develop strong preferences about which one is the best for their use-cases.