from mcp_servers.linkedin_server import (
    fetch_profile_views,
    fetch_recent_comments,
    create_text_share,
    send_direct_message,
)


def linkedin_mcp_tool(tool_name: str, **kwargs):
    tools = {
        "fetch_profile_views": fetch_profile_views,
        "fetch_recent_comments": fetch_recent_comments,
        "create_text_share": create_text_share,
        "send_direct_message": send_direct_message,
    }

    if tool_name not in tools:
        return {
            "error": f"Unknown LinkedIn MCP tool: {tool_name}"
        }

    return tools[tool_name](**kwargs)