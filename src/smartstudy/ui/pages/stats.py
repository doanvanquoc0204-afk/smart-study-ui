from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS
from smartstudy.services.stats_service import StatsService


class StatsPage(ctk.CTkFrame):
    def __init__(self, master, *, stats_service: StatsService, on_navigate=None):
        super().__init__(master, fg_color=COLORS["app_bg"])
        self._stats_service = stats_service
        self._on_navigate = on_navigate

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_body()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 10))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(header, text="Thống kê", font=FONTS["h1"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=16, pady=(12, 2)
        )
        ctk.CTkLabel(
            header,
            text="Tổng quan tiến độ học tập dựa trên dữ liệu service hiện tại.",
            font=FONTS["body"].tk(),
            text_color=COLORS["muted"],
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        if self._on_navigate is not None:
            ctk.CTkButton(header, text="Về tổng quan", width=110, command=lambda: self._on_navigate("dashboard")).grid(
                row=0, column=1, rowspan=2, padx=16, pady=12
            )

    def _build_body(self) -> None:
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.grid(row=1, column=0, sticky="nsew", padx=24, pady=(10, 24))
        for column in range(4):
            body.grid_columnconfigure(column, weight=1)
        body.grid_rowconfigure(1, weight=1)

        summary = self._stats_service.get_summary()
        cards = [
            ("Lịch học", str(summary.total_events)),
            ("Việc hôm nay", str(summary.total_tasks)),
            ("Việc gấp", str(summary.urgent_tasks)),
            ("Hoàn thành", f"{summary.completed_percent}%"),
        ]
        for column, (label, value) in enumerate(cards):
            self._summary_card(body, label, value).grid(row=0, column=column, sticky="ew", padx=6, pady=(0, 12))

        focus = ctk.CTkFrame(body, fg_color=COLORS["surface"], corner_radius=10)
        focus.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=6)

        ctk.CTkLabel(focus, text="Mức độ tập trung theo môn", font=FONTS["h2"].tk(), text_color=COLORS["text"]).pack(
            anchor="w", padx=14, pady=(14, 8)
        )

        for subject, percent in self._stats_service.weekly_focus():
            self._progress_row(focus, subject, percent)

    def _summary_card(self, parent: ctk.CTkFrame, label: str, value: str) -> ctk.CTkFrame:
        card = ctk.CTkFrame(parent, fg_color=COLORS["surface"], corner_radius=10)
        ctk.CTkLabel(card, text=value, font=FONTS["title"].tk(), text_color=COLORS["primary"]).pack(
            anchor="w", padx=14, pady=(14, 2)
        )
        ctk.CTkLabel(card, text=label, font=FONTS["body"].tk(), text_color=COLORS["muted"]).pack(
            anchor="w", padx=14, pady=(0, 14)
        )
        return card

    def _progress_row(self, parent: ctk.CTkFrame, subject: str, percent: int) -> None:
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=14, pady=8)
        row.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(row, text=subject, font=FONTS["body_bold"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w"
        )
        ctk.CTkLabel(row, text=f"{percent}%", font=FONTS["small"].tk(), text_color=COLORS["muted"]).grid(
            row=0, column=1, sticky="e"
        )
        progress = ctk.CTkProgressBar(row)
        progress.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(6, 0))
        progress.set(percent / 100)
