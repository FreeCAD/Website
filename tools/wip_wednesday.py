import argparse
import requests
import time
from collections import defaultdict
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, DefaultDict


GITHUB_REPO = "FreeCAD/FreeCAD"
GITHUB_API = "https://api.github.com"
GITHUB_API_SLEEP = 0.05

WORKBENCH_ORDER = [
    "Gui",
    "Core",
    "Sketcher",
    "Draft",
    "Part",
    "PartDesign",
    "Assembly",
    "TechDraw",
    "BIM",
    "CAM",
    "FEM",
    "Measure",
    "Mesh",
    "Material",
    "Spreadsheet",
    "Surface",
]


def warn(text: str) -> str:
    """Return text colored red for warnings."""
    return f"\033[31m{text}\033[0m"


def bold(text: str) -> str:
    """Return text in bold blue."""
    return f"\033[1;34m{text}\033[0m"


def parse_time(timestr: str) -> datetime:
    """
    Parse time string in ISO 8601 (2026-01-01T01:23:45+00:00)
    or RFC 2822 (Thu, 01 Jan 2026 01:23:45 GMT) format.
    """

    original = timestr
    if timestr.endswith("Z"):
        timestr = timestr[:-1] + "+00:00"

    try:
        dt = datetime.fromisoformat(timestr)
    except ValueError:
        try:
            dt = parsedate_to_datetime(timestr)
        except Exception:
            raise SystemExit(f"{warn('⚠️ Error:')} Unsupported time format: {original}")

    if dt.tzinfo is not None:
        dt = dt.astimezone().replace(tzinfo=None)

    return dt


def is_wednesday(dt: datetime) -> bool:
    return dt.weekday() == 2  # Monday=0, Wednesday=2


def previous_wednesday(
    dt: datetime, set_time: tuple[int, int, int] | None = None
) -> datetime:
    """Return the most recent Wednesday with optional time (hour, minute, second)."""

    days_back = (dt.weekday() - 2) % 7
    new_dt = dt - timedelta(days=days_back)
    if set_time is not None:
        hour, minute, second = set_time
        new_dt = new_dt.replace(hour=hour, minute=minute, second=second, microsecond=0)
    return new_dt


def format_dt(dt: datetime) -> str:
    return dt.strftime("%A, %d %B %Y %H:%M:%S")


def info(message: str, dt: datetime) -> None:
    print(f"→ {message}: {bold(format_dt(dt))}")


def prompt_user_for_date(dt: datetime) -> datetime:

    new_dt = previous_wednesday(
        dt, set_time=(12, 0, 0)
    )  # suggest Wednesday at 12:00 UTC

    print(f"\n{warn('⚠️ Warning:')} The selected time is not a Wednesday.")
    info("Selected time", dt)
    print(f"How to proceed?")
    print(f"  [Enter/Y] Continue with selected time")
    print(f"  [W]       Pick most recent Wednesday: {format_dt(new_dt)}")

    try:
        choice = input("> ").strip().lower()
    except EOFError:
        print(f"\n{warn('⚠️ Warning:')} No input available.")
        info("Continuing with", dt)
        return dt

    if choice in ("", "y", "yes"):
        info("Continuing with", dt)
        return dt
    elif choice == "w":
        info("Continuing with most recent Wednesday", new_dt)
        return new_dt
    else:
        print(f"\n{warn('⚠️ Warning:')} Invalid choice, defaulting to selected time.")
        info("Continuing with", dt)
        return dt


def build_output_path(base_dir: Path, dt: datetime) -> Path:
    """Return markdown output path for selected date."""

    slug = dt.strftime("wip-wednesday-%d-%B-%Y").lower()

    return (
        base_dir / "content" / "en" / "news" / dt.strftime("%Y/%m") / slug / "index.md"
    )


def generate_front_matter(dt: datetime, author: str) -> str:
    """Generate YAML front matter for markdown used in Hugo."""

    return f"""---
title: WIP Wednesday - {dt.strftime("%d %B %Y")}
date: {dt.strftime("%Y-%m-%d")}
authors: {author}
draft: false
categories: update
tags:
- WIP
cover:
  image:
  caption:
---
"""


def build_headers(token: str | None = None) -> dict[str, str]:

    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def github_get(
    url: str, headers: dict[str, str], params: dict[str, Any]
) -> requests.Response:

    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    return r


