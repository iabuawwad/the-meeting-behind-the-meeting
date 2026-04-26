# Testing

Use this document to manually test The Meeting Behind the Meeting across transcript types and output modes.

## Expected First Output

Every transcript analysis must start with the quality gate.

The first output must include:

- Transcript Quality Score
- Reconstruction Confidence
- Sentiment and Tone Confidence
- Conversation Integrity Check
- Issues detected
- Recommended handling
- Disclaimer

If an output begins with interpretation, risks, decisions, or people dynamics before the quality gate, the test fails.

## Exact Test Prompts

### 1. Run Quality Gate Only

```text
$the-meeting-behind-the-meeting Run quality gate only on this transcript. Do not continue into decisions, risks, tone, or people dynamics.
```

### 2. Run Full Deep Mode

```text
$the-meeting-behind-the-meeting Run full deep mode on this transcript. Start with the quality gate, then produce factual reconstruction, decisions, actions, risks, said-vs-meant hypotheses, people dynamics, and a next-meeting playbook.
```

### 3. Run Forensic Mode On Mixed Thread

```text
$the-meeting-behind-the-meeting Run forensic mode on this mixed conversation thread. Start with the quality gate, detect mixed content, split the thread into segments, and only analyze segments with enough integrity.
```

### 4. Generate Follow-Up Pack

```text
$the-meeting-behind-the-meeting Generate a follow-up pack from this meeting. Include participant email, internal private notes, one-to-one follow-up prompts, and next-meeting questions. Start with the quality gate.
```

### 5. Create Participant Context Note

```text
$the-meeting-behind-the-meeting Create a participant context note for [participant name] using only evidence from this transcript and prior notes. Include basic information, meeting history, communication observations, open items, evidence, and confidence.
```

For Claude surfaces, replace `$the-meeting-behind-the-meeting` with `/the-meeting-behind-the-meeting`.

## Manual Test Cases

### Test Transcript: Good Meeting

Use this sample:

```text
Title: Website Launch Review
Date: 2026-04-20
Attendees: Maya Chen, Omar Patel, Lina Brooks

Maya: The goal today is to confirm whether we can launch the website on May 10.
Omar: Engineering can support May 10 if final copy is frozen by April 27.
Lina: Marketing can freeze copy by April 26, but legal still needs to review the privacy page.
Maya: Who owns the legal review?
Lina: I will send the privacy page to legal today and get approval by April 29.
Omar: If legal approval arrives by April 29, engineering can deploy staging by May 3.
Maya: Decision: we keep May 10 as the launch date, conditional on legal approval by April 29 and staging by May 3.
Lina: Agreed.
Omar: Agreed.
Maya: I will send the recap after this meeting.
```

Expected:

- Quality gate first.
- High transcript quality.
- Formal or management meeting classification.
- Confirmed conditional decision.
- Action owner and deadline for Lina.
- Action owner and deadline for Omar.
- Legal approval dependency.
- No unsupported tone or nonverbal claims.

### Test Transcript: Poor Transcript

Use this sample:

```text
Speaker 1: yeah so that thing is probably fine
Speaker 2: wait no
Speaker ?: [inaudible]
Speaker 1: as discussed before
Speaker 3: but they said not to
[missing 12 minutes]
Speaker 2: ok we are agreed then
```

Expected:

- Quality gate first.
- Low transcript quality.
- Low reconstruction confidence.
- Conversation integrity concerns.
- No confirmed decision unless stated as uncertain.
- Output should stop or proceed minimally.
- Clarifying input requested.

### Test Transcript: Mixed Conversation Thread

Use this sample:

```text
Thread export:

Mon 09:00 - Priya: Can we confirm the vendor contract renewal today?
Mon 09:02 - Sam: Finance approved the renewal if the data-processing clause stays unchanged.
Mon 09:05 - Priya: I will ask Legal to confirm the clause by Friday.

---

Voice note transcript:
Alex: Quick note, the customer demo crashed twice yesterday. I need engineering to check the auth service before tomorrow.

---

Meeting notes:
Project: Office move
Rina: Facilities needs the seating list by Thursday.
Noah: HR will send it by Wednesday afternoon.
```

Expected:

- Quality gate first.
- Mixed transcript detection.
- Segment split into vendor renewal, voice note, and office move.
- Separate quality and classification per segment.
- No whole-thread conclusion unless clearly linked.
- Forensic mode should state what cannot be concluded.

### Test Transcript: Voice Note

Use this sample:

```text
Voice note from Dana:
I just left the client call. They are not blocking the renewal, but they sounded worried about the support response time. Please do not send pricing yet. First, can someone pull the last three support tickets and draft a short response plan? I would like to send it before Thursday.
```

Expected:

- Quality gate first.
- Voice note classification.
- Intent identified as renewal follow-up and support concern.
- Key points extracted.
- Emotional load only if supported by wording, with limited confidence.
- Next actions: pull support tickets, draft response plan, send before Thursday.
- No claim that the client is hiding intent.

## Regression Checklist

Run this checklist after editing `SKILL.md`, `frameworks/`, `references/`, `templates/`, or docs:

- Quality gate appears first in every test output.
- Transcript quality controls output depth.
- Mixed threads are split before interpretation.
- Advanced claims include fact, signal, interpretation, alternative explanation, confidence, and recommended action.
- Tone analysis is absent unless tone evidence exists.
- Nonverbal analysis is absent unless behavioral, visual, pause, interruption, or tone markers exist.
- Decisions are separated from candidate decisions.
- Actions include owner, deadline, output criteria, and dependency where possible.
- Public record and private notes remain separated when sensitive dynamics are included.
- Participant context notes are evidence-based and do not become fixed profiles.
- No output claims private-thought access, truthfulness certainty, clinical mental-health assessment, or certainty about private intent.

## Failure Conditions

A test fails if the skill:

- Skips the quality gate.
- Treats weak transcript content as reliable.
- Analyzes a mixed thread as one conversation without segmentation.
- Presents interpretation as fact.
- Claims deception, diagnosis, personality certainty, or hidden intent certainty.
- Infers tone from plain text without support.
- Performs nonverbal analysis without behavioral or delivery markers.
- Invents owners, deadlines, decisions, participants, or platform facts.
- Produces follow-up messages that include private intelligence notes as public record.
- Ignores stop conditions from `frameworks/00-transcript-quality-gate.md`.

## Repository Tests

Run local validation after documentation or packaging edits:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
python3 -m json.tool skill/cowork-plugin/plugin.json
```
