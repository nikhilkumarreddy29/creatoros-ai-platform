from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
from backend.approvals.store import DRAFT_STORE
from backend.approvals.audit_store import AUDIT_LOGS
import difflib
from backend.agents.guardrail_agent import run_guardrail_check
from backend.agents.fact_check_agent import run_fact_check
from backend.agents.citation_agent import run_citation_check
from backend.agents.hallucination_agent import run_hallucination_check
from backend.database.repository import save_audit_log_to_db
from backend.memory.redis_client import set_cache, get_cache

router = APIRouter(prefix="/drafts", tags=["Approvals"])


class EditDraftRequest(BaseModel):
    draft: str


@router.get("/pending")
def get_pending_drafts():
    return {
        "pending_drafts": [
            draft for draft in DRAFT_STORE.values()
            if draft.get("status") == "pending_approval"
        ]
    }


@router.post("/{workflow_id}/approve")
def approve_draft(workflow_id: str):
    if workflow_id not in DRAFT_STORE:
        raise HTTPException(status_code=404, detail="Draft not found")

    draft_entry = DRAFT_STORE[workflow_id]
    draft_text = draft_entry.get("draft", "")
    
    # 1. Guardrail Check
    guardrail_result = run_guardrail_check(draft_text)

    if not guardrail_result.get("safe_to_publish", False):
        draft_entry["status"] = "blocked_by_guardrail"
        draft_entry["guardrail_result"] = guardrail_result
        draft_entry["updated_at"] = datetime.now(timezone.utc).isoformat()

        set_cache(
            key=f"workflow:{workflow_id}:status",
            value=draft_entry["status"],
            expiry_seconds=3600
        )
        add_audit_log(workflow_id, "approve_blocked", "blocked_by_guardrail")

        return {
            "message": "Draft blocked by guardrail. Cannot approve unsafe content.",
            "draft": draft_entry
        }

    # 2. Fact Check 
    fact_check_result = run_fact_check(draft_text)

    if not fact_check_result.get("fact_safe", False):
        draft_entry["status"] = "needs_fact_review"
        draft_entry["fact_check_result"] = fact_check_result
        draft_entry["updated_at"] = datetime.now(timezone.utc).isoformat()

        set_cache(
            key=f"workflow:{workflow_id}:status",
            value=draft_entry["status"],
            expiry_seconds=3600
        )
        add_audit_log(workflow_id, "approve_blocked", "needs_fact_review")

        return {
            "message": "Draft needs fact review before approval.",
            "draft": draft_entry
        }

    # 3. Citation Check
    citation_result = run_citation_check(draft_entry)

    if not citation_result.get("citation_safe", False):
        draft_entry["status"] = "needs_citation_review"
        draft_entry["citation_result"] = citation_result
        draft_entry["updated_at"] = datetime.now(timezone.utc).isoformat()

        set_cache(
            key=f"workflow:{workflow_id}:status",
            value=draft_entry["status"],
            expiry_seconds=3600
        )
        add_audit_log(workflow_id, "approve_blocked", "needs_citation_review")

        return {
            "message": "Draft needs citation review before approval.",
            "draft": draft_entry
        }

    # 4. Hallucination Check
    hallucination_result = run_hallucination_check(draft_entry)

    if not hallucination_result.get("hallucination_safe", False):
        draft_entry["status"] = "needs_hallucination_review"
        draft_entry["hallucination_result"] = hallucination_result
        draft_entry["updated_at"] = datetime.now(timezone.utc).isoformat()

        set_cache(
            key=f"workflow:{workflow_id}:status",
            value=draft_entry["status"],
            expiry_seconds=3600
        )
        add_audit_log(workflow_id, "approve_blocked", "needs_hallucination_review")

        return {
            "message": "Draft needs hallucination review before approval.",
            "draft": draft_entry
        }

    # 5. Successful Approval 
    draft_entry["status"] = "approved"
    draft_entry["guardrail_result"] = guardrail_result
    draft_entry["fact_check_result"] = fact_check_result  
    draft_entry["updated_at"] = datetime.now(timezone.utc).isoformat()
    draft_entry["citation_result"] = citation_result
    draft_entry["hallucination_result"] = hallucination_result

    set_cache(
        key=f"workflow:{workflow_id}:status",
        value=draft_entry["status"],
        expiry_seconds=3600
    )
    add_audit_log(workflow_id, "approve", "approved")
    
    return {
        "message": "Draft approved successfully",
        "draft": draft_entry
    }


