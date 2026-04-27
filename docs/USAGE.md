# Usage

The Meeting Behind the Meeting analyzes transcripts, meeting notes, conversation threads, interviews, voice notes, minutes, action items, decisions, and risks.

Every run starts with the transcript quality gate. Output depth depends on transcript quality, reconstruction confidence, sentiment/tone confidence, and conversation integrity.

## Interactive Mode

Interactive Mode is the default. The skill first produces the Transcript Quality and Reliability Gate, then asks intake questions before deep analysis.

Use Interactive Mode when:

- You want the output tailored to a specific audience.
- The transcript may contain mixed conversations or missing context.
- Participant context notes may need to be created or updated.
- You need a clear split between public record and private intelligence notes.

After the intake questions, answer briefly or say `proceed with defaults`.

## Autonomous Mode

Use Autonomous Mode only when you want the skill to continue without waiting for intake answers.

Example prompt:

```text
Analyze this transcript in autonomous mode.
```

Default autonomous settings:

- Mode: Deep.
- Output audience: Personal use.
- Output type: Both public record and private intelligence notes.
- Date/time: Extract if present, otherwise mark unknown.
- Profiles: Generate participant context notes, but do not claim saved files unless file-write access exists.
- Sentiment: Use numeric confidence and evidence discipline.

## How To Force Full Forensic Analysis

Ask directly for full forensic analysis when the source may be mixed, disputed, contradictory, incomplete, or politically sensitive.

Example prompt:

```text
Run full forensic analysis on this mixed thread. Segment it first and do not merge unrelated conversations.
```

Forensic analysis still starts with the quality gate. If the source is too weak, the skill must limit analysis or stop and request cleaner input.

## How To Request Profile Updates

Ask for profile updates when you want participant context notes maintained from the transcript.

Example prompt:

```text
Create or update participant context notes for each named participant. Separate evidence from interpretation.
```

In Claude Desktop or Cowork, the skill may only be able to generate Participant Context Notes and Profile Update Blocks for manual saving. In Claude Code or Codex with file access, it may create or update files under `profiles/`, `outputs/`, `meetings/`, `conversations/`, or `voice-notes/` when requested.

## How To Request Public Record Vs Private Intelligence Notes

Use public record when the output may be shared with participants, management, clients, vendors, legal/compliance, or a team. Use private intelligence notes when the output is for personal preparation and should keep hypotheses, risks, and strategy separate from the official record.

Example prompts:

```text
Produce public record only.
```

```text
Produce both public record and private intelligence notes.
```

## Book Summary Reference Guides

The skill includes user-created book summary reference guides in `resources/book-summaries/`.

Use them as supporting lenses for:

- Behavioral observation caution.
- Communication style analysis.
- Trust and reliability signals.
- Influence and persuasion patterns.
- Culture and psychological safety signals.
- Voice, tone, and presence analysis.
- Nonverbal analysis when the transcript includes behavioral, visual, pause, interruption, or tone markers.

Use the references when:

- The transcript quality gate allows interpretation.
- The output needs deeper explanation of a signal.
- The analysis can cite transcript evidence first.
- The reference helps produce a practical recommended action.

Do not use the references when:

- The quality gate says to stop.
- The transcript does not contain evidence for the claim.
- The user asks for certainty about motives or truthfulness.
- The task only needs factual minutes, decisions, or action items.
- The output would reproduce book content instead of converting it into meeting analysis.

When using any book summary reference, keep the output structure evidence-based:

- Fact
- Signal
- Interpretation
- Alternative explanation
- Confidence
- Recommended action

## How To Provide Transcripts

Provide the cleanest source available:

- Raw transcript with speaker labels and timestamps when possible.
- Meeting notes with date, attendees, and source context.
- Conversation thread with clear separators between messages.
- Voice note transcript with pause, emphasis, or tone markers only if they were actually captured.
- Any participant context that is factual and relevant, such as role, company, decision authority, prior action items, or known meeting history.

If the transcript is incomplete, say what is missing. Do not ask the skill to fill gaps as fact.

## Quick Mode

Use Quick Mode when you need a compact operational readout.

Best for:

- Short meeting notes.
- Fast recap.
- Decision and action extraction.
- Low-risk follow-up.

Typical outputs:

- Quality badge.
- Bottom line.
- Decisions.
- Action items.
- Main risks.
- Immediate next steps.

Recommended template:

- `templates/01-one-page-intelligence-brief.md`

## Standard Mode

Use Standard Mode for normal meeting analysis.

Best for:

- Complete meeting transcripts.
- Internal project meetings.
- Customer, vendor, or stakeholder meetings.
- Follow-up planning.

Typical outputs:

- Quality assessment.
- Factual reconstruction.
- Decisions and actions.
- Accountability gaps.
- Risk register.
- Next meeting questions.

Recommended templates:

- `templates/02-meeting-minutes.md`
- `templates/05-decisions-actions.md`
- `templates/06-risk-register.md`

## Deep Mode

Use Deep Mode when the meeting has important decisions, unclear alignment, or meaningful follow-up risk.

