interface Props {
  pendingDrafts: any[];
  approveDraft: (workflowId: string) => void;
  rejectDraft: (workflowId: string) => void;
  regenerateDraft: (workflowId: string) => void;
}

export default function ApprovalQueue({
  pendingDrafts,
  approveDraft,
  rejectDraft,
  regenerateDraft,
}: Props) {
  return (
    <section
      id="approval-queue"
      className="mt-8 rounded-2xl border border-slate-300 bg-white p-6 shadow-xl dark:border-slate-700 dark:bg-slate-900"
    >
      <h3 className="text-2xl font-bold text-slate-950 dark:text-white">
        Approval Queue
      </h3>

      <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">
        Human-in-the-loop review before publishing.
      </p>

      <div className="mt-5 space-y-4">
        {pendingDrafts.length === 0 ? (
          <p className="text-slate-500 dark:text-slate-400">
            No pending drafts. Create one from Swagger using /agents/rag-draft.
          </p>
        ) : (
          pendingDrafts.map((draft) => (
            <div
              key={draft.workflow_id}
              className="rounded-xl border border-slate-300 bg-slate-100 p-5 dark:border-slate-700 dark:bg-slate-800"
            >
              <p className="text-lg font-bold text-cyan-600 dark:text-cyan-300">
                {draft.topic}
              </p>

              <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
                Workflow: {draft.workflow_id}
              </p>

              <pre className="mt-4 max-h-60 overflow-auto whitespace-pre-wrap rounded-lg bg-white p-4 text-sm text-slate-900 dark:bg-slate-950 dark:text-slate-100">
                {draft.draft || draft.suggested_reply}
              </pre>

              <div className="mt-4 flex gap-3">
                <button
                  onClick={() => approveDraft(draft.workflow_id)}
                  className="rounded-lg bg-green-500 px-4 py-2 font-bold text-slate-950"
                >
                  Approve
                </button>

                <button
                  onClick={() => rejectDraft(draft.workflow_id)}
                  className="rounded-lg bg-red-500 px-4 py-2 font-bold text-white"
                >
                  Reject
                </button>

                <button
                  onClick={() => regenerateDraft(draft.workflow_id)}
                  className="rounded-lg bg-cyan-500 px-4 py-2 font-bold text-slate-950"
                >
                  Regenerate
                </button>
              </div>
            </div>
          ))
        )}
      </div>
    </section>
  );
}