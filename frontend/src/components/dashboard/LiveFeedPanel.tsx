interface Props {
  liveEvents: any[];
}

export default function LiveFeedPanel({ liveEvents }: Props) {
  return (
    <section
      id="live-feed"
      className="mt-8 rounded-2xl border border-slate-300 bg-white p-6 shadow-xl dark:border-slate-700 dark:bg-slate-900"
    >
      <h3 className="text-2xl font-bold text-slate-950 dark:text-white">
        Live Feed
      </h3>

      <div className="mt-5 space-y-3">
        {liveEvents.length === 0 ? (
          <p className="text-slate-500 dark:text-slate-400">
            No live events received yet.
          </p>
        ) : (
          liveEvents.map((event, index) => (
            <div
              key={index}
              className="rounded-xl border border-slate-300 bg-slate-100 p-4 dark:border-slate-700 dark:bg-slate-800"
            >
              <pre className="overflow-auto whitespace-pre-wrap text-sm font-semibold text-cyan-700 dark:text-cyan-200">
                {JSON.stringify(event, null, 2)}
              </pre>
            </div>
          ))
        )}
      </div>
    </section>
  );
}