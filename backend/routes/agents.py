from fastapi import APIRouter
from backend.agents.supervisor_agent import run_supervisor_agent
from backend.agents.youtube_agent import run_youtube_agent
from backend.agents.linkedin_agent import run_linkedin_agent
from backend.agents.genre_agent import classify_genre
from backend.agents.sentiment_agent import analyze_sentiment, analyze_recent_comments
from backend.agents.trend_agent import run_trend_agent
from backend.agents.draft_agent import generate_content_draft
from backend.agents.guardrail_agent import run_guardrail_check
from backend.agents.fact_check_agent import run_fact_check
from backend.agents.rag_draft_agent import generate_rag_draft
from backend.agents.citation_agent import run_citation_check
from backend.approvals.store import DRAFT_STORE
from backend.agents.hallucination_agent import run_hallucination_check
from backend.security.pii_detector import mask_pii
from backend.agents.toxicity_agent import run_toxicity_agent
from backend.agents.community_agent import suggest_comment_reply
from backend.agents.notification_agent import create_notification, get_notifications
from backend.agents.growth_strategy_agent import run_growth_strategy_agent
from backend.agents.monetization_agent import run_monetization_agent
from backend.agents.competitor_agent import run_competitor_agent
from backend.agents.audience_persona_agent import run_audience_persona_agent
from backend.agents.retention_agent import run_retention_agent
from backend.agents.knowledge_graph_agent import build_creator_graph, get_graph
from backend.agents.knowledge_graph_agent import (
    build_creator_graph,
    get_graph,
    query_related_entities,
)
from backend.agents.evaluation_agent import run_agent_evaluation

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


@router.get("/supervisor")
def supervisor():
    return run_supervisor_agent()


@router.get("/youtube")
def youtube_agent():
    return run_youtube_agent()


@router.get("/linkedin")
def linkedin_agent():
    return run_linkedin_agent()


@router.get("/genre")
def genre_agent(text: str):
    return classify_genre(text)

@router.get("/sentiment")
def sentiment_agent(text: str):
    return analyze_sentiment(text)


@router.get("/comments/sentiment")
def comment_sentiment_agent():
    return analyze_recent_comments()

@router.get("/trends")
def trend_agent():
    return run_trend_agent()

@router.get("/draft")
def draft_agent(topic: str, genre: str = "Tech", platform: str = "linkedin"):
    return generate_content_draft(topic, genre, platform)

@router.get("/guardrail")
def guardrail_agent(text: str):
    return run_guardrail_check(text)

@router.get("/fact-check")
def fact_check_agent(text: str):
    return run_fact_check(text)

@router.get("/rag-draft")
def rag_draft_agent(
    topic: str,
    genre: str = "Tech",
    platform: str = "linkedin"
):
    return generate_rag_draft(topic, genre, platform)

@router.get("/citation-check/{workflow_id}")
def citation_check_agent(workflow_id: str):
    if workflow_id not in DRAFT_STORE:
        return {
            "error": "Draft not found"
        }

    return run_citation_check(DRAFT_STORE[workflow_id])

@router.get("/hallucination-check/{workflow_id}")
def hallucination_check_agent(workflow_id: str):
    if workflow_id not in DRAFT_STORE:
        return {
            "error": "Draft not found"
        }

    return run_hallucination_check(DRAFT_STORE[workflow_id])

@router.get("/mask-pii")
def pii_mask_agent(text: str):
    return {
        "original_text": text,
        "masked_text": mask_pii(text)
    }
@router.get("/toxicity")
def toxicity_agent(text: str):
    return run_toxicity_agent(text)

@router.get("/reply-suggestion")
def reply_suggestion_agent(comment: str, platform: str = "youtube"):
    return suggest_comment_reply(comment, platform)

@router.post("/notify")
def notification_agent(
    title: str,
    message: str,
    priority: str = "medium",
    category: str = "general"
):
    return create_notification(title, message, priority, category)


@router.get("/notifications")
def notification_list():
    return get_notifications()

@router.get("/growth-strategy")
def growth_strategy_agent():
    return run_growth_strategy_agent()

@router.get("/monetization")
def monetization_agent():
    return run_monetization_agent()

@router.get("/competitors")
def competitor_agent():
    return run_competitor_agent()

@router.get("/audience-personas")
def audience_persona_agent():
    return run_audience_persona_agent()

@router.get("/retention")
def retention_agent():
    return run_retention_agent()

@router.post("/knowledge-graph/build")
def build_knowledge_graph():
    return build_creator_graph()


@router.get("/knowledge-graph")
def knowledge_graph():
    return get_graph()

@router.get("/knowledge-graph/query")
def query_knowledge_graph(name: str):
    return query_related_entities(name)

@router.get("/evaluation")
def evaluation_agent():
    return run_agent_evaluation()