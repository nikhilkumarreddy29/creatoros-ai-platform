import { Moon, Sun } from "lucide-react";

interface Props {
  theme: string;
  toggleTheme: () => void;
}

export default function ThemeToggle({ theme, toggleTheme }: Props) {
  return (
    <button
      onClick={toggleTheme}
      className="rounded-xl border border-slate-600 bg-slate-800 px-4 py-2 font-bold text-slate-100 hover:border-cyan-400 hover:bg-slate-700 dark:border-slate-600 dark:bg-slate-800"
    >
      {theme === "dark" ? (
        <span className="flex items-center gap-2">
          <Sun size={18} />
          Light Mode
        </span>
      ) : (
        <span className="flex items-center gap-2">
          <Moon size={18} />
          Dark Mode
        </span>
      )}
    </button>
  );
}