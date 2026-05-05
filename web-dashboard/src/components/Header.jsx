export default function Header() {
  return (
    <header className="mb-5 border-b border-slate-200/80 pb-4">
      <div className="flex flex-col gap-4 xl:flex-row xl:items-center xl:justify-between">
        <div>
          <h2 className="text-2xl font-extrabold tracking-tight text-slate-950">Lịch học</h2>
        </div>

        <div className="flex items-center gap-5 self-end xl:self-auto">
          <button className="relative grid h-10 w-10 place-items-center rounded-2xl bg-white text-xl text-slate-600 shadow-card transition hover:-translate-y-0.5 hover:text-blue-600">
            🔔
            <span className="absolute -right-1 -top-1 grid h-5 w-5 place-items-center rounded-full bg-red-500 text-[10px] font-bold text-white">3</span>
          </button>
          <button className="grid h-10 w-10 place-items-center rounded-2xl bg-white text-xl text-slate-600 shadow-card transition hover:-translate-y-0.5 hover:text-blue-600">
            ☼
          </button>
          <div className="flex items-center gap-3 rounded-2xl bg-white py-1.5 pl-1.5 pr-3 shadow-card">
            <div className="grid h-10 w-10 place-items-center rounded-full bg-slate-300 text-xl">👤</div>
            <span className="hidden text-sm font-semibold text-slate-800 sm:block">Nguyễn Văn A</span>
            <span className="text-xs text-slate-500">▼</span>
          </div>
        </div>
      </div>

      <div className="mt-6 flex flex-col gap-3 xl:flex-row xl:items-center xl:justify-between">
        <div className="flex flex-wrap items-center gap-3">
          <button className="rounded-xl border border-slate-200 bg-white px-6 py-3 text-sm font-semibold text-slate-700 shadow-card transition hover:-translate-y-0.5 hover:border-blue-200 hover:text-blue-700">
            Hôm nay
          </button>
          <button className="grid h-11 w-11 place-items-center rounded-xl border border-slate-200 bg-white text-lg font-bold text-slate-700 shadow-card transition hover:-translate-y-0.5 hover:text-blue-700">
            ‹
          </button>
          <button className="grid h-11 w-11 place-items-center rounded-xl border border-slate-200 bg-white text-lg font-bold text-slate-700 shadow-card transition hover:-translate-y-0.5 hover:text-blue-700">
            ›
          </button>
          <p className="px-3 text-sm font-semibold text-slate-700">20/04/2026 - 26/04/2026</p>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <div className="flex rounded-xl border border-slate-200 bg-white p-1 shadow-card">
            <button className="rounded-lg bg-blue-50 px-8 py-2.5 text-sm font-bold text-blue-700 ring-1 ring-blue-200">Tuần</button>
            <button className="rounded-lg px-8 py-2.5 text-sm font-semibold text-slate-700 transition hover:bg-slate-100">Tháng</button>
          </div>
          <button className="rounded-xl bg-blue-600 px-6 py-3 text-sm font-bold text-white shadow-lg shadow-blue-200 transition hover:-translate-y-0.5 hover:bg-blue-700">
            + Thêm lịch
          </button>
        </div>
      </div>
    </header>
  );
}
