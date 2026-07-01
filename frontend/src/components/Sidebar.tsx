const MENU_ITEMS = [
  "Dashboard",
  "Live Feed",
  "AI Strategy",
  "Approval Queue",
  "Knowledge Graph",
  "Audit Trail",
];

export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 h-full w-72 border-r border-slate-700 bg-slate-900 p-6 shadow-xl">
      <h1 className="text-3xl font-extrabold text-white">
        CreatorOS
      </h1>

      <p className="mt-2 text-base font-semibold text-cyan-300">
        Multi-Agent Intelligence Hub
      </p>

      <nav className="mt-10 space-y-3">
        {MENU_ITEMS.map((item) => (
          <a
            key={item}
            href={`#${item.toLowerCase().replaceAll(" ", "-")}`}
            className="block cursor-pointer rounded-xl px-4 py-3 text-lg font-semibold text-slate-100 transition-all duration-200 hover:translate-x-1 hover:bg-cyan-500 hover:text-slate-950"
          >
            {item}
          </a>
        ))}
      </nav>
    </aside>
  );
}