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

For PRs that are larger and consist of multiple commits and are larger of size, see the [Rebasing](#rebasing) section.


## PR Review Process

Maintainers review PRs on a rolling basis throughout the week, and also in a more concentrated review meeting on Mondays
(see the [FreeCAD Events Calendar](https://freecad.org/events.php) for the exact date and time in your timezone). When reviewing,
Maintainers strive to uphold the tenets of the [CONTRIBUTING](https://github.com/freecad/freecad/blob/main/CONTRIBUTING.md)
document. These meetings are open to the public and all developers are welcome to attend: particularly if you have a PR under review,
you may be able to accelerate that process by being present to address and questions or concerns that arise. You can also participate
in the process by reviewing PRs yourself. Although only Maintainers may merge PRs, anyone is welcome to test and provide feedback, and
Maintainers take that feedback into consideration when evaluating PRs. Any time you can contribute to the project is appreciated!

To expedite the PR review process, consider the following guidelines:

1. If your PR is still a work-in-progress, please mark it as a "Draft" so that Maintainers don't spend time reviewing something that is not yet ready to be merged.
2. If you get a question on your PR, it is unlikely to be merged until you respond to that question (particularly if the question is from a Maintainer).
3. The PR review meeting proceeds by going linearly through a [manually curated list of ready-to-review PRs](https://github.com/orgs/FreeCAD/projects/40): the goal is that no under-review PR ever sits for more than a week without action.
4. Adding automated tests (in Python or C++) can greatly expedite the review process by providing a clear demonstration of how the new code works and what problem it solves.
5. A good description in your PR's submission text helps Maintainers determine who is best suited to evaluate a PR, and prevents wasting time sorting through the code itself to figure out who should be looking at it.
6. FreeCAD's Maintainer team is currently quite small, and sometimes the Maintainer responsible for a certain part of the code is unable to attend the review meeting: this sometimes unavoidably delays the merge process through no fault of the submitter. We ask for your patience as we work to grow our team.
7. It helps the merge process if you can ensure you have a clean commit history in your PR, squashing any intermediate work and only retaining separate commits for logically separate parts of the PR and not merging the main branch into your branch PR (in most cases, we hope that this is only a single commit, see [Rebasing](#rebasing) for more information).


## Rebasing

The PR queue of FreeCAD can become quite lengthy.  This may mean that it takes some time for reviewers to get to review and merge your PR.  This can be frustrating especially for the larger PRs that consist of multiple commits because after some time those PR can become outdated because of other smaller PR that have been merged.

In this section, we give some do's and don'ts for rebasing and to make sure your work can remain up-to-date without much effort.

### Do's

1. **Small PRs:** Smaller PRs are much easier to rebase.
2. **Clean commit history**: A clean and logical commit history not only helps the review process (as mentioned above), it also helps rebasing where the rebase maintains the logic.
3. **Amend the logical commits**: When rebasing, amend the logical commits updating them in such a way as if they were originally written on the updated main branch.  The benefit is that if you need to do a new rebase, you only need to solve the new conflicts and not the old ones again (see don'ts 1 and 2).

```
*  (main) Core: Update feature 1
*  Gui: Improve the 3D view
*  Sketcher: Update the solver
| *  (my-pr) Test: Add a test for MyModule
| *  Gui: Add Gui support for MyModule
| *  MyModule: Add the new feature
| *  Core: Add support for a new MyModule feature
|/
*  PartDesign: Fix bug #23
*  ...
```

A rebase should give this:

```
*  (my-pr) Test: Add a test for MyModule
*  Gui: Add Gui support for MyModule
*  MyModule: Add the new feature
*  Core: Add support for a new MyModule feature
*  (main) Core: Update feature 1
*  Gui: Improve the 3D view
*  Sketcher: Update the solver
*  PartDesign: Fix bug #23
*  ...
```

In this example, all conflicts are resolved and stored in the original logical commits with amends to those commits.  It is as if the PR has been based on the new main.  The command to use is: `git rebase -i` (interactive).

### Don'ts

1. **Merge main into your PR branch**: This effectively adds a new (merge) commit that captures an update to your PR given changed circumstances.  This does not follow rule 2. "Clean commit history" because it is not a "logical" commit.  The merge commit has nothing to do with your work, but has only to do with changed circumstances.  This means that if you need to rebase the PR on top of main, you need to replay all those commits onto main.  This effectively means that you are rebasing your work multiple times.
2. **Create commits to update to a new main branch**: This follows the same reasoning as above.  It is not a logical commit belonging to the work, which means that each time you need to do a rebase, you need to solve conflicts again and again for the earlier commits.

The following git history for `my-pr` is not a clean, logical history:

```
*  (main) Core: Update feature 1
*  Gui: Improve the 3D view
*  Sketcher: Update the solver
| *  (my-pr) Fix the test
| *  Test MyModule
| *  Make the Gui really work
| *  Make the Gui work
| *  Fix issue in core
| *  MyModule: Add the new feature
|/
*  PartDesign: Fix bug #23
*  ...
```

Adapting to the new `main` branch should not look like this:

```
*  (my-pr) Fix for the rebase
*    Merge branch 'main' into my-pr
|\
| *  (main) Core: Update feature 1
| *  Gui: Improve the 3D view
| *  Sketcher: Update the solver
* |  Fix the test
* |  Test myModule
* |  Make the Gui really work
* |  Make the Gui work
* |  Fix issue in core
* |  MyModule: Add the new feature
|/
*  PartDesign: Fix bug #23
```

If you would now rebase `my-pr` onto `main`, you would need to solve all conflicts again that are stored into commits "Merge branch 'main' into my-pr" and "Fix for the rebase" because all the commits of `my-pr` are still based on "PartDesign: Fix bug #23".  So, having a commit history like this can lead to much double work in making your PR up-to-date with a newly updated main branch.
