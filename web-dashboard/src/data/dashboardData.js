export const days = [
  { key: "mon", label: "Thứ 2", date: "20/04" },
  { key: "tue", label: "Thứ 3", date: "21/04", current: true },
  { key: "wed", label: "Thứ 4", date: "22/04" },
  { key: "thu", label: "Thứ 5", date: "23/04" },
  { key: "fri", label: "Thứ 6", date: "24/04" },
  { key: "sat", label: "Thứ 7", date: "25/04" },
  { key: "sun", label: "Chủ nhật", date: "26/04" }
];

export const timeSlots = ["07:00", "08:00", "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00"];

export const classes = [
  {
    id: 1,
    day: "tue",
    start: "07:00",
    end: "09:30",
    subject: "Thiết kế web (9)_TA",
    room: "K.A215",
    place: "P. A215",
    category: "Khoa học máy tính",
    color: "bg-emerald-100 border-emerald-300 text-emerald-950",
    dot: "bg-emerald-500"
  },
  {
    id: 2,
    day: "wed",
    start: "07:00",
    end: "09:30",
    subject: "Kiến trúc máy tính (1)_TA",
    room: "K.A212",
    place: "P. A212",
    category: "Toán",
    color: "bg-amber-100 border-amber-300 text-amber-950",
    dot: "bg-amber-700"
  },
  {
    id: 3,
    day: "thu",
    start: "08:00",
    end: "10:30",
    subject: "Tiếng Anh 2 (18)",
    room: "K.B102",
    place: "P. B102",
    category: "Ngoại ngữ",
    color: "bg-slate-800 border-slate-700 text-white",
    dot: "bg-emerald-300"
  },
  {
    id: 4,
    day: "sat",
    start: "07:00",
    end: "09:30",
    subject: "GDTC 2 (Bóng chuyền) (5)",
    room: "K. Sân bóng chuyền",
    place: "Sân bóng chuyền",
    category: "GDTC",
    color: "bg-rose-950 border-rose-900 text-white",
    dot: "bg-pink-500"
  },
  {
    id: 5,
    day: "mon",
    start: "13:00",
    end: "14:30",
    subject: "Đại số tuyến tính (9)_TA",
    room: "K.A212",
    place: "P. A212",
    category: "Khoa học máy tính",
    color: "bg-emerald-900 border-emerald-800 text-white",
    dot: "bg-emerald-300"
  },
  {
    id: 6,
    day: "mon",
    start: "15:00",
    end: "16:30",
    subject: "Khởi nghiệp và đổi mới sáng tạo (9)",
    room: "K.A110",
    place: "P. A110",
    category: "Khoa học máy tính",
    color: "bg-green-900 border-green-800 text-white",
    dot: "bg-emerald-300"
  },
  {
    id: 7,
    day: "tue",
    start: "13:00",
    end: "16:00",
    subject: "Lập trình Python (1)_TA",
    room: "K.A312",
    place: "P. A312",
    category: "Ngoại ngữ",
    color: "bg-cyan-950 border-cyan-900 text-white",
    dot: "bg-emerald-300"
  },
  {
    id: 8,
    day: "wed",
    start: "13:00",
    end: "16:00",
    subject: "Tiếng Anh chuyên ngành 2 (IT) (9)",
    room: "K.B102",
    place: "P. B102",
    category: "Toán",
    color: "bg-stone-700 border-stone-600 text-white",
    dot: "bg-stone-400"
  },
  {
    id: 9,
    day: "fri",
    start: "13:00",
    end: "16:00",
    subject: "Cấu trúc dữ liệu và giải thuật (9)_TA",
    room: "K.A313",
    place: "P. A313",
    category: "Khác",
    color: "bg-purple-900 border-purple-800 text-white",
    dot: "bg-violet-500"
  }
];

export const tasks = [
  { title: "Nộp bài tập Lập trình Python", code: "K.A312", deadline: "Hạn: 23:59 hôm nay", urgent: true },
  { title: "Ôn tập Tiếng Anh 2", code: "K.B102", deadline: "20:30" },
  { title: "Đọc tài liệu Kiến trúc máy tính", code: "K.A212", deadline: "21:00" },
  { title: "Làm đề thi Cấu trúc dữ liệu", code: "K.A313", deadline: "22:00" }
];

export const quickActions = [
  { label: "Đề thi", icon: "📄", color: "text-indigo-500" },
  { label: "Tài liệu", icon: "📁", color: "text-yellow-500" },
  { label: "Thống kê", icon: "📊", color: "text-violet-500" },
  { label: "Ghi chú", icon: "📝", color: "text-pink-500" }
];

export const notifications = [
  { text: "Lịch học K.A215 đã được cập nhật", time: "2 giờ trước", icon: "✣", color: "text-slate-400" },
  { text: "Có 3 đề thi mới được thêm vào", time: "5 giờ trước", icon: "✖", color: "text-rose-400" }
];

export const legends = [
  { label: "Khoa học máy tính", color: "bg-emerald-500" },
  { label: "Ngoại ngữ", color: "bg-blue-600" },
  { label: "Toán", color: "bg-stone-500" },
  { label: "GDTC", color: "bg-rose-800" },
  { label: "Khác", color: "bg-violet-600" }
];
