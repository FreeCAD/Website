---
title: 'WIP Wednesday: 6 March 2024'
date: 2024-03-06
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

This week in FreeCAD development:

- **bgbsww**, **CalligaroV**, and **chennes** made further progress towards mitigating the toponaming issue.

- **WandererFan** fixes several bugs in TechDraw.

- **HowThatWorks** contributed a set of ISO 7200/ISO 5457 templates for TechDraw, he also removed the non-conformant ISO7200_Pep series and the ISO7200TD series of templates.

- **pavltom** reimplemented Leader Line parent linking in TechDraw, this allows to transfer the Leader Line to any other Part View present on the page, while keeping all its children, without the need to re-create them.

- **chennes** updated the Addon Manager to bring back something akin to the original Addon Manager display, with the side-by-side display of the list and details views. He also fixed several build and i18n issues.

- **FEA-eng** implemented 2D mechanical analysis methods using CalculiX: plane stress, plane strain, and axisymmetric. He also implemented isotropic and kinematic hardening as the next step towards support for advanced material models offered by CalculiX. Apart from that, he fixed Elmer FEM 2D electromagnetic examples and remove the need to include geometrical nonlinearity when nonlinear material is used in CalculiX.

- **marioalexis84** contributed a few fixes to FEM.

- **3x380V** updated the Python wrapper code with Qt6 migration in mind, he also introduced the use of std::chrono for time manipulation.

- **wwmayer** made various fixes and small enhancements, he also did some refactoring to reduce code duplication.

- **Roy-043** contributed small technical fixes and improvements to Draft and Sketcher.

- **davidgilkaufman** and **jffmichi** fixed a few issues in Path.

- **djmdjm** added G43 tool height compensation to centroid post-processing in Path, also fixed adaptive glitch by removing adjacent coincident and nearly-coincident points.

- **Rexbas** implemented an opt-out option to use InOutCubic easing function in navigation animations. He also fixed setting rotation center when entering dragging in TinkerCAD style.

- **LemonBoy** patched the UI code to make the dockbars show the same set of buttons with and without the overlay mode enabled.

- **FlachyJoe** introduced object freezing, so that users could toggle parametric behaviour of document objects.

- **AjinkyaDahale** improved the Join Curves command in Sketcher by making a C1 continuity at joining.

- **bdieterm** updated the setEulerAngles API to update rotation axis vector and rotation angle when setting a Rotation object.

- **maxwxyz** made small improvements in Sketcher and around.

- **jcoalson** fixed a bug in Part.

- **mosfet80** made minor fixes in the build system.

**PR stats:** In the week from Wednesday, 28 February to Wednesday, 6 March there were 58 pull requests merged, with a total codebase change of +4,975 / ‑1,227 (not counting translation updates). We had an average merged PR size of +86 / ‑21. 20 new pull requests were opened.

**Issue stats:** we closed 30 issues, and 63 new issues were opened. Overall, 1,311 issues are currently open.