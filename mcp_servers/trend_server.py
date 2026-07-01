from backend.simulated_data import get_trending_topics


def fetch_google_trends():
    return {
        "tool": "fetch_google_trends",
        "status": "simulated_success",
        "result": get_trending_topics(),
        "note": "Free-first simulated trend source."
    }


def fetch_youtube_trending_topics():
    return {
        "tool": "fetch_youtube_trending_topics",
        "status": "simulated_success",
        "result": get_trending_topics()
    }


def fetch_linkedin_trending_hashtags():
    return {
        "tool": "fetch_linkedin_trending_hashtags",
        "status": "simulated_success",
        "result": [
            {"hashtag": "#AIAgents", "score": 94},
            {"hashtag": "#CreatorEconomy", "score": 88},
            {"hashtag": "#LinkedInGrowth", "score": 81}
        ]
    }


def detect_viral_opportunity():
    trends = get_trending_topics()

    high = [
        trend for trend in trends
        if trend["trend_score"] >= 90 and trend["growth_rate"] >= 35
    ]

    return {
        "tool": "detect_viral_opportunity",
        "status": "success",
        "high_opportunities": high
    }