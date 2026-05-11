import hashlib
import json
import shutil
import sys
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

import requests


ADDONS_STATUS = "https://addons.freecad.org/status"
ADDONS_CACHE = "https://addons.freecad.org/addon_catalog_cache.zip"
ADDONS_SHA256 = "https://addons.freecad.org/addon_catalog_cache.zip.sha256"
ADDONS_DOWNLOADS = "https://www.freecad.org/matomo-all-addons-downloads"

ROOT = Path(__file__).resolve().parents[2]

CACHE_DIR = ROOT / ".cache" / "addons"
DATA_DIR = ROOT / "data"
ZIP_PATH = CACHE_DIR / "addons.zip"
ETAG_PATH = CACHE_DIR / "etag.txt"
HASH_PATH = CACHE_DIR / "hash.txt"
OUTPUT_JSON = DATA_DIR / "addons.json"


def ensure_dirs() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def hash_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)

    return h.hexdigest()


def load_text(path: Path) -> str | None:
    if not path.exists():
        return None

    return path.read_text().strip()


def save_text(path: Path, value: str) -> None:
    path.write_text(value.strip())


def check_server_status() -> None:
    try:
        r = requests.get(ADDONS_STATUS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Addons server is not reachable: {e}")


def fetch_remote_sha256() -> str:
    r = requests.get(ADDONS_SHA256, timeout=10)
    r.raise_for_status()

    return r.text.split()[0].strip()


def download_file(url: str, destination: Path) -> tuple[bool, str | None]:
    headers = {}

    local_etag = load_text(ETAG_PATH)

    if local_etag:
        headers["If-None-Match"] = local_etag

    with requests.get(
        url,
        headers=headers,
        stream=True,
        timeout=(10, 60),
    ) as response:

        if response.status_code == 304:
            print("ETag unchanged.")
            return False, None

        response.raise_for_status()

        with destination.open("wb") as f:
            shutil.copyfileobj(response.raw, f)

        etag = response.headers.get("ETag")

        return True, etag.strip('"') if etag else None


def extract_json_from_zip(zip_path: Path) -> Path:
    with zipfile.ZipFile(zip_path) as zf:
        json_files = [n for n in zf.namelist() if n.endswith(".json")]

        if not json_files:
            raise RuntimeError("No JSON files found in ZIP")

        filename = json_files[0]

        extracted_path = CACHE_DIR / Path(filename).name

        with zf.open(filename) as source, extracted_path.open("wb") as destination:
            shutil.copyfileobj(source, destination)

        return extracted_path


def fetch_download_counts() -> dict:
    response = requests.get(ADDONS_DOWNLOADS, timeout=30)
    response.raise_for_status()

    return response.json()


def extract_metadata(package_xml: str | None) -> dict:
    if not package_xml:
        return {}

    try:
        root = ET.fromstring(package_xml)
    except ET.ParseError:
        return {}

    namespace = {}

    if root.tag.startswith("{"):
        uri = root.tag.split("}")[0][1:]
        namespace["ns"] = uri

        def tag(name: str) -> str:
            return f"ns:{name}"

    else:

        def tag(name: str) -> str:
            return name

    def find_text(name: str) -> str | None:
        elem = root.find(tag(name), namespace)
        if elem is not None and elem.text:
            return elem.text.strip()
        return None

    icon = (
        root.findtext(".//ns:icon", namespaces=namespace)
        if namespace
        else root.findtext(".//icon")
    )

    return {
        "name": find_text("name"),
        "description": find_text("description"),
        "version": find_text("version"),
        "maintainer": find_text("maintainer"),
        "license": find_text("license"),
        "icon": icon.strip() if icon else None,
    }


def clean_addons_json(input_path: Path, output_path: Path, download_counts: dict) -> None:
    with input_path.open() as f:
        data = json.load(f)

    cleaned = {}

    for key, entries in data.items():
        normalized_key = key.lower()

        cleaned_entries = []

        for entry in entries:
            metadata = entry.get("metadata") or {}

            cleaned_entries.append(
                {
                    "repository": entry.get("repository"),
                    "git_ref": entry.get("git_ref"),
                    "total_downloads": download_counts.get(normalized_key),
                    "last_update_time": entry.get("last_update_time"),
                    "metadata": extract_metadata(metadata.get("package_xml")),
                    "curated": entry.get("curated"),
                }
            )

        cleaned[key] = cleaned_entries

    tmp_output = output_path.with_suffix(".tmp")

    with tmp_output.open("w") as f:
        json.dump(cleaned, f, indent=2)

    tmp_output.replace(output_path)


def main() -> int:
    ensure_dirs()

    print("Checking Addons server status...")
    check_server_status()

    print("Fetching remote Addons hash...")
    remote_hash = fetch_remote_sha256()

    previous_hash = load_text(HASH_PATH)

    if previous_hash == remote_hash:
        print("No changes in remote Addons hash. Done.")
        return 0

    print("Changes detected, downloading Addons ZIP...")
    tmp_zip = ZIP_PATH.with_suffix(".tmp")

    try:
        downloaded, remote_etag = download_file(ADDONS_CACHE, tmp_zip)

        if not downloaded:
            return 0

        tmp_zip.replace(ZIP_PATH)

    finally:
        tmp_zip.unlink(missing_ok=True)

    current_hash = hash_file(ZIP_PATH)

    if previous_hash == current_hash:
        print("No changes in downloaded Addons ZIP hash. Done.")
        return 0

    json_path = extract_json_from_zip(ZIP_PATH)

    print("Fetching Addons download counts...")
    download_counts = fetch_download_counts()

    print("Cleaning Addons JSON...")
    clean_addons_json(json_path, OUTPUT_JSON, download_counts)

    if remote_etag:
        save_text(ETAG_PATH, remote_etag)

    save_text(HASH_PATH, current_hash)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())