import { Search } from "lucide-react";

interface Props {
  searchQuery: string;
  setSearchQuery: (value: string) => void;
  searchResults: any[];
}

export default function SearchPanel({
  searchQuery,
  setSearchQuery,
  searchResults,
}: Props) {
  return (
    <section className="mt-6 rounded-2xl border border-slate-700 bg-slate-900 p-5 shadow-xl">
      <div className="flex items-center gap-2 text-cyan-300">
        <Search size={20} />
        <h3 className="text-xl font-bold text-white">Global Search</h3>
      </div>

      <input
        value={searchQuery}
        onChange={(event) => setSearchQuery(event.target.value)}
        placeholder="Search drafts, strategies, graph, live events..."
        className="mt-4 w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-white outline-none focus:border-cyan-400"
      />

      {searchQuery && (
        <div className="mt-4 space-y-3">
          {searchResults.length === 0 ? (
            <p className="text-slate-400">No results found.</p>
          ) : (
            searchResults.map((item, index) => (
              <div
                key={index}
                className="rounded-xl border border-slate-700 bg-slate-800 p-4"
              >
                <p className="font-bold text-cyan-300">{item.type}</p>
                <p className="mt-1 text-sm text-slate-200">{item.title}</p>
                <p className="mt-1 text-xs text-slate-400">{item.detail}</p>
              </div>
            ))
          )}
        </div>
      )}
    </section>
  );
}