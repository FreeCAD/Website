#!/usr/bin/env python3
"""Decide whether a pull request is a news post its author may publish.

Used by the Publish news workflow (.github/workflows/publish-news.yaml), which runs on pull_request_target: the
checked-out tree is main, never the pull request (which could otherwise modify *this script* and then run it... not so
smart). The pull request's files are read through the API at its head commit. When every check passes, they are written
into the tree so that the workflow can build the site with them. Prevents "pwn request" attacks.

Usage:
    publish_news.py check    Check the pull request; write the results to GITHUB_OUTPUT and, if it qualifies, its files
                             into the tree.
    publish_news.py comment  Add or update the comment that lists REASONS.

Environment: GITHUB_TOKEN, GITHUB_REPOSITORY, PR_NUMBER, and GITHUB_OUTPUT (check) or REASONS (comment).
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any, Final

API: Final = os.environ.get("GITHUB_API_URL", "https://api.github.com")
BLOGGERS_FILE: Final = Path(".github/bloggers.yml")
DOCS_URL: Final = "https://www.freecad.org/dev/web/news/"
MARKER: Final = "<!-- publish-news -->"
RAW: Final = "application/vnd.github.raw"

BASE_BRANCH: Final = "main"

# Some arbitrary limits to prevent some kind of malicious post from blowing the server up: these don't reject the post,
# they just flag it for review, so keep them relatively conservative. As of this writing, the largest blog post ever was
# 15 files.
MAX_FILES: Final = 25
MAX_FILE_BYTES: Final = 20 * 1024 * 1024

# content/<lang>/news/<anything>.<ext>, but NOT a section page, e.g. _index.md.
PATH_RE: Final = re.compile(
    r"content/[a-z]{2,3}(?:[-_][A-Za-z]{2,4})?/news/(?:[^/]+/)*[^/]+\."
    r"(?:md|webp|png|jpe?g|mp4)"
)

# Front matter fields a post may set. "redirect" is written by the CMS form and is only accepted when empty, so it needs
# some special handling. Generalized because... well, may as well!
ALLOWED_KEYS: Final = frozenset({
    "title", "description", "linkTitle", "date", "draft",
    "author", "category", "tags", "cover",
})
EMPTY_ONLY_KEYS: Final = frozenset({"redirect"})
EMPTY_VALUES: Final = frozenset({"", '""', "''", "null", "~"})

# Raw HTML is rendered by the site as-is (markup.goldmark.renderer.unsafe), so only basic formatting tags are accepted,
# and no attributes are allowed.
ALLOWED_TAGS: Final = frozenset({"sub", "sup", "kbd", "code", "em", "strong", "br"})
ALLOWED_SHORTCODES: Final = frozenset({"youtube", "video", "peertube"})


def github_request(path: str, method: str = "GET", data: Any = None,
                   accept: str = "application/vnd.github+json") -> Any:
    """Make one GitHub API request; return parsed JSON, or bytes for RAW."""
    url = path if path.startswith("http") else API + path
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw: bytes = resp.read()
    if accept == RAW:
        return raw
    return json.loads(raw) if raw else None


def paginate(path: str) -> list[Any]:
    items: list[Any] = []
    page = 1
    while True:
        sep = "&" if "?" in path else "?"
        batch = github_request(f"{path}{sep}per_page=100&page={page}")
        items += batch
        if len(batch) < 100:
            return items
        page += 1


def load_bloggers() -> set[str]:
    logins: set[str] = set()
    in_list = False
    for line in BLOGGERS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].rstrip()
        if not line:
            continue
        if re.fullmatch(r"bloggers:", line):
            in_list = True
        elif in_list and (m := re.fullmatch(r"\s*-\s*([A-Za-z0-9-]+)", line)):
            logins.add(m[1].lower())
        else:
            in_list = False
    return logins


def check_path(path: str) -> str | None:
    """Return a reason the path is not allowed, or None."""
    parts = path.split("/")
    if any(p in ("", ".", "..") or p.startswith(".") for p in parts):
        return f"`{path}`: path not allowed"
    if parts[-1] == "_index.md":
        return f"`{path}`: section pages need review"
    if not PATH_RE.fullmatch(path):
        return (f"`{path}`: only Markdown, WebP, PNG, JPEG and MP4 files "
                "under `content/<language>/news/` publish without review")
    return None


def check_markdown(path: str, text: str) -> list[str]:
    """Return the reasons a news post's Markdown needs review."""
    reasons: list[str] = []
    text = text.replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---(?:\n|$)(.*)", text, flags=re.S)
    if not m:
        return [f"`{path}`: no YAML front matter between `---` lines"]
    front, body = m[1], m[2]

    for line in front.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0] in " \t-":
            continue  # part of the previous field's value
        km = re.match(r"([a-z][A-Za-z]*):(?:\s(.*)|$)", line)
        key: str | None = km[1] if km else None
        value: str | None = (km[2] or "").strip() if km else None
        if key in ALLOWED_KEYS:
            continue
        if key in EMPTY_ONLY_KEYS and value in EMPTY_VALUES:
            continue
        shown = key if key else line.strip()[:40]
        reasons.append(f"`{path}`: front matter `{shown}` needs review")

    # Shortcodes run even inside code blocks: check the whole body
    for sc in re.finditer(r"\{\{\s*[<%]", body):
        nm = re.match(r"\s*/?\s*([\w.-]+)", body[sc.end():])
        if not nm or nm[1] not in ALLOWED_SHORTCODES:
            shown = nm[1] if nm else body[sc.start():sc.end() + 3].strip()
            reasons.append(f"`{path}`: shortcode `{shown}` needs review")

    # Sanitize any HTML *anywhere*, even inside code blocks, to avoid having to be overly clever with our markdown block
    # detection. This does mean that a blog post that has code blocks with HTML in them gets flagged for manual review,
    # but IMO we can live with that.
    prose = re.sub(r"\{\{<.*?>\}\}|\{\{%.*?%\}\}", "", body, flags=re.S)
    prose = re.sub(r"<(?:https?|mailto):[^\s<>]*>", "", prose)
    prose = re.sub(r"<[A-Za-z0-9][^\s<>@]*@[^\s<>@]+>", "", prose)

    def allowed_tag(tag: re.Match[str]) -> str:
        name, attrs = tag[2].lower(), tag[3].strip().rstrip("/").strip()
        if name in ALLOWED_TAGS and not attrs:
            return ""
        reasons.append(f"`{path}`: HTML `<{tag[1]}{tag[2]}>` needs review")
        return ""

    rest = re.sub(r"<\s*(/?)\s*([A-Za-z][A-Za-z0-9-]*)([^<>]*)>", allowed_tag,
                  prose)
    if re.search(r"<[A-Za-z/!?]", rest):
        reasons.append(f"`{path}`: raw HTML needs review")

    scheme = r"<?\s*(?:javascript|vbscript|data):"
    if (re.search(r"\]\(\s*" + scheme, prose, flags=re.I)
            or re.search(r"^ {0,3}\[[^\]]+\]:\s*" + scheme, prose,
                         flags=re.I | re.M)):
        reasons.append(f"`{path}`: link scheme needs review")

    return sorted(set(reasons))


