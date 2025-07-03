---
title: 'WIP Wednesday: 29 Mar 2023'
date: 2023-03-29
author: Chris Hennes
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
  alt:
---

This past week saw the removal of the old Image workbench and the[ integration of its functionality into the core of FreeCAD](https://github.com/FreeCAD/FreeCAD/pull/8955), the merge of a significant [usability improvement to fillets and chamfers](https://github.com/FreeCAD/FreeCAD/pull/8990) in the Part Design workbench, the merge of the [last of the Topological Naming Problem mitigation Stage 1 PRs](https://github.com/FreeCAD/FreeCAD/pull/8974), and the consolidation of some [Workbench-related options into the Workbenches preference pane](https://github.com/FreeCAD/FreeCAD/pull/9026).

In this upcoming week:

- From @yorik: "Lots going on in NativeIFC for me: I'm looking at using ifcopenshell to perform HLR rendering, and started integrating NativeIFC and BIM addons."

- @wandererfan is beginning phase 2 of Dimension reference TNP mitigation.

- @wwmayer reports: "I will finish the last step of the Qt6 port of the TechDraw module. Since QtXmlPatterns has been dropped in Qt6 the only true alternative would be to add some other fat library based on Xerces like xalan or xqilla if we wanted to have true XQuery/XPath support. But since this is like using a sledgehammer to crack a nut I decided to implement an algorithm that traverses the DOM document and collects the required elements directly."

- I (@chennes) am getting closer to merging the Addon Manager's big data-source refactor, but the actual merge is still at least several weeks away. I'll continue to merge the small pieces of it that can be split off without breaking anything.

**PR stats:** In the week from Tuesday, 21 Mar to Tuesday, 28 Mar there were 113 pull requests merged, with a total codebase change of +17,627 / ‑33,614 lines (not counting translation changes). That's an average merged PR size of +156 / ‑297.