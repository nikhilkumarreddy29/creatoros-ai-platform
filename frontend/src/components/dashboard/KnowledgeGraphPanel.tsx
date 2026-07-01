import { Network } from "lucide-react";

interface Props {
  graph: any;
  buildGraph: () => void;
}

export default function KnowledgeGraphPanel({ graph, buildGraph }: Props) {
  return (
    <section
      id="knowledge-graph"
      className="mt-8 rounded-2xl border border-slate-300 bg-white p-6 shadow-xl dark:border-slate-700 dark:bg-slate-900"
    >
      <div className="flex items-center justify-between">
        <div>
          <h3 className="flex items-center gap-2 text-2xl font-bold text-slate-950 dark:text-white">
            <Network className="text-cyan-600 dark:text-cyan-300" />
            Knowledge Graph Viewer
          </h3>

          <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">
            Shows creator intelligence relationships between topics, genres, drafts, platforms, and personas.
          </p>
        </div>

        <button
          onClick={buildGraph}
          className="rounded-lg bg-cyan-500 px-4 py-2 font-bold text-slate-950 hover:bg-cyan-400"
        >
          Build Graph
        </button>
      </div>

      <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-2">
        <GraphColumn title="Nodes">
          {graph.nodes?.length === 0 ? (
            <p className="text-slate-500 dark:text-slate-400">
              No nodes yet. Click Build Graph or create a RAG draft.
            </p>
          ) : (
            graph.nodes?.map((node: any, index: number) => (
              <div key={index} className="rounded-lg bg-white p-3 dark:bg-slate-950">
                <p className="font-bold text-slate-950 dark:text-white">{node.name}</p>
                <p className="text-sm text-cyan-600 dark:text-cyan-300">{node.type}</p>
              </div>
            ))
          )}
        </GraphColumn>

        <GraphColumn title="Relationships">
          {graph.relationships?.length === 0 ? (
            <p className="text-slate-500 dark:text-slate-400">
              No relationships yet.
            </p>
          ) : (
            graph.relationships?.map((rel: any, index: number) => (
              <div key={index} className="rounded-lg bg-white p-3 dark:bg-slate-950">
                <p className="font-semibold text-slate-950 dark:text-white">
                  {rel.source} → {rel.target}
                </p>
                <p className="text-sm text-cyan-600 dark:text-cyan-300">{rel.type}</p>
              </div>
            ))
          )}
        </GraphColumn>
      </div>
    </section>
  );
}

function GraphColumn({ title, children }: any) {
  return (
    <div className="rounded-xl border border-slate-300 bg-slate-100 p-5 dark:border-slate-700 dark:bg-slate-800">
      <h4 className="text-xl font-bold text-cyan-600 dark:text-cyan-300">
        {title}
      </h4>

      <div className="mt-4 space-y-3">{children}</div>
    </div>
  );
}