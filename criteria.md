# Capstone Evaluation Criteria

1. **Extension Latency (Shape C /stats endpoint)**: 
   - **Target**: The `GET /stats` endpoint must return a HTTP 200 JSON response within 100 milliseconds of request receipt when querying an audit log containing up to 1,000 entries.
   - **Reason**: Because `/stats` performs in-memory log reading and simple aggregation, anything slower than 100ms indicates inefficient line-parsing or blocking I/O, which would degrade performance under dashboard polling loads.

2. **Extension Data Parity (Audit Log Aggregation)**:
   - **Target**: The `total_submissions` and `appeals_under_review` counts returned by `/stats` must match an exhaustive manual count of the audit log (`audit.jsonl`) with 100% accuracy.
   - **Reason**: Telemetry and dashboard metrics are useless if they drift from actual recorded events. An error here would misrepresent system usage or unreviewed user disputes.

3. **Extension Label Breakdown Accuracy**:
   - **Target**: The `label_breakdown` dictionary returned by `/stats` must correctly categorize 100% of historical entries into their respective guesses (`ai`, `human`, `unsure`) without dropping unclassified or legacy rows.
   - **Reason**: The model relies on precise threshold categorization; miscategorizing breakdown counts would invalidate creator trust and audit integrity.

4. **Core Detection Threshold Consistency**:
   - **Target**: The dual-signal combination score in `/submit` must map to the exact confidence and label ranges defined in `config.py` (Human: $\le 0.35$, Unsure: $0.36 - 0.74$, AI: $\ge 0.75$) across 20 consecutive validation samples.
   - **Reason**: Core detection logic must remain stable and deterministic; threshold drift would violate the core contract of Provenance Guard.

5. **Failure & Malformed Input Handling (`/stats` or `/submit`)**:
   - **Target**: When the service encounters malformed JSON bodies or missing required keys on protected routes, it must return a structured JSON error payload with the correct HTTP status code (e.g., 400 for bad input, 429 for rate-limiting) and log the rejection event with a timestamp and reason 100% of the time.
   - **Reason**: Unhandled exceptions crash workers and silent failures obscure attack vectors. Every rejected request must be observable in the audit log.
