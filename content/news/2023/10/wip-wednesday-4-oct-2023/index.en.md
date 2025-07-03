---
title: 'WIP Wednesday: 4 Oct 2023'
date: 2023-10-05
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

- **@obelisk79** is spearheading the formation of a UI/UX working group -- more details coming soon! If you are interested in participating, consider joining the [FreeCAD Discord](https://discord.gg/w2cTKGzccC) and checking out the #ui-ux-themes channel.

- **@yorik** is preparing the help module to become builtin

- **@kadet** is working on the implementation of preferences navigation redesign ([https://github.com/FreeCAD/FreeCAD/issues/10886](https://github.com/FreeCAD/FreeCAD/issues/10886)), and then probably going back to thin walls support ([https://github.com/FreeCAD/FreeCAD/issues/10538](https://github.com/FreeCAD/FreeCAD/issues/10538))

- **@paddle** is working on sketcher tool settings initial implementation + offset : [https://github.com/FreeCAD/FreeCAD/pull/10892](https://github.com/FreeCAD/FreeCAD/pull/10892)
And assembly wb : [https://github.com/FreeCAD/FreeCAD/pull/10764](https://github.com/FreeCAD/FreeCAD/pull/10764)

- **@andrecaldas** is developing "thread safe containers":[ https://github.com/andre-caldas/FreeCAD ... /README.md](https://github.com/andre-caldas/FreeCAD/blob/SmartPointerDocumentObject/src/Base/Threads/README.md)

- **@DavesRocketShop** is making progress on material arrays. 2D and 3D arrays can be edited, saved, and restored. Still some UI issues to fix before it is considered complete.

- I (**@chennes**) put the finishing touches on the next Toponaming PR (related to storing binary data in our XML files), and am now moving on to actually calculating and storing names for the TopoShape class.

**PR stats:** In the week from Wednesday, 27 Sept to Wednesday, 4 Oct there were 43 pull requests merged, with a total codebase change of +12,993 / ‑4,451 lines. Not counting translation updates we had an average merged PR size of +302 / ‑104. We closed 17 Issues, and 34 new Issues were opened (though many of those are related to implementing the new Materials system, so don't represent bugs, _per se_).