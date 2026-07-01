from backend.database.db import SessionLocal
from backend.database.models import Draft, AuditLog


def save_draft_to_db(draft_data: dict):
    db = SessionLocal()

    try:
        draft = Draft(
            workflow_id=draft_data["workflow_id"],
            topic=draft_data["topic"],
            genre=draft_data["genre"],
            platform=draft_data["platform"],
            draft=draft_data["draft"],
            status=draft_data["status"],
            approval_required=draft_data["approval_required"],
        )

        db.add(draft)
        db.commit()
        db.refresh(draft)

        return draft

    finally:
        db.close()


def save_audit_log_to_db(workflow_id: str, action: str, status: str):
    db = SessionLocal()

    try:
        log = AuditLog(
            workflow_id=workflow_id,
            action=action,
            status=status
        )

        db.add(log)
        db.commit()
        db.refresh(log)

        return log

    finally:
        db.close()
def get_all_drafts_from_db():
    db = SessionLocal()

    try:
        return db.query(Draft).all()

    finally:
        db.close()


def get_draft_by_workflow_id(workflow_id: str):
    db = SessionLocal()

    try:
        return (
            db.query(Draft)
            .filter(Draft.workflow_id == workflow_id)
            .first()
        )

    finally:
        db.close()


def get_audit_logs_by_workflow_id(workflow_id: str):
    db = SessionLocal()

    try:
        return (
            db.query(AuditLog)
            .filter(AuditLog.workflow_id == workflow_id)
            .all()
        )

    finally:
        db.close()