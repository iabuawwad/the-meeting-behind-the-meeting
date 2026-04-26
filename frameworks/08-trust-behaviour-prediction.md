# 08 - Trust Behaviour Prediction

Use this framework to assess trust signals in a specific working context. Trust is not a character judgment.

## Core Rule

Trust assessment must be limited to the relationship, task, and evidence in the transcript. Do not claim that a person is trustworthy or untrustworthy in general.

## Trust Dimensions

### Vesting

What the person has at stake.

Signals:

- Ownership of outcome
- Public commitment
- Resource contribution
- Reputational exposure

Question:

- What does this participant gain or lose if the commitment succeeds or fails?

### Longevity

Whether the relationship or work is likely to continue.

Signals:

- Future meetings
- Renewal or long-term partnership
- Ongoing dependencies
- References to past collaboration

Question:

- Does the participant have reason to preserve long-term trust?

### Reliability

Evidence of follow-through in this context.

Signals:

- Completed past actions
- Clear ownership
- Specific commitments
- Acknowledged constraints

Question:

- Has this participant shown task-specific follow-through?

### Actions

Observable behavior over claims.

Signals:

- Takes ownership
- Provides resources
- Resolves blockers
- Confirms decisions in writing

Question:

- Do actions match stated commitments?

### Language

Commitment strength and clarity.

Signals:

- Specific verbs and deadlines
- Conditional language
- Vague agreement
- Passive phrasing

Question:

- Does the language create a usable commitment?

### Stability

Consistency across the transcript.

Signals:

- Stable position
- Clear criteria for changes
- No unexplained reversal
- Consistent explanation of constraints

Question:

- Are changes explained by new facts or unexplained shifts?

## Output Format

```markdown
### Context-Specific Trust Signal

- Context:
- Evidence:
- Dimension:
- Interpretation:
- Alternative explanation:
- Confidence:
- Practical implication:
```

## Guardrails

- Do not label a person's character.
- Do not predict behavior outside the specific context.
- Do not infer dishonesty.
- Treat weak transcript quality as a reason to reduce confidence.
