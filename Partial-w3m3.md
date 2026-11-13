# **Milestone 3 README Text**

Below is the raw Markdown content for the Milestone 3: Instrumentation & Cost README section.

## **Milestone 3: Instrumentation & Cost**

Instrumentation

The following structured log entries were captured from the `logs/audit.jsonl` file via the `GET /log?limit=10` endpoint. This sample demonstrates structured decision records (timestamp, scores, label) and the required capture of system failures/rejections (rate limiting).

```
[
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "f0b73668-2f4c-4f01-b4a2-65884069eb09",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:11+00:00"
  },
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "35b1169c-010a-4fd7-bed8-bcd4f9e29e3e",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:11+00:00"
  },
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "11fca35a-2d44-4b99-8bac-960766b82a85",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:12+00:00"
  },
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "93121ca4-8597-4725-a454-44fd47fc7f1c",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:12+00:00"
  },
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "579d341a-9e12-44ac-9a87-3704ce5a137a",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:12+00:00"
  },
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "663062e9-ebb3-4a83-a127-ff54600de504",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:12+00:00"
  },
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "28471ede-c868-4131-ba31-bed1886d5ada",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:12+00:00"
  },
  {
    "combined_score": 0.1744,
    "confidence": 0.65,
    "content_id": "4cdcd031-90de-4f4a-a46b-4a7fa04a094e",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "logged",
    "style_score": 0.32,
    "text": "Testing the rate limit with a repeated submission body.",
    "timestamp": "2026-11-07T21:16:13+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-07T21:16:13+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-07T21:16:13+00:00"
  }
]
```

**What It Costs**

* **Average Compute Cost:** 0.2532 seconds of compute per run.  
* **Measurement Method:** Measured locally on the `HP-ProBook-6560b` development environment. We executed the `measure_cost.py` script, which triggered one warm-up request followed by 10 sequential HTTP POST requests to `/submit` using the Python `time.time()` module. The script calculated the average duration of the 9 successful requests (trial 10 was correctly rejected via rate limiting). The full reproducible record is saved in `cost_measurement_record.json`.

```
Individual runs (successful): [0.2472, 0.253, 0.255, 0.2517, 0.2508, 0.251, 0.2549, 0.2553, 0.26]
Average compute cost per run: 0.2532 seconds
```

