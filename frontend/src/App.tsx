import { useEffect, useState } from "react";

import { api } from "./services/api";
import { useDashboard } from "./hooks/useDashboard";

import DashboardLayout from "./layout/DashboardLayout";

import DashboardCards from "./components/DashboardCards";
import AnalyticsCharts from "./components/AnalyticsCharts";
import SearchPanel from "./components/SearchPanel";
import NotificationCenter from "./components/NotificationCenter";
import UserProfilePanel from "./components/UserProfilePanel";
import ThemeToggle from "./components/ThemeToggle";

import FilterPanel from "./components/dashboard/FilterPanel";
import ApprovalQueue from "./components/dashboard/ApprovalQueue";
import KnowledgeGraphPanel from "./components/dashboard/KnowledgeGraphPanel";
import LiveFeedPanel from "./components/dashboard/LiveFeedPanel";
import LangGraphHistoryPanel from "./components/dashboard/LangGraphHistoryPanel";
import AgentEvaluationPanel from "./components/dashboard/AgentEvaluationPanel";
import SystemStatusPanel from "./components/dashboard/SystemStatusPanel";

function App() {
  const { summary } = useDashboard();

  const [theme, setTheme] = useState(localStorage.getItem("theme") || "dark");
  const [strategy, setStrategy] = useState<any>(null);
  const [liveEvents, setLiveEvents] = useState<any[]>([]);
  const [notifications, setNotifications] = useState<any[]>([]);
  const [pendingDrafts, setPendingDrafts] = useState<any[]>([]);
  const [graph, setGraph] = useState<any>({ nodes: [], relationships: [] });
  const [timeseries, setTimeseries] = useState<any[]>([]);
  const [genreData, setGenreData] = useState<any[]>([]);
  const [activeFilter, setActiveFilter] = useState("All");
  const [searchQuery, setSearchQuery] = useState("");
  const [graphRuns, setGraphRuns] = useState<any[]>([]);
  const [evaluation, setEvaluation] = useState<any>(null);
  const [systemStatus, setSystemStatus] = useState<any>(null);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", theme === "dark");
    localStorage.setItem("theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((current) => (current === "dark" ? "light" : "dark"));
  };

  const loadPendingDrafts = () => {
    api.get("/drafts/pending").then((res) => {
      setPendingDrafts(res.data.pending_drafts || []);
    });
  };

  const loadKnowledgeGraph = () => {
    api.get("/agents/knowledge-graph").then((res) => {
      setGraph(res.data || { nodes: [], relationships: [] });
    });
  };

  const loadGraphHistory = () => {
    api.get("/langgraph/history").then((res) => {
      setGraphRuns(res.data.history || []);
    });
  };

  const loadEvaluation = () => {
    api.get("/agents/evaluation").then((res) => {
      setEvaluation(res.data);
    });
  };

  useEffect(() => {
    api.get("/agents/growth-strategy").then((res) => setStrategy(res.data));
    api.get("/analytics/timeseries").then((res) => setTimeseries(res.data.data || []));
    api.get("/analytics/genre-breakdown").then((res) => setGenreData(res.data.data || []));
    api.get("/agents/notifications").then((res) => {
      setNotifications(res.data.notifications || []);
    });
    api.get("/system/status").then((res) => setSystemStatus(res.data));

    loadPendingDrafts();
    loadKnowledgeGraph();
    loadGraphHistory();
    loadEvaluation();
  }, []);

  useEffect(() => {
    const socket = new WebSocket("ws://127.0.0.1:8000/stream/live-feed");

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setLiveEvents((prev) => [data, ...prev.slice(0, 9)]);

      if (data.type === "notification") {
        setNotifications((prev) => [data.data, ...prev]);
      }
    };

    return () => socket.close();
  }, []);

  const approveDraft = async (workflowId: string) => {
    await api.post(`/drafts/${workflowId}/approve`);
    setNotifications((prev) => [
      {
        title: "Draft Approved",
        message: `Workflow ${workflowId} was approved successfully.`,
        created_at: new Date().toISOString(),
      },
      ...prev,
    ]);
    loadPendingDrafts();
    loadEvaluation();
  };

  const rejectDraft = async (workflowId: string) => {
    await api.post(`/drafts/${workflowId}/reject`);
    setNotifications((prev) => [
      {
        title: "Draft Rejected",
        message: `Workflow ${workflowId} was rejected.`,
        created_at: new Date().toISOString(),
      },
      ...prev,
    ]);
    loadPendingDrafts();
    loadEvaluation();
  };

  const regenerateDraft = async (workflowId: string) => {
    await api.post(`/drafts/${workflowId}/regenerate`);
    setNotifications((prev) => [
      {
        title: "Draft Regenerated",
        message: `Workflow ${workflowId} was regenerated and needs review.`,
        created_at: new Date().toISOString(),
      },
      ...prev,
    ]);
    loadPendingDrafts();
    loadKnowledgeGraph();
    loadEvaluation();
  };

  const buildGraph = async () => {
    await api.post("/agents/knowledge-graph/build");
    setNotifications((prev) => [
      {
        title: "Knowledge Graph Updated",
        message: "Creator knowledge graph was rebuilt successfully.",
        created_at: new Date().toISOString(),
      },
      ...prev,
    ]);
    loadKnowledgeGraph();
  };

  const clearNotifications = () => {
    setNotifications([]);
  };

  const filteredGenreData =
    activeFilter === "All" ||
    activeFilter === "YouTube" ||
    activeFilter === "LinkedIn"
      ? genreData
      : genreData.filter((item) => item.genre === activeFilter);

  const filteredStrategy =
    activeFilter === "All" ||
    activeFilter === "YouTube" ||
    activeFilter === "LinkedIn"
      ? strategy?.recommendations || []
      : (strategy?.recommendations || []).filter(
          (item: any) => item.genre === activeFilter
        );

  const normalizedSearch = searchQuery.toLowerCase();

  const searchResults = searchQuery
    ? [
        ...(filteredStrategy || []).map((item: any) => ({
          type: "Strategy",
          title: item.topic,
          detail: item.strategy,
        })),
        ...(pendingDrafts || []).map((draft: any) => ({
          type: "Draft",
          title: draft.topic || draft.workflow_id,
          detail: draft.draft || draft.suggested_reply || draft.status,
        })),
        ...(graph.nodes || []).map((node: any) => ({
          type: "Graph Node",
          title: node.name,
          detail: node.type,
        })),
        ...(graph.relationships || []).map((rel: any) => ({
          type: "Graph Relationship",
          title: `${rel.source} → ${rel.target}`,
          detail: rel.type,
        })),
        ...(liveEvents || []).map((event: any) => ({
          type: "Live Event",
          title: event.type || "event",
          detail: JSON.stringify(event),
        })),
        ...(notifications || []).map((notification: any) => ({
          type: "Notification",
          title: notification.title || notification.type || "Alert",
          detail: notification.message || JSON.stringify(notification),
        })),
        ...(graphRuns || []).map((run: any) => ({
          type: "LangGraph Run",
          title: run.topic,
          detail: run.run_id,
        })),
        ...(evaluation?.agents || []).map((agent: any) => ({
          type: "Agent Evaluation",
          title: agent.name,
          detail: `${agent.success_rate}% success, ${agent.latency_ms} ms`,
        })),
      ].filter((item) =>
        `${item.type} ${item.title} ${item.detail}`
          .toLowerCase()
          .includes(normalizedSearch)
      )
    : [];

  return (
    <DashboardLayout>
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-4xl font-extrabold text-slate-950 dark:text-white">
            Dashboard Home
          </h2>
          <p className="mt-3 text-lg font-medium text-slate-700 dark:text-slate-200">
            Real-time creator analytics powered by multi-agent AI.
          </p>
        </div>

        <ThemeToggle theme={theme} toggleTheme={toggleTheme} />
      </div>

      <section id="dashboard">
        <UserProfilePanel />

        <SystemStatusPanel systemStatus={systemStatus} />

        <FilterPanel
          activeFilter={activeFilter}
          setActiveFilter={setActiveFilter}
        />

        <SearchPanel
          searchQuery={searchQuery}
          setSearchQuery={setSearchQuery}
          searchResults={searchResults}
        />

        <NotificationCenter
          notifications={notifications}
          clearNotifications={clearNotifications}
        />

        <DashboardCards
          summary={summary}
          growthIdeas={filteredStrategy.length}
          activeFilter={activeFilter}
        />
      </section>

      <AnalyticsCharts
        timeseries={timeseries}
        filteredGenreData={filteredGenreData}
        activeFilter={activeFilter}
      />

      <ApprovalQueue
        pendingDrafts={pendingDrafts}
        approveDraft={approveDraft}
        rejectDraft={rejectDraft}
        regenerateDraft={regenerateDraft}
      />

      <section
        id="ai-strategy"
        className="mt-8 rounded-2xl border border-slate-300 bg-white p-6 shadow-xl dark:border-slate-700 dark:bg-slate-900"
      >
        <h3 className="text-2xl font-bold text-slate-950 dark:text-white">
          AI Growth Strategy
        </h3>

        <div className="mt-5 space-y-4">
          {filteredStrategy.length === 0 ? (
            <p className="text-slate-500 dark:text-slate-400">
              No strategy recommendation for this filter yet.
            </p>
          ) : (
            filteredStrategy.map((item: any, index: number) => (
              <div
                key={index}
                className="rounded-xl border border-slate-300 bg-slate-100 p-5 dark:border-slate-700 dark:bg-slate-800"
              >
                <p className="text-xl font-bold text-cyan-600 dark:text-cyan-300">
                  {item.topic}
                </p>
                <p className="mt-3 text-lg font-medium text-slate-900 dark:text-white">
                  {item.strategy}
                </p>
                <p className="mt-3 text-base text-slate-600 dark:text-slate-300">
                  {item.reason}
                </p>
              </div>
            ))
          )}
        </div>
      </section>

      <KnowledgeGraphPanel graph={graph} buildGraph={buildGraph} />

      <LangGraphHistoryPanel graphRuns={graphRuns} />

      <AgentEvaluationPanel evaluation={evaluation} />

      <LiveFeedPanel liveEvents={liveEvents} />
    </DashboardLayout>
  );
}

export default App;