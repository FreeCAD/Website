---
title: 'WIP Wednesday: 11 Oct 2023'
date: 2023-10-15
author: Chris Hennes
draft: false
categories: update
tags: []
cover:
  image:
  caption:
  alt:
---

This week in FreeCAD development:

- We merged the **@realthunder **PR that adds a transparency to the sidebars. There is still some work to do with the themes to smooth things out, but the basic feature is present now.

- **@paddle** reports: "I'm making good progress on assembly solving. I connected to OndselSolver correctly and managed to solve for the first time some fixed joints. Some quirks remaining and more work to be done, but we're getting there."

- **@yorik** switched our primary branch's name from master to main, in keeping with the current standard for new primary branches.

- I (**@chennes**) got the new Base64-handling code merged, and am now writing tests for the toponaming-related functions being added to the `PropertyTopoShape` class.

**PR stats:** In the week from Wednesday, 4 Oct to Wednesday, 11 Oct there were 43 pull requests merged, with a total codebase change of +13,855 / ‑1,452 lines. We had an average merged PR size of +322 / ‑34 (though that's a little bit skewed by the [#7888 PR](https://github.com/FreeCAD/FreeCAD/pull/7888), which itself was +11,428/−322). We closed 40 Issues, and 9 new Issues were opened.