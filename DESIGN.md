# Provenance Guard: System Design & Milestone 1

## 1. End-to-End Submission Path
1. **Client Request**: A client sends an HTTP POST request to /submit with a JSON payload containing text and an optional creator_id.
2. **Transport & Validation**: The Flask server receives the request, enforces rate limits, and validates that the JSON body is well-formed and non-empty.
3. **Signal 1 Processing (detector.py)**: The text is tokenized and passed through the local GPT-2 model to compute log-likelihoods, yielding a perplexity score and a normalized model_signal probability.
4. **Signal 2 Processing (stylometry.py)**: Procedural functions analyze the text string to extract surface-level statistical metrics (e.g., Type-Token Ratio, sentence length variance, punctuation density).
5. **Score Aggregation & Thresholding**: The backend combines Signal 1 and Signal 2 scores via a weighting or decision rule to determine a final classification label (Human vs. AI).
6. **Audit Logging**: The request metadata, combined scores, and final label are appended as a structured JSON object to the local audit.jsonl log file.
7. **Response Delivery**: A structured JSON response is returned to the client detailing the evaluation results.

---

## 2. Signal Analysis & Blind Spots

### Signal One: GPT-2 Perplexity (detector.py)
* **Property Measured**: Autoregressive token predictability (how surprising or fluid word sequences are to a language model).
* **Why it differs**: AI-generated text typically exhibits artificially low and uniform perplexity because models select high-probability tokens. Human writing features erratic, organic fluctuations in word choice and surprise.
* **Blind Spot**: **Highly structured or formal human prose.** Technical documentation, academic abstracts, or rigid legal writing often mimic the low perplexity and predictable syntax of language models, causing Signal One to falsely flag human experts as AI.

### Signal Two: Procedural Stylometry (stylometry.py)
* **Property Measured**: Surface-level linguistic distributions (vocabulary richness via Type-Token Ratio, sentence length variance, and punctuation frequency).
* **Why it differs**: Human writers naturally mix very short sentences with long, complex clauses, whereas baseline AI generations often maintain a homogenized sentence structure and uniform vocabulary spread.
* **Blind Spot**: **Prompt-engineered or style-tuned AI outputs.** Modern AI can be explicitly prompted to inject structural variance, mimic colloquialisms, or adopt a specific stylistic voice, completely masking its predictable surface-level metrics from statistical rules.

---

## 3. False Positive Trace Scenario
* **The Scenario**: A meticulous student submits an exceptionally structured, formal essay written entirely by hand.
* **The Score**: Signal One flags the low token perplexity (~8.5), and Signal Two notes a remarkably uniform sentence length distribution. The combined aggregator outputs a high AI probability score (0.89).
* **The Label**: The system returns a verdict marking the submission as Flagged / Likely AI.
* **The Recourse**: The student receives an automated flag with no immediate explanation. Because the system includes an audit log (audit.jsonl), the instructor or reviewer can inspect the raw signal breakdown, evaluate the student's revision history or creator ID context, and manually override the false positive.

---

## 4. Endpoint Contracts

### POST /ping
* **Request Body Example (application/json):**
    {
      "message": "hello"
    }
* **Response Body (200 OK):**
    {
      "ok": true,
      "service": "provenance-guard",
      "you_sent": "hello"
    }

### POST /submit
* **Request Body Example (application/json):**
    {
      "text": "The string of text to evaluate for AI provenance.",
      "creator_id": "optional-student-identifier"
    }
* **Response Body (200 OK):**
    {
      "status": "success",
      "creator_id": "optional-student-identifier",
      "text_length": 45,
      "signals": {
        "model_signal": 0.12,
        "stylometry_signal": 0.15
      },
      "verdict": "human"
    }
* **Error Response (400 Bad Request):**
    {
      "error": "invalid_request",
      "message": "Missing required 'text' field."
    }
