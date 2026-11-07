# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 16:16
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `10bd9b5b-7cbd-4fbc-b757-bb7db5a87273` | human | 0.430 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `db6ba125-0aeb-4a93-be85-58c885a2f69d` | unsure | 0.270 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d1291b3a-ce2b-45e4-86f3-1afd0e64dc6e` | unsure | 0.020 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `00873808-cb60-4e11-aa44-491cc17b5206` | unsure | 0.020 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `90e02ef9-278e-4e1f-9fe8-830b3eda67fe` | human | 0.420 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ad4d414d-4422-440e-a3fc-e24aa60cbd99` | human | 0.310 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `9921d657-a570-4cad-b496-915d81aa55ff` | unsure | 0.080 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `b3d3d248-4e2d-45f9-bcc7-ad114b3f50d3` | human | 0.470 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `7a288699-8056-4c45-810e-b68d8022b70d` | unsure | 0.000 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `159a5561-e0d1-44b6-9c6e-6b0a8e4b3752` | ai | 0.490 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `5ecf5b57-de5b-4b53-9a0a-017b98ac6580` | unsure | 0.040 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `e272c3d6-df80-4ddb-a21a-db1f5114a8f0` | unsure | 0.160 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `3478500d-1fff-44ca-95ce-b71ea1bf0299` | unsure | 0.180 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `4e316c8c-8f08-48dc-898d-795e9ae2e088` | unsure | 0.170 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `535ccc71-f2bc-4779-a5ac-099597b46287` | unsure | 0.270 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `eaf869a2-fc10-43a9-8d82-5752484463b9` | unsure | 0.020 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `4f052919-ec6b-45f1-9309-792834af8d6f` | unsure | 0.060 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `b869f05e-f560-4202-a77b-2ab54eaf5157` | human | 0.450 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `bd7046e6-d0bb-4570-93e6-0b6c9071da15` | human | 0.380 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `3ba01569-222b-4962-b7e0-78b9d400b0c4` | human | 0.620 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `952d3ca9-9ef9-42dc-8aef-c3e8a088197b` | unsure | 0.100 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `f1c8f461-0726-4ebe-83a2-f6f44b10eb23` | unsure | 0.180 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d16c86b1-5a1f-40ed-8866-ffa41d7cdd06` | unsure | 0.050 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `29945df2-18b4-4e4b-b893-c9e0d285afb8` | unsure | 0.090 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `03e44b64-6f95-4f11-9a82-021ee66c6607` | human | 0.680 |  |
| MF04 | malformed | text is only punctuation | 200 | `04856e98-3c70-4c84-9795-d296d0787c5a` | human | 0.360 |  |
| MF05 | malformed | text is a very long single word | 200 | `4c8e514d-cc6e-4f9a-bff3-10c3299916b9` | unsure | 0.110 |  |
| MF06 | malformed | text is emoji only | 200 | `345d67cb-de56-4694-9de0-dc37904af0c1` | ai | 0.720 |  |
| MF07 | malformed | text is right-to-left script | 200 | `9467768a-8e13-4bb2-94fe-ec446dadea7a` | ai | 0.630 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `15e15e26-9fda-40ae-8f85-8f7e78a18732` | ai | 0.630 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `3032645c-1b5d-4b0d-8ffb-ff4b4c95441b` | human | 0.440 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `5617978b-4c03-4acf-870c-a108a196c036` | human | 0.630 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cfb42cde-65a7-48de-b45a-5ecd94dae243` | human | 0.650 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e3f76592-f6f1-44b1-bc0d-84529c009be8` | human | 0.650 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f0b73668-2f4c-4f01-b4a2-65884069eb09` | human | 0.650 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `35b1169c-010a-4fd7-bed8-bcd4f9e29e3e` | human | 0.650 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `11fca35a-2d44-4b99-8bac-960766b82a85` | human | 0.650 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `93121ca4-8597-4725-a454-44fd47fc7f1c` | human | 0.650 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `579d341a-9e12-44ac-9a87-3704ce5a137a` | human | 0.650 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `663062e9-ebb3-4a83-a127-ff54600de504` | human | 0.650 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `28471ede-c868-4131-ba31-bed1886d5ada` | human | 0.650 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4cdcd031-90de-4f4a-a46b-4a7fa04a094e` | human | 0.650 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "10bd9b5b-7cbd-4fbc-b757-bb7db5a87273",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.43,
  "model_score": 0.1635,
  "style_score": 0.4057,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "db6ba125-0aeb-4a93-be85-58c885a2f69d",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.27,
  "model_score": 0.5943,
  "style_score": 0.1349,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "d1291b3a-ce2b-45e4-86f3-1afd0e64dc6e",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.02,
  "model_score": 0.6662,
  "style_score": 0.31,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "00873808-cb60-4e11-aa44-491cc17b5206",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.02,
  "model_score": 0.6114,
  "style_score": 0.4043,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "90e02ef9-278e-4e1f-9fe8-830b3eda67fe",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.42,
  "model_score": 0.3212,
  "style_score": 0.2617,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "ad4d414d-4422-440e-a3fc-e24aa60cbd99",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.31,
  "model_score": 0.5727,
  "style_score": 0.1141,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "9921d657-a570-4cad-b496-915d81aa55ff",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.08,
  "model_score": 0.5862,
  "style_score": 0.4948,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "b3d3d248-4e2d-45f9-bcc7-ad114b3f50d3",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.47,
  "model_score": 0.2452,
  "style_score": 0.2869,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "7a288699-8056-4c45-810e-b68d8022b70d",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.7042,
  "style_score": 0.2966,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "159a5561-e0d1-44b6-9c6e-6b0a8e4b3752",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.49,
  "model_score": 0.9792,
  "style_score": 0.5142,
  "label": "Our analysis indicates this text was very likely generated by an artificial intelligence system.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "5ecf5b57-de5b-4b53-9a0a-017b98ac6580",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.04,
  "model_score": 0.6175,
  "style_score": 0.345,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "e272c3d6-df80-4ddb-a21a-db1f5114a8f0",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.16,
  "model_score": 0.7387,
  "style_score": 0.4259,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "3478500d-1fff-44ca-95ce-b71ea1bf0299",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.18,
  "model_score": 0.8051,
  "style_score": 0.3796,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "4e316c8c-8f08-48dc-898d-795e9ae2e088",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.17,
  "model_score": 0.8329,
  "style_score": 0.3366,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "535ccc71-f2bc-4779-a5ac-099597b46287",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.27,
  "model_score": 0.8005,
  "style_score": 0.4702,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "eaf869a2-fc10-43a9-8d82-5752484463b9",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.02,
  "model_score": 0.8814,
  "style_score": 0.3071,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "4f052919-ec6b-45f1-9309-792834af8d6f",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.06,
  "model_score": 0.8816,
  "style_score": 0.3425,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "b869f05e-f560-4202-a77b-2ab54eaf5157",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.45,
  "model_score": 0.3223,
  "style_score": 0.2268,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "bd7046e6-d0bb-4570-93e6-0b6c9071da15",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.38,
  "model_score": 0.4625,
  "style_score": 0.1616,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "3ba01569-222b-4962-b7e0-78b9d400b0c4",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.62,
  "model_score": 0.2044,
  "style_score": 0.1757,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "952d3ca9-9ef9-42dc-8aef-c3e8a088197b",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.1,
  "model_score": 0.5943,
  "style_score": 0.3071,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "f1c8f461-0726-4ebe-83a2-f6f44b10eb23",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.18,
  "model_score": 0.4998,
  "style_score": 0.318,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "d16c86b1-5a1f-40ed-8866-ffa41d7cdd06",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.05,
  "model_score": 0.6401,
  "style_score": 0.3093,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "29945df2-18b4-4e4b-b893-c9e0d285afb8",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.09,
  "model_score": 0.5583,
  "style_score": 0.3488,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the s",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "03e44b64-6f95-4f11-9a82-021ee66c6607",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.68,
  "model_score": 0.0,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "04856e98-3c70-4c84-9795-d296d0787c5a",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.36,
  "model_score": 0.0112,
  "style_score": 0.9,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "4c8e514d-cc6e-4f9a-bff3-10c3299916b9",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.11,
  "model_score": 0.9976,
  "style_score": 0.32,
  "label": "We could not determine with certainty whether this text was written by a person or an AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "345d67cb-de56-4694-9de0-dc37904af0c1",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.72,
  "model_score": 0.9969,
  "style_score": 0.72,
  "label": "Our analysis indicates this text was very likely generated by an artificial intelligence system.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "9467768a-8e13-4bb2-94fe-ec446dadea7a",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.63,
  "model_score": 0.9064,
  "style_score": 0.72,
  "label": "Our analysis indicates this text was very likely generated by an artificial intelligence system.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "15e15e26-9fda-40ae-8f85-8f7e78a18732",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.63,
  "model_score": 0.9876,
  "style_score": 0.6376,
  "label": "Our analysis indicates this text was very likely generated by an artificial intelligence system.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "3032645c-1b5d-4b0d-8ffb-ff4b4c95441b",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.44,
  "model_score": 0.2395,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "5617978b-4c03-4acf-870c-a108a196c036",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.63,
  "model_score": 0.0492,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "cfb42cde-65a7-48de-b45a-5ecd94dae243",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "e3f76592-f6f1-44b1-bc0d-84529c009be8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "f0b73668-2f4c-4f01-b4a2-65884069eb09",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "35b1169c-010a-4fd7-bed8-bcd4f9e29e3e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "11fca35a-2d44-4b99-8bac-960766b82a85",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "93121ca4-8597-4725-a454-44fd47fc7f1c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "579d341a-9e12-44ac-9a87-3704ce5a137a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "663062e9-ebb3-4a83-a127-ff54600de504",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "28471ede-c868-4131-ba31-bed1886d5ada",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "4cdcd031-90de-4f4a-a46b-4a7fa04a094e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.65,
  "model_score": 0.0287,
  "style_score": 0.32,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
