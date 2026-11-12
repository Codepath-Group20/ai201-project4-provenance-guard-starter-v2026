#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      ← Built (Milestones 3, 4, 5)
    POST /appeal      ← Built (Milestone 5)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config

app = Flask(__name__)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.
    """
    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    import detector
    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── COMPLETED ENDPOINTS ───────────────────────────────────────────────────────

@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, run dual signals, combine score, map to label, log, and answer.
    """
    payload = request.get_json(silent=True)
    
    if not isinstance(payload, dict):
        return jsonify({
            "error": "invalid_request",
            "message": "Payload must be a JSON object."
        }), 400

    # Strict validation update for Milestone 5 to catch missing keys, None values, or empty text
    if "text" not in payload or payload.get("text") is None:
        return jsonify({
            "error": "invalid_request",
            "message": "Missing or empty 'text' field."
        }), 400

    text = payload.get("text")
    if not isinstance(text, str) or not text.strip():
        return jsonify({
            "error": "invalid_request",
            "message": "Missing or empty 'text' field."
        }), 400

    creator_id = payload.get("creator_id")
    if not isinstance(creator_id, str) or not creator_id.strip():
        creator_id = "anonymous"

    content_id = str(uuid.uuid4())

    import detector
    import stylometry
    import scoring

    # 1. Compute both signals
    model_score = detector.model_signal(text)
    style_score = stylometry.style_signal(text)

    # 2. Combine signals into a single score
    combined_score = scoring.combine_signals(model_score, style_score)

    # 3. Map score to human-readable label and guess
    guess, label = scoring.score_to_label(combined_score)
    confidence = round(abs(combined_score - 0.5) * 2, 2)

    # 4. Log the decision with both signal scores and combined score
    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        text=text,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined_score,
        confidence=confidence,
        label=label,
        status="logged"
    )

    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": confidence,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined_score
    }), 200


@app.post("/appeal")
def appeal():
    """
    A writer disputes an accusation. Records the appeal and flags status to under_review.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "error": "invalid_request",
            "message": "Payload must be a JSON object."
        }), 400

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning", "No reasoning provided.")

    if not isinstance(content_id, str) or not content_id.strip():
        return jsonify({
            "error": "invalid_request",
            "message": "Missing or invalid 'content_id'."
        }), 400

    # 1. Check if the content_id exists in the log and fetch its creator_id
    existing_entries = audit.entries_for(content_id)
    if not existing_entries:
        return jsonify({
            "error": "not_found",
            "message": f"No audit record found for content_id: {content_id}"
        }, 404)

    # Grab the creator_id from the original log entry
    creator_id = existing_entries[0].get("creator_id", "unknown")

    # 2. Record the appeal passing the required creator_id
    audit.log_appeal(
        content_id=content_id,
        creator_id=creator_id,
        reasoning=reasoning
    )

    return jsonify({
        "ok": True,
        "content_id": content_id,
        "message": "Your appeal has been received and logged for review.",
        "status": "under_review"
    }), 200

@app.get("/stats")
def stats():
    """
    Return aggregate telemetry and submission statistics from the audit log.
    """
    entries = audit.read_entries()
    total_submissions = sum(1 for e in entries if "combined_score" in e)
    appeals_under_review = sum(1 for e in entries if e.get("status") == "under_review")
    
    scores = [e.get("combined_score") for e in entries if e.get("combined_score") is not None]
    avg_score = round(sum(scores) / len(scores), 4) if scores else 0.0

    return jsonify({
        "total_audit_entries": len(entries),
        "total_submissions": total_submissions,
        "appeals_under_review": appeals_under_review,
        "average_combined_score": avg_score
    }), 200

# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
