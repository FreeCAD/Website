---
title: Q1 2026 grants announced
date: 2026-04-06
author: Aleksandr Prokudin
draft: false
category: announcement
tags:
  - FPA
  - grant
cover:
  image:
  caption:
---


The FPA members have voted for Q1 2026 grants.

The following work will be paid for once completed:

1. [Websites improvements - Step 2.1: Modernize Doxygen setup and output](https://github.com/FreeCAD/FPA-grant-proposals/issues/78) by marcuspollio. The existing source code documentation is severely out of date. Marcus will update and refactor the current Doxygen setup and config, create a new repository for the generated output, set up CI and CD from FreeCAD/FreeCAD source to this new repo, and deploy to live site, then update website and wiki links and other places to this new live site. He will be awarded a grant of EUR 500 for the project.
2. [Maintenance, improvement and development Assembly & Sketcher](https://github.com/FreeCAD/FPA-grant-proposals/issues/79) by PaddleStroke. Pierre-Louis will continue his work on bug fixing, maintenance, reorganization, standardization of the two workbenches, and the addition of new features. Pierre-Louis will be awarded a grant of EUR 6,000 for working on this project for the next 3 months.
3. [Upgrade the CAM geometry kernel from Clipper 1 to Clipper 2](https://github.com/FreeCAD/FPA-grant-proposals/issues/80) by davidgilkaufman. Polygon boolean and offset operations form the backbone of nearly all CAM operations. We currently perform these functions using Clipper 1, but it has been superseded by Clipper 2, and Clipper 1 is now obsolete. So David will rewrite the affected functions with Clipper 2. David will be awarded a grant of USD 3,750 for the project.
4. [Implement ISO 13715 (Edge Symbols) and ISO 15785 (Joint Symbols) in TechDraw Workbench](https://github.com/FreeCAD/FPA-grant-proposals/issues/81) by rehan-ahmed-aix. FreeCAD already supports edge and face selection, so the implementation by Ahmed will leverage that existing capability, and users will be able to attach symbols directly to selected edges, vertices, or faces on drawing views, or attach symbols to leader lines (traditional approach). Ahmed will be awarded a grant of EUR 751 for the project.
5. [OpenID Connect Authentication, FreeCAD Scripting in Viewer, and Matomo Docker Image Replacement for Lens Platform](https://github.com/FreeCAD/FPA-grant-proposals/issues/82) by amrit3701. Ondsel Lens will gain OpenID-based authentication, and users will be able to run custom FreeCAD Python scripts on the loaded model from the web interface. Additionally, the currently defunct Matomo docker image will be replaced so you can run web analytics on your own instance of Lens. Amritpal will be awarded a grant of EUR 8,000 from the [separate Ondsel Onwards fund](/news/the-ondsel-onwards-fund/) submitted by a private sponsor.

The total non-Ondsel allocated funding is EUR 10,721 against a budget of EUR 10,000. However, the "CAM/BIM: 2D Nesting Tool for FreeCAD" grant has been recently cancelled due to the developer's inactivity, which freed up EUR 1,650, so we are not over the budget after all.
