# proj6_repo
# Threat Intelligence Dashboard

An AI-powered **Threat Intelligence Dashboard** for detecting suspicious network activity using a combination of:

* Machine Learning
* Rule-Based Detection
* Feature Engineering
* Risk Assessment
* Multi-Agent AI Analysis
* Real-Time WebSocket Communication

The system analyzes network and authentication events, detects anomalies, assigns risk levels, and generates AI-powered threat reports for suspicious activities.

---

## 📌 Project Overview

This project is designed to simulate a Threat Intelligence and Security Monitoring system.

A network event is sent to the backend, where it goes through multiple stages:

1. Log Parsing
2. Feature Engineering
3. Rule-Based Detection
4. Machine Learning Anomaly Detection
5. Risk Assessment
6. AI Multi-Agent Analysis
7. Threat Report Generation
8. Real-Time Dashboard Update

The final result is displayed on a React-based dashboard.

---

# 🏗️ Project Architecture

```text
Network Log Event
        │
        ▼
   FastAPI Backend
        │
        ▼
    Log Parser
        │
        ▼
 Feature Engineering
        │
        ├──────────────► Rule-Based Detection
        │
        ▼
 Isolation Forest Model
        │
        ▼
   Risk Assessment
        │
        ▼
 Suspicious Activity?
      │       │
     No      Yes
      │       │
      ▼       ▼
   Normal    AI Multi-Agent
 Activity      Analysis
                  │
                  ▼
            Threat Report
                  │
                  ▼
          React Dashboard
```

---

# 🚀 Features

* 🔍 Network log analysis
* 🤖 Isolation Forest anomaly detection
* 📏 Rule-based threat detection
* 🧠 Feature engineering
* ⚠️ Risk level classification
* 🤖 Multi-agent AI threat analysis using CrewAI
* 📊 Threat statistics dashboard
* 🔴 Real-time threat updates using WebSockets
* 📋 Threat history and reports
* ⚡ FastAPI backend
* ⚛️ React + Vite frontend

---

# 🧠 Detection Pipeline

## 1. Log Parsing

Incoming network events are parsed and normalized using:

```text
backend/services/log_parser.py
```

The system extracts important information such as:

* Timestamp
* Source IP
* Destination IP
* Event Type
* Action
* Port
* Status
* Failed Logins
* Request Frequency
* Unique Ports

---

## 2. Feature Engineering

The system transforms raw log information into numerical features for the Machine Learning model.

Current features:

```text
failed_logins
request_frequency
unique_ports
```

Implemented in:

```text
backend/services/feature_engineering.py
```

Example feature vector:

```text
[8, 250.5, 15]
```

---

## 3. Rule-Based Detection

The system uses baseline security rules to detect obvious suspicious behavior.

Current rules include:

### Excessive Failed Logins

```text
failed_logins > 5
```

This may indicate a brute-force attack.

### Abnormal Request Frequency

```text
request_frequency > 200
```

This may indicate an unusual traffic spike or flooding behavior.

Implemented in:

```text
backend/services/rule_detector.py
```

---

# 🤖 Machine Learning Model

The project uses an **Isolation Forest** model for anomaly detection.

Isolation Forest is an unsupervised Machine Learning algorithm that identifies unusual observations in data.

The model analyzes:

```text
failed_logins
request_frequency
unique_ports
```

Model training script:

```text
backend/models/train_model.py
```

The trained model is saved as:

```text
backend/models/isolation_forest.joblib
```

---

## Model Training

To train or regenerate the Isolation Forest model:

```bash
cd backend
python models/train_model.py
```

The trained model will be saved automatically in:

```text
backend/models/isolation_forest.joblib
```

---

# ⚠️ Risk Assessment

The system assigns a risk level based on:

* Machine Learning anomaly score
* Rule-based detection results

Risk levels include:

