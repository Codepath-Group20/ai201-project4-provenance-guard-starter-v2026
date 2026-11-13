## **Milestone 7: Final Capstone Write-Up**

**What It Costs**

* **Measured Per-Run Cost:** 0.2532 seconds of compute time per run (measured locally via `measure_cost.py` across 10 trials; record saved in `cost_measurement_record.json`).  
* **Scale Arithmetic (100 people a day):** Assuming each person executes 1 request per day (100 requests/day), total daily compute time is 100 x 0.2532s \= 25.32 seconds/day. At scale, running this for 100 users daily requires less than half a minute of total server compute time per day.

**What's Still Broken / Tightened Targets**

* Because all five criteria successfully passed their evaluations, no criteria remain unmet. As reflected in our Milestone 6 evaluation, Criterion 1 (`/stats` endpoint latency) was initially set too conservatively (\< 100ms) given actual performance (\~41ms). We tightened this target to **\< 30ms** and successfully verified it (\~25ms) following our in-memory query optimization.

**What Next?**

* If this were a production system and we had another unit, the very first thing we would implement is **persistent database-backed caching (or asynchronous log indexing)** for the audit log. As historical submission volume grows into tens of thousands of rows, reading and parsing raw JSON lines from `audit.jsonl` on every `/stats` call will eventually bottleneck I/O, whereas an indexed SQLite or PostgreSQL backend would maintain constant O(1) telemetry retrieval times.

**How I Used AI**

* Throughout this capstone, AI was utilized as an architectural sounding board and collaborative partner to structure endpoint extensions (`/stats`), design reproducible cost-measurement scripts (`measure_cost.py`), draft quantitative evaluation criteria, and diagnose performance bottlenecks. Every line of code, test trial, and acceptance target was manually verified, executed, and committed locally inside the development environment.

