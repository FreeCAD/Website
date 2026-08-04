# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 FreeCAD
# SPDX-FileNotice: Part of the FreeCAD website.


"""
Fetch and process FreeCAD addons data as JSON for website use.

- Download addons data
- Detects changes via hashing
- Transform data into key-value maps
"""


import hashlib
import json
import logging
import shutil
import xml.etree.ElementTree as ET
import zipfile

from pathlib import Path
from typing import Any

import requests


ADDONS_STATUS: str = "https://addons.freecad.org/status"
ADDONS_CACHE: str = "https://addons.freecad.org/addon_catalog_cache.zip"
ADDONS_SHA256: str = "https://addons.freecad.org/addon_catalog_cache.zip.sha256"
ADDONS_DOWNLOADS: str = "https://www.freecad.org/matomo-all-addons-downloads"

ROOT: Path = Path(__file__).resolve().parents[2]

CACHE_DIR: Path = ROOT / ".cache" / "addons"
DATA_DIR: Path = ROOT / "data"
ZIP_PATH: Path = CACHE_DIR / "addons.zip"
ETAG_PATH: Path = CACHE_DIR / "etag.txt"
HASH_PATH: Path = CACHE_DIR / "hash.txt"
OUTPUT_JSON: Path = DATA_DIR / "addons.json"

REQUEST_TIMEOUT_SHORT: int = 10
REQUEST_TIMEOUT_LONG: int = 60


logger = logging.getLogger(__name__)


def ensure_dirs() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def hash_file(path: Path) -> str:
    hf = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hf.update(chunk)

    return hf.hexdigest()


def load_text(path: Path) -> str | None:
    if not path.exists():
        return None

    return path.read_text(encoding="utf-8").strip()


def save_text(path: Path, value: str) -> None:
    path.write_text(value.strip(), encoding="utf-8")


def check_server_status() -> None:
    try:
        response = requests.get(ADDONS_STATUS, timeout=REQUEST_TIMEOUT_SHORT)
        response.raise_for_status()

    except requests.RequestException as err:
        raise RuntimeError(f"Addons server is not reachable: {err}") from err


def fetch_remote_sha256() -> str:
    try:
        response = requests.get(ADDONS_SHA256, timeout=REQUEST_TIMEOUT_SHORT)
        response.raise_for_status()

    except requests.RequestException as err:
        raise RuntimeError(f"Failed to fetch remote SHA256: {err}") from err

    return response.text.split()[0].strip()


def download_file(
    url: str,
    destination: Path,
) -> tuple[bool, str | None]:
    headers: dict[str, str] = {}
    local_etag = load_text(ETAG_PATH)

    if local_etag:
        headers["If-None-Match"] = local_etag

    try:
        response = requests.get(
            url,
            headers=headers,
            stream=True,
            timeout=(REQUEST_TIMEOUT_SHORT, REQUEST_TIMEOUT_LONG),
        )

        if response.status_code == 304:
            logger.info("ETag unchanged, skipping download.")
            return False, None

        response.raise_for_status()

        with destination.open("wb") as f:
            shutil.copyfileobj(response.raw, f)

        etag = response.headers.get("ETag")
        return True, etag.strip('"') if etag else None

    except requests.RequestException as err:
        raise RuntimeError(f"Failed to download file: {err}") from err


def extract_json_from_zip(zip_path: Path) -> Path:
    try:
        with zipfile.ZipFile(zip_path) as zf:
            json_files = [nf for nf in zf.namelist() if nf.endswith(".json")]

            if not json_files:
                raise RuntimeError("No JSON files found in ZIP")

            filename = json_files[0]
            extracted_path = CACHE_DIR / Path(filename).name

            with zf.open(filename) as source, extracted_path.open("wb") as destination:
                shutil.copyfileobj(source, destination)

            return extracted_path

    except zipfile.BadZipFile as err:
        raise RuntimeError(f"Invalid ZIP file: {err}") from err


