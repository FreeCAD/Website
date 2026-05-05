---
title: Release Process
description: High-level overview of the release planning and management process.
weight: 13
---


We recognize significant wisdom in the philosophy to ["Release Early and Release Often"](https://en.wikipedia.org/wiki/Release_early,_release_often). However, releases can require significant coordinated work within the community.  FreeCAD aspires to produce a major release every 3-6 months. In order to meet this goal, we will work to make releases more predicatable and automated.


## Major and Minor Releases

A major release introduces new features and introduces key improvements.  Major releases may also introduce breaking changes that invalidate documentation or change existing APIs. They may also deprecate older functionality.

Between major releases, bugs are occasionally found and repaired. These fixes may be urgent enough or isolated enough that applying them incrementally to the existing 'stable' version is both possible and desirable.  A set of such changes may be grouped together and released as a 'minor' version.

Major and minor releases have slightly different processes.


## Major Releases

Each major release goes through the following milestones and stages:

### Announcement Preparation

A release may be triggered for several reasons.
- An event or dependency in the development roadmap may require a release.
- There may be a desire to have a major release included in a major platform release like the next version of Ubuntu.
- Or it may be that a significant set of features has matured to the point that they are ready for general usage.

Whatever the reason, the first step in the determination by the maintainers that a release is needed.

The maintainers will create a Github project to track the release.
The maintainers will schedule a meeting to review outstanding Pull Requests.

### Announcement milestone

Next, the maintainers will make a formal announcment on the forum. The announcement will layout the expected timeline for the release and call for final submissions.  The announcment should be further communicated through official and unofficial channels like Twitter and Reddit.

### Final Feature Submission Stage

The purpose of the announcment is to let contributors know that a feature freeze is imminent. Any work in process should be finalized and a Pull Request submitted.

At this point, a PR may not be ready to merge and can be marked as _draft_.  Creating the PR makes the maintainer community aware of pending changes that the contributor would like to have considered for the release. The maintainers will allow time (typically 1-2 weeks) for Pull Requests to be submitted.

The announcment should include a date for the PR Review meeting.

The announcment should also announce a splash-screen contest and provide a forum thread for submissions.

### PR Review Milestone

After the Submission Stage is closed, the maintainers will review all outstanding Pull Requests. For each one, they will determine if the feature is sufficiently mature to include in the release. Specifically they will consider:

- How significant is the feature
- How likely is the feature to negatively impact user workflow
- How well documented is the new feature
- How much additional testing and stabilization is likely required

Maintainers will strive to include as many mature features as possible while minimizing the time needed to resolve bugs, complete documentation, and stabilize the release.

Each PR will be tagged with the current release if it is to be included.

Following the PR Review, any new feature Pull Requests will be held for a later version.  Contributors should adjust their expectations about code reviews.

### PR Merge Phase

During this phase, development focus will turn towards merging the remaining tagged outstanding PRs.
After the PR Merge phase, only bug-fix PRs will be merged.

### Release Candidates

After all outstanding PRs are merged and all critical bugs are resolved, a Release Candidate (RC) version will be created and a public announcment made.  This is a request to the community for intentional and deliberate testing with the goal of uncovering as many bugs as possible. This is the point at which the formal branch is created for the releases. First, create a branch called "releases/FreeCAD-X-Y" where X and Y are the major and minor release numbers. Next use the GitHub "Draft new release" button on the Releases page to create a new release. Set it up to create a new tag with the release number in it, e.g. "0.21rc1" and ensure that the release is based on the "releases/FreeCAD-X-Y" branch. Mark the release as a "pre-release" so that it does not display as the latest version. Attach all of the necessary installers, appimages, packages, etc. to this release. Note that the release can be edited after creation, so assets can be added as they become available.

Translation files will be pushed to CrowdIn and a public call for translation assistance should be made.

Release notes should be reviewed at this point and any ommisions corrected.

Any problems identified with the release candidate should be addressed via PRs made to the release branch. If necessary, multiple release candidates may be tagged using the same "Draft new release" process described above, and incrementing the release candidate number.

### Final Release

- The result of the splash screen contest is announced and the new splash screen is added to the source, if that was not done in earlier stages.
- Update all versions in a number of source code locations where they are not automatically generated:
    - README
    - CMakeLists.txt
- Manually tag the release on the appropriate branch using semantic versioning for the tag name, e.g. "1.2.3". Launch the various build-creation tasks based on this tag.
    - Conda builds for all platforms
    - Manual compilation of a Windows LibPack-based binary and NSIS-created installer
    - Sign and notarize the Mac OS Conda builds once they are complete (See [Code signing](../signing))
    - (Future work) Sign the Windows builds
- Create a new release on GitHub, this time marking the "Set as latest release" box and not marking it as a pre-release, and setting the release to use the tag created above. It's best to ensure all assets are attached prior to publication of the final release, so save the release as a draft as necessary until all builds are completed. The release contains a release announcement text that should be appropriate for the general user audience (not targeted at developers).
- Prepare a packager's release files and alert the packagers.
- Update the website [downloads page](https://www.freecad.org/downloads.php) to point to the new files
- Update the website [features page](https://www.freecad.org/features.php) to point to the new release notes
- Update the stable branch of the [Snap package](https://github.com/freecad/freecad-snap) to the new version number by editing snap/snapcraft.yaml

### Release Announcement

Once all release files are in place, a release announcement should be posted to all "official" FreeCAD channels:

- FreeCAD News (https://blog.freecad.org)
- The FreeCAD Forum (https://forum.freecad.org)
- Facebook
- X
- Mastodon (automatic from the blog post)
- Discord
- LinkedIn

There are also other active communities where FreeCAD does not maintain any sort of official presence, but where nevertheless users are likely to benefit from an announcement:

- Social medias
- TBD


## Minor Releases

Between major releases, bugs are occasionally found and repaired. These fixes may be urgent enough or isolated enough that applying them incrementally to the existing ‘stable’ version is both possible and desirable. A set of such changes may be grouped together and released as a ‘minor’ version.

Usually these fixes have already been applied to the development branch.  The process of applying them to the previous stable version is called 'backporting'

Each minor release goes through the following stages:

### Creation of Release Milestone

The need for a minor release is triggered by a PR or commit which is deemed worth backporting to the stable version.  The consideration is based on a couple factors

- Does the bug result in the loss of data under normal circumstances?
- Does the bug expose user data or present the possibility of user data being
  exposed?
- Does the bug create a significant inconvenience for the user?

When a PR or commit is found worth backporting, a maintainer will create a new issue. The issue should have suitable title like  [BACKPORT REQUEST] <some description>

The issue should link to the PR in question.

The issue should be labeled with a Milestone label for the next minor release.  If the milestone label doesn't exist, the maintainer will create it.

### Create a backport PR

A maintainer will create a new PR targeting the stable branch.  The relevant commits can be cherry-picked and added to the new PR.

The backport PR will go through the same process as any other PR.

### Creating the Minor version release

Minor bugs may be gathered together for a period of days or weeks to batch them together. A significant bug or one that risks user data may require an expedited release.

When the determination is made to proceed with the release, the following things happen:
