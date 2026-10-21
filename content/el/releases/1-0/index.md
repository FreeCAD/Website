---
title: FreeCAD 1.0 Notes
description: A new chapter for free and open-source CAD.
date: 2024-11-19
cover:
  image: 1-0.webp
  caption: FreeCAD 1.0 release
---

After more than 20 years of development, the 1.0 release marks a major milestone for the FreeCAD project.

With a strong focus on stability, usability, and long-requested core features, FreeCAD is now more powerful, flexible, extensible, and robust than ever before.

{{< block title="Robust Solid Modeling" css_class="accent-1" >}}

{{< group >}}

> [!NOTE]
> FreeCAD now tracks how individual sub-elements (faces, edges, vertices) evolve through modeling operations by building a history map that records whether elements were modified, generated, or deleted.
> This allows stable references to be maintained even as the underlying topology changes.

- The mitigation algorithm to the long-standing topological naming problem has finally been merged
- Models now better survive edits without randomly breaking dependencies
- Parametric workflows and complex design iterations are far more predictable, resilient, and effective

{{< /group >}}

```cpp {file="src/Mod/Part/App/PropertyTopoShape.cpp"}
void ShapeHistory::reset(
    BRepBuilderAPI_MakeShape& mkShape,
    TopAbs_ShapeEnum type,
    const TopoDS_Shape& newS,
    const TopoDS_Shape& oldS
)
{
    shapeMap.clear();
    this->type = type;

    TopTools_IndexedMapOfShape newM, oldM;
    TopExp::MapShapes(newS, type, newM);  // map with all old objects
    TopExp::MapShapes(oldS, type, oldM);  // map with all new objects
```

{{< /block >}}

{{< block title="Integrated Assembly" css_class="accent-2" >}}

![Exploded View in the Assembly](exploded-view.webp)

- A brand-new built-in Assembly workbench powered by a modern solver
- Define constraints between parts with improved reliability
- Designed for real-world multi-part engineering workflows

{{< /block >}}

{{< block title="Polished Interface" css_class="dots" >}}

- New light and dark themes for better comfort
- Smarter selection tools (filter vertices, edges, faces)
- Rotation center indicator for precise navigation
- Reworked panels, tabs, and preferences dialog
- Faster, cleaner start page

![Side panels overlay](assembly.webp)

{{< /block >}}

{{< block title="Better Tools for Everyday" css_class="accent-3" >}}

![Measurement tool](measurement.webp)

- Universal measurement tools available across workbenches
- Improved Sketcher and Part Design workflows
- More consistent behavior across tools

{{< /block >}}

{{< block title="BIM Upgrade" css_class="πλέγμα" >}}

- A unified Building Information Modeling workbench with Native IFC support
- Better project structure, data handling, and building workflows
- Improved interoperability with other open BIM tools

![BIM workbench](bim.webp "BIM)

{{< /block >}}

{{< block title="Core Engine and Scripting Power" css_class="accent-4" >}}

- Expressions now support the vector API
- New ==App::VarSet== for managing design variations
- Expanded and cleaner Python API
- Improved Python editor and scripting workflow

{{< /block >}}

{{< block title="Materials and Simulation Improvements" css_class="κλίση" >}}

![FEM workbench](fem.webp)

- A new materials system for visual and physical properties
- Many enhancements across FEM and simulation tools

{{< /block >}}

{{< block title="Identity Evolution" css_class="accent-5" >}}

![Refreshed FreeCAD logo chosen by the community](symbol.svg "Refreshed FreeCAD logo chosen by the community")

{{< /block >}}

{{< button url="https://wiki.freecad.org/Release_notes_1.0" label="Read the complete release notes" >}}

And so much more, by hundreds of contributors around the world!

**What to be part of this adventure too?** Join the [community](community) and [support](donate) its development.

As always, have fun and keep _FreeCADing_!