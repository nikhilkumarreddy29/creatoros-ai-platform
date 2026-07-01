from uuid import uuid4
from datetime import datetime
from backend.approvals.store import DRAFT_STORE
from backend.database.repository import save_draft_to_db
from backend.memory.redis_client import set_cache


def generate_content_draft(topic: str, genre: str, platform: str):
    workflow_id = str(uuid4())

    draft = (
        f"🚀 {topic} is becoming a major opportunity in {genre}.\n\n"
        "Creators can use this trend to create:\n"
        "1. A YouTube video\n"
        "2. A LinkedIn post\n"
        "3. A short-form hook\n"
        "4. A community discussion\n\n"
        "The key is using data-backed content strategy."
    )

    draft_data = {
        "agent": "Draft Generation Agent",
        "workflow_id": workflow_id,
        "topic": topic,
        "genre": genre,
        "platform": platform,
        "draft": draft,
        "approval_required": True,
        "status": "pending_approval",
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }

    DRAFT_STORE[workflow_id] = draft_data
    save_draft_to_db(draft_data)
    set_cache(
    key=f"workflow:{workflow_id}:status",
    value=draft_data["status"],
    expiry_seconds=3600
    )
    return draft_data