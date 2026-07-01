from prometheus_client import REGISTRY, Counter, Histogram

def _get_metric(name):
    try:
        return REGISTRY._names_to_collectors[name]
    except Exception:
        return None


REQUEST_COUNT = _get_metric("creatoros_requests_total")
if REQUEST_COUNT is None:
    REQUEST_COUNT = Counter(
        "creatoros_requests_total",
        "Total API Requests"
    )


REQUEST_LATENCY = _get_metric("creatoros_request_latency_seconds")
if REQUEST_LATENCY is None:
    REQUEST_LATENCY = Histogram(
        "creatoros_request_latency_seconds",
        "API Request Latency"
    )


GRAPH_RUN_COUNTER = _get_metric("creatoros_graph_runs_total")
if GRAPH_RUN_COUNTER is None:
    GRAPH_RUN_COUNTER = Counter(
        "creatoros_graph_runs_total",
        "LangGraph executions"
    )


TOOL_CALL_COUNTER = _get_metric("creatoros_tool_calls_total")
if TOOL_CALL_COUNTER is None:
    TOOL_CALL_COUNTER = Counter(
        "creatoros_tool_calls_total",
        "External MCP tool calls"
    )