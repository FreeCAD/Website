#!/usr/bin/env bash
#
# deploy-website.sh -- server-side staging deploy for the FreeCAD website.
#
# Fetches the pinned branch, rebuilds the Hugo site into a temporary
# directory, and swaps it into place only after a successful build.
# Runs on the Incus staging container as a dedicated unprivileged account.
#
# The deployed branch is hard-coded on purpose -- it is never taken from a
# caller argument.

set -euo pipefail

REMOTE="origin"
BRANCH="main"
REMOTE_REF="${REMOTE}/${BRANCH}"

REPO_DIR="${DEPLOY_REPO_DIR:-/var/www/Website}"
PUBLIC_DIR="${REPO_DIR}/public"
LOCK_FILE="${DEPLOY_LOCK_FILE:-/tmp/freecad-website.lock}"
HUGO_BIN="${HUGO_BIN:-hugo}"
HUGO_ENVIRONMENT="${HUGO_ENVIRONMENT:-production}"

BUILD_DIR=""
OLD_PUBLIC=""

log() {
    printf '%s deploy-website: %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"
}

cleanup() {
    [ -n "$BUILD_DIR" ] && rm -rf "$BUILD_DIR"
    [ -n "$OLD_PUBLIC" ] && rm -rf "$OLD_PUBLIC"
}
trap cleanup EXIT

if [ "$(id -u)" -eq 0 ]; then
    log "refusing to run as root; use the dedicated deploy account"
    exit 1
fi

exec 9>"$LOCK_FILE"
if ! flock -n 9; then
    log "another deployment is already in progress; aborting"
    exit 1
fi

if [ ! -d "${REPO_DIR}/.git" ]; then
    log "no git repository at ${REPO_DIR}"
    exit 1
fi

cd "$REPO_DIR"

log "fetching ${REMOTE_REF}"
git fetch --prune "$REMOTE" "$BRANCH"
git reset --hard "$REMOTE_REF"

DEPLOYED_COMMIT="$(git rev-parse HEAD)"
log "building ${BRANCH} at ${DEPLOYED_COMMIT}"

BUILD_DIR="$(mktemp -d "${REPO_DIR}/.deploy.XXXXXX")"

"$HUGO_BIN" \
    --gc \
    --minify \
    --environment "$HUGO_ENVIRONMENT" \
    --destination "${BUILD_DIR}/public"

OLD_PUBLIC="${PUBLIC_DIR}.old"
rm -rf "$OLD_PUBLIC"
if [ -d "$PUBLIC_DIR" ]; then
    mv "$PUBLIC_DIR" "$OLD_PUBLIC"
fi
mv "${BUILD_DIR}/public" "$PUBLIC_DIR"

log "deployed ${BRANCH} at ${DEPLOYED_COMMIT}"
logger -t website-deploy "Deployed $(git rev-parse --short origin/main)"
