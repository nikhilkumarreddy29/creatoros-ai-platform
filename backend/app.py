from urllib import request

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.routes.analytics import router as analytics_router
from backend.routes.agents import router as agents_router
from backend.routes.approvals import router as approvals_router
from backend.routes.live_feed import router as live_feed_router
import time
from fastapi import Request
from backend.observability.metrics import record_request, metrics_response
from backend.observability.logger import logger
from uuid import uuid4
from backend.routes.langgraph_routes import router as langgraph_router
from backend.routes.langgraph_routes import router as langgraph_router
from backend.routes.rag_routes import router as rag_router
from backend.routes.db_routes import router as db_router
from backend.routes.db_read_routes import router as db_read_router
from backend.routes.cache_routes import router as cache_router
from backend.security.rate_limiter import check_rate_limit
from backend.routes.mcp_routes import router as mcp_router
from backend.routes.system_routes import router as system_router
from backend.routes.prometheus_routes import router as prometheus_router
from backend.observability.tracing import setup_tracing
from backend.routes.version_routes import router as version_router

app=FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Real-Time CreatorOS Multi-Agent Intelligence Hub"
)
tracer = setup_tracing(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(analytics_router)
app.include_router(agents_router)
app.include_router(approvals_router)
app.include_router(live_feed_router)
app.include_router(langgraph_router)
app.include_router(langgraph_router)
app.include_router(rag_router)
app.include_router(db_router)
app.include_router(db_read_router)
app.include_router(cache_router)
app.include_router(mcp_router)
app.include_router(system_router)
app.include_router(prometheus_router)
app.include_router(version_router)
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    request_id = str(uuid4())
    start_time = time.time()
    client_ip = request.client.host if request.client else "unknown"

    if request.url.path not in ["/metrics", "/docs", "/openapi.json"]:
        check_rate_limit(
            key=client_ip,
            limit=100,
            window_seconds=60
        )
    response = await call_next(request)

    record_request(
        method=request.method,
        endpoint=request.url.path,
        start_time=start_time
    )

    response.headers["X-Request-ID"] = request_id

    logger.info(
        "api_request_completed",
        request_id=request_id,
        method=request.method,
        endpoint=request.url.path,
        status_code=response.status_code
    )

    return response


@app.get("/metrics")
def metrics():
    return metrics_response()
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "env": settings.ENV
    }


@app.get("/")
def root():
    return {
        "message": "CreatorOS backend is running",
        "docs": "/docs"
    }

