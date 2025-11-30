from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import time
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import PlainTextResponse

model = joblib.load("models/baseline.joblib")

# Prometheus metrics
REQUEST_COUNT = Counter("predict_requests_total", "Total predict requests")
REQUEST_LATENCY = Histogram("predict_latency_seconds", "Latency for predictions")

app = FastAPI(title="W9D2 Model Serving Project")

class Input(BaseModel):
    x1: float
    x2: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: Input):
    start = time.time()
    REQUEST_COUNT.inc()

    prediction = model.predict([[data.x1, data.x2]])[0]

    REQUEST_LATENCY.observe(time.time() - start)

    return {
        "score": float(prediction),
        "model_version": "v1.0"
    }

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return PlainTextResponse(generate_latest().decode("utf-8"))
