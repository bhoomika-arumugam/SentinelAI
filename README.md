# SentinelAI 🛡️

### AI-Powered Real-Time Cyber Threat Detection, Analysis & Response Platform

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![WebSocket](https://img.shields.io/badge/WebSocket-Real--Time-56f0e4?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

---

## 1. Project Overview & Problem Statement

Modern enterprise Security Operations Centers (SOCs) are overwhelmed by thousands of disconnected security alerts every day. Traditional rule-only SIEM systems suffer from high false-positive rates and cannot adapt to evolving attack patterns or off-hours anomalous employee account hijacking. Conversely, standalone "black-box" machine learning tools provide vague risk flags without grounded evidence, leaving analysts unable to explain *why* an event is dangerous or what next steps to take.

**SentinelAI** solves this challenge by operating as an intelligent, real-time Security Operations Center platform. It combines:
1. **Deterministic Rule Heuristics**
2. **Multi-Dimensional Scikit-Learn Isolation Forest Machine Learning**
3. **User Behavior Baseline Fingerprinting & Deviation Engine**
4. **Grounded Explainable AI & Attack Path Kill-Chain Modeling**
5. **Interactive Threat Replay & Safe Response Simulation**

---

## 2. Core Hackathon Innovations (USP)

> **"SentinelAI does not only detect suspicious activity. It learns normal behavior, identifies anomalies, explains why an event is risky, estimates a possible attack path, and helps analysts investigate and respond in real time."**

* **Real-Time 4-Way Hybrid Scoring:**
  $$\text{Risk Score} = (0.35 \times \text{Rules}) + (0.30 \times \text{ML Anomaly}) + (0.25 \times \text{Behavior Deviation}) + (0.10 \times \text{Threat Intel})$$
* **User Behavior Fingerprinting:** Establishes working-hour baselines (e.g., 09:00–18:00), known hardware device IDs, and source IP whitelists to calculate mathematical deviation percentages (e.g. *91% Deviation: Login at 02:43 AM from unrecognized device*).
* **Explainable AI & AI Security Analyst:** Provides grounded evidence checklists directly tied to database telemetry with deterministic Q&A inquiry support.
* **Attack Path Progression Modeler:** Estimates prospective risk trajectories (Initial Access $\to$ Account Compromise $\to$ Privilege Escalation $\to$ Exfiltration) clearly labeled as *potential risk scenarios*.
* **Incident Threat Replay:** Animates step-by-step forensic reconstruction of historical telemetry frames with time offsets.
* **Interactive Live Network Map:** Visualizes network nodes, servers, databases, and hostile IPs with real-time status updates via WebSockets.
* **Safe Response Center:** Non-destructive simulation of host isolation, IP blocking, and incident triage with full audit logging.

---

## 3. Technology Stack

* **Backend & API:** Python 3.11+, FastAPI, Uvicorn, Pydantic v2, SQLAlchemy 2.0, WebSockets.
* **Machine Learning:** Scikit-learn (Isolation Forest), Joblib, NumPy, Pandas (Trained ROC-AUC: **0.9974**).
* **Database Layer:** PostgreSQL with automated local SQLite out-of-the-box fallback.
* **Security & Auth:** RFC 7519 HMAC-SHA256 JWT, PBKDF2-HMAC-SHA256 password hashing, RBAC.
* **Frontend:** Modern Vanilla HTML5/CSS3/JavaScript (Dark Cybersecurity SOC Aesthetic), Chart.js, Cytoscape.js.
* **External Threat Intelligence:** Async adapters for VirusTotal and AbuseIPDB with graceful fallback.
* **Alert Channels:** Real-time WebSockets, Slack Webhook, SMTP Email, and Twilio SMS.

---

## 4. Architecture

```
SECURITY EVENT INGRESS (API / Telemetry Stream / Demo Trigger)
       │
       ▼
   [VALIDATE & STORE] ───► Relational Store (PostgreSQL / SQLite)
       │
       ▼
[FEATURE EXTRACTION] ────► [01] Deterministic SOC Rules Engine
       │                   [02] Isolation Forest Anomaly Inference
       │                   [03] User Behavior Baseline Profiler
       │                   [04] VirusTotal / AbuseIPDB Threat Intel
       ▼
[DYNAMIC RISK ENGINE] ───► Calibrated 0–100 Score & Severity Mapping
       │
       ▼
[EXPLAINABLE AI ENGINE] ─► Ground Truth Factors & Attack Path Modeler
       │
       ▼
[INCIDENT DISPATCHER] ───► Multi-Channel Alert & WebSocket Broadcaster
       │
       ▼
[REAL-TIME SOC DASHBOARD] (Live Feed, Network Map, Radar, Replay & Safe Response)
```

---

## 5. Getting Started (Local Setup in VS Code)

### Prerequisites
* Python 3.10+ (Tested on Python 3.11, 3.12, 3.13, 3.14)
* Modern web browser (Chrome, Edge, Firefox, Brave)

### Installation Steps

1. **Clone or Navigate to the Project:**
   ```powershell
   cd sentinelai
   ```

2. **Install Dependencies:**
   ```powershell
   python -m pip install -r requirements.txt
   ```

3. **Train the ML Isolation Forest Model:**
   ```powershell
   python backend/ml/train_model.py
   ```
   *Output will generate `data/sample_security_events.csv` and train `backend/ml/isolation_forest.joblib`.*

4. **Launch the Application:**
   ```powershell
   python run.py
   ```
   *The launcher automatically initializes the database schema, verifies the ML model, and launches your browser at `http://localhost:8000`.*

---

## 6. Default Demo Credentials

| Role | Username | Password |
| :--- | :--- | :--- |
| **SOC Lead / Admin** | `admin` | `SentinelAdmin2026!` |
| **Security Analyst** | `analyst` | `SentinelAnalyst2026!` |

---

## 7. Hackathon Demo Presentation Flow

Follow this exact sequence for a high-impact presentation:

1. **Step 1 — Baseline Status:** Open `http://localhost:8000/dashboard.html`. Note that the system status displays **🟢 SOC ONLINE** and health score is **100/100**.
2. **Step 2 — Trigger Attack:** Click the `[⚡ Suspicious Login]` or `[🚨 Brute Force]` button on the top banner.
3. **Step 3 — Real-Time Detection:** Without page refresh, the WebSocket instantly pushes a new threat card and table row: **🔴 HIGH / CRITICAL RISK** with risk score calculation.
4. **Step 4 — Ground Truth Explanation:** Click `[Investigate]` on the threat row. Show the **Explainable Factors Checklist** detailing why the event was flagged (failed logins, off-hours, new device fingerprint).
5. **Step 5 — Attack Path Modeler:** Show the kill-chain progression: *Initial Access $\to$ Account Compromise $\to$ Privilege Escalation $\to$ Exfiltration*.
6. **Step 6 — Threat Replay:** Navigate to `incidents.html` and click `[▶ Replay]`. Watch the animated step-by-step reconstruction of the event timeline.
7. **Step 7 — Safe Containment:** Click `[Simulate Host Isolation]` or `[Simulate IP Block]`. The incident state transitions to **CONTAINED**, an audit log entry is recorded, and the health score updates in real time.
8. **Step 8 — Interactive Network Map:** Navigate to `network.html` to see the hostile IP highlighted in red connected to the target database node.

---

## 8. Docker Deployment Option

Run the full stack with PostgreSQL and Redis:
```bash
docker-compose up --build
```
Access the application at `http://localhost:8000`.

---

## 9. API Documentation & Endpoints

Interactive Swagger UI documentation is available at:
👉 **`http://localhost:8000/docs`**

Key Endpoints:
* `POST /api/auth/login` — Authenticate and issue signed JWT bearer token.
* `POST /api/events` — Ingest raw security event into detection pipeline.
* `GET /api/threats` — List detected threats with filters (severity, min risk).
* `GET /api/threats/{id}` — Full threat analysis with explainable factors & attack path.
* `POST /api/threats/{id}/analyst-query` — AI Security Analyst grounded Q&A.
* `GET /api/incidents` — List active and historical incidents.
* `POST /api/incidents/{id}/response` — Execute safe response simulation.
* `GET /api/incidents/{id}/replay` — Retrieve timeline frames for animated replay.
* `GET /api/analytics` — Live SOC metrics and dynamic health score.
* `GET /api/network` — Cytoscape.js network topology elements.
* `GET /api/users/{username}/behavior` — Baseline profile and deviation breakdown.
* `GET /api/reports/export` — Export full forensic threat database to CSV.
* `GET /api/health` — Multi-component system health monitor.
* `WS /ws` — Real-time bi-directional streaming WebSocket.

---

## 10. Automated Test Suite

Run the full unit and integration test suite:
```powershell
python tests/runner.py
```
*Executes all 17 unit and integration tests covering authentication, rule heuristics, Isolation Forest inference, attack path modeling, risk scoring, safe responses, and health checks.*

---

## 11. Honest Disclaimers & Scope

* **Defensive Prototype:** SentinelAI is designed as an AI-assisted detection and decision-support prototype. It does not claim 100% attack detection or zero-day immunity.
* **Safe Simulations:** Response actions (IP blocking, host isolation) are executed in a safe simulation sandbox to prevent accidental disruptions of local host environments.
* **External APIs:** If VirusTotal or AbuseIPDB API keys are not supplied in `.env`, the system gracefully continues operation using its trained local Isolation Forest ML and rule engine.

---

## 12. Future Scope

* Distributed Kafka/RabbitMQ event streaming pipeline for 100,000+ EPS enterprise scaling.
* Continuous online model retraining (Incremental River / Active Learning).
* Native integration with AWS GuardDuty, CrowdStrike Falcon, and Splunk SIEM.
* Cross-platform mobile push alerts for on-call SOC incident responders.
