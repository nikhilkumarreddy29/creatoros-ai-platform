from backend.simulated_data import get_trending_topics


def detect_viral_opportunity(topic):
    score = topic["trend_score"]
    growth = topic["growth_rate"]

    if score >= 90 and growth >= 35:
        level = "High"
        action = "Create content immediately within the next 24 hours."
    elif score >= 80 and growth >= 25:
        level = "Medium"
        action = "Create a post or short-form video soon."
    else:
        level = "Low"
        action = "Monitor this topic before creating content."

    return {
        **topic,
        "viral_opportunity": level,
        "recommended_action": action
    }


def run_trend_agent():
    trends = get_trending_topics()

    analyzed_trends = []
    for topic in trends:
        analyzed_trends.append(detect_viral_opportunity(topic))

    high_opportunities = [
        item for item in analyzed_trends
        if item["viral_opportunity"] == "High"
    ]

    return {
        "agent": "Trend Discovery Agent",
        "total_trends": len(analyzed_trends),
        "high_opportunity_count": len(high_opportunities),
        "trends": analyzed_trends
    }