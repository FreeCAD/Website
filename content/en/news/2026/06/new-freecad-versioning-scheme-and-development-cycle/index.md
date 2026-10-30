---
title: New FreeCAD versioning scheme and development cycle
date: 2026-06-26
author: prokoudine
draft: false
category: announcement
tags:
  - release
cover:
  image:
  caption:
---


FreeCAD is switching to the CalVer scheme for versioning releases and a new development cycle that introduces time-based releases. Here is a quick explainer on why the team is doing that and how this will affect users.

## Why the switch?

There are multiple issues with the current development cycle, such as an unpredictable, irregular release schedule, as well as major updates being too far apart, which encourages users to rely on less stable weekly builds. The scheduled branching for releases should aid with that, and the CalVer scheme is being introduced to support the new release schedule.

In other words, users should expect more release predictability and have fewer reasons to use unstable builds, unless they need to test fixes for bugs they reported or new features they requested.

If you are interested in the developers' perspective, please see [this forum announcement](https://forum.freecad.org/viewtopic.php?p=894794).

## What is a CalVer scheme?

The two most common ways to version a software release are semantic versioning, or SemVer for short, and calendar versioning, or CalVer.

FreeCAD used to rely on a form of semantic versioning with releases like 1.0 and 1.1 representing major updates and releases like 0.21.2 or 1.1.1 representing updates with bugfixes (patch releases).

Calendar versioning schemes typically contain the number of the year and then either the sequential number of the release within a year or the month of the release. The particular CalVer format we are switching to is YY.N, where YY is the two-digit year of the January quality-focused release, and N is the sequential release number within that year (1, 2, or 3).

The next major releases will be 26.3, 27.1, 27.2, and 27.3. Patch releases will follow the YY.N.P format, e.g., 27.1.1.

## What's the new development cycle?

We settled on three major releases per year as a compromise between sufficient frequency of releases and having enough time to make quality releases.

The releases within each year will have a slightly different focus.

YY.1 release, branched on January 31, will be quality-focused. This means the team will prioritize bugfixes over new features.

YY.2 and YY.3 releases, branched on May 31 and September 30, respectively, will be more like regular FreeCAD releases you already know, with a more or less equal share of new features and fixes.

The accepted proposal also covers topics like feature freezes, the stabilization period, release candidate scheduling, and more. You can read the proposal [on GitHub](https://github.com/FreeCAD/FreeCAD-Enhancement-Proposals/blob/master/FEPs/FEP-0003-release-schedule/README.md).

## How the plan was discussed

Jackson Oursland and Kacper Donat made the proposal and discussed it with the broader community of developers on GitHub and during the bi-monthly dev calls. After the discussions and some fleshing out, the community voted to accept it.

## When is the first CalVer release?

The first release under this new scheme will be 26.3. We will create a branch for it on 30 September 2026. Releases are expected to ship within 4-6 weeks after branching, with 2-3 release candidates.

The development builds are already versioned as 26.3dev.
