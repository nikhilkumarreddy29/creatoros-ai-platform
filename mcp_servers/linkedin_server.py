from backend.simulated_data import get_linkedin_metrics, get_recent_comments


def fetch_profile_views():
    return {
        "tool": "fetch_profile_views",
        "result": get_linkedin_metrics()
    }


def fetch_recent_comments():
    comments = get_recent_comments()

    linkedin_comments = [
        comment for comment in comments
        if comment["platform"] == "linkedin"
    ]

    return {
        "tool": "fetch_recent_comments",
        "result": linkedin_comments
    }


def create_text_share(text: str):
    return {
        "tool": "create_text_share",
        "status": "simulated_success",
        "text": text,
        "note": "No real LinkedIn API called. This is safe mock execution."
    }


def send_direct_message(user_id: str, message: str):
    return {
        "tool": "send_direct_message",
        "status": "blocked_pending_approval",
        "user_id": user_id,
        "message": message,
        "note": "DM sending requires human approval."
    }