Best for:

- Executive or management meetings.
- High-stakes vendor or customer meetings.
- Strategic planning.
- Cross-functional disagreement.

Typical outputs:

- Full quality assessment.
- Transcript classification.
- Factual reconstruction.
- Decision and accountability review.
- Risk register.
- Evidence-linked people dynamics.
- Said-vs-meant hypotheses with alternatives.
- Next meeting playbook.

Required evidence structure for advanced claims:

- Fact
- Signal
- Interpretation
- Alternative explanation
- Confidence
- Recommended action

Recommended templates:

- `templates/01-one-page-intelligence-brief.md`
- `templates/07-accountability-gap-review.md`
- `templates/08-said-vs-meant.md`
- `templates/09-next-meeting-playbook.md`

## Forensic Mode

Use Forensic Mode when the source may be mixed, contradictory, incomplete, or disputed.

Best for:

- Mixed conversation threads.
- Disputed summaries.
- Inconsistent meeting notes.
- Threads containing emails, chat, voice notes, and meeting fragments.

Mandatory steps:

1. Run `frameworks/00-transcript-quality-gate.md`.
2. Detect mixed content.
3. Split the source into candidate conversations or segments.
4. Analyze only segments with sufficient integrity.
5. Label uncertainty and stop conditions clearly.

Typical outputs:

- Segment map.
- Quality score per segment.
- What can be reconstructed.
- Contradictions.
- What cannot be concluded.
- Clarifying questions.

Recommended templates:

- `templates/00-quality-assessment.md`
- `templates/03-conversation-notes.md`
- `templates/06-risk-register.md`

## Follow-Up Mode

Use Follow-Up Mode after an analysis has already identified decisions, action items, open questions, or participant-specific next steps.

Best for:

- Sending a meeting recap.
- Preparing one-to-one follow-up.
- Aligning with absent stakeholders.
- Building the next meeting agenda.

Typical outputs:

- Participant email.
- Internal private notes.
- One-to-one prompts.
- Next meeting questions.
- Evidence to attach or cite.

Recommended template:

- `templates/10-follow-up-pack.md`

## Public Record Vs Private Intelligence Notes

Keep two output layers when needed.

### Public Record

Use for material that can be shared with participants.

Allowed:

- Decisions.
- Actions.
- Owners.
- Deadlines.
- Open questions.
- Neutral meeting summary.
- Confirmed risks.

Avoid:

- Speculation about motives.
- Sensitive people dynamics.
- Hypotheses about implied meaning.
- Private strategy notes.

### Private Intelligence Notes

Use for internal preparation and cautious planning.

Allowed:

- Evidence-linked hypotheses.
- Alternative explanations.
- Confidence levels.
- Relationship and alignment risks.
- Questions to ask privately.
- What not to say in the next meeting.

Rules:

- Do not present private notes as fact.
- Do not include diagnosis, deception claims, or certainty about private intent.
- Convert hypotheses into clarifying questions.

## Participant Context Notes

Participant context notes are created with `templates/11-participant-context-note.md`.

Create or update a note only from evidence:

- Basic information: name, role, organization, decision authority.
- Meeting history: dates, topics, commitments, outcomes.
- Communication observations: behavior in context, not personality.
- Open items: owner, deadline, status, evidence.
- Confidence: why the note is reliable or limited.

Update rules:

- Add new evidence, do not overwrite prior context without reason.
- Keep dated meeting history.
- Mark stale or contradicted observations.
- Treat the note as preparation context, not a fixed profile.
- Never infer personality, motive, honesty, or private intent.

## Mixed Conversations

Mixed conversations must be split before interpretation.

Split when the source contains:

- Multiple meetings.
- Unrelated email or chat threads.
- Voice note plus meeting transcript.
- Abrupt participant, project, date, or topic changes.
- Repeated timestamps or broken chronology.

For each segment:

- Assign a segment label.
- Identify participants.
- Identify source type.
- Score transcript quality.
- State whether analysis can proceed.

Do not make whole-thread conclusions unless the segments are explicitly connected.

## How Transcript Quality Affects Output Depth

### Full Proceed

Use when Transcript Quality Score and Reconstruction Confidence are both 75 or higher.

Allowed:

- Full factual reconstruction.
- Decisions and action review.
- Risk register.
- People dynamics.
- Said-vs-meant hypotheses with alternatives.
- Next meeting playbook.

### Limited Proceed

Use when either score is 60-74.

Allowed:

- Summary.
- Decisions and actions.
- Open questions.
- Low-confidence signals.

Avoid:

- Strong tone claims.
- Strong implied-meaning claims.
- Trust or influence conclusions beyond direct evidence.

### Minimal Proceed

Use when either score is 40-59.

Allowed:

- Basic summary.
- Missing information list.
- Known facts.
- Transcript cleanup recommendations.

Avoid:

- Advanced interpretation.
- Tone analysis unless directly annotated.
- Stakeholder inference.

### Do Not Proceed

Use when a stop condition applies.

Output only:

- Why analysis cannot proceed.
- Quality issues found.
- What input is needed next.
