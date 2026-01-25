---
title: 'WIP Wednesday: 17 April 2024'
date: 2024-04-17
authors: Aleksandr Prokudin
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

In the **toponaming project**, bgbsww and chennes are getting really close to finalizing the port of RealThunder's patches to upstream FreeCAD. There is probably a week more of work, then the planned performance evaluation and improvements can begin.

**TechDraw:**

- WandererFan fixed several issues, such as broken zigzag lines orientation with rotated 3D view, as well as incorrect dimensions in the new Broken View feature.

- wwmayer fixed hatch clipping in SVG exporting code.

- dplanella organized TechDraw template translations into locale folders so that they wouldn't mix up with original English templates.

**Arch:**

- Roy-043 fixed several issues with Arch_Panel, Arch_Structure, and Arch_Wall.

- marcuspollio updated the tooltip of ArchSpace Text to mention recently implemented $longname and $description support.

There are three more notable changes that are user-visible:

- pskowronskiTDx contributed code to better support **3Dconnexion** devices such as SpaceMouse on Windows using Navlib.

- PaddleStroke updated the Trim tool in **Sketcher** to support continuous mode. Now you can select the tool, press and hold the mouse button and then drag the pointer over segments you want to delete. The tool will delete all segments you hover.

- davesrocketshop implemented support for older FCMat files in the new **materials system** (and wwmayer fixed some issue in that system).

Additional fixes, new tests, and minor improvements came from wwmayer, luzpaz, cjmayo, bgbsww, oursland, and Roy-043.

**PR stats:** In the week from Wednesday, 10 April to Wednesday, 17 April there were 40 pull requests merged, with a total codebase change of +16,750 / ‑1,535, the vast majority of changes coming in the new 3DConnexion support code. 24 new pull requests were opened.

**Issue stats:** we closed 21 issues, and 49 new issues were opened. Overall, 1,480 issues are currently open.