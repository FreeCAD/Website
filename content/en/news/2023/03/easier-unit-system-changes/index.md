---
title: Easier Unit System Changes
date: 2023-03-20
author: Chris Hennes
draft: false
category: feature
tags:
  - unit
cover:
  image:
  caption:
---


FreeCAD requires a single unit system to be used throughout the entire program, even if multiple files are open. One of the consequences of that design is that creators who work with multiple unit systems have to switch back and forth between systems regularly. Until now this was quite cumbersome, buried in the Preferences dialog. Thanks to a new menu from developer PaddleStroke, there is now an alternative. With the merge of [PR 8870](https://github.com/freecad/freecad/pull/8870), FreeCAD now has an always-available menu for quickly changing the unit system in use.

![The new unit system menu in FreeCAD 0.21dev](UnitMenu.webp "The new unit system menu in FreeCAD 0.21dev")