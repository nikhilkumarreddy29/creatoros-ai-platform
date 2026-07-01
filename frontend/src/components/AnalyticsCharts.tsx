import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
} from "recharts";

interface Props {
  timeseries: any[];
  filteredGenreData: any[];
  activeFilter: string;
}

export default function AnalyticsCharts({
  timeseries,
  filteredGenreData,
  activeFilter,
}: Props) {
  return (
    <section className="mt-8 grid grid-cols-1 gap-6 xl:grid-cols-2">
      <ChartCard title="Weekly Platform Growth">
        <ResponsiveContainer width="100%" height={320}>
          <LineChart data={timeseries}>
            <XAxis dataKey="day" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip />
            {activeFilter !== "LinkedIn" && (
              <Line type="monotone" dataKey="youtube_views" stroke="#22d3ee" strokeWidth={3} />
            )}
            {activeFilter !== "YouTube" && (
              <Line type="monotone" dataKey="linkedin_impressions" stroke="#a78bfa" strokeWidth={3} />
            )}
          </LineChart>
        </ResponsiveContainer>
      </ChartCard>

      <ChartCard title="Engagement Trend">
        <ResponsiveContainer width="100%" height={320}>
          <BarChart data={timeseries}>
            <XAxis dataKey="day" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip />
            <Bar dataKey="engagement" fill="#22d3ee" radius={[8, 8, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </ChartCard>

      <ChartCard title="Genre Performance">
        <ResponsiveContainer width="100%" height={320}>
          <PieChart>
            <Pie data={filteredGenreData} dataKey="value" nameKey="genre" outerRadius={110} label>
              {filteredGenreData.map((_, index) => (
                <Cell key={index} fill={["#22d3ee", "#a78bfa", "#f97316", "#22c55e", "#f43f5e"][index % 5]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </ChartCard>

      <ChartCard title="Filter Insight">
        <div className="space-y-4 text-lg text-slate-200">
          <p>
            Current view is filtered by <span className="font-bold text-cyan-300">{activeFilter}</span>.
          </p>
          <p>
            Use platform filters to compare YouTube and LinkedIn performance. Use genre filters to focus strategy recommendations.
          </p>
          <p>
            Recommended action: choose the strongest genre and convert one idea into multiple platform assets.
          </p>
        </div>
      </ChartCard>
    </section>
  );
}

function ChartCard({ title, children }: any) {
  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-6 shadow-xl">
      <h3 className="mb-4 text-2xl font-bold text-white">{title}</h3>
      {children}
    </div>
  );
}