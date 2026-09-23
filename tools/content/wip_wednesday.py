# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 FreeCAD
# SPDX-FileNotice: Part of the FreeCAD website.


"""
Fetch and process FreeCAD/FreeCAD repository activity data for website weekly reports as Markdown.

- Generate Markdown summary of merged PRs, opened issues, and workbench-specific changes
- Support time selection with default Wednesday
- Use GitHub API v3 with retry and concurrent processing for efficiency

Usage:
    python script.py --time "2026-01-08T12:00:00Z" --author "Alice and Bob"
    python script.py --ci  # CI mode: skip prompts, use most recent Wednesday
    python script.py --token "github_token"  # Increase API rate limits
"""


import argparse
import logging
import time

from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from textwrap import dedent
from typing import Any, DefaultDict

import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


GITHUB_REPO: str = "FreeCAD/FreeCAD"
GITHUB_API: str = "https://api.github.com"
GITHUB_API_SLEEP: float = 0.05
MAX_RETRIES: int = 3
RETRY_BACKOFF: float = 0.3
MAX_PAGES: int = 20

WORKBENCH_ORDER: list[str] = [
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

PR_TYPE_KEYWORDS: dict[str, dict[str, list[str]]] = {
    "feature": {
        "labels": ["feature", "enhancement"],
        "titles": ["add", "feature", "implement", "support", "enable", "improve", "introduce"],
    },
    "fix": {
        "labels": ["bug", "bugfix", "fix"],
        "titles": ["fix", "bug", "crash", "error", "resolve", "regression", "correct"],
    },
    "backport": {
        "labels": ["backport"],
        "titles": ["backport"],
    },
}

BOT_SUFFIXES: tuple[str, ...] = ("[bot]", "[ci]", "-bot", "-ci", "dependabot")


logger: logging.Logger = logging.getLogger(__name__)


class GitHubSession:

    def __init__(self, token: str | None = None) -> None:
        self.session: requests.Session = requests.Session()
        retry_strategy: Retry = Retry(
            total=MAX_RETRIES,
            backoff_factor=RETRY_BACKOFF,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
        )
        adapter: HTTPAdapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        headers: dict[str, str] = {"Accept": "application/vnd.github.v3+json"}
        if token:
            headers["Authorization"] = f"token {token}"
        self.session.headers.update(headers)

    def get(self, url: str, params: dict[str, Any] | None = None) -> requests.Response:
        response: requests.Response = self.session.get(url, params=params or {})
        response.raise_for_status()

        remaining = response.headers.get("X-RateLimit-Remaining")
        if remaining:
            logger.debug(f"API rate limit remaining: {remaining}")

        return response

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "GitHubSession":
        return self

    def __exit__(self, *args: Any) -> bool:
        self.close()
        return False


def warn(text: str) -> str:
    """Return text formatted in red ANSI color for warnings."""
    colored: str = f"\033[31m{text}\033[0m"
    return colored


def bold(text: str) -> str:
    """Return text formatted in bold blue ANSI color."""
    colored: str = f"\033[1;34m{text}\033[0m"
    return colored


def parse_time(timestr: str) -> datetime:
    """
    Parse time string in ISO 8601 (2026-01-01T01:23:45+00:00)
    or RFC 2822 (Thu, 01 Jan 2026 01:23:45 GMT) format.
    Returns timezone-aware datetime in UTC.
    """
    original: str = timestr

    if timestr.endswith("Z"):
        timestr = timestr[:-1] + "+00:00"

    try:
        dt: datetime = datetime.fromisoformat(timestr)

    except ValueError:
        try:
            dt = parsedate_to_datetime(timestr)
        except Exception as exc:
            raise SystemExit(f"{warn('⚠️ Error:')} Unsupported time format: {original}") from exc

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc)

    return dt


def is_wednesday(dt: datetime) -> bool:
    result: bool = dt.weekday() == 2
    return result


