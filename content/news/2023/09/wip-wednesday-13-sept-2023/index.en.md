---
title: 'WIP Wednesday: 13 Sept 2023'
date: 2023-09-13
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

This week in FreeCAD development:

- **@PaddleStroke** is working on an assembly constraining system. He posted a draft PR to share advancement if anyone wants to follow along: [https://github.com/FreeCAD/FreeCAD/pull/10611](https://github.com/FreeCAD/FreeCAD/pull/10611).

- **@yorik** is working on NativeIFC, trying to make the FreeCAD document a 1:1 alter ego of an IFC document.

- **@kaktus** is continuing to clean up Crowdin: This time strings from FreeCAD's home page are under the microscope. The subject of the research is unnecessary end-of-line characters in strings to be translated.

- **@wandererfan** is wrapping up Part Scale implementation, working on Google Summer of Code UMF testing, and working on the cosmetic circle command.

- I (**@chennes**) am starting in on the next phase of the [Topological Naming Problem mitigation project](https://github.com/orgs/FreeCAD/projects/2).

**PR stats:** In the week from Wednesday, 6 Sept to Wednesday, 13 Sept there were 55 pull requests merged, with a total codebase change of +44,100 / ‑33,089 lines (not counting translation changes). That's an average merged PR size of +817 / ‑613 (this is a little misleading because several of these PRs were large-scale code reformatting actions, not actual code changes). We closed 16 Issues, and 26 new Issues were opened.