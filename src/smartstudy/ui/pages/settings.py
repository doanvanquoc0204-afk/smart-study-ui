from __future__ import annotations

import os

import customtkinter as ctk

from smartstudy.config.settings import AppSettings
from smartstudy.config.theme import COLORS, FONTS
from smartstudy.services.user_service import UserService


class SettingsPage(ctk.CTkFrame):
    def __init__(self, master, *, settings: AppSettings, user_service: UserService, on_navigate=None):
        super().__init__(master, fg_color=COLORS["app_bg"])
        self._settings = settings
        self._user_service = user_service
        self._on_navigate = on_navigate

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_body()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 10))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(header, text="Cài đặt", font=FONTS["h1"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=16, pady=(12, 2)
        )
        ctk.CTkLabel(
            header,
            text="Thông tin cấu hình mẫu cho người nối database và chatbot.",
            font=FONTS["body"].tk(),
            text_color=COLORS["muted"],
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        if self._on_navigate is not None:
            ctk.CTkButton(header, text="Về tổng quan", width=110, command=lambda: self._on_navigate("dashboard")).grid(
                row=0, column=1, rowspan=2, padx=16, pady=12
            )

    def _build_body(self) -> None:
        body = ctk.CTkScrollableFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        body.grid(row=1, column=0, sticky="nsew", padx=24, pady=(10, 24))
        body.grid_columnconfigure(0, weight=1)

        user = self._user_service.get_user()
        sections = [
            ("Người dùng", [("Họ tên", user.full_name), ("Mã sinh viên", user.student_code)]),
            (
                "Ứng dụng",
                [("Tên cửa sổ", self._settings.window_title), ("Kích thước", self._settings.window_geometry), ("Giao diện", "Light")],
            ),
            (
                "Database",
                [("SMARTSTUDY_DB_URL", os.getenv("SMARTSTUDY_DB_URL", "sqlite:///smartstudy.db"))],
            ),
            (
                "Chatbot",
                [
                    ("Base URL", os.getenv("SMARTSTUDY_ASSISTANT_BASE_URL", "Chưa cấu hình")),
                    ("Model", os.getenv("SMARTSTUDY_ASSISTANT_MODEL", "Mock assistant")),
                    ("API key", "Đọc từ biến môi trường, không hiển thị trong app"),
                ],
            ),
        ]

        for title, rows in sections:
            self._section(body, title, rows)

    def _section(self, parent: ctk.CTkFrame, title: str, rows: list[tuple[str, str]]) -> None:
        frame = ctk.CTkFrame(parent, fg_color=COLORS["surface_2"], corner_radius=8)
        frame.pack(fill="x", padx=12, pady=10)
        frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(frame, text=title, font=FONTS["h2"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=12, pady=(12, 8)
        )

        for index, (label, value) in enumerate(rows, start=1):
            ctk.CTkLabel(frame, text=label, font=FONTS["body_bold"].tk(), text_color=COLORS["muted"]).grid(
                row=index, column=0, sticky="w", padx=12, pady=5
            )
            ctk.CTkLabel(frame, text=value, font=FONTS["body"].tk(), text_color=COLORS["text"], wraplength=720).grid(
                row=index, column=1, sticky="w", padx=12, pady=5
            )
