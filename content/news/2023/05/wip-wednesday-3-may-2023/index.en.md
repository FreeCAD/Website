---
title: 'WIP Wednesday: 3 May 2023'
date: 2023-05-03
author: Chris Hennes
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

It was a relatively quiet week for FreeCAD developers, with only 32 merged pull requests, mostly related to small translation problems and minor bugfixes (though one of the fixed bugs prevented Windows builds from starting if the splashscreen was disabled, so I'm sure there are going to be some happy Windows users out there!). We also finally removed the Raytracing workbench from the repository: it has long since been superseded by the Render addon and had not been maintained for many years.

In this upcoming week:

- @wandererfan is investigating placement anomalies with Link sources, and the replacement of BaseGeom (with @benj5378).

- I (@chennes) am working on streamlining the translation update process, and cleaning up whatever bugs our translators throw at me this week.

**PR stats:** In the week from Tuesday, 25 Apr to Tuesday, 2 May there were 32 pull requests merged, with a total codebase change of +1,003 / ‑31,619 lines (not counting translation changes, but counting the removal of Raytracing). That's an average merged PR size of +31 / ‑1019. Yeah, the removal of an entire 30k-line workbench might throw those stats off this week...