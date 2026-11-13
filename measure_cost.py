import json
from datetime import datetime, timezone
import time
import requests

URL = "http://127.0.1.1:5000/submit"
PAYLOAD = {
    "text": "This is a benchmark test sentence to measure local inference compute duration for Provenance Guard capstone evaluation.",
    "creator_id": "cost_benchmark_bot"
}
TRIALS = 10
OUTPUT_FILE = "cost_measurement_record.json"

def main():
    print("Warming up model and service (first load may take a moment)...")
    try:
        requests.post(URL, json=PAYLOAD, timeout=60)
    except Exception as e:
        print(f"Warm-up notice: {e}")

    print(f"Starting cost measurement: {TRIALS} trials against {URL}")
    results = []
    
    for i in range(1, TRIALS + 1):
        start = time.time()
        try:
            response = requests.post(URL, json=PAYLOAD, timeout=30)
            duration = time.time() - start
            success = response.status_code == 200
        except Exception as e:
            duration = time.time() - start
            success = False
            print(f"Trial {i} failed: {e}")

        trial_data = {
            "trial": i,
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "duration_seconds": round(duration, 4),
            "success": success
        }
        results.append(trial_data)
        print(f"Trial {i}/{TRIALS}: {duration:.3f}s (Success: {success})")
        time.sleep(0.5)

    durations = [r["duration_seconds"] for r in results if r["success"]]
    avg_duration = round(sum(durations) / len(durations), 4) if durations else 0.0

    output_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_trials": TRIALS,
        "successful_trials": len(durations),
        "average_compute_cost_seconds": avg_duration,
        "trials": results
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print("\n--- Summary ---")
    print(f"Average compute cost per run: {avg_duration} seconds")
    print(f"Saved permanent record to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