def get_open_issues_counts(
    until: str, since: str, headers: dict[str, str]
) -> tuple[int, int]:
    """Return open issues at `until` and `since` in one function to reduce API calls."""

    search_url = f"{GITHUB_API}/search/issues"
    issues_params = {
        "q": f"repo:{GITHUB_REPO} is:issue",
        "per_page": 1,
    }

    counts = {}
    for key, date in [("until", until), ("since", since)]:
        r_created = github_get(
            search_url,
            headers,
            {**issues_params, "q": f"{issues_params['q']} created:<={date}"},
        )
        r_closed = github_get(
            search_url,
            headers,
            {**issues_params, "q": f"{issues_params['q']} is:closed closed:<={date}"},
        )
        counts[key] = max(
            0,
            r_created.json().get("total_count", 0)
            - r_closed.json().get("total_count", 0),
        )

    return counts["until"], counts["since"]


def fetch_github_data(
    dt: datetime, headers: dict[str, str]
) -> tuple[list[dict[str, Any]], int, int, int]:
    """
    Fetch FreeCAD PR and issue data for the week ending at dt (12:00 UTC Wednesday).
    Returns:
        prs_merged: list of merged PRs in the week
        prs_opened_count: number of opened PRs in the week
        issues_open_count: number of open issues at selected timestamp
        issues_delta: difference in open issues from previous week
    """

    until_dt = dt
    since_dt = dt - timedelta(days=7)
    until = until_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    since = since_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    search_url = f"{GITHUB_API}/search/issues"

    prs_merged = []
    page = 1
    while True:
        params = {
            "q": f"repo:{GITHUB_REPO} is:pr is:merged merged:{since}..{until}",
            "sort": "updated",
            "order": "desc",
            "per_page": 100,
            "page": page,
        }
        r = github_get(search_url, headers, params)
        items = r.json().get("items", [])
        if not items:
            break
        prs_merged.extend(items)
        if "next" not in r.links:
            break
        page += 1

    params_prs_opened = {
        "q": f"repo:{GITHUB_REPO} is:pr created:{since}..{until}",
        "per_page": 1,
    }
    r_prs_opened = github_get(search_url, headers, params_prs_opened)
    prs_opened_count = r_prs_opened.json().get("total_count", 0)

    issues_open_count, issues_open_prev = get_open_issues_counts(until, since, headers)
    issues_delta = issues_open_count - issues_open_prev

    return prs_merged, prs_opened_count, issues_open_count, issues_delta


def get_pr_type(pr: dict) -> str:
    """
    Classify PR into backport, feature, fix, other.
    Uses labels first then falls back to title heuristics.
    """

    labels = [label["name"].lower() for label in pr.get("labels", [])]
    title = pr.get("title", "").lower()

    if "backport" in title:
        return "backport"

    if any(l in ("feature", "enhancement") for l in labels) or any(
        k in title
        for k in [
            "add",
            "feature",
            "implement",
            "support",
            "enable",
            "improve",
            "introduce",
        ]
    ):
        return "feature"

    if any(l in ("bug", "bugfix", "fix") for l in labels) or any(
        k in title
        for k in [
            "fix",
            "bug",
            "crash",
            "error",
            "resolve",
            "regression",
            "correct"
        ]
    ):
        return "fix"

    return "other"


def get_pr_type_stats(prs: list[dict[str, Any]]) -> dict[str, int]:

    stats = {
        "total": len(prs),
        "backport": 0,
        "feature": 0,
        "fix": 0,
        "other": 0,
    }

    for pr in prs:
        pr_type = get_pr_type(pr)
        stats[pr_type] += 1

    return stats


def get_pr_base_branch(pr_number: int, headers: dict[str, str]) -> str:

    url = f"{GITHUB_API}/repos/{GITHUB_REPO}/pulls/{pr_number}"
    r = github_get(url, headers, {})
    data = r.json()
    return data.get("base", {}).get("ref", "unknown")


def get_branch_type_stats(
    prs: list[dict[str, Any]], headers: dict[str, str]
) -> dict[str, dict[str, int]]:
    """Classify PRs by base branch and PR type using caching to reduce API calls."""

    stats: dict[str, dict[str, int]] = {}
    cache: dict[int, str] = {}  # cache PR number -> base branch

    def get_branch_cached(pr_number: int) -> str:
        if pr_number in cache:
            return cache[pr_number]

        time.sleep(GITHUB_API_SLEEP)
        url = f"{GITHUB_API}/repos/{GITHUB_REPO}/pulls/{pr_number}"
        r = github_get(url, headers, {})
        branch = r.json().get("base", {}).get("ref", "unknown")
        cache[pr_number] = branch

        return branch

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(get_branch_cached, pr["number"]): pr
            for pr in prs
            if pr.get("number") is not None
        }

        for future in as_completed(futures):
            pr = futures[future]
            try:
                branch = future.result()
            except Exception:
                branch = "unknown"

            pr_type = get_pr_type(pr)
            if branch not in stats:
                stats[branch] = {
                    "total": 0,
                    "backport": 0,
                    "feature": 0,
                    "fix": 0,
                    "other": 0,
                }

            stats[branch]["total"] += 1
            stats[branch][pr_type] += 1

    return stats


