---
title: Upcoming Feature freeze and UI freeze for FreeCAD 1.0
date: 2024-05-15
author: Aleksandr Prokudin
draft: false
categories: announcement
tags:
- roadmap
- release
cover:
  image:
  caption:
  alt:
---

During the planned online developers meeting today, we agreed on the following plan towards FreeCAD 1.0.

The development branch will enter **feature freeze on June 3**, at the PR merge meeting. Here is what it means to contributors:

- Are you working on patches that add new features or improvements? Are you shooting for inclusion of your patch in v1.0? Please submit your pull request for review by the time the meeting starts on June 3, preferably, a week ahead of that to have the time to respond to review and fix code.

- Do you already have a pull request with a draft status and you want your change to be part of v1.0? Please complete your work and remove the draft status in time for the meeting on June 3.

- Do you already have an open pull request that is not in the draft status? You are good to go. It will be reviewed for inclusion to v1.0.

After that, the development branch will enter **UI freeze on June 24**. This means that no user-visible messages are allowed to change until the release is out. This should help both translators and people writing documentation alike.

Based on what we see on Crowdin, three weeks should be sufficient for many translations to be updated. However, we don't expect any major UI changes between now and the UI freeze, so translators should feel relatively safe to start working now.

While much depends on how many major and critical bugs we have to fix, we hope to have v1.0 ready in time for the [FreeCAD 2024 North American Meeting](https://forum.freecad.org/viewtopic.php?style=5&p=751341#p751341) in Springfield, IL in mid-August. For the forum discussion, please [see here](https://forum.freecad.org/viewtopic.php?p=759605#p759605).