def fetch_download_counts() -> dict[str, int]:
    try:
        response = requests.get(ADDONS_DOWNLOADS, timeout=REQUEST_TIMEOUT_LONG)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as err:
        raise RuntimeError(f"Failed to fetch download counts: {err}") from err


def extract_metadata(package_xml: str | None) -> dict[str, Any]:
    if not package_xml:
        return {}

    try:
        root = ET.fromstring(package_xml)

    except ET.ParseError:
        logger.warning("Failed to parse package.xml")
        return {}

    namespace: dict[str, str] = {}
    if root.tag.startswith("{"):
        uri = root.tag.split("}")[0][1:]
        namespace["ns"] = uri

    def find_text(name: str) -> str | None:
        elem = root.find(f"ns:{name}", namespace) if namespace else root.find(name)

        if elem is not None and elem.text:
            return elem.text.strip()

        return None

    icon_xpath = ".//ns:icon" if namespace else ".//icon"
    icon = root.findtext(icon_xpath, namespaces=namespace if namespace else None)

    return {
        "name": find_text("name"),
        "description": find_text("description"),
        "version": find_text("version"),
        "maintainer": find_text("maintainer"),
        "license": find_text("license"),
        "icon": icon.strip() if icon else None,
    }


def clean_addons_json(
    input_path: Path,
    output_path: Path,
    download_counts: dict[str, int],
) -> None:
    try:
        with input_path.open(encoding="utf-8") as file:
            data: dict[str, list[dict[str, Any]]] = json.load(file)

    except (json.JSONDecodeError, OSError) as err:
        raise RuntimeError(f"Failed to load input JSON: {err}") from err

    cleaned: dict[str, list[dict[str, Any]]] = {}

    for key, entries in data.items():
        normalized_key = key.lower()
        cleaned_entries = []

        for entry in entries:
            metadata = entry.get("metadata") or {}

            cleaned_entries.append({
                "repository": entry.get("repository"),
                "git_ref": entry.get("git_ref"),
                "total_downloads": download_counts.get(normalized_key),
                "last_update_time": entry.get("last_update_time"),
                "metadata": extract_metadata(metadata.get("package_xml")),
                "curated": entry.get("curated"),
            })

        cleaned[key] = cleaned_entries

    tmp_output = output_path.with_suffix(".tmp")

    try:
        with tmp_output.open("w", encoding="utf-8") as file:
            json.dump(cleaned, file, indent=2, ensure_ascii=False)
            file.write("\n")

        tmp_output.replace(output_path)

    except OSError as err:
        tmp_output.unlink(missing_ok=True)
        raise RuntimeError(f"Failed to write output JSON: {err}") from err


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        ensure_dirs()

        logger.info("Checking Addons server status...")
        check_server_status()

        logger.info("Fetching remote Addons hash...")
        remote_hash = fetch_remote_sha256()
        previous_hash = load_text(HASH_PATH)

        if previous_hash == remote_hash:
            logger.info("No changes in remote Addons hash. Done.")
            return 0

        logger.info("Changes detected, downloading Addons ZIP...")
        tmp_zip = ZIP_PATH.with_suffix(".tmp")

        try:
            downloaded, remote_etag = download_file(ADDONS_CACHE, tmp_zip)

            if not downloaded:
                return 0

            tmp_zip.replace(ZIP_PATH)

        except Exception:
            tmp_zip.unlink(missing_ok=True)
            raise

        current_hash = hash_file(ZIP_PATH)

        if previous_hash == current_hash:
            logger.info("No changes in downloaded Addons ZIP hash. Done.")
            return 0

        logger.info("Extracting JSON from ZIP...")
        json_path = extract_json_from_zip(ZIP_PATH)

        logger.info("Fetching Addons download counts...")
        download_counts = fetch_download_counts()

        logger.info("Cleaning Addons JSON...")
        clean_addons_json(json_path, OUTPUT_JSON, download_counts)

        if remote_etag:
            save_text(ETAG_PATH, remote_etag)

        save_text(HASH_PATH, current_hash)

        logger.info("Done.")
        return 0

    except RuntimeError as err:
        logger.error("%s", err)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