| Risk Level  | Description                               |
| ----------- | ----------------------------------------- |
| 🔴 Critical | Strong anomaly or security rule triggered |
| 🟠 High     | Significant suspicious behavior           |
| 🟡 Medium   | Moderate anomaly detected                 |
| 🟢 Low      | Normal or low-risk behavior               |

Implemented in:

```text
backend/services/risk_service.py
```

---

# 🤖 AI Multi-Agent Threat Analysis

When suspicious activity is detected, the system uses multiple AI agents to analyze the event.

The agents are implemented using **CrewAI**.

## Agents

### 1. Threat Analyzer Agent

Responsible for:

* Analyzing suspicious log entries
* Identifying anomalous behavior
* Detecting suspicious patterns

File:

```text
backend/agents/analyzer.py
```

---

### 2. Risk Assessment Agent

Responsible for:

* Evaluating threat severity
* Assessing operational impact
* Analyzing the anomaly score

File:

```text
backend/agents/risk_assessor.py
```

---

### 3. Security Reporter Agent

Responsible for:

* Combining the analysis results
* Creating a human-readable incident report
* Generating a security briefing

File:

```text
backend/agents/reporter.py
```

---

## Agent Workflow

```text
Suspicious Event
       │
       ▼
Threat Analyzer Agent
       │
       ▼
Risk Assessment Agent
       │
       ▼
Security Reporter Agent
       │
       ▼
Final Threat Report
```

The agent orchestration is implemented in:

```text
backend/agents/crew.py
```

---

# 🌐 API Endpoints

The backend API is built using FastAPI.

Base URL:

```text
http://127.0.0.1:8000
```

---

## POST `/api/detect`

Analyzes a network event and returns a threat detection result.

Example request:

```json
{
  "source_ip": "203.0.113.10",
  "destination_ip": "192.168.1.5",
  "event_type": "login",
  "action": "login_failed",
  "port": 22,
  "status": "failed",
  "failed_logins": 10,
  "request_frequency": 250.0,
  "unique_ports": 20
}
```

Example response:

```json
{
  "id": "generated-uuid",
  "timestamp": "2026-08-30T10:00:00",
  "source_ip": "203.0.113.10",
  "destination_ip": "192.168.1.5",
  "classification": "Suspicious Activity",
  "anomaly_score": -0.45,
  "risk_level": "Critical",
  "reason": "Baseline Rule Triggered",
  "report": "AI-generated threat analysis report"
}
```

---

## GET `/api/threats`

Returns all detected threats stored in memory.

Example:

```text
GET /api/threats
```

---

## GET `/api/threats/stats`

Returns dashboard statistics.

Example response:

```json
{
  "total": 20,
  "critical": 5,
  "high": 6,
  "medium": 4,
  "low": 5
}
```

---

# 🔴 WebSocket

The system supports real-time threat updates using WebSockets.

WebSocket endpoint:

```text
ws://127.0.0.1:8000/ws/threats
```

When a new event is processed:

1. The event is received through WebSocket.
2. The detection pipeline analyzes it.
3. The result is stored.
4. The threat result is broadcast to connected clients.
5. The frontend updates in real time.

---

# 📊 Frontend Dashboard

The frontend is built using:

* React
* Vite
* Axios
* Recharts
* Lucide React
* Tailwind CSS

The dashboard includes components for:

* Threat statistics
* Threat detection form
* Live threat feed
* Threat table
* Risk badges
* Alert panels

Frontend components are located in:

```text
frontend/src/components/
```

The main dashboard page is located in:

```text
frontend/src/pages/Dashboard.jsx
```

---

# 📂 Project Structure

