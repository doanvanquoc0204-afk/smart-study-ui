import BottomSection from "./components/BottomSection.jsx";
import Header from "./components/Header.jsx";
import RightPanel from "./components/RightPanel.jsx";
import Sidebar from "./components/Sidebar.jsx";
import Timetable from "./components/Timetable.jsx";

export default function App() {
  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top_right,_#eef4ff,_transparent_38%),#f6f8fc]">
      <Sidebar />

      <main className="lg:pl-[270px]">
        <div className="mx-auto max-w-[1680px] px-4 py-5 sm:px-6 lg:px-7">
          <Header />

          <div className="grid gap-5 xl:grid-cols-[minmax(0,1fr)_360px]">
            <div className="min-w-0 space-y-5">
              <div className="overflow-x-auto rounded-3xl">
                <Timetable />
              </div>
              <BottomSection />
            </div>
            <RightPanel />
          </div>
        </div>
      </main>
    </div>
  );
}
