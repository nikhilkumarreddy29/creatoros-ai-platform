import { ReactNode } from "react";
import Sidebar from "../components/Sidebar";

interface Props {
  children: ReactNode;
}

export default function DashboardLayout({
  children,
}: Props) {
  return (
    <div className="min-h-screen bg-slate-100 text-slate-950 dark:bg-slate-950 dark:text-white">

      <Sidebar />

      <main className="ml-72 p-8">

        {children}

      </main>

    </div>
  );
}