```text
proj6_repo/
│
├── backend/
│   │
│   ├── agents/
│   │   ├── analyzer.py
│   │   ├── crew.py
│   │   ├── reporter.py
│   │   └── risk_assessor.py
│   │
│   ├── data/
│   │   ├── generate_logs.py
│   │   └── network_logs.csv
│   │
│   ├── models/
│   │   ├── train_model.py
│   │   └── isolation_forest.joblib
│   │
│   ├── routes/
│   │   ├── detection.py
│   │   └── threats.py
│   │
│   ├── schemas/
│   │   └── threat.py
│   │
│   ├── services/
│   │   ├── detection_service.py
│   │   ├── feature_engineering.py
│   │   ├── log_parser.py
│   │   ├── risk_service.py
│   │   ├── rule_detector.py
│   │   └── websocket_manager.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── AlertPanel.jsx
│   │   │   ├── DetectionForm.jsx
│   │   │   ├── LiveThreatFeed.jsx
│   │   │   ├── RiskBadge.jsx
│   │   │   ├── ThreatStats.jsx
│   │   │   └── ThreatTable.jsx
│   │   │
│   │   ├── pages/
│   │   │   └── Dashboard.jsx
│   │   │
│   │   ├── services/
│   │   │   └── threatApi.js
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── index.html
│   └── package.json
│
├── .gitignore
├── LICENSE
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd proj6_repo
```

---

# 🐍 Backend Setup

## Create a Virtual Environment

From the project root:

```bash
python -m venv venv
```

Activate the environment.

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

Move to the backend directory:

```bash
cd backend
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

If AI agents require API credentials, create a `.env` file inside the `backend` directory and add the required environment variables.

Example:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not upload `.env` files containing private API keys to GitHub.

---

# 🧪 Generate Simulated Network Logs

The project includes a script that generates simulated network and authentication logs.

Run:

```bash
cd backend
python data/generate_logs.py
```

The generated dataset will be stored in:

```text
backend/data/network_logs.csv
```

The simulated dataset includes:

* Normal network activity
* Brute-force login attempts
* Port scanning
* High-frequency traffic
* Off-hours suspicious activity

---

# 🤖 Train the Machine Learning Model

Run:

```bash
cd backend
python models/train_model.py
```

This creates:

```text
models/isolation_forest.joblib
```

---

# ▶️ Run the Backend

From the `backend` directory:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The backend will run on:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛️ Frontend Setup

Open another terminal and move to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

The Vite server will display the frontend URL in the terminal.

Usually:

```text
http://localhost:5173
```

---

# ▶️ Running the Complete System

You need two terminals.

## Terminal 1 — Backend

```bash
cd proj6_repo/backend

source ../venv/bin/activate

uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

## Terminal 2 — Frontend

```bash
cd proj6_repo/frontend

npm install

npm run dev
```

Then open the frontend URL displayed by Vite.

---

# 🧪 Example Suspicious Event

You can test the system using:

```json
{
  "source_ip": "203.0.113.50",
  "destination_ip": "192.168.1.10",
  "event_type": "login",
  "action": "login_failed",
  "port": 22,
  "status": "failed",
  "failed_logins": 12,
  "request_frequency": 350,
  "unique_ports": 25
}
```

This event should likely trigger:

```text
Classification: Suspicious Activity
Risk Level: Critical
```

Because:

* Failed logins exceed the baseline threshold.
* Request frequency is abnormally high.
* The feature vector may be identified as anomalous by Isolation Forest.

---

# 🛠️ Technologies Used

## Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* Scikit-learn
* NumPy
* Joblib
* CrewAI
* WebSockets

## Frontend

* React
* Vite
* Axios
* Recharts
* Lucide React
* Tailwind CSS

## Machine Learning

* Isolation Forest
* Unsupervised Anomaly Detection

---

# 🔮 Future Improvements

Possible future improvements include:

* Database integration
* Persistent threat storage
* User authentication
* Real network log ingestion
* Additional Machine Learning models
* Model evaluation metrics
* SHAP explainability
* IP reputation analysis
* Threat intelligence API integration
* Docker deployment
* Cloud deployment
* Alert notifications via Email or Telegram
* Advanced attack classification

---

# 👥 Authors

Developed as a Practical Training / AI and Cybersecurity project.

---

# 📄 License

This project is licensed under the terms included in the `LICENSE` file.
