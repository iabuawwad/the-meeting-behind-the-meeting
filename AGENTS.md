# Codex Agent Instructions

Use this repository as a public Agent Skill package for The Meeting Behind the Meeting.

## Working Style

- Work in small stages and keep changes easy to review.
- Do not skip tests. If tests cannot run, state the blocker directly.
- Do not invent platform facts. Verify Claude Code, Claude Cowork, and ChatGPT Codex packaging claims before documenting them.
- Keep `SKILL.md` files concise. Move long procedures, frameworks, examples, and background material into `frameworks/`, `references/`, and `templates/`.

## Evidence Discipline

- Preserve a clear boundary between transcript evidence and interpretation.
- Never present behavioral interpretation as fact.
- Label uncertainty and confidence where transcript quality or context is limited.
- Do not claim private-thought access, truthfulness certainty, clinical mental-health assessment, or private mental-state certainty.

## Repository Discipline

- Keep the output contract stable within a release line.
- Update `VERSION`, `CHANGELOG.md`, and relevant package metadata together.
- Keep markdown-first outputs unless a platform-specific manifest requires another format.
