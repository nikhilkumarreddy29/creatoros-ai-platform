from backend.simulated_data import get_linkedin_metrics


def run_linkedin_agent():
    data = get_linkedin_metrics()

    return {
        "agent": "LinkedIn Analytics Agent",
        "status": "success",
        "analysis": {
            "summary": "LinkedIn engagement is strong.",
            "followers": data["followers"],
            "profile_views": data["profile_views"],
            "recommendation": "Convert the best YouTube topic into a LinkedIn carousel post."
        }
    }