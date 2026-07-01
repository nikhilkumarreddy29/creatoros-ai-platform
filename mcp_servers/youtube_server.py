from backend.simulated_data import (
    get_youtube_metrics,
    get_recent_comments,
    get_video_retention,
)


def fetch_channel_metrics():
    return {
        "tool": "fetch_channel_metrics",
        "result": get_youtube_metrics()
    }


def fetch_recent_comments():
    return {
        "tool": "fetch_recent_comments",
        "result": get_recent_comments()
    }


def fetch_video_retention():
    return {
        "tool": "fetch_video_retention",
        "result": get_video_retention()
    }


def reply_to_comment(comment_id: str, reply: str):
    return {
        "tool": "reply_to_comment",
        "status": "simulated_success",
        "comment_id": comment_id,
        "reply": reply,
        "note": "No real YouTube API called. This is safe mock execution."
    }