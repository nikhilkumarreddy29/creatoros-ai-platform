# CreatorOS AI Platform - Architecture

```mermaid
flowchart LR

User[React Dashboard]

User --> FastAPI

subgraph Backend
FastAPI --> Supervisor
Supervisor --> YouTubeAgent
Supervisor --> LinkedInAgent
Supervisor --> TrendAgent
Supervisor --> SentimentAgent
Supervisor --> RAGAgent
Supervisor --> DraftAgent
Supervisor --> GuardrailAgent
Supervisor --> FactCheckAgent
Supervisor --> KnowledgeGraph
Supervisor --> ApprovalWorkflow
Supervisor --> NotificationAgent
end

YouTubeAgent --> MCPYouTube
LinkedInAgent --> MCPLinkedIn
TrendAgent --> MCPTrend

RAGAgent --> ChromaDB
KnowledgeGraph --> KGStore

ApprovalWorkflow --> PostgreSQL

NotificationAgent --> Redis

Backend --> Prometheus
Prometheus --> Grafana
```