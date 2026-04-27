#!/usr/bin/env bash
set -euo pipefail

NAME="the-meeting-behind-the-meeting"
DISPLAY_NAME="The Meeting Behind the Meeting"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT_DIR/VERSION")"
SOURCE_DIR="$ROOT_DIR/.claude/skills/$NAME"
DIST_DIR="$ROOT_DIR/dist"
BUILD_ROOT="$DIST_DIR/build-plugin"
PLUGIN_ROOT="$BUILD_ROOT/$NAME"
PLUGIN_SKILL_DIR="$PLUGIN_ROOT/skills/$NAME"
ZIP_PATH="$DIST_DIR/$NAME-plugin-v$VERSION.zip"

zip_contains() {
  local zip_path="$1"
  local expected_path="$2"
  unzip -Z1 "$zip_path" | awk -v expected="$expected_path" '$0 == expected { found = 1 } END { exit found ? 0 : 1 }'
}

rm -rf "$BUILD_ROOT"
mkdir -p "$PLUGIN_ROOT/.claude-plugin" "$PLUGIN_SKILL_DIR" "$DIST_DIR"

cat > "$PLUGIN_ROOT/.claude-plugin/plugin.json" <<JSON
{
  "name": "$NAME",
  "display_name": "$DISPLAY_NAME",
  "version": "$VERSION",
  "description": "Evidence-based meeting analysis skill for transcripts, meeting notes, decisions, action items, and risks.",
  "skills": [
    {
      "name": "$NAME",
      "path": "skills/$NAME/SKILL.md"
    }
  ],
  "connectors": [],
  "mcp_servers": [],
  "permissions": []
}
JSON

cp "$SOURCE_DIR/SKILL.md" "$PLUGIN_SKILL_DIR/SKILL.md"
cp -R "$ROOT_DIR/frameworks" "$PLUGIN_SKILL_DIR/frameworks"
cp -R "$ROOT_DIR/templates" "$PLUGIN_SKILL_DIR/templates"
cp -R "$ROOT_DIR/references" "$PLUGIN_SKILL_DIR/references"
cp -R "$ROOT_DIR/resources" "$PLUGIN_SKILL_DIR/resources"

cat > "$PLUGIN_ROOT/README.md" <<README
# $DISPLAY_NAME

Claude Cowork plugin package for $DISPLAY_NAME.

This plugin bundles only the skill. It does not include connectors, MCP servers, or elevated permissions.
README

(cd "$BUILD_ROOT" && zip -qr "$ZIP_PATH" "$NAME")

if ! zip_contains "$ZIP_PATH" "$NAME/.claude-plugin/plugin.json"; then
  echo "Plugin ZIP is missing .claude-plugin/plugin.json" >&2
  exit 1
fi

if ! zip_contains "$ZIP_PATH" "$NAME/skills/$NAME/SKILL.md"; then
  echo "Plugin ZIP is missing skills/$NAME/SKILL.md" >&2
  exit 1
fi

for folder in frameworks templates references resources; do
  if ! unzip -Z1 "$ZIP_PATH" | awk -v prefix="$NAME/skills/$NAME/$folder/" 'index($0, prefix) == 1 { found = 1 } END { exit found ? 0 : 1 }'; then
    echo "Plugin ZIP is missing skills/$NAME/$folder/" >&2
    exit 1
  fi
done

echo "$ZIP_PATH"
