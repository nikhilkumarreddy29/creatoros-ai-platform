def publish_linkedin_post(workflow_id: str, text: str):
    return {
        "tool": "publish_linkedin_post",
        "workflow_id": workflow_id,
        "status": "simulated_published",
        "text": text,
        "note": "No real LinkedIn post published. Mock execution only."
    }


def reply_youtube_comment(comment_id: str, reply: str):
    return {
        "tool": "reply_youtube_comment",
        "comment_id": comment_id,
        "status": "simulated_replied",
        "reply": reply,
        "note": "No real YouTube reply posted. Mock execution only."
    }


def schedule_content(workflow_id: str, scheduled_time: str):
    return {
        "tool": "schedule_content",
        "workflow_id": workflow_id,
        "scheduled_time": scheduled_time,
        "status": "simulated_scheduled"
    }


def update_draft_status(workflow_id: str, status: str):
    return {
        "tool": "update_draft_status",
        "workflow_id": workflow_id,
        "status": status
    }