# Capstone Evaluation Run Log & Results

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1\. `/stats` Endpoint Latency | \< 100ms response time | 42ms | 39ms | 41ms | **MET** |
| 2\. `/stats` Data Parity | 100% match with raw audit log counts | 348/348 | 348/348 | 348/348 | **MET** |
| 3\. Label Breakdown Categorization | 100% valid category distribution (`ai`, `human`, `unsure`) | 100% | 100% | 100% | **MET** |
| 4\. Core Detection Threshold Consistency | 20/20 valid confidence mappings per batch | 20/20 | 20/20 | 20/20 | **MET** |
| 5\. Malformed Input & Failure Handling | Structured JSON error (400/429) \+ audit log rejection entry | 5/5 | 5/5 | 5/5 | **MET** |

## Supporting Evidence & Real Outputs

### Criterion 1: `/stats` Endpoint Latency

- **Source File:** `app.py`  
- **Function:** `stats()`  
- **Real Output (Sample Trial 1):**

```sh
real	0m0.042s
user	0m0.005s
sys	0m0.003s
```

### Criterion 2 & 3: Data Parity & Label Breakdown Accuracy

- **Source File:** `app.py`  
- **Function:** `stats()`  
- **Real Output (Sample Response Across Trials):**

```json
{
  "appeals_under_review": 1,
  "average_combined_score": 0.2381,
  "label_breakdown": {
    "ai": 0,
    "human": 345,
    "unsure": 3
  },
  "total_audit_entries": 357,
  "total_submissions": 348
}
```

### Criterion 4: Core Detection Threshold Consistency

- **Source File:** `detector.py` & `app.py`  
- **Function:** `model_signal()` & `submit()`  
- **Real Output (Validation Log Sample):**

```json
{
  "combined_score": 0.1744,
  "confidence": 0.65,
  "content_id": "f0b73668-2f4c-4f01-b4a2-65884069eb09",
  "guess": "human",
  "label": "We think this was probably written by a person.",
  "model_score": 0.0287,
  "status": "logged",
  "style_score": 0.32
}
```

### Criterion 5: Malformed Input & Failure Handling

- **Source File:** `app.py`  
- **Function:** `submit()` / Error Handler  
- **Real Output (Rejection Test Trial):**

```sh
{"error":"invalid_request","message":"Missing or empty 'text' field."}
```

