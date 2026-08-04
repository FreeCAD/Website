# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 FreeCAD
# SPDX-FileNotice: Part of the FreeCAD website.


"""
Fetch and process FreeCAD telemetry data as JSON for website use.

- Download telemetry data
- Detects changes via hashing
- Transform data into key-value maps
"""


import hashlib
import json
import logging

from collections import Counter
from pathlib import Path
from typing import Any

import requests


TELEMETRY_URL: str = "https://www.freecad.org/chart_data.json"
REQUEST_TIMEOUT: int = 30

ROOT: Path = Path(__file__).resolve().parents[2]
CACHE_DIR: Path = ROOT / ".cache" / "telemetry"
DATA_DIR: Path = ROOT / "data"
HASH_PATH: Path = CACHE_DIR / "hash.txt"
OUTPUT_JSON: Path = DATA_DIR / "telemetry.json"


logger = logging.getLogger(__name__)


def ensure_dirs() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_text(path: Path) -> str | None:
    if not path.exists():
        return None

    return path.read_text(encoding="utf-8").strip()


def save_text(path: Path, content: str) -> None:
    path.write_text(content.strip(), encoding="utf-8")


def fetch_telemetry_json() -> dict:
    try:
        response: requests.Response = requests.get(
            TELEMETRY_URL,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        data: dict = response.json()

    except requests.RequestException as err:
        raise RuntimeError(f"Failed to fetch telemetry data: {err}") from err

    except ValueError as err:
        raise RuntimeError(f"Invalid telemetry JSON: {err}") from err

    if not data:
        raise RuntimeError("Telemetry JSON is empty")

    return data


def hash_data(data: dict) -> str:
    serialized: bytes = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    return hashlib.sha256(serialized).hexdigest()


def extract_most_common_total_users(data: dict) -> int | None:
    user_counts: list[int] = [
        value.get("totalUsers")
        for value in data.values()
        if isinstance(value, dict) and value.get("totalUsers") is not None
    ]

    if not user_counts:
        return None

    return Counter(user_counts).most_common(1)[0][0]


def validate_data_structure(data: dict) -> list[str]:
    invalid_keys: list[str] = []

    for key, value in data.items():
        if key == "totalUsers":
            continue

        if not is_valid_entry(key, value):
            invalid_keys.append(key)

    return invalid_keys


def is_valid_entry(key: str, value: Any) -> bool:
    if not isinstance(value, dict):
        return False

    labels: list | None = value.get("labels")
    series: list | None = value.get("data")

    return (labels is not None and
            series is not None and
            len(labels) == len(series))


def transform_telemetry_data(
    data: dict,
    total_users: int | None,
) -> dict:
    transformed: dict = {}

    for key, value in data.items():
        if not isinstance(value, dict):
            transformed[key] = value
            continue

        labels: list | None = value.get("labels")
        series: list | None = value.get("data")

        if labels is not None and series is not None:
            transformed[key] = {
                label: series[index]
                for index, label in enumerate(labels)
            }
        else:
            transformed[key] = value

    transformed["total_users"] = total_users

    return transformed


def write_json(path: Path, data: dict) -> None:
    tmp_path: Path = path.with_suffix(".tmp")

    with tmp_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
        )
        file.write("\n")

    tmp_path.replace(path)


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        ensure_dirs()

        logger.info("Fetching remote telemetry data...")
        data: dict = fetch_telemetry_json()
        current_hash: str = hash_data(data)
        previous_hash: str | None = load_text(HASH_PATH)

        if previous_hash == current_hash:
            logger.info("No changes detected. Done.")
            return 0

        logger.info("Changes detected, processing telemetry data...")

        total_users: int | None = extract_most_common_total_users(data)
        logger.info(f"Most common total users: {total_users}")

        invalid_keys: list[str] = validate_data_structure(data)

        if invalid_keys:
            logger.warning("Invalid keys: %s", ", ".join(invalid_keys))

        else:
            logger.info("All keys valid.")

        transformed: dict = transform_telemetry_data(data, total_users)

        logger.info("Writing cleaned telemetry JSON...")
        write_json(OUTPUT_JSON, transformed)
        save_text(HASH_PATH, current_hash)

        logger.info("Done.")
        return 0

    except RuntimeError as err:
        logger.error("%s", err)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())