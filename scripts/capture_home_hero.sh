#!/usr/bin/env sh
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 FreeCAD

set -eu

capture=${1:-desktop}
case "$capture" in
  desktop|mobile) ;;
  *)
    echo "Usage: $0 [desktop|mobile]" >&2
    exit 2
    ;;
esac

freecad_executable=${FREECAD_EXECUTABLE:-FreeCAD}
if ! command -v "$freecad_executable" >/dev/null 2>&1; then
  echo "FreeCAD executable not found: $freecad_executable" >&2
  echo "Set FREECAD_EXECUTABLE to a GUI-enabled FreeCAD build." >&2
  exit 1
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
config_dir=$(mktemp -d "${TMPDIR:-/tmp}/freecad-home-hero.XXXXXX")
cleanup() {
  find "$config_dir" -type f -delete
  rmdir "$config_dir"
}
trap cleanup EXIT HUP INT TERM

HOMEPAGE_HERO_CAPTURE=$capture \
HOMEPAGE_HERO_ISOLATED_CONFIG=1 \
  "$freecad_executable" \
    --user-cfg "$config_dir/user.cfg" \
    --system-cfg "$config_dir/system.cfg" \
    "$script_dir/generate_home_hero.py"
