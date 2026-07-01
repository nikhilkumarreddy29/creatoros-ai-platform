from fastapi import APIRouter
from backend.database.db import Base, engine
from backend.database import models

router = APIRouter(
    prefix="/db",
    tags=["Database"]
)


@router.post("/init")
def init_database():
    Base.metadata.create_all(bind=engine)

    return {
        "message": "Database tables created successfully",
        "tables": [
            "drafts",
            "audit_logs",
            "metrics"
        ]
    }