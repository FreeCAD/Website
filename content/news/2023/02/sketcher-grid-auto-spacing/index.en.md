---
title: Sketcher Grid Auto-Spacing
date: 2023-02-27
authors: Chris Hennes
draft: false
categories: feature
tags:
- sketcher
cover:
  image:
  caption:
---

This week saw the merge of a long-awaited Sketcher feature that has been in progress by a team of developers for several months: the Sketcher Workbench now features a massively-refactored grid view that includes automatic-resizing when you zoom in and out, with a refined user interface for turning it on and off and changing the scaling parameters.

Since late last year developers @[PaddleStroke](https://github.com/PaddleStroke), @[abdullahtahiriyo](https://github.com/abdullahtahiriyo), and @[0penBrain](https://github.com/0penBrain) have been working together to polish up a pull request from @PaddleStroke: the final product is a change that touches over 10,000 lines of code spread over 36 files. The under-the-hood changes should help to make the Sketcher code base more maintainable and flexible, and the automatic rescaling of the grid makes the user experience much more pleasant.

Congratulations to the Sketcher team for this excellent improvement!