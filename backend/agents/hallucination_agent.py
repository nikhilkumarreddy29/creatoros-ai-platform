def run_hallucination_check(draft_data: dict):
    draft = draft_data.get("draft", "").lower()
    sources = draft_data.get("rag_sources", [])

    if not sources:
        return {
            "agent": "Hallucination Detection Agent",
            "status": "failed",
            "hallucination_safe": False,
            "reason": "No RAG sources available to verify grounding."
        }

    source_text = " ".join(sources).lower()

    important_words = [
        word for word in draft.split()
        if len(word) > 6
    ]

    matched_words = [
        word for word in important_words
        if word in source_text
    ]

    grounding_score = 0

    if important_words:
        grounding_score = round(
            len(matched_words) / len(important_words),
            2
        )

    if grounding_score >= 0.15:
        status = "passed"
        hallucination_safe = True
        reason = "Draft appears partially grounded in RAG sources."
    else:
        status = "needs_review"
        hallucination_safe = False
        reason = "Draft may contain unsupported content."

    return {
        "agent": "Hallucination Detection Agent",
        "status": status,
        "hallucination_safe": hallucination_safe,
        "grounding_score": grounding_score,
        "reason": reason
    }