from backend.simulated_data import get_recent_comments


def run_audience_persona_agent():
    comments = get_recent_comments()

    personas = []

    for comment in comments:
        text = comment["text"].lower()

        if any(word in text for word in ["explain", "simple", "understand", "confusing"]):
            persona = "Beginner Learner"
            need = "Needs simple explanations and step-by-step examples."
        elif any(word in text for word in ["langgraph", "api", "agent", "python"]):
            persona = "Technical Builder"
            need = "Wants implementation details and technical depth."
        elif any(word in text for word in ["great", "useful", "helpful"]):
            persona = "Growth-Oriented Creator"
            need = "Likes practical tips and reusable frameworks."
        else:
            persona = "General Audience"
            need = "Needs clear, engaging content."

        personas.append({
            "platform": comment["platform"],
            "comment": comment["text"],
            "persona": persona,
            "audience_need": need
        })

    return {
        "agent": "Audience Persona Agent",
        "personas": personas
    }