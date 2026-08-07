# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 FreeCAD
# SPDX-FileNotice: Part of the FreeCAD website.


"""
Fetch and process FreeCAD releases data as JSON for website use.

- Download release and downloadable assets metadata from GitHub.
- Reuse existing releases data if possible.
- Classify assets in dictionaries by platform, architecture, and package.
- Transform data into clean key-value maps.
"""


import json
import logging
import os
import time

from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


REPOSITORY: str = "FreeCAD/FreeCAD"
API_RELEASES: str = f"https://api.github.com/repos/{REPOSITORY}/releases"

ROOT: Path = Path(__file__).resolve().parents[2]
OUTPUT_JSON: Path = ROOT / "data/releases.json"

USER_AGENT: str = "github-release-exporter/1.0"
TIMEOUT: int = 120
PER_PAGE: int = 100
MAX_RETRIES: int = 3

SKIPPED_TAGS: set[str] = {"weeklies"}
PLATFORMS: tuple[str] = ("windows", "linux", "mac")
IGNORED_ASSETS: tuple[str] = (".txt", ".zsync", ".pdf")
WINDOWS_PLATFORM: tuple[str] = ("win", "setup", "installer")
MAC_PLATFORM: tuple[str] = ("mac", "osx")
ARM_ARCH: tuple[str] = ("aarch64", "arm64")
X86_64_ARCH: tuple[str] = ("x86_64", "x64", "amd64", "osx_10", "os10", "intel_x86") # Old Intel macOS builds may only contain OS version (e.g. "10.15")
IA32_ARCH: tuple[str] = ("x86", "x32", "i386", "ia-32")
WINDOWS_PORTABLE: tuple[str] = (".7z", ".zip")
WINDOWS_INSTALLER: tuple[str] = (".exe", ".msi")
MAC_ARCHIVE: tuple[str] = (".zip", ".tar.gz")


logger = logging.getLogger(__name__)


def github_headers() -> dict[str, str]:
    """Return GitHub API request headers."""
    headers: dict[str, str] = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }

    token: str | None = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def github_api_get(url: str) -> tuple[Any, dict[str, str]]:
    """Fetch and decode JSON response from GitHub."""
    request: Request = Request(url, headers=github_headers())
    last_error: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urlopen(request, timeout=TIMEOUT) as response:
                encoding: str = response.headers.get_content_charset() or "utf-8"
                data: Any = json.loads(response.read().decode(encoding))
                headers: dict[str, str] = dict(response.headers.items())
                return data, headers

        except HTTPError as exc:
            last_error = exc

            if exc.code == 403 and exc.headers.get("X-RateLimit-Remaining") == "0":
                reset: str | None = exc.headers.get("X-RateLimit-Reset")
                if reset:
                    wait: int = max(int(reset) - int(time.time()) + 1, 1)
                    logger.warning("Rate limit reached, waiting %s seconds.", wait)
                    time.sleep(wait)
                    continue

            if exc.code >= 500 and attempt < MAX_RETRIES:
                time.sleep(attempt * 2)
                continue

            raise RuntimeError(f"GitHub HTTP error {exc.code}") from exc

        except URLError as exc:
            last_error = exc

            if attempt < MAX_RETRIES:
                time.sleep(attempt * 2)
                continue

    raise RuntimeError(f"Unable to contact GitHub: {last_error}")


def next_page_url(link: str | None) -> str | None:
    """URL pagination for GitHub header."""
    if not link:
        return None

    for item in link.split(","):
        if 'rel="next"' not in item:
            continue

        start: int = item.find("<")
        end: int = item.find(">")

        if start >= 0 and end > start:
            return item[start + 1:end]

    return None


def fetch_releases() -> list[dict[str, Any]]:
    """Fetch all releases with GitHub pagination."""
    releases: list[dict[str, Any]] = []
    url: str | None = f"{API_RELEASES}?per_page={PER_PAGE}"

    while url:
        logger.info("Fetching %s", url)
        data, headers = github_api_get(url)

        if not isinstance(data, list):
            raise RuntimeError("Unexpected GitHub releases response.")

        for release in data:
            tag = release.get("tag_name")

            if tag in SKIPPED_TAGS:
                logger.info("Skipping release '%s'", tag)
                continue

            releases.append(release)

        url = next_page_url(headers.get("Link"))

    return releases


