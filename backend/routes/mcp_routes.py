from fastapi import APIRouter
from backend.mcp_clients.youtube_client import youtube_mcp_tool
from backend.mcp_clients.linkedin_client import linkedin_mcp_tool
from backend.mcp_clients.trend_client import trend_mcp_tool
from backend.mcp_clients.publishing_client import publishing_mcp_tool


router = APIRouter(prefix="/mcp", tags=["MCP Tools"])


@router.get("/youtube/channel-metrics")
def youtube_channel_metrics():
    return youtube_mcp_tool("fetch_channel_metrics")


@router.get("/youtube/comments")
def youtube_comments():
    return youtube_mcp_tool("fetch_recent_comments")


@router.get("/youtube/retention")
def youtube_retention():
    return youtube_mcp_tool("fetch_video_retention")


@router.post("/youtube/reply")
def youtube_reply(comment_id: str, reply: str):
    return youtube_mcp_tool(
        "reply_to_comment",
        comment_id=comment_id,
        reply=reply
    )
@router.get("/linkedin/profile-views")
def linkedin_profile_views():
    return linkedin_mcp_tool("fetch_profile_views")


@router.get("/linkedin/comments")
def linkedin_comments():
    return linkedin_mcp_tool("fetch_recent_comments")


@router.post("/linkedin/create-share")
def linkedin_create_share(text: str):
    return linkedin_mcp_tool(
        "create_text_share",
        text=text
    )


@router.post("/linkedin/send-dm")
def linkedin_send_dm(user_id: str, message: str):
    return linkedin_mcp_tool(
        "send_direct_message",
        user_id=user_id,
        message=message
    )

@router.get("/trends/google")
def mcp_google_trends():
    return trend_mcp_tool("fetch_google_trends")


@router.get("/trends/youtube")
def mcp_youtube_trends():
    return trend_mcp_tool("fetch_youtube_trending_topics")


@router.get("/trends/linkedin")
def mcp_linkedin_trends():
    return trend_mcp_tool("fetch_linkedin_trending_hashtags")


@router.get("/trends/viral-opportunity")
def mcp_viral_opportunity():
    return trend_mcp_tool("detect_viral_opportunity")

@router.post("/publishing/linkedin")
def mcp_publish_linkedin(workflow_id: str, text: str):
    return publishing_mcp_tool(
        "publish_linkedin_post",
        workflow_id=workflow_id,
        text=text
    )


@router.post("/publishing/youtube-reply")
def mcp_reply_youtube(comment_id: str, reply: str):
    return publishing_mcp_tool(
        "reply_youtube_comment",
        comment_id=comment_id,
        reply=reply
    )


@router.post("/publishing/schedule")
def mcp_schedule_content(workflow_id: str, scheduled_time: str):
    return publishing_mcp_tool(
        "schedule_content",
        workflow_id=workflow_id,
        scheduled_time=scheduled_time
    )


@router.post("/publishing/status")
def mcp_update_draft_status(workflow_id: str, status: str):
    return publishing_mcp_tool(
        "update_draft_status",
        workflow_id=workflow_id,
        status=status
    )