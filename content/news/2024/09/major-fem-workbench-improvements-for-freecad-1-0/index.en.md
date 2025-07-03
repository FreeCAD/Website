---
title: Major FEM Workbench improvements for FreeCAD 1.0
date: 2024-09-28
author: NewJoker
draft: false
categories: announcement
tags:
- FEM
cover:
  image:
  caption:
  alt:
---

FreeCAD 1.0 brings a true revolution. But apart from the TNP mitigation, built-in Assembly workbench, material handling rework, and major Sketcher improvements, there's a less common module that received many updates - **FEM**.

![Fem Figure 1](fem-fig1.webp "Fem Figure 1")

In fact, it's one of the workbenches that changed the most. Over 80 issues from the [FEM Roadmap](https://github.com/orgs/FreeCAD/projects/19) were fixed. This includes many bugs - some of them serious and long-standing - but also completely new features and various small usability improvements. I've been maintaining the FEM workbench for almost a year. In this post, I'd like to outline some of the most important new features coming in FreeCAD 1.0 soon.

The biggest new FEM feature is [ConstraintRigidBody](https://wiki.freecad.org/FEM_ConstraintRigidBody) - a tool providing support for CalculiX's rigid body constraint. The constraint is commonly used to apply moment/rotation or force/displacement to any selected face via a so-called reference point which can be located at a distance from the face. This makes it possible to apply a force acting on a lever (_remote force_). The constraint is particularly useful since it finally provides a way to simulate torsion of arbitrarily shaped parts in FreeCAD FEM.

![Fem Figure 2](fem-fig2.webp "Fem Figure 2")

The second major change is the introduction of 2D analyses with CalculiX. That includes plane stress (for very thin parts with in-plane loads), plane strain (for very thick parts with in-plane loads) ,and axisymmetry (for revolved parts with loads uniform around the circumference). The analyses can be performed by just following the approach for analyses with shell elements (but using only the XY plane) and changing the _Model Space_ property of the [CalculiX solver](https://wiki.freecad.org/FEM_SolverCalculixCxxtools).

![Fem Figure 3](fem-fig3.webp "Fem Figure 3")

Another new form of symmetry supported with the CalculiX solver is cyclic symmetry. It can be defined with the [tie constraint](https://wiki.freecad.org/FEM_ConstraintTie) and used for parts consisting of circular patterns of repetitive segments (sectors) around an axis and subjected to loads exhibiting the same type of symmetry. Thus, many rotating components such as shafts, flywheels, turbines, or fans can be analyzed this way.

Smaller but also important changes include more settings for tie and contact constraints, beam elements with reduced integration (necessary for pipe cross-sections and accurate results with plasticity), additional incrementation, and output frequency settings for CalculiX, adjustable acceleration magnitude for gravity load and support for plasticity with kinematic hardening in addition to isotropic one, among others.

Several improvements were introduced for thermomechanical analyses. You can change their type to uncoupled or purely thermal, radiation heat flux can be modeled, volumetric heat source is usable with CalculiX and heat flux was added to this solver's outputs.

![Fem Figure 4](fem-fig4.webp "Fem Figure 4")

Some other changes include capabilities of suppressing analysis features, hiding the selected finite elements and canceling ongoing meshing.

The implementation of Netgen was also replaced to work on Linux. Symbols of analysis features are now properly scaled and their size can be adjusted. There are several mesh appearance improvements as well. Old FEM examples on the Start page were updated and replaced with one file including three different approaches (1D, 2D and 3D) to the classic cantilever beam analysis.

Finally, the menu/toolbar names of several analysis features were changed to eliminate incorrect usage of the word "constraint" and make their meaning more clear.

A full list of changes, excluding minor bug fixes, can be found in the [release notes](https://wiki.freecad.org/Release_notes_1.0#FEM_Workbench).

Such enormous improvements wouldn't be possible without our new developer - Mario Passaglia (marioalexis84), working with whom is a pleasure. His contributions were [sponsored](https://wiki.freecad.org/Donate) by you, the community, via a grant from the FreeCAD Project Association. There's still a lot to do in order to make FEM as powerful as it could be, and more contributors are always welcome.

Current plans for further development include fixing any remaining bugs, standardizing the core of the workbench to make it easier to implement additional solvers (there is a new initiative to add support for [Code_Aster](https://code-aster.org/spip.php?rubrique2)), as well as further extending the support for CalculiX and Elmer and introducing advanced material models based on the reworked material system in FreeCAD.

Hopefully, many of these goals will be achieved and available in the next major release. All users are welcome to test as much as possible, report any issues and propose new features if they aren't on the roadmap yet.