def load_existing_data() -> dict[str, dict[str, Any]]:
    """Reuse existing releases data indexed by tag."""

    if not OUTPUT_JSON.exists():
        return {}

    try:
        with OUTPUT_JSON.open(encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        logger.warning("Ignoring invalid JSON: %s", OUTPUT_JSON)
        return {}

    releases = data.get("releases", [])

    if not isinstance(releases, list):
        return {}

    return {
        release["tag"]: release
        for release in releases
        if isinstance(release, dict) and "tag" in release
    }


def build_asset(
    asset: dict[str, Any],
    existing_assets: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Convert assets data into simpler JSON for web use."""

    filename: str = asset["name"]
    url: str = asset["browser_download_url"]
    sha256: str | None = None

    if asset.get("digest"):
        sha256 = asset["digest"].removeprefix("sha256:")
    else:
        existing_asset = existing_assets.get(url)
        if existing_asset:
            sha256 = existing_asset.get("sha256")

    return {
        "name": filename,
        "size": asset.get("size", 0),
        "url": url,
        "sha256": sha256,
        "type": asset.get("content_type"),
        "updated": asset.get("updated_at"),
    }


def classify_asset(asset: dict[str, Any]) -> tuple[str, str, str] | None:
    """Class asset by platform, architecture, and package."""

    name = asset["name"].lower()

    if name.endswith(".tar.gz") and "source" in name:
        return "source", "", ""

    if any(t in name for t in WINDOWS_PLATFORM):
        platform = "windows"
    elif "linux" in name or name.endswith(".appimage"):
        platform = "linux"
    elif any(t in name for t in MAC_PLATFORM):
        platform = "mac"
    else:
        return None

    if any(t in name for t in ARM_ARCH):
        arch = "arm"
    elif any(t in name for t in X86_64_ARCH):
        arch = "x86-64"
    elif any(t in name for t in IA32_ARCH):
        arch = "ia-32"
    else:
        return None

    if platform == "windows":
        if name.endswith(WINDOWS_PORTABLE):
            package = "portable"
        elif name.endswith(WINDOWS_INSTALLER):
            package = "installer"
        else:
            return None

    elif platform == "linux":
        if name.endswith(".appimage"):
            package = "appimage"
        else:
            return None

    elif platform == "mac":
        if name.endswith(".dmg"):
            package = "dmg"
        elif name.endswith(MAC_ARCHIVE):
            package = "archive"
        else:
            return None

    return platform, arch, package


def build_release(
    release: dict[str, Any],
    latest_tag: str,
    existing_release: dict[str, Any] | None,
) -> dict[str, Any]:
    """Convert release data into simpler JSON for web use."""
    assets: dict[str, Any] = {}
    existing_assets: dict[str, dict[str, Any]] = {}

    if existing_release:
        existing = existing_release.get("assets", {})

        source = existing.get("source")
        if source:
            existing_assets[source["url"]] = source

        for platform in PLATFORMS:
            for arch_assets in existing.get(platform, {}).values():
                for asset in arch_assets.values():
                    existing_assets[asset["url"]] = asset

    for raw_asset in release.get("assets", []):

        filename: str = raw_asset["name"]

        if filename.endswith(IGNORED_ASSETS):
            continue

        asset_class = classify_asset(raw_asset)

        if asset_class is None:
            logger.warning("Ignoring unknown asset '%s'", filename)
            continue

        asset = build_asset(raw_asset, existing_assets)

        platform, arch, package = asset_class

        if platform == "source":
            assets["source"] = asset
            continue

        assets.setdefault(platform, {})
        assets[platform].setdefault(arch, {})
        assets[platform][arch][package] = asset

    return {
        "name": release.get("name") or release.get("tag_name"),
        "tag": release.get("tag_name"),
        "branch": release.get("target_commitish"),
        "published": release.get("published_at"),
        "updated": release.get("updated_at"),
        "draft": release.get("draft"),
        "prerelease": release.get("prerelease"),
        "latest": release.get("tag_name") == latest_tag,
        "url": release.get("html_url"),
        "assets": assets,
    }


def main() -> int:
    """Generate releases JSON file."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        raw_releases: list[dict[str, Any]] = fetch_releases()

        latest_release: dict[str, Any] | None = next(
            (
                release
                for release in raw_releases
                if not release.get("draft") and not release.get("prerelease")
            ),
            None,
        )

        if latest_release is None:
            raise RuntimeError("No stable releases found.")

        releases: list[dict[str, Any]] = []
        existing_data = load_existing_data()
        latest_tag: str = latest_release["tag_name"]
        reused = 0

        for rel in raw_releases:

            tag: str = rel["tag_name"]
            existing_release = existing_data.get(tag)

            if (
                existing_release
                and existing_release.get("updated") == rel.get("updated_at")
            ):
                existing_release["latest"] = tag == latest_tag
                releases.append(existing_release)
                reused += 1
                continue

            if existing_release:
                logger.info("Rebuilding data for release '%s'", tag)
            else:
                logger.info("Adding data for release '%s'", tag)

            release = build_release(rel, latest_tag, existing_release)
            releases.append(release)

        if reused:
            logger.info("Reusing existing data for %d releases", reused)

        # Sort and store oldest to newest for minimal Git diffs.
        releases.sort(key=lambda item: item["published"])

        document: dict[str, Any] = {
            "platform": "GitHub",
            "repository": REPOSITORY,
            "releases": releases,
        }

        OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)

        temporary = OUTPUT_JSON.with_suffix(".tmp")

        with temporary.open("w", encoding="utf-8") as output:
            json.dump(document, output, indent=2, ensure_ascii=False)
            output.write("\n")

        temporary.replace(OUTPUT_JSON)

        logger.info("Generated %s", OUTPUT_JSON)
        return 0

    except RuntimeError as err:
        logger.error("%s", err)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())