def set_output(**values: str) -> None:
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        for key, value in values.items():
            delim = f"EOF_{uuid.uuid4().hex}"
            out.write(f"{key}<<{delim}\n{value}\n{delim}\n")


def check() -> None:
    repo, number = os.environ["GITHUB_REPOSITORY"], os.environ["PR_NUMBER"]
    pr = github_request(f"/repos/{repo}/pulls/{number}")
    author: str = pr["user"]["login"]
    head_sha: str = pr["head"]["sha"]
    is_blogger = author.lower() in load_bloggers()
    reasons: list[str] = []

    if not is_blogger:
        reasons.append(f"@{author} is not in `.github/bloggers.yml`")
    elif pr["draft"]:
        reasons.append("the pull request is a draft")
    elif pr["state"] != "open" or pr["base"]["ref"] != BASE_BRANCH:
        reasons.append(f"the pull request is not open against `{BASE_BRANCH}`")
    elif pr["changed_files"] > MAX_FILES:
        reasons.append(f"more than {MAX_FILES} files changed")
    elif not pr["head"]["repo"]:
        reasons.append("the pull request's source repository is gone")

    writes: dict[str, bytes] = {}
    removals: list[str] = []
    if not reasons:
        head_repo: str = pr["head"]["repo"]["full_name"]
        for f in paginate(f"/repos/{repo}/pulls/{number}/files"):
            paths: list[str] = [f["filename"]] + ([f["previous_filename"]]
                                                  if f.get("previous_filename") else [])
            bad = [r for p in paths if (r := check_path(p))]
            if bad:
                reasons += bad
                continue
            if f.get("previous_filename"):
                removals.append(f["previous_filename"])
            if f["status"] == "removed":
                removals.append(f["filename"])
                continue
            quoted = urllib.parse.quote(f["filename"])
            data: bytes = github_request(
                f"/repos/{head_repo}/contents/{quoted}?ref={head_sha}", accept=RAW)
            if len(data) > MAX_FILE_BYTES:
                reasons.append(f"`{f['filename']}`: larger than "
                               f"{MAX_FILE_BYTES // 2**20} MB")
                continue
            if f["filename"].endswith(".md"):
                try:
                    reasons += check_markdown(f["filename"], data.decode("utf-8"))
                except UnicodeDecodeError:
                    reasons.append(f"`{f['filename']}`: not UTF-8 text")
            writes[f["filename"]] = data

    eligible = not reasons
    if eligible:
        root = Path("content").resolve()
        for name in removals:
            target = Path(name).resolve()
            if target.is_relative_to(root) and target.is_file():
                target.unlink()
        for name, data in writes.items():
            target = Path(name).resolve()
            if not target.is_relative_to(root):
                sys.exit(f"refusing to write outside content/: {name}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)

    # A comment is only useful to a listed blogger whose post is ready for review
    notify = is_blogger and not pr["draft"] and not eligible
    set_output(eligible=str(eligible).lower(), notify=str(notify).lower(),
               head_sha=head_sha, reasons=json.dumps(reasons))
    print(f"PR #{number} by @{author} at {head_sha}: "
          + ("eligible" if eligible else "not eligible"))
    for reason in reasons:
        print(f"  - {reason}")


def comment() -> None:
    repo, number = os.environ["GITHUB_REPOSITORY"], os.environ["PR_NUMBER"]
    reasons: list[str] = json.loads(os.environ["REASONS"])
    body = "\n".join([
        MARKER,
        "This post was not published automatically, so it is waiting for a "
        "maintainer's review:",
        "",
        *(f"- {r}" for r in reasons),
        "",
        f"See [Publishing news]({DOCS_URL}) for what publishes on its own.",
    ])
    path = f"/repos/{repo}/issues/{number}/comments"
    for c in paginate(path):
        if c["user"]["login"] == "github-actions[bot]" and MARKER in c["body"]:
            github_request(c["url"], method="PATCH", data={"body": body})
            return
    github_request(path, method="POST", data={"body": body})


if __name__ == "__main__":
    try:
        {"check": check, "comment": comment}[sys.argv[1]]()
    except (IndexError, KeyError):
        sys.exit(__doc__)
    except urllib.error.HTTPError as e:
        sys.exit(f"GitHub API error {e.code} for {e.url}: {e.read()[:500]!r}")
