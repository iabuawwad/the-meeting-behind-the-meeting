# Install

Use GitHub Releases ZIP assets for installation.

Do not upload the GitHub source ZIP.

Do not use Code -> Download ZIP unless you are a developer. The GitHub source ZIP contains several package layouts and multiple `SKILL.md` files. Claude Skill upload expects a skill package with exactly one `SKILL.md`.

## 1. Install for normal users

Download one of these files from GitHub Releases:

- `the-meeting-behind-the-meeting-skill-v0.2.2.zip`
- `the-meeting-behind-the-meeting-plugin-v0.2.2.zip`

Use the skill ZIP for normal Claude Desktop Skill upload. Use the plugin ZIP only when you specifically need the Claude Cowork plugin package.

## 2. Install As Claude Skill

Use:

```text
the-meeting-behind-the-meeting-skill-v0.2.2.zip
```

Install:

1. Open Claude Desktop.
2. Open Customize.
3. Open Skills.
4. Click `+`.
5. Choose Upload a skill.
6. Upload `the-meeting-behind-the-meeting-skill-v0.2.2.zip`.
7. Invoke the skill with `/the-meeting-behind-the-meeting` from Slash commands.

Expected ZIP structure:

```text
the-meeting-behind-the-meeting/
├── SKILL.md
├── frameworks/
├── templates/
├── references/
└── resources/
```

This ZIP is built so it contains exactly one `SKILL.md`.

## 3. Install In Claude Cowork

Cowork runs in Claude Desktop and can use selected files and installed skills depending on the active desktop build and plan.

Normal path:

1. Install `the-meeting-behind-the-meeting-skill-v0.2.2.zip` as a Claude Skill.
2. Open Cowork.
3. Use the installed skill from the available skill or Slash command controls.

Plugin path:

1. Download `the-meeting-behind-the-meeting-plugin-v0.2.2.zip` from GitHub Releases.
2. Open Claude Desktop.
3. Go to Cowork.
4. Open Customize.
5. Upload the plugin ZIP when plugin upload is available.
6. Invoke the bundled skill with `/the-meeting-behind-the-meeting`.

Expected plugin ZIP structure:

```text
the-meeting-behind-the-meeting/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── the-meeting-behind-the-meeting/
│       ├── SKILL.md
│       ├── frameworks/
│       ├── templates/
│       ├── references/
│       └── resources/
└── README.md
```

## 4. Install As Claude Code Project Skill

Use this path when developing from a cloned source repository.

Project skill path:

```text
.claude/skills/the-meeting-behind-the-meeting/SKILL.md
```

Invoke:

```text
/the-meeting-behind-the-meeting
```

Verify:

```bash
test -f .claude/skills/the-meeting-behind-the-meeting/SKILL.md
grep -R "transcript quality gate" .claude/skills/the-meeting-behind-the-meeting/SKILL.md
```

Claude Code Terminal install:

```bash
npm install -g @anthropic-ai/claude-code
claude
```

Warp is only a terminal surface. Open Warp in the repository folder, run `claude`, and invoke the skill normally.

## 5. Install For Codex

Codex project skill path:

```text
.agents/skills/the-meeting-behind-the-meeting/
```

Invoke:

```text
$the-meeting-behind-the-meeting
```

Codex CLI install options:

```bash
npm install -g @openai/codex
```

or:

```bash
brew install codex
```

Run:

```bash
codex
```

## 6. Developer Installation From Source

Use source installation only if you are editing, testing, or rebuilding the package.

Clone the repository, then run:

```bash
python -m unittest discover -s tests
bash scripts/build-release-assets.sh
```

Generated release assets are written to `dist/`:

```text
dist/the-meeting-behind-the-meeting-skill-v0.2.2.zip
dist/the-meeting-behind-the-meeting-plugin-v0.2.2.zip
```

Before publishing release assets, confirm:

```bash
unzip -l dist/the-meeting-behind-the-meeting-skill-v0.2.2.zip | grep SKILL.md
unzip -l dist/the-meeting-behind-the-meeting-plugin-v0.2.2.zip | head -80
find . -type f \( -name "*.pdf" -o -name "*.epub" -o -name "*.azw3" -o -name "*.mobi" \)
```
