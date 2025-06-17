---
title: 'Coming Soon: FreeCAD 0.21'
date: 2023-04-28
author: Chris Hennes
draft: false
categories: announcement
tags:
- release
cover:
  image:
  caption:
  alt:
---

"[Releasing JAXA's HTV7 cargo vehicle from the ISS](https://www.flickr.com/photos/72482589@N07/45052467584)" by [Astro_Alex](https://www.flickr.com/photos/72482589@N07) is licensed under [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/?ref=openverse).

Last week a group of FreeCAD administrators, maintainers, and developers met to discuss the next release of FreeCAD. We decided to begin the process of creating our next release now. The timing is appropriate because:

1. It has been almost a year since the 0.20, which was released on 13 June 2022, and many new features have been added in the interim.

2. The[ work-in-progress towards merging Realthunder's toponaming](https://github.com/orgs/FreeCAD/projects/2) solution is progressing. It has reached a point where the next portion of code to be merged will start to negatively affect FreeCAD's performance. Ultimately those performance problems will be addressed through optimization, but there will be a period of time when the development version of FreeCAD will have degraded performance.

For these reasons it makes sense to make a new release now, before the potential performance drop, so people have a performant version with recent features to use.

Everybody was expecting the next release to be tagged 1.0, and to have a working solution for toponaming. Since this intermediate release doesn't include a working solution yet, it won't be called "1.0".

Concerning the naming of this release, there were other suggestions, such as naming it version 0.30 or even 0.99. In the end, it seemed best and least confusing to stick with the current scheme until 1.0 is released. This intermediate release will be tagged "0.21".

### Release schedule and tasks

A rough timeline of the release process includes the following major milestones:

1. Release announcement (today). By announcing the release we are notifying all contributors of an imminent "Feature Freeze" in preparation for the release. Any developer with Work In Process ([WIP](https://blog.freecad.org/2023/04/19/wip-wednesday-19-april-2023/)) should strive to prepare a Pull Request. If the work isn't ready to merge, the PR may be left in DRAFT.

2. In approximately two weeks, the maintainers will review the open PR queue. Any open PRs will be tagged either for the 0.21 release or pushed until a later release. Any new PRs received after this review will be tagged for a later release.

3. As soon as all PRs tagged for 0.21 are merged, we will enter a hard freeze period during which only bug fix PRs will be merged.

4. A release candidate will be prepared and we encourage thorough testing and bug reporting. Development effort will focus on resolving critical bugs.

5. When all critical bugs are resolved, a final release will be tagged and released.

Additionally, We have a number of important tasks to perform to make the release happen. A roadmap has been set up at [https://github.com/orgs/FreeCAD/projects/4](https://github.com/orgs/FreeCAD/projects/4). Please contribute there and notify of any issues that you think should be solved for 0.21.

Besides the tasks already in the roadmap above, we'll also need to:

- Translate as much as possible

- Verify that the documentation is more or less up to date for all workbenches

- Produce a windows installer

- Produce a MacOS dmg

- Produce a Linux Appimage

- Migrate the release notes at [https://wiki.freecad.org/Release_notes_1.0](https://wiki.freecad.org/Release_notes_1.0) to 0.21 and verify they are complete

- Produce a release text to be put on the blog and social networks

- Select a splash screen

### Documenting the release

We also want to use this release as an opportunity to document the release process in the [developer handbook](https://freecad.github.io/DevelopersHandbook/) at [https://freecad.github.io/DevelopersHandbook/](https://freecad.github.io/DevelopersHandbook/). This will help future releases be more streamlined. We ask all possible contributions here to help writing this and making FreeCAD releases a more open and trustable process.