@router.post("/{workflow_id}/reject")
def reject_draft(workflow_id: str):
    if workflow_id not in DRAFT_STORE:
        raise HTTPException(status_code=404, detail="Draft not found")

    DRAFT_STORE[workflow_id]["status"] = "rejected"
    DRAFT_STORE[workflow_id]["updated_at"] = datetime.now(timezone.utc).isoformat()

    set_cache(
        key=f"workflow:{workflow_id}:status",
        value=DRAFT_STORE[workflow_id]["status"],
        expiry_seconds=3600
    )
    add_audit_log(workflow_id, "reject", "rejected")

    return {
        "message": "Draft rejected successfully",
        "draft": DRAFT_STORE[workflow_id]
    }


@router.post("/{workflow_id}/edit")
def edit_draft(workflow_id: str, request: EditDraftRequest):
    if workflow_id not in DRAFT_STORE:
        raise HTTPException(status_code=404, detail="Draft not found")

    old_text = DRAFT_STORE[workflow_id].get("draft", "")
    new_text = request.draft

    diff = list(
        difflib.unified_diff(
            old_text.splitlines(),
            new_text.splitlines(),
            fromfile="before",
            tofile="after",
            lineterm=""
        )
    )

    DRAFT_STORE[workflow_id]["previous_draft"] = old_text
    DRAFT_STORE[workflow_id]["draft"] = new_text
    DRAFT_STORE[workflow_id]["diff"] = diff
    DRAFT_STORE[workflow_id]["status"] = "edited_pending_approval"
    DRAFT_STORE[workflow_id]["updated_at"] = datetime.now(timezone.utc).isoformat()

    set_cache(
        key=f"workflow:{workflow_id}:status",
        value=DRAFT_STORE[workflow_id]["status"],
        expiry_seconds=3600
    )
    add_audit_log(workflow_id, "edit", "edited_pending_approval")

    return {
        "message": "Draft edited successfully",
        "draft": DRAFT_STORE[workflow_id]
    }


def add_audit_log(workflow_id: str, action: str, status: str):
    log = {
        "workflow_id": workflow_id,
        "action": action,
        "status": status,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    AUDIT_LOGS.append(log)

    save_audit_log_to_db(
        workflow_id=workflow_id,
        action=action,
        status=status
    )


@router.get("/{workflow_id}/audit")
def get_draft_audit(workflow_id: str):
    logs = [
        log for log in AUDIT_LOGS
        if log["workflow_id"] == workflow_id
    ]

    return {
        "workflow_id": workflow_id,
        "audit_logs": logs
    }


@router.post("/{workflow_id}/regenerate")
def regenerate_draft(workflow_id: str):
    if workflow_id not in DRAFT_STORE:
        raise HTTPException(status_code=404, detail="Draft not found")

    old_draft = DRAFT_STORE[workflow_id]
    topic = old_draft.get("topic", "Trending Topic")
    genre = old_draft.get("genre", "Content Creation")

    regenerated_text = (
        f"🔥 New version: {topic} is a strong opportunity in {genre}.\n\n"
        "Here is a sharper content angle:\n"
        "1. Start with a painful creator problem\n"
        "2. Explain why this trend matters now\n"
        "3. Give a simple 3-step strategy\n"
        "4. End with a question to increase comments\n\n"
        "This version is optimized for engagement and creator growth."
    )

    DRAFT_STORE[workflow_id]["draft"] = regenerated_text
    DRAFT_STORE[workflow_id]["status"] = "regenerated_pending_approval"
    DRAFT_STORE[workflow_id]["updated_at"] = datetime.now(timezone.utc).isoformat()

    set_cache(
        key=f"workflow:{workflow_id}:status",
        value=DRAFT_STORE[workflow_id]["status"],
        expiry_seconds=3600
    )
    add_audit_log(
        workflow_id,
        "regenerate",
        "regenerated_pending_approval"
    )

    return {
        "message": "Draft regenerated successfully",
        "draft": DRAFT_STORE[workflow_id]
    }


@router.get("/{workflow_id}/status")
def get_workflow_status(workflow_id: str):
    status = get_cache(f"workflow:{workflow_id}:status")

    if not status and workflow_id in DRAFT_STORE:
        status = DRAFT_STORE[workflow_id]["status"]

    return {
        "workflow_id": workflow_id,
        "status": status
    }
