from langgraph.graph import StateGraph, END

from backend.graph.state import CreatorState

from backend.agents.genre_agent import classify_genre
from backend.agents.trend_agent import run_trend_agent
from backend.agents.sentiment_agent import analyze_recent_comments
from backend.agents.draft_agent import generate_content_draft


def genre_node(state):
    result = classify_genre(state["topic"])

    state["genre"] = result["genre"]

    return state


def sentiment_node(state):
    analyze_recent_comments()

    state["sentiment_status"] = "completed"

    return state


def trend_node(state):
    run_trend_agent()

    state["trend_status"] = "completed"

    return state


def draft_node(state):
    draft = generate_content_draft(
        topic=state["topic"],
        genre=state["genre"],
        platform="linkedin"
    )

    state["draft_status"] = "generated"

    state["approval_required"] = True

    state["final_result"] = draft

    return state


builder = StateGraph(CreatorState)

builder.add_node("genre", genre_node)
builder.add_node("sentiment", sentiment_node)
builder.add_node("trend", trend_node)
builder.add_node("draft", draft_node)

builder.set_entry_point("genre")

builder.add_edge("genre", "sentiment")
builder.add_edge("sentiment", "trend")
builder.add_edge("trend", "draft")
builder.add_edge("draft", END)

creator_graph = builder.compile()