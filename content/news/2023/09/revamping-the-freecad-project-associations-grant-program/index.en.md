---
title: Revamping the FreeCAD Project Association’s Grant program
date: 2023-09-28
authors: Chris Hennes
draft: false
categories: announcement
tags:
- FPA
- grant
cover:
  image:
  caption:
---

_TL;DR: the FreeCAD Project Association studied best practices of other organizations that have grant programs and is now working towards improving its own program._

In 2022, the FreeCAD Project Association announced a grant program and issued several grants to people actively contributing to the well-being of FreeCAD and its ecosystem: to RealThunder for his work on the toponaming problem mitigation, to Ajinkya Dahale for his work on Sketcher, and to Adrián Insaurralde Avalos for managing FreeCAD releases. Several more grants are in process or are currently being discussed.

However, the organization would like to expand the program and is unsure how to go about it. Here are the key pain points.

**Small payouts.** The FPA doesn't have experience managing grants, thus so far, we've been sticking mostly to "honorary" single-time $1,000 payouts. The organization has a much larger budget than that, but we want to spend money responsibly and with maximum efficiency, so we feel that we need a better plan for managing the program.

**Little interest from the community.** There have been very few proposals for grants coming from the community. The FPA admin board is not sure why that is the case.

**Lack of clarity on program supervision.** On one hand, the FPA would rather issue grants to developers who know their way around FreeCAD code, can come up with a sensible plan, and will execute on it. On the other hand, it's unclear how many potential contributors match that description, plus either way, this would put extra burden on maintainers doing code review.

Thus another grant was issued to Alexandre Prokoudine to study the experience of other organizations that issue grants to free and open-source software developers. The objective was to find answers to the following questions:

- What to do to start increasing engagement?

- How to find talent and bring them to the project?

- If people think this looks too much like work, do we want to change how it looks or do we find devs who don't think like that?

- How do other organizations and applicants structure grants? Too specific or too open in scope? How much specificity to do? Is it like GSoC project ideas?

- Do we do small/medium/large projects?

To do that Alexandre studied what the FPA has done so far with its grant program and how the program was communicated to the FreeCAD community.,He then identified organizations whose experience could be applicable, conducted interviews and studied what they've been doing and why, then summarized main takeaways and came up with a list of actionable recommendations.

[You can read the full report on the research here](https://github.com/FreeCAD/FPA/blob/main/reports/2023_09_27_Prokoudine.md). Let's briefly discuss its key findings.

## **FPA's activity**

So far, most grants have been more like gifts to people who were already doing great work for FreeCAD. There was neither planning, nor budget estimation, and no supervision was done.

All payouts were $1,000 single-time ones, done 100% upfront, no strings attached. Meanwhile the FPA accumulates close to $8K a month and is prepared to spend between $50K and $75K a year on development grants and supervision.

The program communication has been rather scarce so far: very few posts in this blog and on social media, not much discussion on the forum. The [development fund](https://fpa.freecad.org/programs/fpadf-announcement) page has a number of ambiguities that are easy to fix.

Overall, the research finds that the FPA "hesitates to go big on its grant program while having sufficient funds to do so".

## **What other organizations do**

The research focused on QGIS, GRASS GIS, Cesium, Blender, Godot, and Open Toolchain Foundation, with honorary mentions of Google Summer of Code, Krita Foundation, Epic MegaGrants, Python Foundation, NLnet Foundation, and Prototype Fund.

**General approach to acquiring talent.** Most organizations gravitate towards giving grants to developers who have already proven their worth in the community - either by actively contributing as volunteers or by successfully completing a GSoC project.

**Rolling schedule vs batching submissions.** There is a strong bias towards batching proposal submissions and making annual runs of the grant program.

**Project ideas.** Just one organization, GRASS GIS, provides a list of topics for potential grant applicants. Organizations mostly expect applicants to be people with hands-on experience, capable of coming up with a sensible proposal of their own.

**Paperwork.** Proposals are generally expected to have a general project description, expected completion time, timeline/milestones, a list of deliverables, and a budget estimation. Interim reports are encouraged. A final report is commonly expected as the last payout usually depends on it.

**Project supervision.** Organizations mostly expect applicants to be experienced enough to not require much supervision. Except for GRASS, mentorship is not provided except for the usual code review procedures or communication in chat rooms for developers.

**Scope and size of projects.** Organizations typically allow small, medium, and large projects even if it only shows through project descriptions and allocated budgets.

**Payout schedule.** Organizations mostly pay 50% before the project and 50% after successful completion of the project.

**Public communication.** This is one aspect where organizations differ the most. Some actively post about the program on social media and publish announcements and recaps in their respective blogs, others don't even have a single place of entry for people willing to learn more about the program.

One question that the research was unable to answer directly based on studying other organizations was how to increase the amount of grant applications. This is in part due to a relatively small sampling in the study, but also because FreeCAD has very specific challenges. However, Alexandre pointed out that, so far, there hasn't been a lot of public communication about the program. And while this blog posts updates on donations, it's possible that potential applicants are mostly unaware that the FPA does have a substantial budget for grants.

## **What's next**

Based on actionable recommendations provided at the end of the report, Alexandre will design an updated grant program and revamp the approach to public communication about it.

One of the main challenges here is that the FPA is a non-governing body that cannot directly meddle into development affairs. Therefore the FPA is interested to work with a group of active contributors who are willing to spend time reviewing grant applications and doing code review. We've just made [a post about that to the 'Developers corner' section of the forum](https://forum.freecad.org/viewtopic.php?t=81567). If you are interested and you think you qualify, please respond to that post.