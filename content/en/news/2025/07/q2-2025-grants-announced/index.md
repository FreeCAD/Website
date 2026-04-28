---
title: Q2 2025 grants announced
date: 2025-07-10
authors: Aleksandr Prokudin
categories: announcement
draft: false
tags:
  - FPA
  - grant
cover:
  image:
  caption:
---


The FreeCAD Project Association general assembly has voted for Q2 grants based on recommendations from the grant technical review committee.

Here are the projects we are allocating available money for (in order of submission):

[Pattern tools refactor, unification, and additional functionality](https://github.com/FreeCAD/FPA-grant-proposals/issues/38) by Pierre-Louis Boyer. Pierre intends to refactor, unify, and enhance existing linear/polar pattern tools in multiple workbenches. He has been awarded a grant of €2,000. The first pull request has already been [submitted](https://github.com/FreeCAD/FreeCAD/pull/22389).

[Configuration Space Visualization for Computer-Aided Geometric Design](https://github.com/FreeCAD/FPA-grant-proposals/issues/39) by Brad Eric Hollister. This method allows for the visualization of contact curves between pairs of parts. For a general introduction to the concept, you can refer to the video below. Brad's job is to implement an exporter in Python that will translate parts and assemblies designed in FreeCAD into the [HIPAIR](https://www.cs.purdue.edu/archives/2008/eps/hipair.html) input language. The visualization will be done outside FreeCAD, at least as part of this grant work. Brad has been awarded $500 USD (€430) for the project.

{{< youtube id=2s_Y5fSRx_g title="2013 - Interactive Visualization of 3D Configuration Spaces" loading=lazy >}}

[Websites improvements initiative - Step 1](https://github.com/FreeCAD/FPA-grant-proposals/issues/40) by Marcus Pollio. Marcus has been actively working on the redesign and unification of the website for almost a year now. This particular project's deliverables are features parity between the old and the new website and unification of the Homepage, the News blog, and the Developers Handbook. Marcus has been awarded a grant of €4,000 for this project.

[PartDesign: Extrude in two directions](https://github.com/FreeCAD/FPA-grant-proposals/issues/41) by Pierre-Louis Boyer. Pierre has already submitted a [pull request](https://github.com/FreeCAD/FreeCAD/pull/21794) that implements this feature (which will fix two issues in the tracker, [#20845](https://github.com/FreeCAD/FreeCAD/issues/20845) and [#16175](https://github.com/FreeCAD/FreeCAD/issues/16175)). He has been awarded a grant of €500 for the project.

[Maintenance, improvement, and development of new features on the Assembly workbench](https://github.com/FreeCAD/FPA-grant-proposals/issues/42) by Pierre-Louis Boyer. This project is similar to past grants issued to Mario Passaglia (FEM workbench) and is expected to involve both bugfixing and development of new features. FPA's recommendation for Pierre is to focus on fixes. He has been awarded a grant of €3,000 for working 10 hours a week on this for the next 3 months.

[Maintenance, improvement, and development of new features on the Sketcher workbench](https://github.com/FreeCAD/FPA-grant-proposals/issues/43) by Pierre-Louis Boyer. This project is structured exactly like the Assembly project above: fixes and improvements in Sketcher, 10 hours a week for the next 3 months, for €3,000 total.

[CAM/BIM: 2D Nesting Tool for FreeCAD](https://github.com/FreeCAD/FPA-grant-proposals/issues/44) by Abhiram Masda. He will either improve the existing nesting algorithm or integrate a more efficient open-source library to reduce material waste and improve layout quality. Abhiram was awarded a grant of ₹150,000 INR (€1,650).

[Research ISO GPS / GD&T for an overall concept as implementation in FreeCAD](https://github.com/FreeCAD/FPA-grant-proposals/issues/45) by Max Wilfinger. Max reworked and narrowed down his original proposal from Q1 2025 to researching standards and industry workflows, developing an overall workflow for FreeCAD, and structuring the project for future implementation. No coding is expected to be done as part of this grant work. Max was awarded a grant of €3,000 for the project.

[CAM improvements for machining metals](https://github.com/FreeCAD/FPA-grant-proposals/issues/46) by David Kaufman. David aims to improve control of feed rates, submit LeadInOut dressup fixes and improvements, and fix the RampEntry dressup performance. David has been awarded a grant of USD $3,500 for the project. He has already submitted his first [pull request](https://github.com/FreeCAD/FreeCAD/pull/21944) for review.

[Assembly Solver Interface Abstraction and Alternative Solver Implementation](https://github.com/FreeCAD/FPA-grant-proposals/issues/47) by Jackson Oursland. Jackson intends to abstract the use of solvers in the Assembly workbench aiming to add support for the [MuJoCo](https://mujoco.org/) solver (work in progress). Other possibilities include support for the [Project Chrono](https://projectchrono.org/) solver. Jackson was awarded a grant of USD $2,000.

[Update OSH Automated Documentation for FreeCAD 1.0](https://github.com/FreeCAD/FPA-grant-proposals/issues/48) by Pieter Hijma. Pieter will update his [OSH Automated Documentation (osh-autodoc)](https://osh-autodoc.org/) workbench to support FreeCAD 1.0+ (this assumes fixing several issues), the [custom PDF compiler](https://codeberg.org/osh-autodoc/osh-autodoc-pdf), and the documentation. He was awarded a grant of €2,000 for the project.

Unlike Q1 2025 when we had a lot of competition for funds, the total amount of funds requested in Q2 (€24,310) almost matched the quarter's budget allocation (€20,000) + leftovers from Q1 (€3,160). There has been no strong and unanimous objection to grant proposals in Q2, thus, all grant applications that were submitted have been approved. Should all projects be successful, we'll be over the budget by approx. €1,000  for Q2 2025 (USD <> EUR exchange rates will likely fluctuate).