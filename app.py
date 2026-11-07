import os
import uuid
from flask import Flask, request, jsonify
from detector import calculate_model_score
from stylometry import calculate_style_score
from scoring import combine_signals, score_to_label

app = Flask(__name__)

# Ensure audit log directory exists
AUDIT_LOG_DIR = "logs"
AUDIT_LOG_PATH = os.path.join(AUDIT_LOG_DIR, "audit.jsonl")
os.makedirs(AUDIT_LOG_DIR, exist_ok=True)

@app.route("/ping", methods=["POST", "OPTIONS"])
def ping():
    if request.method == "OPTIONS":
        return "", 204
    data = request.get_json(silent=True) or {}
    message = data.get("message", "hello")
    return jsonify({"ok": True, "service": "provenance-guard", "you_sent": message}), 200

@app.route("/submit", methods=["POST"])
def submit():
    # Strict payload validation added for Milestone 5 fix
    data = request.get_json(silent=True)
    if not data or "text" not in data or not isinstance(data.get("text"), str) or not data["text"].strip():
        return jsonify({"error": "Missing or empty 'text' field in payload.", "status_code": 400}), 400

    text = data["text"]
    creator_id = data.get("creator_id", request.remote_addr)
    content_id = str(uuid.uuid4())

    # Calculate dual-signal analysis
    model_score = calculate_model_score(text)
    style_score = calculate_style_score(text)
    combined_score = combine_signals(model_score, style_score)
    guess, confidence, label_text = score_to_label(combined_score)

    response_payload = {
        "content_id": content_id,
        "creator_id": creator_id,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined_score,
        "guess": guess,
        "confidence": confidence,
        "label": label_text,
        "status": "logged"
    }

    # Persist entry to audit log
    with open(AUDIT_LOG_PATH, "a") as f:
        import json
        f.write(json.dumps(response_payload) + "\n")

    return jsonify(response_payload), 200

@app.route("/appeal", methods=["POST"])
def appeal():
    data = request.get_json(silent=True) or {}
    content_id = data.get("content_id")
    reasoning = data.get("reasoning", "")

    if not content_id:
        return jsonify({"error": "Missing 'content_id' field in appeal payload."}), 400

    appeal_record = {
        "content_id": content_id,
        "event": "appeal",
        "reasoning": reasoning,
        "status": "under_review",
        "timestamp": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat()
    }

    with open(AUDIT_LOG_PATH, "a") as f:
        import json
        f.write(json.dumps(appeal_record) + "\n")

    return jsonify({
        "ok": True,
        "content_id": content_id,
        "status": "under_review",
        "message": "Your appeal has been received and logged for review."
    }), 200

@app.route("/log", methods=["GET"])
def get_log():
    limit = request.args.get("limit", default=100, type=int)
    entries = []
    if os.path.exists(AUDIT_LOG_PATH):
        with open(AUDIT_LOG_PATH, "r") as f:
            import json
            for line in f:
                if line.strip():
                    entries.append(json.loads(line.strip()))
    
    return jsonify({
        "count": len(entries[-limit:]),
        "entries": entries[-limit:]
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
