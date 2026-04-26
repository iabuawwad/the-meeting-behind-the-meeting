# Model Routing

This document defines the model and effort strategy for **The Meeting Behind the Meeting** across Claude and Codex surfaces.

Use native runtime controls where available. They are safer, easier to document, and more maintainable than random third-party model switcher plugins.

## Claude Strategy

Claude surfaces should use native Claude Code model aliases and effort controls when the runtime supports them.

Exact model availability depends on the user's plan, organization policy, Claude Code version, and the active Claude runtime surface. Do not hard-code assumptions that a specific user can access every alias.

### Recommended Default For Skill Build

Use `opusplan` as the recommended default for building and maintaining this skill because the repository requires careful instruction design, evidence discipline, and multi-file consistency.

### Model Use By Task

| Task | Recommended Claude model family or alias | Reason |
|---|---|---|
| Cheap cleanup and basic classification | Haiku, if manually selected | Lower-cost cleanup, formatting, simple source classification |
| Structured outputs and normal analysis | Sonnet | Good balance for minutes, decisions, actions, risks, and standard briefs |
| Deep reasoning and difficult interpretation | Opus | Better fit for forensic mode, said-vs-meant, decision integrity, trust prediction, and next-meeting strategy |
| Skill build and architecture work | `opusplan` | Good default for planning, governance, tests, and cross-file consistency |

### Effort Use By Task

| Task | Recommended effort |
|---|---|
| Cleanup, formatting, file renaming, simple classification | `low` |
| Simple notes, short voice-note analysis, lightweight recap | `medium` |
| Standard mode, deep mode, decision/accountability review | `high` |
| Difficult forensic analysis, mixed-thread reconstruction, disputed record review | `xhigh` or `max` when supported |

### Claude Mode Guidance

- Start every analysis with the transcript quality gate.
- Use Haiku only when the user explicitly wants cheap cleanup or simple classification and the runtime exposes that choice.
- Use Sonnet for ordinary structured deliverables.
- Use Opus for high-stakes reasoning, ambiguous evidence, and strategy.
- Use `xhigh` or `max` only when the transcript is difficult enough to justify the extra cost and latency.
- Do not claim that a model can infer private intent, verify truthfulness, or perform clinical assessment.

## Codex Strategy

Codex does not switch Claude models. Treat Codex routing as workflow routing.

The Codex implementation should improve reliability through repository structure, progressive disclosure, tests, and examples rather than cross-runtime model switching.

### Codex Workflow Routing

Use:

- Small prompts focused on one stage at a time.
- Tests after each stage.
- Concise skill descriptions for progressive disclosure.
- `AGENTS.md` for project-level working instructions.
- Examples for regression behavior.
- Narrow reference loading instead of loading all references at once.

Avoid:

- Loading all frameworks, references, templates, and examples into one prompt.
- Treating every analysis as forensic mode.
- Skipping the quality gate to save time.
- Claiming Codex can switch Claude models.
- Adding third-party model switcher plugins as a default recommendation.

### Codex Routing By Work Type

| Work type | Routing approach |
|---|---|
| Repository edits | Small staged edits, then `python -m unittest discover tests` |
| Skill discovery | Keep `description` concise and trigger-rich |
| Transcript analysis | Quality gate first, then load only needed frameworks/templates |
| Regression testing | Compare output against `examples/expected-outputs/` |
| Deep analysis | Use framework sequence, not all references at once |
| Documentation | Update docs and tests together when behavior changes |

## Frontmatter Examples

### Claude High-Effort Skill

Use this pattern for the main Claude skill when deep reasoning is the expected default and the runtime supports model/effort frontmatter.

```yaml
---
name: the-meeting-behind-the-meeting
description: Analyze transcripts, meeting notes, interviews, voice notes, decisions, action items, and risks with evidence discipline.
model: opusplan
effort: high
---
```

### Claude Lighter Sub-Skill Idea

Use this pattern only if a future package splits lightweight cleanup/classification into a separate sub-skill.

```yaml
---
name: meeting-transcript-cleanup
description: Clean up transcript formatting, classify source type, and prepare inputs for the quality gate.
model: haiku
effort: low
---
```

### Codex SKILL.md Description Optimized For Discovery

Codex initially loads name, description, and path, so the description should include trigger terms early.

```yaml
---
name: the-meeting-behind-the-meeting
description: Analyze transcript, meeting notes, conversation thread, interview, voice note, minutes, action items, decisions, and risks with evidence discipline.
---
```

## Maintenance Rules

- Keep model and effort guidance in docs, not scattered across templates.
- Keep Codex guidance about workflow routing, not Claude model switching.
- Prefer native runtime controls where available.
- Do not recommend random third-party model switcher plugins.
- Re-run repository tests after changing routing docs:

```bash
python -m unittest discover tests
```
