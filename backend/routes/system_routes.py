from fastapi import APIRouter
from backend.config import settings

router = APIRouter(prefix="/system", tags=["System"])


@router.get("/status")
def system_status():
    return {
        "app_name": getattr(settings, "APP_NAME", "CreatorOS AI Platform"),
        "environment": getattr(settings, "APP_ENV", "development"),
        "api_version": "1.0.0",
        "backend": "healthy",
        "database": "configured",
        "redis": "configured",
        "status": "operational"
    }