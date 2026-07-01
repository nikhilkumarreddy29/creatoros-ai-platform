from backend.agents.youtube_agent import run_youtube_agent
from backend.agents.linkedin_agent import run_linkedin_agent
from backend.agents.sentiment_agent import analyze_recent_comments
from backend.agents.trend_agent import run_trend_agent
from backend.agents.genre_agent import classify_genre


def run_supervisor_agent():
    youtube_result = run_youtube_agent()
    linkedin_result = run_linkedin_agent()
    sentiment_result = analyze_recent_comments()
    trend_result = run_trend_agent()

    sample_topic = "AI Agents for Creators"
    genre_result = classify_genre(sample_topic)

    return {
        "agent": "Supervisor Agent",
        "status": "success",
        "workflow": [
            "Collected YouTube analytics",
            "Collected LinkedIn analytics",
            "Classified content genre",
            "Analyzed comment sentiment",
            "Detected trend opportunities"
        ],
        "results": {
            "youtube": youtube_result,
            "linkedin": linkedin_result,
            "genre": genre_result,
            "sentiment": sentiment_result,
            "trends": trend_result
        },
        "final_strategy": {
            "primary_genre": genre_result["genre"],
            "recommended_topic": sample_topic,
            "recommended_action": "Create a YouTube video and repurpose it into a LinkedIn post.",
            "approval_required": True
        }
    }