from mcp_servers.trend_server import (
    fetch_google_trends,
    fetch_youtube_trending_topics,
    fetch_linkedin_trending_hashtags,
    detect_viral_opportunity,
)


def trend_mcp_tool(tool_name: str):
    tools = {
        "fetch_google_trends": fetch_google_trends,
        "fetch_youtube_trending_topics": fetch_youtube_trending_topics,
        "fetch_linkedin_trending_hashtags": fetch_linkedin_trending_hashtags,
        "detect_viral_opportunity": detect_viral_opportunity,
    }

    if tool_name not in tools:
        return {"error": f"Unknown Trend MCP tool: {tool_name}"}

    return tools[tool_name]()