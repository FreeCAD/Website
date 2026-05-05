---
title: FreeCAD 1.1
description: Free and open-source CAD, refined.
date: 2026-03-24
lastmod: 2026-04-14
versions: ["1.1", "1.1.1"]
cover:
  image: relnotes_1-1.webp
  caption: FreeCAD 1.1 release
builds:
  windows_msi: https://github.com/freecad/freecad/releases/download/1.1.1/FreeCAD_1.1.1-Windows-x86_64-py311-installer.exe
  windows_zip: https://github.com/freecad/freecad/releases/download/1.1.1/FreeCAD_1.1.1-Windows-x86_64-py311.7z
  mac_x86: https://github.com/freecad/freecad/releases/download/1.1.1/FreeCAD_1.1.1-macOS-x86_64-py311.dmg
  mac_arm: https://github.com/freecad/freecad/releases/download/1.1.1/FreeCAD_1.1.1-macOS-arm64-py311.dmg
  linux_x86: https://github.com/freecad/freecad/releases/download/1.1.1/FreeCAD_1.1.1-Linux-x86_64-py311.AppImage
  linux_arm: https://github.com/freecad/freecad/releases/download/1.1.1/FreeCAD_1.1.1-Linux-aarch64-py311.AppImage
---


After one year and a half of continuous development, FreeCAD 1.1 builds on the 1.0 milestone with meaningful new tools and improved workflows across the board.

This release focuses on making everyday modeling more reliable, faster, and more intuitive — while expanding capabilities for hobbyists, advanced users and professionals alike.

{{< button url="https://www.youtube.com/watch?v=a9biWv_M8p8" label="Watch the release video" icon="youtube_fill" >}}


{{< block title="Your refined user interface and experience" style="background: linear-gradient(135deg, #ffd6e0, #fff3b0, #caffbf);" title_style="color: darkslategrey;" content_style="color: darkslategrey;" >}}

{{< group >}}

{{< carousel "transform_1-1.webp" "transform2_1-1.webp" >}}

<br>

- Three-point lighting improving rendering of models in the 3D view.
- Transform tool overhaul, with draggers, precise input, alignment, snapping, and target features.
- New Theme Editor and theme token system to easily customize stylesheets.
- Consolidated ==Add Property== dialog and Expression Editor with better completion and VarSet input.

{{< /group >}}

{{< group >}}

- New tools and shortcut hints and quick measure in the Status bar.
- The new clarify selection enables temporary transparency to shows all nearby geometrical entities.
- Improved navigation controls, align to selection, and visual utility tools.
- New search in the Preferences Editor.

<br>

![Clarify selection](clarify_1-1.webp)

{{< /group >}}

{{< /block >}}


{{< block title="Part Design and Assembly on the move" style="background: var(--bg-gradient);" >}}

![Feature preview and adjustments by gizmos](pd_1-1.webp)

- Enhanced feedback during modeling and editing thanks to transparent previews and interactive draggers.
- Overhauled hole tool task panel, taper and thread support, and performance.
- Two sided mode for padding and different spacing in transform tools.
- New part insertion, simulation for joints motion and animations, and Bill of Materials for Assemblies.

{{< /block >}}


{{< block title="Born to Sketch" style="background: var(--bg-dots);" >}}

{{< group >}}

{{< compare "sketcher_1-1.webp" "pad_1-1.webp" >}}

- Projection, intersection, and external geometry in the Sketcher.
- Improved master sketch workflow via make internals for closed contours.
- Many usability and interface tweaks to streamline sketching workflows.

{{< /group >}}

{{< /block >}}


{{< block title="CAM, FEM and TechDraw flow" style="background: linear-gradient(135deg, #e0c3fc, #f9f7ff, #c3f0ff);" title_style="color: darkslateblue;" content_style="color: darkslateblue;" >}}

- New toolbit library and editor, better multi-pass support and post-processors introduced in CAM.
- FEM results now support animations, electrostatic analyses, and glyph filters.
- TechDraw has improved snapping, frame toggle, annotation, and dimension tools.

![Forces visualization for glyph filters](glyph_1-1.webp)

{{< /block >}}


{{< block title="Build on BIM and Draft" style="background: var(--bg-grid);" >}}

![Better layers, dimensions, and style management](plan_1-1.webp)

- View panel to view, interact, and manage the project spatial structure and 2D views.
- Interactive sun position and ray visualization for sites.
- Improved layers management with overrides, array tools, drafting objects creation and editing.

{{< /block >}}


{{< block title="General performance and stability" style="background: linear-gradient(135deg, #dbe6c4 0%, #c3d2a4 40%, #aebf7a 70%, #8f9f5a 100%);" title_style="color: darkolivegreen;" content_style="color: darkolivegreen;" >}}

- Continued improvements to topological naming mitigation for greater model stability.
- Better Wayland support for Linux users.
- Faster startup and reduced memory usage.
- Numerous bug fixes across all workbenches.

![CNC lathe model assembly](cnc_1-1.webp)

{{< /block >}}


{{< button url="https://wiki.freecad.org/Release_notes_1.1" label="Read the complete release notes" >}}

And much more, thanks to hundreds of contributions from the community around the world.

**Want to be part of the journey?** Join the [community](/community) and [help shape](/donate) the future of FreeCAD.

As always — have fun and keep *FreeCADing*!