# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST [http://127.0.0.1:5000/ping](http://127.0.0.1:5000/ping) \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

1. **Client Request**: A client sends an HTTP `POST` request to `/submit` with a JSON payload containing `text` and an optional `creator_id`.
2. **Transport & Validation**: The Flask server receives the request, validates that the JSON body is well-formed, and ensures non-empty text.
3. **Signal 1 Processing (`detector.py`)**: The text is evaluated via a local GPT-2 model to compute token predictability, yielding a perplexity score and normalized `model_signal`.
4. **Signal 2 Processing (`stylometry.py`)**: Procedural functions analyze surface-level statistical metrics (e.g., Type-Token Ratio and punctuation density).
5. **Score Aggregation**: Combined scoring rules evaluate the multi-signal metrics to produce a classification decision.
6. **Audit Logging**: Request metadata, signal scores, and verdicts are appended as structured JSON to `logs/audit.jsonl`.
7. **Response Delivery**: A structured JSON response returns the evaluation metrics back to the client.

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:** Autoregressive token predictability and log-likelihood strings via a local GPT-2 model.

**Why that might differ between human and AI writing:** AI-generated text features artificially low and uniform token perplexity, whereas human writing exhibits erratic, organic shifts in phrasing surprise.

**What it can't see:** Highly structured or formal human prose (like academic abstracts or legal documentation) that mimics the predictable syntax of language models.

### Signal two — the style signal

**What it measures:** Surface-level linguistic distributions including vocabulary richness and sentence length variance.

**Why that might differ between human and AI writing:** Humans mix clause lengths and maintain diverse lexical spread, whereas baseline AI models produce homogenized syntax structures.

**What it can't see:** Prompt-engineered or style-tuned AI outputs explicitly instructed to mimic colloquialisms or structural variance.

### The combining rule

**The rule:** Weighted combination of model perplexity and procedural stylometry scores.

**The numbers:** `model_signal * 0.7 + style_signal * 0.3`

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** A code snippet yields very high model perplexity (low AI score) but uniform formatting structures. The weighting blends these metrics to balance structural syntax against word-choice predictability.

---

## Label Variants

| Score range | The exact text a reader sees |
|---|---|
| 0.0 - 0.39 | High-confidence human generation |
| 0.40 - 0.69 | Unsure / borderline review required |
| 0.70 - 1.00 | High-confidence AI generation |

**Why I worded the "unsure" one this way:** It admits system uncertainty without issuing an immediate false accusation against human writers.

---

## Sample Run

**A submission**

```bash
$ curl -X POST http://HP-ProBook-6560b:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Test submission payload", "creator_id": "student-123"}'
```

```json
{
  "confidence": 0.0,
  "content_id": "ad77ff29-7abd-4ce0-9af1-7fadb63888af",
  "guess": "human",
  "label": "pending",
  "model_score": 0.0,
  "style_score": 0.0
}
```

**An appeal**

```bash
$ curl -X POST http://HP-ProBook-6560b:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "ad77ff29-7abd-4ce0-9af1-7fadb63888af", "reasoning": "Written completely by hand."}'
```

```json
{
  "error": "not_implemented",
  "message": "POST /appeal isn't built yet — see the TODO in app.py.",
  "you_sent": {
    "content_id": "ad77ff29-7abd-4ce0-9af1-7fadb63888af",
    "reasoning": "Written completely by hand."
  }
}
```

**What the log shows afterwards**

```bash
$ curl "[http://127.0.0.1:5000/log?limit=3](http://127.0.0.1:5000/log?limit=3)"
```

```json
{
  "count": 1,
  "entries": [
    {
      "combined_score": null,
      "confidence": 0.0,
      "content_id": "ad77ff29-7abd-4ce0-9af1-7fadb63888af",
      "creator_id": "student-123",
      "guess": "human",
      "label": "pending",
      "model_score": 0.0,
      "status": "logged",
      "style_score": 0.0,
      "text": "Test submission payload",
      "timestamp": "2026-11-02T01:39:58+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Assistance structuring Milestone 1 design documentation and endpoint contracts.
- *What came back:* Clean markdown layout for system architecture and JSON schemas.
- *What I changed:* Adjusted field properties to match our exact route implementation.

**Moment 2**

- *What I asked for:* Guidance implementing the Milestone 3 request parsing and audit logger integration in Flask.
- *What came back:* Robust payload validation and error responses for missing text fields.
- *What I changed:* Integrated specific variable lookups and uuid generators to match project requirements.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**

**What a caller counts as:**

**The run of status codes when I pushed past it:**

```

```

---

## Attack Run — Before

```

```

**Ten audit log entries from the run**

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

---

## Run Log and Verdicts

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. | | | | | |
| 2. | | | | | |
| 3. | | | | | |
| 4. | | | | | |
| 5. | | | | | |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

**Did it help, and how do I know:**

---

## What's Still Broken

**The trade I'd make if this ran for real:**

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
