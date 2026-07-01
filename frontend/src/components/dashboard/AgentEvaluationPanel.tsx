interface Props {
  evaluation: any;
}

export default function AgentEvaluationPanel({ evaluation }: Props) {
  const summary = evaluation?.summary;

  return (
    <section
      id="agent-evaluation"
      className="mt-8 rounded-2xl border border-slate-300 bg-white p-6 shadow-xl dark:border-slate-700 dark:bg-slate-900"
    >
      <h3 className="text-2xl font-bold text-slate-950 dark:text-white">
        Agent Evaluation Dashboard
      </h3>

      <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">
        Tracks agent quality, latency, safety checks, and workflow reliability.
      </p>

      <div className="mt-6 grid grid-cols-1 gap-4 md:grid-cols-4">
        <Metric label="Success Rate" value={`${summary?.success_rate ?? "-"}%`} />
        <Metric label="Avg Latency" value={`${summary?.average_latency_ms ?? "-"} ms`} />
        <Metric label="Tool Calls" value={summary?.tool_calls ?? "-"} />
        <Metric label="Guardrail Blocks" value={summary?.guardrail_blocks ?? "-"} />
      </div>

      <div className="mt-6 space-y-3">
        {evaluation?.agents?.map((agent: any, index: number) => (
          <div
            key={index}
            className="rounded-xl border border-slate-300 bg-slate-100 p-4 dark:border-slate-700 dark:bg-slate-800"
          >
            <div className="flex items-center justify-between">
              <p className="font-bold text-cyan-600 dark:text-cyan-300">
                {agent.name}
              </p>

              <p className="text-sm font-bold text-slate-700 dark:text-slate-200">
                {agent.success_rate}% success · {agent.latency_ms} ms
              </p>
            </div>

            <div className="mt-3 h-3 rounded-full bg-slate-300 dark:bg-slate-700">
              <div
                className="h-3 rounded-full bg-cyan-500"
                style={{ width: `${agent.success_rate}%` }}
              />
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

function Metric({ label, value }: any) {
  return (
    <div className="rounded-xl border border-slate-300 bg-slate-100 p-4 dark:border-slate-700 dark:bg-slate-800">
      <p className="text-sm font-bold text-slate-600 dark:text-slate-300">
        {label}
      </p>
      <p className="mt-2 text-2xl font-extrabold text-cyan-600 dark:text-cyan-300">
        {value}
      </p>
    </div>
  );
}