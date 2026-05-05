---
title: FreeCAD 1.0
description: A new chapter for free and open-source CAD.
date: 2024-11-19
lastmod: 2025-08-06
versions: ["1.0", "1.0.1", "1.0.2"]
cover:
  image: relnotes_1-0.webp
  caption: FreeCAD 1.0 release
builds:
  windows_msi: https://github.com/freecad/freecad/releases/download/1.0.2/FreeCAD_1.0.2-conda-Windows-x86_64-installer-1.exe
  windows_zip: https://github.com/freecad/freecad/releases/download/1.0.2/FreeCAD_1.0.2-conda-Windows-x86_64-py311.7z
  mac_x86: https://github.com/freecad/freecad/releases/download/1.0.2/FreeCAD_1.0.2-conda-macOS-x86_64-py311.dmg
  mac_arm: https://github.com/freecad/freecad/releases/download/1.0.2/FreeCAD_1.0.2-conda-macOS-arm64-py311.dmg
  linux_x86: https://github.com/freecad/freecad/releases/download/1.0.2/FreeCAD_1.0.2-conda-Linux-x86_64-py311.AppImage
  linux_arm: https://github.com/freecad/freecad/releases/download/1.0.2/FreeCAD_1.0.2-conda-Linux-aarch64-py311.AppImage
---


After more than 20 years of development, the 1.0 release marks a major milestone for the FreeCAD project.

With a strong focus on stability, usability, and long-requested core features, FreeCAD is now more powerful, flexible, extensible, and robust than ever before.


{{< block title="Robust Solid Modeling" >}}

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

// Look all objects in old shape and find modified object in new shape
    for (int i = 1; i <= oldM.Extent(); i++) {
        bool found = false;
        TopTools_ListIteratorOfListOfShape it;
        // Find all new objects modified from old object (e.g. resized face)
        for (it.Initialize(mkShape.Modified(oldM(i))); it.More(); it.Next()) {
            found = true;
            for (int j = 1; j <= newM.Extent();
                 j++) {  // one old object might create several new ones!
                if (newM(j).IsPartner(it.Value())) {
                    shapeMap[i - 1].push_back(j - 1);
                    break;

// Find all new objects generated from old object (e.g. face generated from edge)
        for (it.Initialize(mkShape.Generated(oldM(i))); it.More(); it.Next()) {
            found = true;
            for (int j = 1; j <= newM.Extent(); j++) {
                if (newM(j).IsPartner(it.Value())) {
                    shapeMap[i - 1].push_back(j - 1);
                    break;

// Find all old objects that don't exist anymore (e.g. face completely cut away)
        if (!found) {
            if (mkShape.IsDeleted(oldM(i))) {
                shapeMap[i - 1] = std::vector<int>();
```

{{< /block >}}


{{< block title="Integrated Assembly" >}}

![Exploded View in the Assembly](exploded-view_1-0.webp "Exploded View in the Assembly")

- A brand-new built-in Assembly workbench powered by a modern solver
- Define constraints between parts with improved reliability
- Designed for real-world multi-part engineering workflows

{{< /block >}}


{{< block title="Polished Interface" >}}

- New light and dark themes for better comfort
- Smarter selection tools (filter vertices, edges, faces)
- Rotation center indicator for precise navigation
- Reworked panels, tabs, and preferences dialog
- Faster, cleaner start page

![Side panels overlay](assembly_1-0.webp "Side panels overlay")

{{< /block >}}


{{< block title="Better Tools for Everyday" >}}

![Measurement tool](measurement_1-0.webp "Measurement tool")

- Universal measurement tools available across workbenches
- Improved Sketcher and Part Design workflows
- More consistent behavior across tools

{{< /block >}}


{{< block title="BIM Upgrade" >}}

- A unified Building Information Modeling workbench with Native IFC support
- Better project structure, data handling, and building workflows
- Improved interoperability with other open BIM tools

![BIM workbench](bim_1-0.webp "BIM workbench")

{{< /block >}}


{{< block title="Core Engine and Scripting Power" >}}

- Expressions now support the vector API
- New ==App::VarSet== for managing design variations
- Expanded and cleaner Python API
- Improved Python editor and scripting workflow

{{< /block >}}


{{< block title="Materials and Simulation Improvements" >}}

![FEM workbench](fem_1-0.webp "FEM workbench")

- A new materials system for visual and physical properties
- Many enhancements across FEM and simulation tools

{{< /block >}}


{{< block title="Identity Evolution" >}}

![Refreshed FreeCAD logo chosen by the community](/FreeCAD-symbol.webp "Refreshed FreeCAD logo chosen by the community")

{{< /block >}}


{{< button url="https://wiki.freecad.org/Release_notes_1.0" label="Read the complete release notes" >}}

And so much more, by hundreds of contributors around the world!

**What to be part of this adventure too?** Join the [community](community) and [support](donate) its development.

As always, have fun and keep *FreeCADing*!