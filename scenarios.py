# scenarios.py

def validate():
    """Validates the custom criteria scenarios configuration."""
    problems = []
    if not isinstance(SCENARIOS, list) or len(SCENARIOS) == 0:
        problems.append("SCENARIOS must be a non-empty list.")
    return problems

SCENARIOS = [
    {
        "id": "c1_false_positive_human",
        "name": "My own writing flagged as AI",
        "description": "Tests whether natural human writing is incorrectly flagged as high-confidence AI.",
        "target": "<= 1 of 10",
        "texts": [
            "Just finished setting up the new SSH config aliases on the desktop workstation.",
            "Honestly, trying to debug local environment PATH variables on Linux can be tedious.",
            "Working through the RAG text chunking pipeline logic for the CodePath milestone.",
            "Let's grab some coffee and look over the Flask route handler code again.",
            "The network interface configuration using SLAAC privacy addresses is working smoothly.",
            "Updating the documentation markdown files before pushing the final commit to GitHub.",
            "Testing out the zero-shot text classification baselines with Hugging Face transformers.",
            "It turns out the connection timeout was caused by a minor typo in the host alias.",
            "Writing procedural stylometry metrics in Python requires careful handling of edge cases.",
            "Everything looks solid after running the automated headless smoke tests."
        ]
    },
    {
        "id": "c2_label_coverage",
        "name": "All three labels reachable",
        "description": "Validates that inputs span across all three confidence label tiers.",
        "target": "3 of 3",
        "texts": [
            "The quick brown fox jumps over the lazy dog.",
            "Overall, this system works reasonably well for general tasks, though minor adjustments might be necessary depending on configuration parameters.",
            "In conclusion, it is evident that artificial intelligence systems leverage extensive parameter distributions to optimize predictive performance across multifaceted benchmarks."
        ]
    },
    {
        "id": "c3_appeal_status",
        "name": "Appeal always changes status",
        "description": "Ensures POST /appeal correctly transitions record status to under_review.",
        "target": "5 of 5",
        "action": "submit_and_appeal",
        "texts": ["Test appeal content one.", "Test appeal content two.", "Test appeal content three.", "Test appeal content four.", "Test appeal content five."]
    },
    {
        "id": "c4_empty_text_400",
        "name": "Empty text returns a 400, not a 500",
        "description": "Verifies graceful error handling for blank payloads.",
        "target": "5 of 5",
        "texts": ["", "   ", "Test text for validation", "Another test text", "Final test text"]
    },
    {
        "id": "c5_audit_log_completeness",
        "name": "Every decision appears in the audit log",
        "description": "Checks that 20 rapid sequential submissions all successfully log to audit.jsonl.",
        "target": "20 of 20",
        "texts": [f"Sequential audit log test payload number {i}" for i in range(1, 21)]
    }
]
