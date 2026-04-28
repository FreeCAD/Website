# FreeCAD Website project Tools


This directory contains scripts and utilities used for the FreeCAD website project.
Tools are primarily for content generation, automation, data collection, and reporting tasks related to maintenance and development workflows.
Please see the website repository [ReadMe](https://github.com/FreeCAD/Website?tab=readme-ov-file#readme) for contributions guidelines.


## Included Scripts

### `wip_wednesday.py`

Python3 script to generate a boilerplate WIP Wednesday article based on the activity from the [`FreeCAD/FreeCAD`](https://github.com/FreeCAD/FreeCAD/) repository over the past week.
It classifies Pull Requests (PRs) and issues, and produces a Markdown file with front matter suitable for use in the Hugo website.

**Features:**

- Interactive mode to confirm or adjust the date (defaults to Wednesday 12:00 UTC)
- Class PRs by type for general information: backport, feature, fix, and other by git branch.
- Group PRs by FreeCAD workbenches with commit authors, title and link for each PR.
- Generate `index.md` in the correct `/content/en/news/<YYYY>/<MM>/wip-wednesday-<DD>-<Month>-<YYYY>/` folder.
- Support non-interactive mode and GitHub tokens to increase API rate limits.

**Usage:**

```sh
python3 wip_wednesday.py [optional arguments]
```

**Optional arguments:**

- `--time <timestamp>`: optional date input like ISO 8601 (2026-01-01T12:00:00) or RFC 2822 (Thu, 01 Jan 2026 12:00:00 GMT)
- `--author <name>`: optional article authors field in front matter
- `--root <path>`: optional path to directory of website Hugo project (default: current working dir)
- `--ci`: optional non-interactive mode with automatically most recent Wednesday
- `--token <github_token>`: optional GitHub token or PAT (recommended to avoid rate limits)

**Output Example:**

```sh
Created: website/content/en/news/2026/04/wip-wednesday-01-april-2026/index.md
```

---

### `script.py`