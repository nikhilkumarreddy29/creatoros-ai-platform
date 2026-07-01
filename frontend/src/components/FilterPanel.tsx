import { Filter } from "lucide-react";

const FILTERS = [
  "All",
  "YouTube",
  "LinkedIn",
  "Tech",
  "Sports",
  "Movies",
  "Food",
  "Friends",
];

interface Props {
  activeFilter: string;
  setActiveFilter: (value: string) => void;
}

export default function FilterPanel({
  activeFilter,
  setActiveFilter,
}: Props) {
  return (
    <section className="mt-6 rounded-2xl border border-slate-300 bg-white p-5 shadow-xl dark:border-slate-700 dark:bg-slate-900">
      <div className="flex items-center gap-2 text-cyan-600 dark:text-cyan-300">
        <Filter size={20} />
        <p className="text-lg font-bold">
          Filters
        </p>
      </div>

      <div className="mt-4 flex flex-wrap gap-3">
        {FILTERS.map((filter) => (
          <button
            key={filter}
            onClick={() => setActiveFilter(filter)}
            className={
              activeFilter === filter
                ? "rounded-full bg-cyan-500 px-5 py-2 font-bold text-slate-950"
                : "rounded-full border border-slate-300 bg-slate-100 px-5 py-2 font-bold text-slate-900 hover:border-cyan-400 hover:bg-slate-200 dark:border-slate-600 dark:bg-slate-800 dark:text-slate-100 dark:hover:bg-slate-700"
            }
          >
            {filter}
          </button>
        ))}
      </div>

      <p className="mt-3 text-sm text-slate-600 dark:text-slate-400">
        Active Filter

        <span className="ml-2 font-bold text-cyan-600 dark:text-cyan-300">
          {activeFilter}
        </span>
      </p>
    </section>
  );
}