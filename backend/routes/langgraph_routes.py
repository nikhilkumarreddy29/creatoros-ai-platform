from fastapi import APIRouter
from datetime import datetime
from uuid import uuid4

from backend.graph.workflow import creator_graph
from backend.graph.memory_store import GRAPH_RUN_HISTORY
from backend.observability.prometheus_metrics import GRAPH_RUN_COUNTER


router = APIRouter(
    prefix="/langgraph",
    tags=["LangGraph"]
)


@router.get("/run")
def run_graph(topic: str):
    run_id = str(uuid4())

    input_state = {
        "topic": topic,
        "genre": "",
        "sentiment_status": "",
        "trend_status": "",
        "draft_status": "",
        "approval_required": False,
        "final_result": {}
    }
    GRAPH_RUN_COUNTER.inc()
    result = creator_graph.invoke(input_state)

    history_item = {
        "run_id": run_id,
        "topic": topic,
        "input_state": input_state,
        "output_state": result,
        "timestamp": datetime.utcnow().isoformat()
    }

    GRAPH_RUN_HISTORY.append(history_item)

    return {
        "run_id": run_id,
        "result": result
    }


@router.get("/history")
def get_graph_history():
    return {
        "count": len(GRAPH_RUN_HISTORY),
        "history": GRAPH_RUN_HISTORY
    }


@router.get("/history/{run_id}")
def get_graph_run(run_id: str):
    for item in GRAPH_RUN_HISTORY:
        if item["run_id"] == run_id:
            return item

    return {
        "error": "Run not found"
    }