from uuid import uuid4
from datetime import datetime

from backend.security.pii_detector import mask_pii
from backend.agents.sentiment_agent import analyze_sentiment
from backend.agents.toxicity_agent import run_toxicity_agent
from backend.approvals.store import DRAFT_STORE


def suggest_comment_reply(comment_text: str, platform: str = "youtube"):
    workflow_id = str(uuid4())

    masked_comment = mask_pii(comment_text)
    sentiment = analyze_sentiment(masked_comment)
    toxicity = run_toxicity_agent(masked_comment)

    if toxicity["is_toxic"]:
        reply = "This comment needs human review before replying."
        status = "blocked_pending_review"
        approval_required = True
    elif sentiment["sentiment"] == "Positive":
        reply = "Thanks a lot! Glad you found this useful 🚀"
        status = "pending_approval"
        approval_required = True
    elif sentiment["sentiment"] == "Negative":
        reply = "Thanks for the feedback. I’ll make the next explanation simpler and clearer."
        status = "pending_approval"
        approval_required = True
    elif sentiment["sentiment"] == "Mixed":
        reply = "Thanks for the honest feedback. Glad some parts helped, and I’ll improve the confusing section next time."
        status = "pending_approval"
        approval_required = True
    else:
        reply = "Thanks for sharing your thoughts!"
        status = "pending_approval"
        approval_required = True

    reply_data = {
        "agent": "Community Interaction Agent",
        "workflow_id": workflow_id,
        "platform": platform,
        "comment": masked_comment,
        "sentiment": sentiment["sentiment"],
        "toxicity_status": toxicity["status"],
        "suggested_reply": reply,
        "approval_required": approval_required,
        "status": status,
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }

    DRAFT_STORE[workflow_id] = reply_data

    return reply_data