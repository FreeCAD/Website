---
title: 'WIP Wednesday: 18 Oct 2023'
date: 2023-10-19
authors: Chris Hennes
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---

This week in FreeCAD development:

- **@yorik** merged the Help Module into main so that an external mod is no longer required to view the new Help system.

- @**[kadet1090](https://github.com/kadet1090)** modified the preference pack code to find the new Overlay stylesheets, and **[MisterMakerNL](https://github.com/MisterMakerNL)** made some Overlay changes to the included stylesheets and preference packs

- **@Paddle** has the new Assembly workbench to a point where it can actually solve some types of assemblies using the new solver. The next step is to add that solver as a submodule to the main FreeCAD repo.

- I (**@chennes**) split off some work to get Qt6 working on Windows under MSVC into its own PR, enabling compilation with the `/fpermissive-` flag.

**PR stats:** In the week from Wednesday, 11 Oct to Wednesday, 18 Oct there were 50 pull requests merged, with a total codebase change of +6,838 / ‑5,159 lines. We had an average merged PR size of +137/ ‑103. We closed 23 Issues, and 27 new Issues were opened.