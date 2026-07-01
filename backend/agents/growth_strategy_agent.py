from backend.agents.youtube_agent import run_youtube_agent
from backend.agents.linkedin_agent import run_linkedin_agent
from backend.agents.trend_agent import run_trend_agent


def run_growth_strategy_agent():
    youtube = run_youtube_agent()
    linkedin = run_linkedin_agent()
    trends = run_trend_agent()

    high_trends = [
        trend for trend in trends["trends"]
        if trend["viral_opportunity"] == "High"
    ]

    recommendations = []

    for trend in high_trends:
        recommendations.append({
            "topic": trend["topic"],
            "genre": trend["genre"],
            "strategy": "Create one YouTube video, one LinkedIn post, and one short-form hook within 24 hours.",
            "reason": "High trend score and strong growth rate detected."
        })

    if not recommendations:
        recommendations.append({
            "topic": "General creator growth",
            "genre": "Mixed",
            "strategy": "Repurpose top YouTube content into LinkedIn posts and monitor comments for new ideas.",
            "reason": "No high viral opportunity detected currently."
        })

    return {
        "agent": "Growth Strategy Agent",
        "youtube_summary": youtube["analysis"],
        "linkedin_summary": linkedin["analysis"],
        "recommendations": recommendations
    }