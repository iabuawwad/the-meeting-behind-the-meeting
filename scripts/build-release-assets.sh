#!/usr/bin/env bash
set -euo pipefail

NAME="the-meeting-behind-the-meeting"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT_DIR/VERSION")"
SKILL_ZIP="$ROOT_DIR/dist/$NAME-skill-v$VERSION.zip"
PLUGIN_ZIP="$ROOT_DIR/dist/$NAME-plugin-v$VERSION.zip"

zip_contains() {
  local zip_path="$1"
  local expected_path="$2"
  unzip -Z1 "$zip_path" | awk -v expected="$expected_path" '$0 == expected { found = 1 } END { exit found ? 0 : 1 }'
}

cd "$ROOT_DIR"

python -m unittest discover -s tests

bash "$ROOT_DIR/scripts/build-skill-zip.sh"
bash "$ROOT_DIR/scripts/build-plugin-zip.sh"

skill_count="$(unzip -Z1 "$SKILL_ZIP" | awk -F/ '$NF == "SKILL.md" { count++ } END { print count + 0 }')"
if [ "$skill_count" != "1" ]; then
  echo "Expected skill ZIP to contain exactly one SKILL.md, found $skill_count" >&2
  exit 1
fi

for folder in frameworks templates references resources; do
  if ! unzip -Z1 "$SKILL_ZIP" | awk -v prefix="$NAME/$folder/" 'index($0, prefix) == 1 { found = 1 } END { exit found ? 0 : 1 }'; then
    echo "Skill ZIP is missing $folder/" >&2
    exit 1
  fi
done

if ! zip_contains "$PLUGIN_ZIP" "$NAME/.claude-plugin/plugin.json"; then
  echo "Plugin ZIP is missing .claude-plugin/plugin.json" >&2
  exit 1
fi

if ! zip_contains "$PLUGIN_ZIP" "$NAME/skills/$NAME/SKILL.md"; then
  echo "Plugin ZIP is missing skills/$NAME/SKILL.md" >&2
  exit 1
fi

for folder in frameworks templates references resources; do
  if ! unzip -Z1 "$PLUGIN_ZIP" | awk -v prefix="$NAME/skills/$NAME/$folder/" 'index($0, prefix) == 1 { found = 1 } END { exit found ? 0 : 1 }'; then
    echo "Plugin ZIP is missing skills/$NAME/$folder/" >&2
    exit 1
  fi
done

echo "Skill ZIP: $SKILL_ZIP"
echo "Plugin ZIP: $PLUGIN_ZIP"
