from mcp_servers.publishing_server import (
    publish_linkedin_post,
    reply_youtube_comment,
    schedule_content,
    update_draft_status,
)


def publishing_mcp_tool(tool_name: str, **kwargs):
    tools = {
        "publish_linkedin_post": publish_linkedin_post,
        "reply_youtube_comment": reply_youtube_comment,
        "schedule_content": schedule_content,
        "update_draft_status": update_draft_status,
    }

    if tool_name not in tools:
        return {"error": f"Unknown Publishing MCP tool: {tool_name}"}

    return tools[tool_name](**kwargs)