def previous_wednesday(
    dt: datetime, set_time: tuple[int, int, int] | None = None
) -> datetime:
    """Return most recent Wednesday with optional time (hour, minute, second)."""
    days_back: int = (dt.weekday() - 2) % 7
    new_dt: datetime = dt - timedelta(days=days_back)

    if set_time is not None:
        hour: int
        minute: int
        second: int
        hour, minute, second = set_time
        new_dt = new_dt.replace(hour=hour, minute=minute, second=second, microsecond=0)

    return new_dt


def format_dt(dt: datetime) -> str:
    formatted: str = dt.strftime("%A, %d %B %Y %H:%M:%S")
    return formatted


def prompt_user_for_date(dt: datetime) -> datetime:
    new_dt: datetime = previous_wednesday(dt, set_time=(12, 0, 0))

    logger.warning(f"{warn('⚠️ Warning:')} The selected time is not a Wednesday.")
    logger.info(f"→ Selected time: {bold(format_dt(dt))}")
    logger.info("How to proceed?")
    enter: str = "[Enter/Y]"
    logger.info(f"  {bold(enter)} Continue with selected time")
    wednesday: str = "[W]"
    logger.info(f"  {bold(wednesday)}       Pick most recent Wednesday: {format_dt(new_dt)}")

    try:
        choice: str = input("> ").strip().lower()
    except EOFError:
        logger.warning(f"{warn('⚠️ Warning:')} No input available.")
        logger.info(f"→ Continuing with: {bold(format_dt(dt))}")
        return dt

    if choice in ("", "y", "yes"):
        logger.info(f"→ Continuing with: {bold(format_dt(dt))}")
        return dt
    elif choice == "w":
        logger.info(f"→ Continuing with most recent Wednesday: {bold(format_dt(new_dt))}")
        return new_dt
    else:
        logger.warning(f"{warn('⚠️ Warning:')} Invalid choice, defaulting to selected time.")
        logger.info(f"→ Continuing with: {bold(format_dt(dt))}")
        return dt


def get_open_issues_counts(
    until: str, since: str, session: GitHubSession
) -> tuple[int, int]:
    search_url: str = f"{GITHUB_API}/search/issues"
    base_query: str = f"repo:{GITHUB_REPO} is:issue"

    counts: dict[str, int] = {}

    for key, date in [("until", until), ("since", since)]:
        response_created: requests.Response = session.get(
            search_url,
            {
                "q": f"{base_query} created:<={date}",
                "per_page": 1,
            },
        )
        created_count: int = response_created.json().get("total_count", 0)

        response_closed: requests.Response = session.get(
            search_url,
            {
                "q": f"{base_query} is:closed closed:<={date}",
                "per_page": 1,
            },
        )
        closed_count: int = response_closed.json().get("total_count", 0)

        counts[key] = max(0, created_count - closed_count)

    return counts["until"], counts["since"]


def fetch_github_data(
    dt: datetime, session: GitHubSession
) -> tuple[list[dict[str, Any]], int, int, int]:
    until_dt: datetime = dt.astimezone()
    since_dt: datetime = (dt - timedelta(days=7)).astimezone()
    until: str = until_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    since: str = since_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    search_url: str = f"{GITHUB_API}/search/issues"
    prs_merged: list[dict[str, Any]] = []
    page: int = 1

    while page <= MAX_PAGES:
        params: dict[str, str | int] = {
            "q": f"repo:{GITHUB_REPO} is:pr is:merged merged:{since}..{until}",
            "sort": "updated",
            "order": "desc",
            "per_page": 100,
            "page": page,
        }
        response: requests.Response = session.get(search_url, params)
        items: list[dict[str, Any]] = response.json().get("items", [])
        if not items:
            break
        prs_merged.extend(items)
        if "next" not in response.links or page >= MAX_PAGES:
            break
        page += 1

    params_prs_opened: dict[str, str | int] = {
        "q": f"repo:{GITHUB_REPO} is:pr created:{since}..{until}",
        "per_page": 1,
    }
    response_prs_opened: requests.Response = session.get(search_url, params_prs_opened)
    prs_opened_count: int = response_prs_opened.json().get("total_count", 0)

    issues_open_count: int
    issues_open_prev: int
    issues_open_count, issues_open_prev = get_open_issues_counts(until, since, session)
    issues_delta: int = issues_open_count - issues_open_prev

    return prs_merged, prs_opened_count, issues_open_count, issues_delta


