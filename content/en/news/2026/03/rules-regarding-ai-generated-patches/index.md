---
title: Rules regarding AI-generated patches
date: 2026-03-16
authors: Aleksandr Prokudin
draft: false
categories: announcement
tags:
  - code
  - AI
cover:
  image:
  caption:
---


Big and small free/open-source projects have been facing an avalanche of AI-generated patches lately. Some patches are more or less OK, others have convoluted, badly designed code. The net effect is that code review becomes more difficult, to the point where numerous projects give up and introduce some form of protection against AI slop.

The team started with a [discussion on GitHub](https://github.com/FreeCAD/FreeCAD/pull/24126) and had a further conversation at a [recent bi-weekly dev call](https://github.com/FreeCAD/FreeCAD-developer-meetings/blob/main/Minutes/minutes-2025-12-20.md). Following that, Reqrefusion updated the contribution guidelines to include two new clauses around AI-generated code. Here they are:

- Contributions must meet existing quality standards. Raw AI output is not accepted under any circumstances. AI may be used only as an assistive tool; in all cases, the resulting content must be reviewed, validated, and justifiable by the contributor. The contributor should be able to explain design and code decisions, answer reviewers' questions, and ensure that AI use does not waste reviewers' time during review. That being said, the use of AI is not recommended under any circumstances or in any manner.
- The contributor provides reasonable assurance that the contribution does not infringe third-party copyrights or license terms.

All pull requests must meet these requirements.