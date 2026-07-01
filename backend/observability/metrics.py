from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response
import time

REQUEST_COUNT = Counter(
    "creatoros_request_count",
    "Total number of API requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "creatoros_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)


def record_request(method: str, endpoint: str, start_time: float):
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(time.time() - start_time)


def metrics_response():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )