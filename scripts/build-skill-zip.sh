#!/usr/bin/env bash
set -euo pipefail

NAME="the-meeting-behind-the-meeting"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT_DIR/VERSION")"
SOURCE_DIR="$ROOT_DIR/.claude/skills/$NAME"
DIST_DIR="$ROOT_DIR/dist"
BUILD_DIR="$DIST_DIR/build-skill/$NAME"
ZIP_PATH="$DIST_DIR/$NAME-skill-v$VERSION.zip"

rm -rf "$DIST_DIR"
mkdir -p "$BUILD_DIR"

cp "$SOURCE_DIR/SKILL.md" "$BUILD_DIR/SKILL.md"
cp -R "$SOURCE_DIR/resources" "$BUILD_DIR/resources"

(cd "$DIST_DIR/build-skill" && zip -qr "$ZIP_PATH" "$NAME")

skill_count="$(unzip -Z1 "$ZIP_PATH" | awk -F/ '$NF == "SKILL.md" { count++ } END { print count + 0 }')"
if [ "$skill_count" != "1" ]; then
  echo "Expected skill ZIP to contain exactly one SKILL.md, found $skill_count" >&2
  exit 1
fi

echo "$ZIP_PATH"