def get_pr_commit_authors(pr_number: int, headers: dict[str, str]) -> set[str]:

    url = f"{GITHUB_API}/repos/{GITHUB_REPO}/pulls/{pr_number}/commits"
    authors = set()

    page = 1
    while True:
        params = {"per_page": 100, "page": page}
        r = github_get(url, headers, params)
        commits = r.json()
        if not commits:
            break

        for c in commits:
            author = c.get("author")
            if author and author.get("login"):
                authors.add(author["login"])
            else:
                commit_author = c.get("commit", {}).get("author", {})
                name = commit_author.get("name")
                if name:
                    authors.add(name)

        if "next" not in r.links:
            break
        page += 1

    return authors


def class_prs(
    prs: list[dict[str, Any]], headers: dict[str, str]
) -> tuple[
    DefaultDict[str, list[tuple[str, str, int, str]]], list[tuple[str, str, int, str]]
]:
    """Classify PRs into workbenches and other changes using cached commit authors."""

    workbench_changes = defaultdict(list)
    other_changes = []

    author_cache: dict[int, set[str]] = {}

    def get_pr_authors_cached(pr_number: int) -> set[str]:
        if pr_number in author_cache:
            return author_cache[pr_number]
        time.sleep(GITHUB_API_SLEEP)
        authors = get_pr_commit_authors(pr_number, headers)
        author_cache[pr_number] = authors
        return authors

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_pr = {
            executor.submit(get_pr_authors_cached, pr.get("number")): pr
            for pr in prs
            if pr.get("number") is not None
        }

        for future in as_completed(future_to_pr):
            pr = future_to_pr[future]
            try:
                authors = future.result()
            except Exception:
                authors = {"unknown"}

            authors.discard("pre-commit-ci[bot]")
            author_str = ", ".join(sorted(authors)) if authors else "unknown"

            labels = [label["name"] for label in pr.get("labels", [])]
            title = pr.get("title", "")
            title_lower = title.lower()
            number = pr.get("number")
            url = pr.get("html_url")

            if number is None:
                continue

            assigned = False
            for wb in WORKBENCH_ORDER:
                if wb.lower() in title_lower or any(
                    wb.lower() in label.lower() for label in labels
                ):
                    workbench_changes[wb].append((author_str, title, number, url))
                    assigned = True
                    break

            if not assigned:
                other_changes.append((author_str, title, number, url))

    return workbench_changes, other_changes


def find_release(dt: datetime, headers: dict[str, str]) -> str | None:
    """Get the latest weekly release build closest to chosen time."""

    url = f"{GITHUB_API}/repos/{GITHUB_REPO}/releases"
    page = 1
    candidates = []

    while True:
        params = {"per_page": 100, "page": page}
        r = github_get(url, headers, params)
        releases = r.json()
        if not releases:
            break

        for rel in releases:
            tag = rel.get("tag_name", "").lower()
            if not any(k in tag for k in ("week", "dev")):
                continue

            published = rel.get("published_at")
            if not published:
                continue

            rel_dt = parse_time(published)

            if rel_dt <= dt:
                candidates.append((rel_dt, rel.get("html_url")))

        if "next" not in r.links:
            break
        page += 1

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


