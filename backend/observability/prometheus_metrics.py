from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "creatoros_requests_total",
    "Total API Requests"
)

REQUEST_LATENCY = Histogram(
    "creatoros_request_latency_seconds",
    "API Request Latency"
)

GRAPH_RUN_COUNTER = Counter(
    "creatoros_graph_runs_total",
    "LangGraph executions"
)

TOOL_CALL_COUNTER = Counter(
    "creatoros_tool_calls_total",
    "External MCP tool calls"
)