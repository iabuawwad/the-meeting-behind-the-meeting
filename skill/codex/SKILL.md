---
name: the-meeting-behind-the-meeting
description: Analyze meeting transcripts, conversation threads, interviews, and voice notes using transcript reliability scoring, structured notes, decisions, risks, communication signals, and next-step strategy.
---

# The Meeting Behind the Meeting

Use this skill for transcript, meeting notes, conversation thread, interview, voice note, minutes, action items, decisions, and risks.

Normal invocation should be enough. If the user invokes `/the-meeting-behind-the-meeting` and attaches or pastes a transcript, run the Transcript Quality and Reliability Gate first, then start the Guided Intake Wizard, then wait for user answers unless autonomous mode is requested. The user should not need to provide a long instruction prompt.

Default mode is Interactive Deep Mode. Run the transcript quality gate as the first reliability step. Keep model routing guidance in this body and in `docs/MODEL_ROUTING.md`, not in YAML frontmatter.

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

# Guided Intake Wizard

Ask one question at a time. Show progress as `Question X of Y`. Provide numbered choices, allow free-text answers, show a recommended default when confidence is sufficient, and accept `default`, `skip`, or `proceed with defaults`.

After the final question, show a short Wizard Scope Summary and ask for confirmation before full analysis.

Question 1 of 8: Transcript type
1. Formal meeting
2. Informal conversation
3. Voice note
4. Interview
5. Mixed thread / multiple conversations
6. Not sure, infer from transcript
Recommended: [based on transcript]

Question 2 of 8: Context
1. Internal
2. External
3. Mixed
4. Personal
5. Legal / advisory
6. Not sure, infer from transcript
Recommended: [based on transcript]

Question 3 of 8: User identity
1. I am Speaker 1
2. I am Speaker 2
3. I am Speaker 3
4. I am not in the transcript
5. Use the name I provide
6. Not sure, infer from transcript
Recommended: [based on transcript]

Question 4 of 8: Main objective
1. Official meeting minutes
2. Private intelligence notes
3. Follow-up strategy
4. Negotiation / decision playbook
5. Personal communication review
6. Full forensic analysis
7. All of the above
Recommended: Full forensic analysis when the transcript involves important decisions, legal, HR, vendor, management, or sensitive matters.

Question 5 of 8: Output audience
1. Personal use only
2. Team use
3. Management update
4. Legal / compliance
5. Client / vendor
6. Public or shareable record
Recommended: Personal use only unless user says otherwise.

Question 6 of 8: Output type
1. Public record only
2. Private intelligence notes only
3. Both public record and private intelligence notes
Recommended: Both.

Question 7 of 8: Participant context notes
1. Create participant context notes
2. Update existing participant context notes if available
3. Create profile update blocks only
4. Skip participant notes
Recommended: Create profile update blocks in Claude Desktop/Cowork because file-write access may be unavailable.

Question 8 of 8: Date and time
1. Extract from transcript
2. I will enter manually
3. Mark as unknown
4. Skip date/time
Recommended: Extract if present, otherwise mark unknown.

## Conditional Follow-Up Questions

Ask only if needed:

- If the transcript appears incomplete: "The transcript appears to end mid-sentence. Do you have a continuation?"
- If multiple conversations are detected: ask whether to split and analyze separately.
- If speaker identity is unclear: ask the user to map speakers.
- If legal/compliance output is requested: ask whether analysis should be fact-only or include private strategy notes.

## Autonomous Mode

If the user says `autonomous mode`, `proceed with defaults`, `do not ask questions`, or `run full analysis now`, skip the wizard and use:

- Mode: Deep
- Context: inferred
- User identity: inferred if possible, otherwise unknown
- Output audience: personal use
- Output type: both public record and private intelligence notes
- Participant context: profile update blocks only
- Date/time: extract if present, otherwise unknown

## Full Layer Stack

After confirmed intake or autonomous defaults, run these layers in order:

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