def generate_body(
    dt: datetime,
    workbench_changes: DefaultDict[str, list[tuple[str, str, int, str]]],
    other_changes: list[tuple[str, str, int, str]],
    contributors: list[str],
    pr_stats: dict[str, int],
    issue_stats: dict[str, int],
    pr_type_stats: dict[str, int],
    branch_type_stats: dict[str, dict[str, int]],
    release_url: str,
) -> str:
    """Generate markdown body of WIP Wednesday article."""

    lines = ["This week in FreeCAD development:\n"]
    lines.append("### Merged PRs statistics:\n")

    branches = sorted(branch_type_stats.keys())

    header = (
        "| Type | " + " | ".join(b.replace("releases/", "") for b in branches) + " |"
    )
    separator = "|------|" + "|".join(["---"] * len(branches)) + "|"

    lines.append(header)
    lines.append(separator)

    for pr_type in ["total", "backport", "feature", "fix", "other"]:
        row = [pr_type.capitalize()]
        for branch in branches:
            row.append(str(branch_type_stats[branch].get(pr_type, 0)))
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    for wb in WORKBENCH_ORDER:
        prs = workbench_changes.get(wb)
        if prs:
            lines.append(f"### {wb}:")
            for user, title, number, url in prs:
                lines.append(f"  - {user} | {title} [PR#{number}]({url})")
            lines.append("")

    if other_changes:
        lines.append("### Other changes:")
        for user, title, number, url in other_changes:
            lines.append(f"  - {user} | {title} [PR#{number}]({url})")
        lines.append("")

    if contributors:
        lines.append(
            f"Additional improvements and fixes were contributed by {', '.join(contributors)}.\n"
        )

    lines.append(
        f"If you are interested in testing the latest weekly build, you can grab it [here]({release_url}).\n"
    )

    lines.append(
        f"### Activity stats:\n"
    )

    lines.append(
        f"PR stats: since the previous report, {pr_stats['merged']} pull requests have been merged, "
        f"and {pr_stats['opened']} new pull requests have been opened.\n"
    )

    delta = issue_stats["delta"]

    if delta > 0:
        change_str = f"up by {delta}"
    elif delta < 0:
        change_str = f"down by {abs(delta)}"
    else:
        change_str = "no change"

    lines.append(
        f"Issue stats: overall, there are {issue_stats['open']} open issues in the tracker, {change_str} from last week.\n"
    )

    return "\n".join(lines)


def main() -> None:

    parser = argparse.ArgumentParser(
        description="Generate Hugo WIP Wednesday markdown."
    )
    parser.add_argument("--time", help="Optional timestamp (ISO 8601 or RFC 2822)")
    parser.add_argument("--author", help="Optional article authors", default="")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--ci", action="store_true", help="Skip prompts")
    parser.add_argument(
        "--token", help="GitHub token to increase API limits", default=None
    )
    args = parser.parse_args()

    dt = (
        parse_time(args.time)
        if args.time
        else datetime.now().astimezone().replace(tzinfo=None)
    )

    if is_wednesday(dt):
        dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
        info("Using Wednesday", dt)
    elif args.ci:
        dt = previous_wednesday(dt, set_time=(12, 0, 0))
        info("Using most recent Wednesday (CI)", dt)
    else:
        dt = prompt_user_for_date(dt)

    out_path = build_output_path(args.root, dt)

    if out_path.exists():
        raise SystemExit(f"{warn('⚠️ Error:')} File exists: {bold(out_path)}")

    out_path.parent.mkdir(parents=True, exist_ok=True)

    headers = build_headers(args.token)
    prs_merged, prs_opened_count, issues_open_count, issues_delta = fetch_github_data(
        dt, headers
    )

    print(f"\nDetected {len(prs_merged)} merged PRs this week.")
    print("Classifying PRs and generating markdown... please wait...\n")

    pr_type_stats = get_pr_type_stats(prs_merged)
    branch_type_stats = get_branch_type_stats(prs_merged, headers)
    workbench_changes, other_changes = class_prs(prs_merged, headers)

    contribs_list = {
        pr.get("user", {}).get("login", "unknown")
        for pr in prs_merged
        if pr.get("user")
    }

    contributors = sorted(
        contrib for contrib in contribs_list
        if not any(discard in contrib.lower() for discard in ("[bot]", "[ci]", "-bot", "-ci"))
    )

    pr_stats = {
        "merged": len(prs_merged),
        "opened": prs_opened_count,
    }

    issue_stats = {
        "open": issues_open_count,
        "delta": issues_delta,
    }

    release_url = find_release(dt, headers) or (
        f"https://github.com/{GITHUB_REPO}/releases/tag/weekly-{dt.strftime('%Y.%m.%d')}"
    )

    front_matter = generate_front_matter(dt, args.author)
    body = generate_body(
        dt,
        workbench_changes,
        other_changes,
        contributors,
        pr_stats,
        issue_stats,
        pr_type_stats,
        branch_type_stats,
        release_url,
    )

    out_path.write_text(front_matter + "\n" + "\n" + body + "\n", encoding="utf-8")

    print(f"Created: {bold(out_path)}")


if __name__ == "__main__":
    main()
