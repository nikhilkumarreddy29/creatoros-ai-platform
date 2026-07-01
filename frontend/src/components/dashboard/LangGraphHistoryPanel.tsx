interface Props {
  graphRuns: any[];
}

export default function LangGraphHistoryPanel({ graphRuns }: Props) {
  return (
    <section
      id="langgraph-history"
      className="mt-8 rounded-2xl border border-slate-300 bg-white p-6 shadow-xl dark:border-slate-700 dark:bg-slate-900"
    >
      <h3 className="text-2xl font-bold text-slate-950 dark:text-white">
        LangGraph Workflow History
      </h3>

      <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">
        Tracks agent workflow executions with run IDs, topics, and timestamps.
      </p>

      <div className="mt-5 space-y-4">
        {graphRuns.length === 0 ? (
          <p className="text-slate-500 dark:text-slate-400">
            No LangGraph runs yet. Run /langgraph/run from Swagger.
          </p>
        ) : (
          graphRuns.map((run) => (
            <div
              key={run.run_id}
              className="rounded-xl border border-slate-300 bg-slate-100 p-5 dark:border-slate-700 dark:bg-slate-800"
            >
              <p className="font-bold text-cyan-600 dark:text-cyan-300">
                {run.topic}
              </p>

              <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
                Run ID: {run.run_id}
              </p>

              <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
                Time: {run.timestamp}
              </p>

              <pre className="mt-4 max-h-56 overflow-auto whitespace-pre-wrap rounded-lg bg-white p-4 text-xs text-slate-900 dark:bg-slate-950 dark:text-slate-100">
                {JSON.stringify(run.output_state, null, 2)}
              </pre>
            </div>
          ))
        )}
      </div>
    </section>
  );
}