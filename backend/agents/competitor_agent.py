from backend.simulated_data import get_competitor_content


def run_competitor_agent():
    competitors = get_competitor_content()

    sorted_content = sorted(
        competitors,
        key=lambda item: item["engagement_score"],
        reverse=True
    )

    insights = []

    for item in sorted_content:
        insights.append({
            "competitor": item["competitor"],
            "topic": item["topic"],
            "genre": item["genre"],
            "platform": item["platform"],
            "insight": "This topic is performing well and can inspire a differentiated content angle."
        })

    return {
        "agent": "Competitor Intelligence Agent",
        "top_competitor_topics": insights
    }