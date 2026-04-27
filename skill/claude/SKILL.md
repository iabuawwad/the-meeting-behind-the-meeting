---
name: the-meeting-behind-the-meeting
description: Use for transcript, meeting notes, conversation thread, interview, voice note, minutes, action items, decisions, and risks that need evidence-based meeting intelligence.
---

# The Meeting Behind the Meeting

Use this skill for transcript, meeting notes, conversation thread, interview, voice note, minutes, action items, decisions, and risks.

Default mode is Interactive Deep Mode. Run the transcript quality gate first and keep every advanced claim evidence-based.

Do not proceed directly into full analysis unless the user explicitly requests autonomous mode, says proceed with defaults, or says do not ask questions. Otherwise, after reading the transcript, produce the Transcript Quality and Reliability Gate, ask the Intake Questions, then stop and wait for answers.

# Transcript Quality and Reliability Gate

Required fields:

- Transcript Quality Score: XX / 100
- Reconstruction Confidence: XX / 100
- Sentiment and Tone Confidence: XX / 100
- Conversation Integrity: Single meeting / Single conversation / Voice note / Mixed thread / Multiple conversations / Unclear
- Source Type: human transcript / auto transcript / chat thread / voice note / unknown
- Main Quality Issues
- Risk of Misinterpretation
- Recommended Handling
- Proceed Level: Full analysis / Proceed with caution / Limited analysis only / Stop and clean transcript first

# Intake Questions

Unless the user requested autonomous mode, ask:

1. Is this a formal meeting, informal conversation, voice note, interview, or mixed thread?
2. Is it internal, external, or mixed?
3. Who are you in the transcript?
4. What is your objective: official minutes, private intelligence, follow-up strategy, personal communication review, or full forensic analysis?
5. Should participant context notes/profiles be created or updated?
6. Is the date/time known, should it be entered manually, or should it be skipped?
7. Who is the output for: personal use, management, legal/compliance, client/vendor, team, or public record?
8. Should the skill produce public record only, private intelligence notes only, or both?

Then stop and wait for user answers.

## Autonomous Mode Defaults

Use these only when autonomous mode, proceed with defaults, or no-questions mode is explicit:

- Mode: Deep
- Output audience: Personal use
- Output type: Both public record and private intelligence notes
- Date/time: Extract if present, otherwise mark unknown
- Profiles: Generate participant context notes but do not claim file persistence unless file-write access exists
- Sentiment: Use confidence rating and evidence discipline

## Full Layer Stack

After intake, run these layers in order:

0. Transcript Quality and Reliability Gate
1. Intake and Scope Confirmation
2. Transcript Type Classification
3. Mixed Conversation Detection and Segmentation
4. Context and Participant Discovery
5. Participant Context/Profile Check
6. Title, Date, Metadata, and Meeting Identity
7. Factual Reconstruction
8. Public Record
9. Private Intelligence Notes
10. Formal Minutes or Conversation Notes
11. Decisions and Actions
12. Action Quality Review
13. Accountability Gap Analysis
14. Risk Register
15. Decision Integrity Review
16. Influence and Participation Map
17. Communication Style Signals
18. Trust and Behaviour Prediction
19. Culture and Psychological Safety Review
20. Voice, Tone, and Presence Review
21. Nonverbal and Behavioural Signals Review only when evidence exists
22. Said-vs-Meant Analysis
23. Red Flags and Missed Signals
24. Questions That Should Have Been Asked
25. Personal Communication Review if user is identified
26. One-Page Intelligence Brief
27. Next-Meeting Playbook
28. Follow-Up Pack
29. Participant Context Notes / Profile Updates
30. Save or Export Guidance based on platform capability

## Platform Capability

In Claude Desktop or Cowork, file-write access may not be available. If file-write access is not available, generate "Participant Context Notes" and "Profile Update Blocks" for the user to save manually.

In Claude Code or Codex with file access, create or update files only when requested under `profiles/`, `outputs/`, `meetings/`, `conversations/`, or `voice-notes/`.

## Navigation

- Quality gate: `frameworks/00-transcript-quality-gate.md`
- Classification: `frameworks/01-transcript-classification.md`
- Evidence standard: `frameworks/02-evidence-confidence-standard.md`
- Factual reconstruction: `frameworks/03-factual-reconstruction.md`
- Decisions and accountability: `frameworks/04-decision-accountability.md`
- Risks: `frameworks/05-risk-register.md`
- Said-vs-meant: `frameworks/06-said-vs-meant.md`
- Communication style: `frameworks/07-communication-style.md`
- Trust signals: `frameworks/08-trust-behaviour-prediction.md`
- Influence and participation: `frameworks/09-influence-participation.md`
- Culture and safety: `frameworks/10-culture-psychological-safety.md`
- Voice and tone: `frameworks/11-voice-tone-presence.md`
- Nonverbal signals: `frameworks/12-nonverbal-behavioural-signals.md`
- Next meeting: `frameworks/13-next-meeting-playbook.md`

Use templates from `templates/` and references from `references/` only as needed. Use `resources/book-summaries/` as supporting lenses; do not quote long sections, do not reproduce book content in outputs, and convert reference material into evidence-based analysis.

Always separate fact, signal, interpretation, alternative explanation, confidence, and recommended action. Never present behavioral interpretation as fact.
