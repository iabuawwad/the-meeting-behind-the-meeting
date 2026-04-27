#!/usr/bin/env bash
set -euo pipefail

NAME="the-meeting-behind-the-meeting"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT_DIR/VERSION")"
SOURCE_DIR="$ROOT_DIR/.claude/skills/$NAME"
DIST_DIR="$ROOT_DIR/dist"
BUILD_DIR="$DIST_DIR/build-skill/$NAME"
ZIP_PATH="$DIST_DIR/$NAME-skill-v$VERSION.zip"

zip_has_prefix() {
  local zip_path="$1"
  local expected_prefix="$2"
  unzip -Z1 "$zip_path" | awk -v prefix="$expected_prefix" 'index($0, prefix) == 1 { found = 1 } END { exit found ? 0 : 1 }'
}

rm -rf "$DIST_DIR"
mkdir -p "$BUILD_DIR"

cp "$SOURCE_DIR/SKILL.md" "$BUILD_DIR/SKILL.md"
cp -R "$ROOT_DIR/frameworks" "$BUILD_DIR/frameworks"
cp -R "$ROOT_DIR/templates" "$BUILD_DIR/templates"
cp -R "$ROOT_DIR/references" "$BUILD_DIR/references"
cp -R "$ROOT_DIR/resources" "$BUILD_DIR/resources"

(cd "$DIST_DIR/build-skill" && zip -qr "$ZIP_PATH" "$NAME")

skill_count="$(unzip -Z1 "$ZIP_PATH" | awk -F/ '$NF == "SKILL.md" { count++ } END { print count + 0 }')"
if [ "$skill_count" != "1" ]; then
  echo "Expected skill ZIP to contain exactly one SKILL.md, found $skill_count" >&2
  exit 1
fi

for folder in frameworks templates references resources; do
  if ! zip_has_prefix "$ZIP_PATH" "$NAME/$folder/"; then
    echo "Skill ZIP is missing $folder/" >&2
    exit 1
  fi
done

echo "$ZIP_PATH"
