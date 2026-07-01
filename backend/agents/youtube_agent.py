from backend.simulated_data import get_youtube_metrics


def run_youtube_agent():
    data = get_youtube_metrics()

    return {
        "agent": "YouTube Analytics Agent",
        "status": "success",
        "analysis": {
            "summary": "YouTube channel is performing steadily.",
            "subscribers": data["subscribers"],
            "views_today": data["views_today"],
            "recommendation": "Create one follow-up video based on today's high view count."
        }
    }