# The Meeting Behind the Meeting

## Normal User Installation

Download the release asset ZIP, not the GitHub source ZIP.

Do not download the GitHub source ZIP for Claude installation. The source ZIP contains multiple package layouts and multiple `SKILL.md` files, so Claude Skill upload can fail. Normal users should use one of these release assets:

- `the-meeting-behind-the-meeting-skill-v0.2.3.zip`
- `the-meeting-behind-the-meeting-plugin-v0.2.3.zip`

For most users, use the Skill ZIP.

1. Open Claude Desktop.
2. Go to Customize > Skills > Upload a skill.
3. Upload `the-meeting-behind-the-meeting-skill-v0.2.3.zip`.
4. Use `/the-meeting-behind-the-meeting` and attach or paste a transcript.
5. The skill will guide you step by step.

Cowork path:

1. Install the skill ZIP first and use it in Cowork where skills are available.
2. Or test `the-meeting-behind-the-meeting-plugin-v0.2.3.zip` from GitHub Releases when Cowork plugin upload is available in your Claude Desktop build.

Version: `0.2.3`  
Slug: `the-meeting-behind-the-meeting`

The Meeting Behind the Meeting is an Agent Skill for analyzing meeting transcripts, notes, and prep material to surface the practical dynamics that shape a meeting: decision pressure, stakeholder positions, unresolved concerns, alignment gaps, follow-up risks, and what needs to happen before or after the formal agenda.

It is built for evidence-based meeting analysis. It does not claim private-thought access, truthfulness certainty, clinical assessment, or hidden intent as fact.

## What It Does

This skill helps an agent:

- Check whether the source transcript or notes are reliable enough to analyze.
- Identify explicit decisions, open questions, objections, commitments, and ownership.
- Separate what was said from cautious interpretation of meeting dynamics.
- Map stakeholder alignment, tension, silence, escalation points, and follow-up risk.
- Produce structured outputs that can support meeting prep, debriefs, and next-step planning.

## Why Transcript Quality Is Checked First

Transcript quality controls the reliability of every downstream conclusion. Poor diarization, missing context, unclear speakers, fragmented audio, or incomplete notes can make ordinary disagreement look like misalignment or make a key commitment disappear.

For that reason, the skill starts with a transcript quality gate. If the input is weak, the agent must lower confidence, ask for clarification, or limit the analysis to observable facts. Interpretation should never outrun the evidence.

## Why the skill asks questions first

The skill is designed to avoid shallow or overconfident analysis. It first rates transcript reliability with numeric scores for transcript quality, reconstruction confidence, and sentiment/tone confidence.

Unless autonomous mode is requested, it asks intake questions before deep analysis. That improves accuracy, profile handling, output relevance, and the separation between public record material and private intelligence notes.

## Core Outputs

The intended output contract includes:

- Transcript quality assessment
- Executive meeting summary
- Decision and commitment log
- Stakeholder alignment map
- Hidden-agenda risk hypotheses, clearly labeled as hypotheses
- Open questions and missing context
- Pre-meeting or post-meeting action plan
- Evidence table linking claims to transcript excerpts or notes

## Book Summary Reference Guides

The skill includes user-created book summary reference guides under `resources/book-summaries/`.

These guides strengthen the behavioral, communication, trust, influence, voice, nonverbal, and culture analysis layers. They are supporting reference material only. They are not full books, not official publications from the original authors or publishers, and not substitutes for reading the original books.

## Supported Platforms

This repository is structured to support:

- Claude Code local skill installation
- Claude Cowork plugin packaging
- ChatGPT Codex skill installation

Platform behavior can change. Do not invent platform-specific facts. Verify packaging, installation, and model-routing details against current official platform documentation before publishing release instructions.

## Repository Structure

```text
.
├── .agents/                 # Local Codex skill install layout
├── .claude/                 # Local Claude Code skill install layout
├── .github/workflows/       # Repository validation workflow
├── docs/                    # Installation, usage, testing, release, and versioning docs
├── examples/                # Sample transcripts and expected outputs
├── frameworks/              # Analysis frameworks loaded as needed
├── references/              # Longer domain references loaded as needed
├── resources/book-summaries/ # User-created book summary reference guides
├── skill/claude/            # Claude Code package source
├── skill/codex/             # Codex package source
├── skill/cowork-plugin/     # Claude Cowork plugin package source
├── templates/               # Reusable output templates
└── tests/                   # Validation tests
```

## Responsible-Use Guardrails

- Treat behavioral interpretation as a hypothesis, not a fact.
- Cite evidence for material claims.
- Preserve uncertainty when the transcript is incomplete or ambiguous.
- Avoid clinical mental-health claims, truthfulness certainty, protected-class inference, or claims about private mental states.
- Do not use the skill to manipulate participants or bypass consent.
- Prefer practical meeting outcomes: clarity, accountability, follow-up quality, and decision hygiene.
