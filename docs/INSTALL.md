# Install

This repository packages **The Meeting Behind the Meeting** for Claude Cowork Desktop, Claude Code, ChatGPT Codex Desktop, and Codex CLI.

Product UIs and packaging surfaces can change. Use this guide with the current official product documentation and keep platform claims conservative.

## 1. Claude Cowork Desktop

### Requirements

- Claude Desktop installed.
- A paid Claude plan. Anthropic describes Claude Cowork as available on paid plans through Claude Desktop.
- This repository's Cowork plugin wrapper at `skill/cowork-plugin/`.

### Install

1. Open Claude Desktop.
2. Go to the Cowork tab.
3. Open Customize.
4. Browse plugins or upload the custom plugin file from `skill/cowork-plugin/`.
5. Install the plugin.
6. Invoke the skill with `/` or the `+` button once installed.

### Notes

- Cowork runs on the desktop and can work with selected local files, folders, and applications that you provide or authorize.
- Plugin packaging is the supported route for delivering skills in Cowork. This repository's Cowork plugin bundles only the skill: no connectors, no MCP servers, and no elevated permissions.

### Verify

```bash
python3 -m json.tool skill/cowork-plugin/plugin.json
grep -R '"connectors": \\[\\]' skill/cowork-plugin/plugin.json
grep -R '"mcp_servers": \\[\\]' skill/cowork-plugin/plugin.json
grep -R '"permissions": \\[\\]' skill/cowork-plugin/plugin.json
```

### Test Prompt

```text
/the-meeting-behind-the-meeting Analyze this meeting transcript. Start with the transcript quality gate, then identify decisions, action items, and risks.
```

## 2. Claude Code Desktop

### Requirements

- Claude Desktop installed.
- Access to the Code tab in Claude Desktop.
- Project skill files in `.claude/skills/the-meeting-behind-the-meeting/`, or plugin installation through the desktop UI when available in your build.

### Install

1. Install and open Claude Desktop.
2. Open the Code tab.
3. Open this repository folder as the project.
4. Use the project skill from `.claude/skills/the-meeting-behind-the-meeting/`.
5. Or install the packaged skill/plugin from the desktop UI if your Claude Desktop build exposes plugin installation there.
6. Invoke the skill by typing `/the-meeting-behind-the-meeting`.

### Notes

- Skills can be selected from Slash commands when the Claude Code Desktop surface exposes them.
- Keep the project copy at `.claude/skills/the-meeting-behind-the-meeting/SKILL.md` aligned with the source skill content.

### Verify

```bash
test -f .claude/skills/the-meeting-behind-the-meeting/SKILL.md
grep -R "name: the-meeting-behind-the-meeting" .claude/skills/the-meeting-behind-the-meeting/SKILL.md
```

### Test Prompt

```text
/the-meeting-behind-the-meeting Use the transcript quality gate first. Then produce a one-page intelligence brief from these meeting notes.
```

## 3. Claude Code Terminal

### Requirements

- Node.js 18 or newer.
- Claude Code installed from the official package.
- A Claude.ai, Anthropic Console, or supported enterprise authentication path.

### Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Start Claude Code from the repository folder:

```bash
claude
```

### Install The Skill

Personal install:

```text
~/.claude/skills/the-meeting-behind-the-meeting/SKILL.md
```

Project install:

```text
.claude/skills/the-meeting-behind-the-meeting/SKILL.md
```

This repository already includes the project install path.

### Invoke

```text
/the-meeting-behind-the-meeting
```

### Verify

```bash
claude --version
test -f .claude/skills/the-meeting-behind-the-meeting/SKILL.md
grep -R "transcript quality gate" .claude/skills/the-meeting-behind-the-meeting/SKILL.md
```

### Test Prompt

```text
/the-meeting-behind-the-meeting Analyze the attached conversation thread. First score transcript quality, then extract decisions, actions, risks, and open questions.
```

## 4. Claude Code Terminal In Warp

Warp is only the terminal surface. Install and run Claude Code normally.

### Install

```bash
npm install -g @anthropic-ai/claude-code
```

### Run

1. Open Warp.
2. Open this repository folder in Warp.
3. Run:

```bash
claude
```

4. Invoke the skill normally:

```text
/the-meeting-behind-the-meeting
```

### Verify

```bash
pwd
claude --version
test -f .claude/skills/the-meeting-behind-the-meeting/SKILL.md
```

### Test Prompt

```text
/the-meeting-behind-the-meeting Analyze these voice-note notes. Start with quality and reconstruction confidence before interpreting intent.
```

## 5. ChatGPT Codex Desktop

### Requirements

- Codex app installed. OpenAI describes the Codex app as available for macOS and Windows.
- Sign in with a ChatGPT account or workspace that has Codex access.
- Select this repository as the project folder.

### Install The Skill

Codex project skills should live under:

```text
.agents/skills/the-meeting-behind-the-meeting/
```

This repository already includes:

```text
.agents/skills/the-meeting-behind-the-meeting/SKILL.md
.agents/skills/the-meeting-behind-the-meeting/agents/openai.yaml
```

### Invoke

Use either:

```text
$the-meeting-behind-the-meeting
```

or the skill picker if available in your Codex Desktop build.

### Verify

```bash
test -f .agents/skills/the-meeting-behind-the-meeting/SKILL.md
test -f .agents/skills/the-meeting-behind-the-meeting/agents/openai.yaml
grep -R "allow_implicit_invocation" .agents/skills/the-meeting-behind-the-meeting/agents/openai.yaml
```

### Test Prompt

```text
$the-meeting-behind-the-meeting Analyze this meeting transcript. Run the quality gate first, then produce decisions, action items, risks, and a next-meeting playbook.
```

## 6. Codex CLI

### Requirements

- Node.js and npm for npm installation, or Homebrew for Homebrew installation.
- ChatGPT or OpenAI account flow supported by your Codex CLI version.

### Install Codex CLI

NPM:

```bash
npm install -g @openai/codex
```

Homebrew:

```bash
brew install codex
```

If Homebrew treats Codex as a cask in your environment, use the current package manager form shown by OpenAI's Codex documentation for your platform.

### Run

```bash
codex
```

### Install The Skill

Project skill:

```text
.agents/skills/the-meeting-behind-the-meeting/
```

User skill:

```text
~/.agents/skills/the-meeting-behind-the-meeting/
```

This repository already includes the project skill path.

### Invoke

```text
$the-meeting-behind-the-meeting
```

### Verify

```bash
codex --version
test -f .agents/skills/the-meeting-behind-the-meeting/SKILL.md
grep -R "name: the-meeting-behind-the-meeting" .agents/skills/the-meeting-behind-the-meeting/SKILL.md
```

### Test Prompt

```text
$the-meeting-behind-the-meeting Review these meeting minutes. Start with transcript quality, then produce a decision/action table and risk register.
```

## Repository Validation

After changing installation docs or skill packaging, run:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
python3 -m json.tool skill/cowork-plugin/plugin.json
```

## Official References

- Anthropic Claude Code setup: `https://docs.anthropic.com/en/docs/claude-code/getting-started`
- Anthropic Claude Code overview: `https://docs.anthropic.com/en/docs/claude-code/overview`
- Anthropic Claude Cowork product page: `https://www.anthropic.com/product/claude-cowork`
- OpenAI Codex with ChatGPT plan: `https://help.openai.com/en/articles/11369540-codex-in-chatgpt`
- OpenAI Codex CLI getting started: `https://help.openai.com/en/articles/11096431-openai-codex-ci-getting-started`
