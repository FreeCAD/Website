---
title: FreeCAD 1.1 Notes
description: Free and open-source CAD, refined.
date: 2026-03-24
cover:
  image: relnotes_1-1.webp
  caption: FreeCAD 1.1 release
---


After one year and a half of continuous development, FreeCAD 1.1 builds on the 1.0 milestone with meaningful new tools and improved workflows across the board.

This release focuses on making everyday modeling more reliable, faster, and more intuitive — while expanding capabilities for hobbyists, advanced users and professionals alike.

{{< button url="https://www.youtube.com/watch?v=a9biWv_M8p8" label="Watch the release video" icon="youtube_fill" >}}


{{< block title="Your refined user interface and experience" css_class="pastel1" >}}

{{< group >}}

{{< carousel "transform_1-1.webp" "transform2_1-1.webp" >}}

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

![Clarify selection](clarify_1-1.webp)

{{< /group >}}

{{< /block >}}


{{< block title="Part Design and Assembly on the move" css_class="background: var(--gradient);" >}}

![Feature preview and adjustments by gizmos](pd_1-1.webp)

- Enhanced feedback during modeling and editing thanks to transparent previews and interactive draggers.
- Overhauled hole tool task panel, taper and thread support, and performance.
- Two sided mode for padding and different spacing in transform tools.
- New part insertion, simulation for joints motion and animations, and Bill of Materials for Assemblies.

{{< /block >}}


{{< block title="Born to Sketch" css_class="dots" >}}

{{< group >}}

{{< compare "sketcher_1-1.webp" "pad_1-1.webp" >}}

- Projection, intersection, and external geometry in the Sketcher.
- Improved master sketch workflow via make internals for closed contours.
- Many usability and interface tweaks to streamline sketching workflows.

{{< /group >}}

{{< /block >}}


{{< block title="CAM, FEM and TechDraw flow" css_class="pastel2" >}}

- New toolbit library and editor, better multi-pass support and post-processors introduced in CAM.
- FEM results now support animations, electrostatic analyses, and glyph filters.
- TechDraw has improved snapping, frame toggle, annotation, and dimension tools.

![Forces visualization for glyph filters](glyph_1-1.webp)

{{< /block >}}


{{< block title="Build on BIM and Draft" css_class="grid" >}}

![Better layers, dimensions, and style management](plan_1-1.webp)

- View panel to view, interact, and manage the project spatial structure and 2D views.
- Interactive sun position and ray visualization for sites.
- Improved layers management with overrides, array tools, drafting objects creation and editing.

{{< /block >}}


{{< block title="General performance and stability" css_class="pastel3" >}}

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