from __future__ import annotations

from smartstudy.core.models import Exam


class ExamService:
    def list_exams(self) -> list[Exam]:
        return [
            Exam("Đề giữa kỳ Python", "Lập trình Python", "HK2 2025-2026", "Chưa làm", 40),
            Exam("Ôn tập Cấu trúc dữ liệu", "Cấu trúc DL", "HK2 2025-2026", "Đang làm", 35),
            Exam("Đề mẫu Tiếng Anh 2", "Tiếng Anh 2", "HK2 2025-2026", "Đã làm", 50),
            Exam("Kiến trúc máy tính - đề 1", "Kiến trúc máy tính", "HK2 2025-2026", "Chưa làm", 30),
        ]

    def search_exams(self, keyword: str) -> list[Exam]:
        normalized = keyword.strip().lower()
        exams = self.list_exams()
        if not normalized:
            return exams

        return [
            exam
            for exam in exams
            if normalized in exam.title.lower()
            or normalized in exam.subject.lower()
            or normalized in exam.status.lower()
        ]