def get_pr_type(pr: dict) -> str:
    """
    Classify PR into backport, feature, fix, other.
    Uses labels first then falls back to title heuristics.
    """

    labels = {label["name"].lower() for label in pr.get("labels", [])}
    title = pr.get("title", "").lower()

    for pr_type, keywords in PR_TYPE_KEYWORDS.items():
        if any(k in title for k in keywords["titles"]) or any(
            l in labels for l in keywords["labels"]
        ):
            return pr_type

    return "other"


def get_pr_type_stats(prs: list[dict[str, Any]]) -> dict[str, int]:
    type_counts = Counter(get_pr_type(pr) for pr in prs)
    return {
        "total": len(prs),
        "backport": type_counts.get("backport", 0),
        "feature": type_counts.get("feature", 0),
        "fix": type_counts.get("fix", 0),
        "other": type_counts.get("other", 0),
    }


def get_pr_base_branch(pr_number: int, session: GitHubSession) -> str:
    url: str = f"{GITHUB_API}/repos/{GITHUB_REPO}/pulls/{pr_number}"
    response: requests.Response = session.get(url)
    branch: str = response.json().get("base", {}).get("ref", "unknown")
    return branch


def get_branch_type_stats(
    prs: list[dict[str, Any]], session: GitHubSession
) -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = {}
    cache: dict[int, str] = {}

    def get_branch_cached(pr_number: int) -> str:
        if pr_number not in cache:
            time.sleep(GITHUB_API_SLEEP)
            cache[pr_number] = get_pr_base_branch(pr_number, session)
        return cache[pr_number]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures: dict[Any, dict[str, Any]] = {
            executor.submit(get_branch_cached, pr["number"]): pr
            for pr in prs
            if pr.get("number") is not None
        }

        for future in as_completed(futures):
            pr: dict[str, Any] = futures[future]

            try:
                branch: str = future.result()
            except Exception as e:
                logger.warning(f"Failed to get branch for PR {pr.get('number')}: {e}")
                branch = "unknown"

            pr_type: str = get_pr_type(pr)
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


def get_pr_commit_authors(pr_number: int, session: GitHubSession) -> set[str]:
    url: str = f"{GITHUB_API}/repos/{GITHUB_REPO}/pulls/{pr_number}/commits"
    authors: set[str] = set()
    page: int = 1

    while True:
        params: dict[str, int] = {"per_page": 100, "page": page}
        response: requests.Response = session.get(url, params)
        commits: list[dict[str, Any]] = response.json() if isinstance(response.json(), list) else []
        if not commits:
            break

        for commit in commits:
            author: dict[str, Any] | None = commit.get("author")
            if author and author.get("login"):
                authors.add(author["login"])
            else:
                commit_author: dict[str, str] = commit.get("commit", {}).get(
                    "author", {}
                )
                name: str | None = commit_author.get("name")
                if name:
                    authors.add(name)

        if "next" not in response.links:
            break
        page += 1

    return authors


