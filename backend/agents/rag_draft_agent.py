from uuid import uuid4
from datetime import datetime

from backend.rag.chroma_rag import vector_search
from backend.approvals.store import DRAFT_STORE
from backend.database.repository import save_draft_to_db
from backend.memory.redis_client import set_cache
from backend.agents.knowledge_graph_agent import add_draft_to_graph


def generate_rag_draft(topic: str, genre: str, platform: str):
    workflow_id = str(uuid4())

    rag_result = vector_search(
        query=f"{platform} content framework for {topic}"
    )

    documents = rag_result["results"].get("documents", [[]])[0]

    context = "\n\n".join(documents)

    draft = (
        f"Topic: {topic}\n"
        f"Genre: {genre}\n"
        f"Platform: {platform}\n\n"
        "RAG-backed draft:\n\n"
        f"🚀 {topic} is becoming important for creators.\n\n"
        "Here is a simple way to use it:\n"
        "1. Start with a strong hook\n"
        "2. Explain the problem clearly\n"
        "3. Give a practical example\n"
        "4. End with a question for engagement\n\n"
        "Source grounding used:\n"
        f"{context}"
    )

    draft_data = {
        "agent": "RAG Draft Agent",
        "workflow_id": workflow_id,
        "topic": topic,
        "genre": genre,
        "platform": platform,
        "draft": draft,
        "rag_sources": documents,
        "approval_required": True,
        "status": "pending_approval",
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }

    DRAFT_STORE[workflow_id] = draft_data
    save_draft_to_db(draft_data)
    add_draft_to_graph(draft_data)
    set_cache(
    key=f"workflow:{workflow_id}:status",
    value=draft_data["status"],
    expiry_seconds=3600
    )
    return draft_data