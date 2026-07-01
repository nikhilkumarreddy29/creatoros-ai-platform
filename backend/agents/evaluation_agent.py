from datetime import datetime


def run_agent_evaluation():
    return {
        "agent": "Agent Evaluation Dashboard",
        "generated_at": datetime.utcnow().isoformat(),
        "summary": {
            "total_agent_runs": 128,
            "successful_runs": 119,
            "failed_runs": 9,
            "success_rate": 92.9,
            "average_latency_ms": 840,
            "tool_calls": 76,
            "guardrail_blocks": 4,
            "fact_review_required": 6,
            "hallucination_review_required": 3
        },
        "agents": [
            {"name": "Supervisor Agent", "success_rate": 96, "latency_ms": 620},
            {"name": "RAG Draft Agent", "success_rate": 91, "latency_ms": 1180},
            {"name": "Trend Discovery Agent", "success_rate": 94, "latency_ms": 540},
            {"name": "Sentiment Agent", "success_rate": 97, "latency_ms": 310},
            {"name": "Guardrail Agent", "success_rate": 99, "latency_ms": 180},
            {"name": "Fact Check Agent", "success_rate": 93, "latency_ms": 420}
        ]
    }