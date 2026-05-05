---
title: Contribution workflow and process
description: FreeCAD contribution workflow and process.
weight: 2
---


## Submitting a PR

The basic process is:

1. Write some code (and possibly some unit tests)

2. `git add file1.cpp file2.cpp`

3. `git commit -m "Sketcher: Fixed bug in constraints" -m "Added foo to bar. Fixes #1234."`

  - When running `git commit` our pre-commit hooks will run to check your code. If the scripts had to make changes, you will have to `git add` the changed files and run `git commit` again.

4. `git push` to send your changes to GitHub

5. Visit https://github.com/freecad/freecad -- at the top of the screen you should see a yellow banner suggesting you create a Pull Request. Follow the instructions on the site to get the process started.


## PR Review Process

Maintainers review PRs on a rolling basis throughout the week, and also in a more concentrated review meeting on Mondays
(see the [FreeCAD Events Calendar](https://freecad.org/events.php) for the exact date and time in your timezone). When reviewing,
Maintainers strive to uphold the tenets of the [CONTRIBUTING](https://github.com/freecad/freecad/blob/main/CONTRIBUTING.md)
document. These meetings are open to the public and all developers are welcome to attend: particularly if you have a PR under review,
you may be able to accelerate that process by being present to address and questions or concerns that arise. You can also participate
in the process by reviewing PRs yourself. Although only Maintainers may merge PRs, anyone is welcome to test and provide feedback, and
Maintainers take that feedback into consideration when evaluating PRs. Any time you can contribute to the project is appreciated!

To expedite the PR review process, consider the following guidelines:

1) If your PR is still a work-in-progress, please mark it as a "Draft" so that Maintainers don't spend time reviewing something that is not yet ready to be merged.

2) If you get a question on your PR, it is unlikely to be merged until you respond to that question (particularly if the question is from a Maintainer).

3) The PR review meeting proceeds by going linearly through a list of ready-to-review PRs sorted by least-recently-updated: the goal is that no under-review PR ever sits for more than a week without action.

4) Adding automated tests (in Python or C++) can greatly expedite the review process by providing clear demonstration of how the new code works, and what problem it solves.

5) A good description in your PRs submission text helps Maintainers determine who is best suited to evaluate a PR, and prevents wasting time sorting through the code itself to figure out who should be looking at it.

6) FreeCAD's Maintainer team is currently quite small, and sometimes the Maintainer responsible for a certain part of the code is unable to attend the review meeting: this sometimes unavoidably delays the merge process through no fault of the submitter. We ask for your patience as we work to grow our team.

7) It helps the merge process if you can ensure you have a clean commit history in your PR, squashing any intermediate work and only retaining separate commits for logically separate parts of the PR (in most cases we hope that this is only a single commit).
