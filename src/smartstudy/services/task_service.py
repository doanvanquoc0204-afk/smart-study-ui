from __future__ import annotations

from smartstudy.core.models import Task


class TaskService:
    def list_tasks_today(self) -> list[Task]:
        return [
            Task("Nộp bài tập Lập trình Python", "K.A312", "23:59 hôm nay", urgent=True),
            Task("Ôn tập Tiếng Anh 2", "K.B102", "20:30", urgent=False),
            Task("Đọc tài liệu Kiến trúc máy tính", "K.A212", "21:00", urgent=False),
            Task("Làm đề thi Cấu trúc dữ liệu", "K.A313", "22:00", urgent=False),
        ]
