from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS
from smartstudy.core.models import Exam
from smartstudy.services.exam_service import ExamService


class ExamsPage(ctk.CTkFrame):
    def __init__(self, master, *, exam_service: ExamService, on_navigate=None):
        super().__init__(master, fg_color=COLORS["app_bg"])
        self._exam_service = exam_service
        self._on_navigate = on_navigate

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._build_header()
        self._build_toolbar()
        self._build_list()
        self._render_exams(self._exam_service.list_exams())

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 10))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(header, text="Đề thi", font=FONTS["h1"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=16, pady=(12, 2)
        )
        ctk.CTkLabel(
            header,
            text="Kho đề thi mẫu theo môn học, học kỳ và trạng thái luyện tập.",
            font=FONTS["body"].tk(),
            text_color=COLORS["muted"],
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        if self._on_navigate is not None:
            ctk.CTkButton(header, text="Về tổng quan", width=110, command=lambda: self._on_navigate("dashboard")).grid(
                row=0, column=1, rowspan=2, padx=16, pady=12
            )

    def _build_toolbar(self) -> None:
        toolbar = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        toolbar.grid(row=1, column=0, sticky="ew", padx=24, pady=10)
        toolbar.grid_columnconfigure(0, weight=1)

        self._search = ctk.CTkEntry(toolbar, placeholder_text="Tìm theo tên đề, môn học hoặc trạng thái")
        self._search.grid(row=0, column=0, sticky="ew", padx=(12, 8), pady=12)
        self._search.bind("<Return>", lambda _event: self._search_exams())

        ctk.CTkButton(toolbar, text="Tìm", width=70, command=self._search_exams).grid(row=0, column=1, padx=4, pady=12)
        ctk.CTkButton(toolbar, text="+ Thêm đề", width=90, command=self._show_mock_notice).grid(
            row=0, column=2, padx=(4, 12), pady=12
        )

    def _build_list(self) -> None:
        self._list = ctk.CTkScrollableFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        self._list.grid(row=2, column=0, sticky="nsew", padx=24, pady=(10, 24))

    def _render_exams(self, exams: list[Exam]) -> None:
        for widget in self._list.winfo_children():
            widget.destroy()

        if not exams:
            ctk.CTkLabel(self._list, text="Không tìm thấy đề thi.", font=FONTS["body"].tk(), text_color=COLORS["muted"]).pack(
                pady=24
            )
            return

        for exam in exams:
            self._exam_card(exam)

    def _exam_card(self, exam: Exam) -> None:
        frame = ctk.CTkFrame(self._list, fg_color=COLORS["surface_2"], corner_radius=8)
        frame.pack(fill="x", padx=12, pady=8)
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(frame, text=exam.title, font=FONTS["body_bold"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=12, pady=(10, 2)
        )
        ctk.CTkLabel(
            frame,
            text=f"{exam.subject} | {exam.term} | {exam.question_count} câu",
            font=FONTS["small"].tk(),
            text_color=COLORS["muted"],
        ).grid(row=1, column=0, sticky="w", padx=12, pady=(0, 10))
        ctk.CTkButton(frame, text=exam.status, width=90, height=28).grid(row=0, column=1, rowspan=2, padx=12, pady=10)

    def _search_exams(self) -> None:
        self._render_exams(self._exam_service.search_exams(self._search.get()))

    def _show_mock_notice(self) -> None:
        self._search.delete(0, "end")
        self._search.insert(0, "Chức năng thêm đề đang chờ nối database")
