# Provenance Guard: Acceptance Criteria (Milestone 2)

1. False Positives
   - **Criterion**: Out of 10 known human-written text samples, at most 1 sample may be incorrectly classified with a high-confidence AI verdict (score >= 0.8).
   - **Rationale**: In educational or professional publishing workflows, a false accusation of AI generation damages trust far more than a missed detection, so false positives must be strictly bounded.

2. Score Spread
   - **Criterion**: The mean composite score differential between 5 baseline AI-generated samples and 5 human-written samples must be at least 0.40 on a 0.0 to 1.0 scale.
   - **Rationale**: A functioning classifier requires distinct mathematical separability between classes to ensure predictions aren't just hovering uselessly in an ambiguous middle band.

3. Bad Input Handling
   - **Criterion**: When a POST request to `/submit` sends an empty string, missing text fields, or payloads exceeding 10,000 characters, the endpoint must return a `400 Bad Request` status code with an explicit error JSON key within 200ms.
   - **Rationale**: Defensive API boundaries protect local model inference threads from crashing or wasting compute cycles on malformed or malicious payloads.

4. Label Coverage
   - **Criterion**: Across a test suite of 15 diverse inputs (comprising academic abstracts, raw code snippets, and casual prose), at least 3 distinct verdict tiers (e.g., human, uncertain, ai) must be successfully triggered and returned.
   - **Rationale**: This ensures the threshold logic and multi-signal aggregator are genuinely active and capable of nuanced classification rather than collapsing into a rigid binary output.

5. Audit Logging Traceability
   - **Criterion**: Every valid invocation of `/submit` must append a timestamped, well-formed JSON line to `audit.jsonl` recording the input length, individual signal scores, and final verdict.
   - **Rationale**: A persistent and complete audit trail is mandatory for accountability, debugging, and reviewing disputed classifications.
