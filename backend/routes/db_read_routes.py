from fastapi import APIRouter, HTTPException
from backend.database.repository import (
    get_all_drafts_from_db,
    get_draft_by_workflow_id,
    get_audit_logs_by_workflow_id,
)

router = APIRouter(prefix="/db-read", tags=["Database Read"])


@router.get("/drafts")
def get_drafts():
    drafts = get_all_drafts_from_db()

    return {
        "count": len(drafts),
        "drafts": drafts
    }


@router.get("/drafts/{workflow_id}")
def get_draft(workflow_id: str):
    draft = get_draft_by_workflow_id(workflow_id)

    if not draft:
        raise HTTPException(status_code=404, detail="Draft not found")

    return draft


@router.get("/audit/{workflow_id}")
def get_audit(workflow_id: str):
    logs = get_audit_logs_by_workflow_id(workflow_id)

    return {
        "workflow_id": workflow_id,
        "audit_logs": logs
    }