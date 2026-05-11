import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import requests


TELEMETRY_URL = "https://www.freecad.org/chart_data.json"

ROOT = Path(__file__).resolve().parents[2]

CACHE_DIR = ROOT / ".cache" / "telemetry"
DATA_DIR = ROOT / "data"
HASH_PATH = CACHE_DIR / "hash.txt"
OUTPUT_JSON = DATA_DIR / "telemetry.json"


def ensure_dirs() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_text(path: Path) -> str | None:
    if not path.exists():
        return None

    return path.read_text().strip()


def save_text(path: Path, value: str) -> None:
    path.write_text(value.strip())


def fetch_json() -> dict:
    try:
        response = requests.get(TELEMETRY_URL, timeout=30)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch Telemetry JSON: {e}") from e

    except ValueError as e:
        raise RuntimeError(f"Invalid Telemetry JSON: {e}") from e

    if not data:
        raise RuntimeError("Telemetry JSON is empty")

    return data


def hash_json(data: dict) -> str:
    serialized = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    return hashlib.sha256(serialized).hexdigest()


def extract_total_users(data: dict) -> int | None:
    values = [
        value.get("totalUsers")
        for value in data.values()
        if isinstance(value, dict) and value.get("totalUsers") is not None
    ]

    if not values:
        return None

    return Counter(values).most_common(1)[0][0]


def log_invalid_keys(data: dict) -> None:
    invalid = []

    for key, value in data.items():
        if key == "totalUsers":
            continue

        if not isinstance(value, dict):
            invalid.append(key)
            continue

        labels = value.get("labels")
        series = value.get("data")

        if (
            labels is None
            or series is None
            or len(labels) != len(series)
        ):
            invalid.append(key)

    if invalid:
        print("Invalid keys:")
        for key in invalid:
            print(f" - {key}")
    else:
        print("No invalid keys found.")


def transform_data(data: dict, total_users: int | None) -> dict:
    transformed = {}

    for key, value in data.items():
        if not isinstance(value, dict):
            transformed[key] = value
            continue

        labels = value.get("labels")
        series = value.get("data")

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
    tmp_path = path.with_suffix(".tmp")

    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
        )
        f.write("\n")

    tmp_path.replace(path)


def main() -> int:
    ensure_dirs()

    print("Fetching remote Telemetry data...")
    data = fetch_json()

    current_hash = hash_json(data)
    previous_hash = load_text(HASH_PATH)

    if previous_hash == current_hash:
        print("No changes detected. Done.")
        return 0

    print("Changes detected, processing Telemetry data...")

    total_users = extract_total_users(data)

    print(f"Most common total users: {total_users}")

    log_invalid_keys(data)
    transformed = transform_data(data, total_users)

    print("Writing cleaned Telemetry JSON...")
    write_json(OUTPUT_JSON, transformed)

    save_text(HASH_PATH, current_hash)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())