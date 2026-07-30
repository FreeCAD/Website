# FreeCAD Website project Tools


This directory contains scripts and utilities used for the FreeCAD website project.
Tools are primarily for content generation, workflows, data collection, and reporting tasks related to maintenance and development.
Please see the website repository [ReadMe](https://github.com/FreeCAD/Website?tab=readme-ov-file#readme) for contributions guidelines.


## Content Scripts

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


## Workflows Scripts

### `addons.py`

Python3 script to fetch and process Addons metadata from the [FreeCAD Addons index](https://github.com/FreeCAD/Addons) repository, produce a JSON data file suitable for use in the Hugo website, and cache the results to avoid redundant processing.

**Features:**

- Download Addons cache ZIP with ETag to avoid unnecessary requests
- Extract Addons JSON from downloaded ZIP archive
- Fetch download statistics from FreeCAD Addons Matomo instance
- Normalize Addon metadata from package XML
- Write cleaned JSON to `data/addons.json`
- Use SHA256 hashing to detect changes and skip processing when data is unchanged

**Usage:**

```sh
python3 addons.py
```

**Output Example:**

```json
{
  "SomeAddon": [
    {
      "repository": "https://github.com/FreeCAD/SomeAddon",
      "git_ref": "main",
      "total_downloads": 1234,
      "last_update_time": "2026-01-01T12:00:00Z",
      "metadata": {
        "name": "SomeAddon",
        "description": "A sample FreeCAD addon",
        "version": "1.2.3",
        "maintainer": "abcd",
        "license": "LGPL-2",
        "icon": "https://example.com/icon.svg"
      },
      "curated": true
    }
  ]
}
```

---

### `telemetry.py`

Python3 script to fetch and process Telemetry data provided from the optional [FreeCAD Telemetry addon](https://github.com/FreeCAD/FreeCAD-Telemetry), produce a JSON data file suitable for use in the Hugo website, and cache the results to avoid redundant processing.

**Features:**

- Fetch remote JSON telemetry data
- Detect changes via SHA256 hash and skip processing if data has not changed
- Extract most common `totalUsers` value from all telemetry metrics
- Log invalid or inconsistent keys in the dataset
- Transform telemetry data into structured dictionary with `labels` and `data` key-value pairs and `total_users` field
- Write cleaned JSON to `data/telemetry.json`
- Store hash of last fetched telemetry

**Usage:**

```sh
python3 telemetry.py
```

**Output Example:**

```json
{
  "versions": {
    "1.2.3": 123,
    "2.4.6": 456
  },
  "total_users": 7890
}
```

---

### `deploy-website.sh`

Bash script for server-side deployment of the website on the FreeCAD staging or production server.

The copy stored here in this git repository is for reference and version tracking.
The deployed server copy must be updated manually by an admin.

**Features:**

* Prevent concurrent deployments using file lock, no `root` run
* Fetch and hard-reset to pinned remote branch (`origin/main`)
* Build website with Hugo using temporary output dir
* Atomically swap new built site into place after successful build
* Preserve previous deployment as `public.old`
* Cleanup temporary files
* Log deployment progress and deployed Git revision

**Output Example:**

```
2026-07-30T12:34:56Z deploy-website: fetching origin/main
2026-07-30T12:34:57Z deploy-website: building main at 0123456789abcdef...
2026-07-30T12:35:01Z deploy-website: deployed main at 0123456789abcdef...
```

---

### `script.py`