def class_prs(
    prs: list[dict[str, Any]], session: GitHubSession
) -> tuple[
    DefaultDict[str, list[tuple[str, str, int, str]]], list[tuple[str, str, int, str]]
]:
    workbench_changes: DefaultDict[str, list[tuple[str, str, int, str]]] = defaultdict(list)
    other_changes: list[tuple[str, str, int, str]] = []
    author_cache: dict[int, set[str]] = {}

    def get_pr_authors_cached(pr_number: int) -> set[str]:
        if pr_number in author_cache:
            return author_cache[pr_number]
        time.sleep(GITHUB_API_SLEEP)
        authors: set[str] = get_pr_commit_authors(pr_number, session)
        author_cache[pr_number] = authors
        return authors

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_pr: dict[Any, dict[str, Any]] = {
            executor.submit(get_pr_authors_cached, pr.get("number")): pr
            for pr in prs
            if pr.get("number") is not None
        }

        for future in as_completed(future_to_pr):
            pr: dict[str, Any] = future_to_pr[future]

            try:
                authors: set[str] = future.result()
            except Exception as e:
                logger.warning(f"Failed to get authors for PR {pr.get('number')}: {e}")
                authors = {"unknown"}

            authors.discard("pre-commit-ci[bot]")
            author_str: str = ", ".join(sorted(authors)) if authors else "unknown"

            labels: list[str] = [label["name"] for label in pr.get("labels", [])]
            title: str = pr.get("title", "")
            title_lower: str = title.lower()
            number: int | None = pr.get("number")
            url: str | None = pr.get("html_url")

            if number is None:
                continue

            assigned: bool = False

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


def find_release(dt: datetime, session: GitHubSession) -> str | None:
    """Get the latest weekly release build closest to chosen time."""

    url: str = f"{GITHUB_API}/repos/{GITHUB_REPO}/releases"
    page: int = 1
    candidates: list[tuple[datetime, str | None]] = []

    while True:
        params: dict[str, int] = {"per_page": 100, "page": page}
        response: requests.Response = session.get(url, params)
        releases: list[dict[str, Any]] = response.json()
        if not releases:
            break

        for rel in releases:
            tag: str = rel.get("tag_name", "").lower()
            if not any(key in tag for key in ("week", "dev")):
                continue

            published: str | None = rel.get("published_at")
            if not published:
                continue

            rel_dt: datetime = parse_time(published)

            if rel_dt <= dt:
                html_url: str | None = rel.get("html_url")
                candidates.append((rel_dt, html_url))

        if "next" not in response.links:
            break
        page += 1

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


def extract_contributors(prs: list[dict[str, Any]]) -> list[str]:
    """Extract and filter human contributors from merged PRs."""
    contribs: set[str] = {
        pr.get("user", {}).get("login", "unknown")
        for pr in prs
        if pr.get("user")
    }
    return sorted(contrib for contrib in contribs if not any(discard in contrib.lower() for discard in BOT_SUFFIXES))


def build_output_path(base_dir: Path, dt: datetime) -> Path:
    """Return markdown output path for selected date."""
    slug = dt.strftime("wip-wednesday-%d-%B-%Y").lower()

    return (
        base_dir / "content" / "en" / "news" / dt.strftime("%Y/%m") / slug / "index.md"
    )


def generate_front_matter(dt: datetime, author: str) -> str:
    """Generate YAML front matter for markdown used in Hugo."""
    return dedent(f"""
        ---
        title: WIP Wednesday - {dt.strftime("%d %B %Y")}
        date: {dt.strftime("%Y-%m-%d")}
        author: {author}
        draft: false
        category: update
        tags:
        - WIP
        cover:
          image:
          caption:
        ---
    """).strip()


