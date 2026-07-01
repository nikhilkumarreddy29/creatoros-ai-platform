from mcp_servers.youtube_server import (
    fetch_channel_metrics,
    fetch_recent_comments,
    fetch_video_retention,
    reply_to_comment,
)


def youtube_mcp_tool(tool_name: str, **kwargs):
    tools = {
        "fetch_channel_metrics": fetch_channel_metrics,
        "fetch_recent_comments": fetch_recent_comments,
        "fetch_video_retention": fetch_video_retention,
        "reply_to_comment": reply_to_comment,
    }

    if tool_name not in tools:
        return {
            "error": f"Unknown YouTube MCP tool: {tool_name}"
        }

    return tools[tool_name](**kwargs)