from backend.agents.growth_strategy_agent import run_growth_strategy_agent


def run_monetization_agent():
    growth = run_growth_strategy_agent()

    opportunities = []

    for item in growth["recommendations"]:
        opportunities.append({
            "topic": item["topic"],
            "genre": item["genre"],
            "monetization_ideas": [
                "Create a paid mini-guide or checklist",
                "Turn the topic into a YouTube tutorial series",
                "Offer a consulting or mentoring CTA",
                "Create a LinkedIn lead magnet post",
                "Build a newsletter issue around this topic"
            ],
            "best_cta": "Comment 'CreatorOS' if you want the full strategy template.",
            "risk_note": "Avoid income guarantees or unsupported performance claims."
        })

    return {
        "agent": "Monetization Insight Agent",
        "opportunities": opportunities
    }