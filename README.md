AISE 26 • Week 9 Day 2 — Mini Model Serving Project
FastAPI • Batch Inference • Prometheus • Docker
<p align="center"> <img src="https://img.shields.io/badge/FastAPI-Model%20Serving-teal?style=for-the-badge"/> <img src="https://img.shields.io/badge/Batch-Inference-blueviolet?style=for-the-badge"/> <img src="https://img.shields.io/badge/Monitoring-Prometheus-orange?style=for-the-badge"/> <img src="https://img.shields.io/badge/Docker-Ready-success?style=for-the-badge"/> </p>

## 🌟 Project Snapshot

This mini-project shows the full journey of taking a simple ML model and serving it two different ways:

🟢 Real-time predictions using FastAPI

📁 Batch CSV predictions in a script

📊 Metrics for monitoring using Prometheus

🐳 Docker packaging for deployment

It's intentionally small, clean, and focused — just enough to demonstrate a real production flow.

## 🗂 Project Layout
```
app/
  main.py          <-- FastAPI app (predict + health + metrics)
  metrics.py       <-- Prometheus counters & histogram
models/
  baseline.joblib  <-- Saved model
data/
  input.csv        <-- Sample rows
  predictions.csv  <-- Batch predictions output
batch_infer.py     <-- Batch inference runner
train_baseline.py  <-- Training script (tiny demo model)
Dockerfile
requirements.txt
README.md
screenshots/
  metrics.png
  terminal_output.png
```

## 🚀 Getting Started
1️⃣ Create & activate your virtual environment
```
python -m venv venv
venv\Scripts\activate
```

2️⃣ Install the dependencies
```
pip install -r requirements.txt
```

🤖 Train the Tiny Baseline Model

You only need to run this once:
```
python train_baseline.py
```


This creates:
```
models/baseline.joblib
```
(A tiny LogisticRegression model with 2 features — perfect for serving demos.)

⚡ Run the API
```
uvicorn app.main:app --reload
```

Now your endpoints are live:
http://localhost:8000

🔥 API Endpoints
✔️ Health Check

GET /health

{"status": "ok"}

✔️ Prediction

POST /predict

Input
{ "x1": 1.0, "x2": 2.0 }

Output
{
  "score": 1.0,
  "model_version": "v1.0"
}

Curl Example
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d "{\"x1\":1.0,\"x2\":2.0}"

✔️ Prometheus Metrics

GET /metrics

Your metrics include:

request counter

request latency histogram

python process memory

GC stats

A screenshot is included:

screenshots/metrics.png

📁 Batch Inference

Run model predictions on a CSV file:

python batch_infer.py data/input.csv data/predictions.csv

Output:

A CSV with the original rows plus a prediction column.

🐳 Docker Setup
Build the image
docker build -t model-server:v1 .

Run the container
docker run -p 8000:8000 model-server:v1


Now test inside Docker:

curl http://localhost:8000/health

📌 Assignment Checklist
Requirement	Status
FastAPI app works	✔️
/predict returns score + version	✔️
Batch inference script runs	✔️
Prometheus metrics at /metrics	✔️
Docker builds & serves app	✔️
README covers everything	✔️