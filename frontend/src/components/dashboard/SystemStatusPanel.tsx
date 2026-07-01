interface Props {
  systemStatus: any;
}

export default function SystemStatusPanel({ systemStatus }: Props) {
  return (
    <section className="mt-6 rounded-2xl border border-slate-300 bg-white p-5 shadow-xl dark:border-slate-700 dark:bg-slate-900">
      <h3 className="text-xl font-bold text-slate-950 dark:text-white">
        System Status
      </h3>

      <div className="mt-4 grid grid-cols-1 gap-4 md:grid-cols-4">
        <StatusItem label="Backend" value={systemStatus?.backend ?? "-"} />
        <StatusItem label="Environment" value={systemStatus?.environment ?? "-"} />
        <StatusItem label="Database" value={systemStatus?.database ?? "-"} />
        <StatusItem label="Redis" value={systemStatus?.redis ?? "-"} />
      </div>
    </section>
  );
}

function StatusItem({ label, value }: any) {
  return (
    <div className="rounded-xl border border-slate-300 bg-slate-100 p-4 dark:border-slate-700 dark:bg-slate-800">
      <p className="text-sm font-bold text-slate-600 dark:text-slate-300">
        {label}
      </p>
      <p className="mt-2 text-xl font-extrabold text-cyan-600 dark:text-cyan-300">
        {value}
      </p>
    </div>
  );
}