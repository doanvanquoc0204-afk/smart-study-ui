from __future__ import annotations

from smartstudy.core.models import StudyDocument


class DocumentService:
    def list_documents(self) -> list[StudyDocument]:
        return [
            StudyDocument("Slide Python cơ bản", "Lập trình Python", "PDF", "Hôm nay", "2.4 MB"),
            StudyDocument("Bài tập ma trận", "Đại số tuyến tính", "DOCX", "Hôm qua", "480 KB"),
            StudyDocument("Tổng hợp từ vựng Unit 4", "Tiếng Anh 2", "PDF", "2 ngày trước", "1.1 MB"),
            StudyDocument("Sơ đồ cây nhị phân", "Cấu trúc DL", "PNG", "3 ngày trước", "720 KB"),
        ]

    def search_documents(self, keyword: str) -> list[StudyDocument]:
        normalized = keyword.strip().lower()
        documents = self.list_documents()
        if not normalized:
            return documents

        return [
            document
            for document in documents
            if normalized in document.title.lower()
            or normalized in document.subject.lower()
            or normalized in document.file_type.lower()
        ]
