from backend.simulated_data import get_recent_comments
from backend.security.pii_detector import mask_pii

def analyze_sentiment(text: str):
    masked_text = mask_pii(text)
    text_lower = masked_text.lower()

    positive_words = ["good", "great", "useful", "amazing", "excellent", "love", "helpful"]
    negative_words = ["bad", "worst", "confusing", "hate", "poor", "not understand", "difficult"]

    positive_score = sum(1 for word in positive_words if word in text_lower)
    negative_score = sum(1 for word in negative_words if word in text_lower)

    if positive_score > negative_score:
        sentiment = "Positive"
    elif negative_score > positive_score:
        sentiment = "Negative"
    elif positive_score == negative_score and positive_score > 0:
        sentiment = "Mixed"
    else:
        sentiment = "Neutral"

    return {
        "agent": "Comment Sentiment Agent",
        "text": masked_text,
        "sentiment": sentiment
    }


def analyze_recent_comments():
    comments = get_recent_comments()

    analyzed = []
    for comment in comments:
        result = analyze_sentiment(comment["text"])
        analyzed.append({
        **comment,
        "text": mask_pii(comment["text"]),
        "sentiment": result["sentiment"]
            })

    return {
        "agent": "Comment Sentiment Agent",
        "total_comments": len(analyzed),
        "comments": analyzed
    }