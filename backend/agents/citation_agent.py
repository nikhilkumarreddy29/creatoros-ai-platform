def run_citation_check(draft_data: dict):
    sources = draft_data.get("rag_sources", [])

    if sources:
        status = "passed"
        citation_safe = True
        reason = "Draft contains RAG source grounding."
    else:
        status = "failed"
        citation_safe = False
        reason = "Draft has no RAG sources."

    return {
        "agent": "Citation Checker Agent",
        "status": status,
        "citation_safe": citation_safe,
        "sources_count": len(sources),
        "reason": reason
    }