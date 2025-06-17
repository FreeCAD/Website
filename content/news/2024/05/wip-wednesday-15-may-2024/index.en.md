---
title: 'WIP Wednesday: 15 May 2024'
date: 2024-05-15
author: Aleksandr Prokudin
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

**Toponaming**: bgsbww added missing bits of toponaming code to core, Part Design, and Sketcher.

**Measure tools** got some really useful updates. hlorus made some improvements to the new unified measurement facility and added measurement values to labels in the project tree. Meanwhile wwmayer rewrote parts of the new Quick Measure feature and fixed errors typically popping up when selecting geometry in Sketcher.

**Materials** got more attention. davesrocketshop updated the material preferences to allow selecting a default material. Roy-043 started adapting Draft for the new materials system. The first patch adds new material handling to setting style: the task panel now has a tabbed interface to accommodate for new properties, and the properties on the Annotation tab have been reordered to match the related Preferences page.

**TechDraw** now features a smart dimension tool similar to that of Sketcher, thanks to PaddleStroke. You can use one tool to add dimension to different types of geometry. You can also choose whether you want all dimension tools grouped or next to each other in the toolbar.

**UI cleanup**: marcuspollio made slight adjustments to some Draft WB icons for better consistency, maxwxyz updated icons in the Addon Manager for legibility on dark themes, MisterMakerNL recreated expand/collapse icons for the Tasks panel in SVG, and kadet1090 moved the 'More' button to the end of the workbench selector TabBar.

Among other changes:

- oursland contributed improvements to Conda builds.

- Roy-043 added a "Legacy importer only" option to DXF importing to fix a bug where the C++ importer would ignore the "Create as" import settings and always creates simple Part shapes

- Bug fixes from wwmayer, ronnystandtke, FlachyJoe, ppphp, realthunder, jwueller, pieterhijma, NewJoker.

**PR stats**: In the week from Wednesday, 8 May to Wednesday, 15 May there were 39 pull requests merged. 34 new pull requests were opened.

**Issue stats**: we closed 29 issues, and 61 new issues were opened. Overall, 1,605 issues are currently open.