def generate_pr_stats_table(
    branch_type_stats: dict[str, dict[str, int]]
) -> str:
    """Generate markdown table of PR statistics by branch and type."""
    branches = sorted(branch_type_stats.keys())

    header_cells: list[str] = ["Type"] + [b.replace("releases/", "") for b in branches]
    header: str = "| " + " | ".join(header_cells) + " |"
    separator: str = "|" + "|".join(["---"] * len(header_cells)) + "|"

    rows: list[str] = [header, separator]
    for pr_type in ["total", "backport", "feature", "fix", "other"]:
        cells = [pr_type.capitalize()]
        cells.extend(
            str(branch_type_stats[branch].get(pr_type, 0))
            for branch in branches
        )
        rows.append("| " + " | ".join(cells) + " |")

    return "\n".join(rows)


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

    lines: list[str] = ["This week in FreeCAD development:\n"]
    lines.append("### Merged PRs statistics\n")

    lines.append(generate_pr_stats_table(branch_type_stats))
    lines.append("")

    for wb in WORKBENCH_ORDER:
        prs = workbench_changes.get(wb)
        if prs:
            lines.append(f"### {wb}")
            for user, title, number, url in prs:
                lines.append(f"  - {user} | {title} [PR#{number}]({url})")
            lines.append("")

    if other_changes:
        lines.append("### Other changes")
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
        f"### Activity stats\n"
    )

    lines.append(
        f"**PR stats**: since the previous report, {pr_stats['merged']} pull requests have been merged, "
        f"and {pr_stats['opened']} new pull requests have been opened.\n"
    )

    delta = issue_stats["delta"]

    if delta > 0:
        change_str: str = f"up by {delta}"

    elif delta < 0:
        change_str = f"down by {abs(delta)}"

    else:
        change_str = "no change"

    lines.append(
        f"**Issue stats**: overall, there are {issue_stats['open']} open issues in the tracker, {change_str} from last week.\n"
    )

    lines.append(
        f"### Elsewhere in the community\n"
    )

    return "\n".join(lines)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    parser = argparse.ArgumentParser(
        description="Generate Hugo WIP Wednesday markdown."
    )
    parser.add_argument("--time", help="Optional timestamp (ISO 8601 or RFC 2822)")
    parser.add_argument("--author", help="Optional article author", default="")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--ci", action="store_true", help="CI mode: skip prompts, use most recent Wednesday")
    parser.add_argument("--token", help="GitHub token to increase API rate limits")
    args = parser.parse_args()

    dt: datetime = (parse_time(args.time) if args.time else datetime.now().astimezone())

    if is_wednesday(dt):
        dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
        logger.info(f"→ Using Wednesday: {bold(format_dt(dt))}")
    elif args.ci:
        dt = previous_wednesday(dt, set_time=(12, 0, 0))
        logger.info(f"→ Using most recent Wednesday (CI): {bold(format_dt(dt))}")
    else:
        dt = prompt_user_for_date(dt)

    out_path: Path = build_output_path(args.root, dt)

    if out_path.exists():
        raise SystemExit(f"{warn('⚠️ Error:')} File exists: {bold(out_path)}")

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)

    except OSError as err:
        raise SystemExit(
            f"{warn('⚠️ Error:')} Cannot create directory {bold(out_path.parent)}: {err}"
        ) from err

    with GitHubSession(args.token) as session:
        prs_merged, prs_opened_count, issues_open_count, issues_delta = fetch_github_data(
            dt, session
        )

        logger.info(f"Detected {len(prs_merged)} merged PRs this week.")
        logger.info("Classifying PRs and generating markdown... please wait...\n")

        pr_type_stats = get_pr_type_stats(prs_merged)
        branch_type_stats = get_branch_type_stats(prs_merged, session)
        workbench_changes, other_changes = class_prs(prs_merged, session)

        release_url: str = find_release(dt, session) or (
            f"https://github.com/{GITHUB_REPO}/releases/tag/weekly-{dt.strftime('%Y.%m.%d')}"
        )

    contributors = extract_contributors(prs_merged)

    pr_stats = {
        "merged": len(prs_merged),
        "opened": prs_opened_count,
    }

    issue_stats = {
        "open": issues_open_count,
        "delta": issues_delta,
    }

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

    content: str = f"{front_matter}\n\n{body}\n"

    out_path.write_text(content, encoding="utf-8")

    logger.info(f"Created: {bold(out_path)}")
    logger.info("Done.")


if __name__ == "__main__":
    main()
