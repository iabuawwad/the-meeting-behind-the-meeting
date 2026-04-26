---
name: the-meeting-behind-the-meeting
description: Analyze transcript, meeting notes, conversation thread, interview, voice note, minutes, action items, decisions, and risks with evidence discipline.
---

# The Meeting Behind the Meeting

Use this skill for a transcript, meeting notes, conversation thread, interview, voice note, minutes, action items, decisions, or risks when the user needs the practical meeting dynamics behind the formal record.

## Mandatory First Step

Run the transcript quality gate before any other analysis:

- `frameworks/00-transcript-quality-gate.md`
- Output template: `templates/00-quality-assessment.md`

If the gate says to stop, do not continue into interpretation. Explain the quality issue and what input is needed.

## Workflow Routing

For Codex, route the workflow by task and evidence level. Keep routing language about workflow selection, not model switching.

- Classify the source: `frameworks/01-transcript-classification.md`
- Apply claim discipline: `frameworks/02-evidence-confidence-standard.md`
- Reconstruct facts: `frameworks/03-factual-reconstruction.md`
- Review decisions and actions: `frameworks/04-decision-accountability.md`
- Register risks: `frameworks/05-risk-register.md`
- Analyze implied meaning cautiously: `frameworks/06-said-vs-meant.md`
- Map communication style: `frameworks/07-communication-style.md`
- Assess context-specific trust signals: `frameworks/08-trust-behaviour-prediction.md`
- Analyze influence and participation: `frameworks/09-influence-participation.md`
- Review culture and psychological safety signals: `frameworks/10-culture-psychological-safety.md`
- Use tone only when supported: `frameworks/11-voice-tone-presence.md`
- Use nonverbal analysis only with markers: `frameworks/12-nonverbal-behavioural-signals.md`
- Prepare the next meeting: `frameworks/13-next-meeting-playbook.md`

## References

Use references only when needed:

- Reference map: `references/reference-engine-map.md`
- Body language and kinesics: `references/body-language-julius-fast.md`
- Emotional intelligence and observation caution: `references/body-language-kate-davis.md`
- Communication styles: `references/people-styles.md`
- Trust and predictability: `references/sizing-people-up.md`
- Voice and presence: `references/voice-tone-presence.md`
- Influence and persuasion: `references/influence-persuasion.md`
- Culture and safety: `references/culture-code.md`
- Nonverbal signal discipline: `references/what-every-body-is-saying.md`

## Book Summary References

Use `resources/book-summaries/` as supporting lenses. Do not quote long sections. Do not reproduce book content in outputs. Convert reference material into evidence-based analysis.

Always separate fact, signal, interpretation, alternative explanation, confidence, and recommended action.

## Templates

Choose the narrowest template that fits:

- Quality assessment: `templates/00-quality-assessment.md`
- One-page brief: `templates/01-one-page-intelligence-brief.md`
- Meeting minutes: `templates/02-meeting-minutes.md`
- Conversation notes: `templates/03-conversation-notes.md`
- Voice note analysis: `templates/04-voice-note-analysis.md`
- Decisions and actions: `templates/05-decisions-actions.md`
- Risk register: `templates/06-risk-register.md`
- Accountability gaps: `templates/07-accountability-gap-review.md`
- Said vs meant: `templates/08-said-vs-meant.md`
- Next meeting playbook: `templates/09-next-meeting-playbook.md`
- Follow-up pack: `templates/10-follow-up-pack.md`
- Participant context note: `templates/11-participant-context-note.md`

## Evidence Rules

- Separate fact, signal, interpretation, alternative explanation, confidence, and recommended action.
- Never present behavioral interpretation as fact.
- Do not claim private-thought access, truthfulness certainty, clinical mental-health assessment, or certainty about private intent.
- Keep tone, sentiment, and nonverbal claims limited to evidence available in the source.

## Repository Editing Rule

When editing this repository, do not skip test gates. Run the relevant validation or explain why it cannot be run.
