from datetime import datetime
from uuid import uuid4


def get_youtube_metrics():
    return {
        "platform": "youtube",
        "channel_name": "CreatorOS Demo Channel",
        "subscribers": 48250,
        "views_today": 18700,
        "watch_time_hours": 920,
        "avg_retention": 61.4,
        "timestamp": datetime.utcnow().isoformat()
    }


def get_linkedin_metrics():
    return {
        "platform": "linkedin",
        "profile_name": "Nikhil Kumar Reddy KESAVAREDDYGARI",
        "followers": 9651,
        "profile_views": 270,
        "post_impressions_today": 537,
        "engagement_rate": 7.8,
        "timestamp": datetime.utcnow().isoformat()
    }

def get_recent_comments():
    return [
        {
            "platform": "youtube",
            "author": "Rahul",
            "text": "This AI agent video is very useful!",
            "likes": 24
        },
        {
            "platform": "linkedin",
            "author": "Sneha",
            "text": "Great post. Can you explain LangGraph next?",
            "likes": 11
        },
        {
            "platform": "youtube",
            "author": "Arjun",
            "text": "The video was good but the middle part was confusing.",
            "likes": 5
        },
        {
            "platform": "linkedin",
            "author": "Meera",
            "text": "I did not understand this. Please make it simple.",
            "likes": 3
        }
    ]
def get_trending_topics():
    return [
        {
            "topic": "AI Agents for Creators",
            "genre": "Tech",
            "trend_score": 96,
            "growth_rate": 42
        },
        {
            "topic": "India cricket highlights",
            "genre": "Sports",
            "trend_score": 88,
            "growth_rate": 31
        },
        {
            "topic": "Marvel trailer reaction",
            "genre": "Movies",
            "trend_score": 84,
            "growth_rate": 27
        },
        {
            "topic": "Hyderabad street food vlog",
            "genre": "Food",
            "trend_score": 79,
            "growth_rate": 21
        },
        {
            "topic": "College friends reunion vlog",
            "genre": "Friends",
            "trend_score": 73,
            "growth_rate": 16
        }
    ]
def get_competitor_content():
    return [
        {
            "competitor": "Creator A",
            "platform": "youtube",
            "topic": "AI Agents for Productivity",
            "genre": "Tech",
            "views": 92000,
            "engagement_score": 88
        },
        {
            "competitor": "Creator B",
            "platform": "linkedin",
            "topic": "How I Use AI to Create Content",
            "genre": "Tech",
            "views": 41000,
            "engagement_score": 81
        },
        {
            "competitor": "Creator C",
            "platform": "youtube",
            "topic": "Street Food Challenge",
            "genre": "Food",
            "views": 67000,
            "engagement_score": 76
        }
    ]
def get_video_retention():
    return {
        "video_title": "AI Agents for Creators",
        "retention_points": [
            {"minute": 0, "retention": 100},
            {"minute": 1, "retention": 92},
            {"minute": 2, "retention": 81},
            {"minute": 3, "retention": 55},
            {"minute": 4, "retention": 50},
            {"minute": 5, "retention": 47}
        ]
    }
def get_analytics_timeseries():
    return [
        {"day": "Mon", "youtube_views": 12000, "linkedin_impressions": 18000, "engagement": 5.2},
        {"day": "Tue", "youtube_views": 14500, "linkedin_impressions": 21000, "engagement": 5.9},
        {"day": "Wed", "youtube_views": 16200, "linkedin_impressions": 24000, "engagement": 6.4},
        {"day": "Thu", "youtube_views": 18700, "linkedin_impressions": 34200, "engagement": 7.8},
        {"day": "Fri", "youtube_views": 22100, "linkedin_impressions": 39000, "engagement": 8.3},
        {"day": "Sat", "youtube_views": 24500, "linkedin_impressions": 41500, "engagement": 8.9},
        {"day": "Sun", "youtube_views": 26900, "linkedin_impressions": 45200, "engagement": 9.4},
    ]


def get_genre_breakdown():
    return [
        {"genre": "Tech", "value": 45},
        {"genre": "Sports", "value": 18},
        {"genre": "Movies", "value": 15},
        {"genre": "Food", "value": 12},
        {"genre": "Friends", "value": 10},
    ]