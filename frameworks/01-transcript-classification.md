# 01 - Transcript Classification

Classify the source before analysis. Classification controls which frameworks are relevant and how much structure to expect.

## Classification Rules

Assign one primary class and optional secondary tags. If the source contains multiple unrelated conversations, classify it as a mixed thread.

## Transcript Types

### Formal Meeting

A scheduled meeting with a clear agenda, multiple participants, and a business purpose.

Signals:

- Opening, agenda, or stated objective.
- Turn-taking around agenda items.
- Decisions, action items, or follow-up owners.

Default analysis:

- Factual reconstruction
- Decision accountability
- Risk register
- Next meeting playbook

### Executive or Management Meeting

A meeting involving senior decision makers, managers, or strategic tradeoffs.

Signals:

- Resource allocation, priorities, risk acceptance, escalation, or policy decisions.
- Participants reference teams, budgets, timelines, or executive stakeholders.

Default analysis:

- Decision quality
- Alignment and disagreement
- Accountability gaps
- Strategic risks

### Technical Meeting

A meeting focused on systems, engineering, product implementation, data, architecture, or operational details.

Signals:

- Technical dependencies, bugs, architecture, implementation tradeoffs, incidents, or design choices.
- Specialized terminology and unresolved technical questions.

Default analysis:

- Factual reconstruction
- Open questions
- Decision and delivery risks
- Owner, deadline, and output criteria

### Vendor or External Meeting

A meeting with customers, suppliers, partners, contractors, agencies, investors, or other outside parties.

Signals:

- Commercial commitments, scope, service levels, renewal, procurement, partnership, or negotiation.
- Participants represent different organizations.

Default analysis:

- Relationship risk
- Commitment clarity
- Negotiation signals
- Follow-up commitments

### One-to-One Conversation

A conversation between two people, often managerial, coaching, sales, feedback, or alignment oriented.

Signals:

- Two primary speakers.
- Personal ownership, feedback, negotiation, concern, or coaching.

Default analysis:

- Question and answer reconstruction
- Implied concerns with evidence
- Trust context
- Next conversation playbook

### Informal Discussion

An unscheduled or lightly structured discussion without a formal agenda.

Signals:

- Casual topic flow.
- Limited formal decisions.
- Brainstorming, venting, or early alignment.

Default analysis:

- Topic sequence
- Emerging themes
- Open items
- Follow-up opportunities

### Voice Note

A one-way or mostly one-way recording, dictated update, or asynchronous spoken message.

Signals:

- One dominant speaker.
- No live turn-taking.
- May contain pauses, corrections, or self-directed notes.

Default analysis:

- Message structure
- Explicit asks
- Risk and ambiguity
- Suggested response or follow-up

### Interview

A structured question-and-answer exchange for hiring, research, investigation, discovery, media, or customer learning.

Signals:

- Interviewer and respondent roles.
- Question sequences.
- Evidence, examples, experiences, or evaluation criteria.

Default analysis:

- Question and answer mapping
- Evidence quality
- Contradictions and follow-up probes
- Decision relevance

### Mixed Thread

A source containing multiple conversations, document fragments, chat exports, voice notes, or unrelated meetings.

Signals:

- Discontinuous speakers, topics, timestamps, or organizations.
- Multiple starts and endings.
- Conflicting context.

Default analysis:

- Segment the source first.
- Analyze only segments with enough integrity.
- Avoid whole-thread conclusions unless the segments are explicitly connected.
