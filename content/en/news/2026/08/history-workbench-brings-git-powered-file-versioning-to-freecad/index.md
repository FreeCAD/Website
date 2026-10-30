---
title: History Workbench brings Git powered File Versioning to FreeCAD
date: 2026-08-28
author: concretedog
draft: false
category: showcase
tags:
  - addon
cover:
  image:
  caption:
---


{{< youtube id=VZJsxJS-CTQ title="FreeCAD North American Meetup 2026 - Version Control for Beginners" loading=lazy >}}

We recently posted [Chris Hennes excellent talk at the FreeCAD](/news/freecad-26-3-top-20-new-features-talk/) North American meetup 2026 which is well worth checking out to see a snapshot of upcoming developments at FreeCAD. The above video is another talk from that day from Ephi who has developed the excellent [History Workbench](https://github.com/eblanshey/HistoryWorkbench).

This workbench is a way to add file versioning to your locally stored FreeCAD project folder to allow you to keep a history of all the changes to your project over time. It also enables you to roll back changes if needed when a change creates an issue.

It's runs using [Git](https://git-scm.com/), the most popular file versioning tool on the planet, but instead of having to learn a lot of terminal commands, all the Git functionality is broken out to the FreeCAD GUI. Interestingly the Ephi has also adapted the language used to make the Git functionality more approachable for those less familiar. However if you are a Git user don't worry the git terms, diff, staging, commit etc are all there as well.

The video is well worth a watch, not only for the excellent way this has been implemented in FreeCAD, but it's also a good primer for how file versioning can work in hardware project.
