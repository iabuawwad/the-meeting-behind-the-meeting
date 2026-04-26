# 00 - Transcript Quality Gate

Use this gate before any substantive meeting analysis. The goal is to decide whether the transcript can support factual reconstruction, tone analysis, and cautious interpretation.

## Required Scores

### Transcript Quality Score

Score out of 100. Assess whether the transcript is complete, readable, speaker-attributed, and internally coherent.

- 90-100: Clean transcript with reliable speaker labels, complete exchanges, and minimal noise.
- 75-89: Usable transcript with minor gaps, occasional unclear labels, or light cleanup needed.
- 60-74: Partially usable transcript with meaningful gaps, unclear speaker turns, or missing context.
- 40-59: Weak transcript. Factual reconstruction may be possible, but interpretation should be limited.
- 0-39: Not reliable enough for meeting-dynamics analysis.

### Reconstruction Confidence

Score out of 100. Assess how confidently the agent can reconstruct what happened.

- Speaker identity confidence
- Topic order confidence
- Question and answer pairing confidence
- Decision and commitment confidence
- Ability to distinguish meeting content from transcript artifacts

### Sentiment and Tone Confidence

Score out of 100. Assess whether the input includes enough evidence for tone or sentiment.

- Text-only transcripts usually support limited tone confidence.
- Tone markers, pauses, interruptions, emphasis notes, or audio-derived annotations can increase confidence.
- Do not infer emotion from ordinary disagreement without evidence.

## Conversation Integrity Check

Before analysis, check for:

- Missing beginning, middle, or ending.
- Speaker turns that appear out of order.
- Abrupt topic jumps without transition.
- Duplicated sections.
- Contradictory timestamps.
- Participants referenced but absent from the transcript.
- Decisions mentioned without the prior discussion.
- Replies that do not answer the preceding question.

## Mixed Transcript Detection

Flag possible mixed transcripts when:

- Speaker names, companies, projects, or dates change without explanation.
- The same participant appears under multiple labels.
- Topic continuity breaks sharply.
- The transcript includes unrelated meetings, chat exports, voice notes, or email fragments.
- Timestamps reset or overlap in ways that cannot be explained.

When mixed content is likely, separate the transcript into candidate segments before analysis. If segmentation is not possible, stop or ask for a cleaner source.

## Stop Conditions

Stop advanced analysis when any condition applies:

- Transcript Quality Score below 40.
- Reconstruction Confidence below 50.
- Mixed transcript cannot be separated.
- The user asks for clinical mental-health assessment, truthfulness certainty, or certainty about private intent.
- The source lacks enough meeting content to identify speakers, topics, or decisions.
- Legal, medical, employment, or disciplinary conclusions are requested without appropriate human review.

## Proceed Levels

### Full Proceed

Use when Transcript Quality Score and Reconstruction Confidence are both 75 or higher.

Allowed:

- Factual reconstruction
- Decision and accountability analysis
- Risk register
- Communication and participation patterns
- Evidence-linked interpretations with confidence labels

### Limited Proceed

Use when either score is 60-74.

Allowed:

- Factual reconstruction with caveats
- Open items and decision logs
- Low-confidence signals
- Clarifying questions

Avoid:

- Strong tone claims
- Strong implied-meaning claims
- Trust or influence conclusions beyond direct evidence

### Minimal Proceed

Use when either score is 40-59.

Allowed:

- Basic summary
- Known facts
- Missing information list
- Transcript cleanup recommendations

Avoid:

- Advanced interpretation
- Tone analysis unless directly annotated
- Stakeholder inference

### Do Not Proceed

Use when any stop condition applies.

Output:

- Reason analysis cannot proceed
- Quality issues found
- What input is needed next
