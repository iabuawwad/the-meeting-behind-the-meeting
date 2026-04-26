Transcript Quality Score: 58/100 - Limited proceed after segmentation

Reconstruction Confidence: 54/100 overall; varies by segment

Sentiment and Tone Confidence: 20/100

Conversation Integrity: Concern

# Mixed Conversation Thread - Expected Output

## Quality Gate

- Issues detected:
  - The source contains multiple unrelated segments.
  - Segment types include chat, voice note transcript, meeting notes, and unclear fragment.
  - Segment D has no timestamp, speaker identity, or context.
- Recommended handling: Split the source and analyze each segment separately. Do not create one combined meeting conclusion.
- Disclaimer: This output identifies segment boundaries and limited evidence-supported findings. It does not infer private intent or connect unrelated segments without evidence.

## Mixed Thread Detection

The source is a mixed conversation thread.

Detected segments:

| Segment | Type | Topic | Integrity | Proceed level |
|---|---|---|---|---|
| A | Chat thread | Vendor renewal | Good | Limited-to-standard segment analysis |
| B | Voice note | Prototype demo issue | Good for voice-note analysis | Limited segment analysis |
| C | Meeting notes | Office move planning | Good but summarized | Limited-to-standard segment analysis |
| D | Unclear fragment | Unknown | Poor | Do not analyze |

## Segment A - Vendor Renewal

### Known Facts

- Lina asks whether the vendor renewal is planned for Friday.
- Omar says Finance approved renewal if the monthly cap stays unchanged.
- Lina says she will ask Legal to confirm the data-processing clause by Thursday afternoon.
- Omar says not to send the renewal notice until Legal confirms.

### Decisions And Actions

| Item | Owner | Deadline | Evidence |
|---|---|---|---|
| Confirm data-processing clause | Lina | Thursday afternoon | Lina states she will ask Legal |
| Hold renewal notice until Legal confirms | Not fully assigned | Before notice is sent | Omar says not to send until confirmation |

### Risks

- Legal/compliance risk if renewal notice is sent before clause confirmation.
- Financial risk if monthly cap changes.

## Segment B - Voice Note

### Known Facts

- Kai says the prototype froze twice when switching accounts.
- Kai recommends not showing that workflow in tomorrow's customer call.
- Kai asks engineering to check the account-switching issue today.
- Kai asks for guidance on what is safe to demo.

### Recommended Handling

Use voice-note analysis, not formal minutes.

Action needed:

- Engineering should confirm whether account switching is safe to demo today.

## Segment C - Office Move Notes

### Known Facts

- Facilities needs the seating list by Wednesday.
- HR can send a draft seating list by Tuesday afternoon.
- Final floor map depends on accessibility review.
- A decision is recorded to use the smaller training room as overflow if the review is not done by Friday.

### Decisions And Actions

| Item | Owner | Deadline | Evidence |
|---|---|---|---|
| Send draft seating list | HR / Dev | Tuesday afternoon | Dev states HR can send it |
| Use smaller training room as overflow if needed | Mira / group unclear | Friday condition | Mira states decision |

## Segment D - Unclear Fragment

Do not analyze. It lacks speaker identity, timestamp, topic, and connection to the other segments.

## Recommendation

Create separate outputs:

1. Vendor renewal decision/action note.
2. Prototype demo voice-note action note.
3. Office move meeting note.
4. Exclude or re-source Segment D before analysis.
