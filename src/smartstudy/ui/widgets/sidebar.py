from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS
from smartstudy.core.models import User


class Sidebar(ctk.CTkFrame):
    def __init__(
        self,
        master,
        *,
        user: User,
        on_navigate,
    ):
        super().__init__(master, width=240, fg_color=COLORS["surface"])

        self._user = user
        self._on_navigate = on_navigate
        self.active_btn = None

        self.pack_propagate(False)
        self.configure(border_width=1, border_color=COLORS["border"])

        self._build_brand()
        self._build_menu()
        self._build_user_card()

    def _build_brand(self) -> None:
        top = ctk.CTkFrame(self, fg_color="transparent")
        top.pack(fill="x", padx=24, pady=(28, 34))

        mark = ctk.CTkFrame(top, width=50, height=50, fg_color=COLORS["primary_soft"], corner_radius=14)
        mark.pack(anchor="w")
        mark.pack_propagate(False)
        ctk.CTkLabel(mark, text="🎓", font=(FONTS["title"].family, 22, "bold")).pack(expand=True)

        ctk.CTkLabel(top, text="SmartStudy AI", font=FONTS["h1"].tk(), text_color=COLORS["text"]).pack(
            anchor="w", pady=(10, 2)
        )
        ctk.CTkLabel(
            top,
            text="Học thông minh, hiệu quả hơn",
            font=FONTS["small"].tk(),
            text_color=COLORS["muted"],
        ).pack(anchor="w")

    def _build_menu(self) -> None:
        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(fill="x", padx=12, pady=4)

        self.add_menu("dashboard", "⌂  Tổng quan", active=True)
        self.add_menu("schedule", "▣  Lịch học")
        self.add_menu("exams", "□  Đề thi")
        self.add_menu("documents", "▱  Tài liệu")
        self.add_menu("assistant", "✦  AI Assistant")
        self.add_menu("stats", "▥  Thống kê")
        self.add_menu("settings", "⚙  Cài đặt")

    def _build_user_card(self) -> None:
        bottom = ctk.CTkFrame(self, fg_color=COLORS["surface_2"], corner_radius=14)
        bottom.pack(side="bottom", fill="x", padx=12, pady=18)

        ctk.CTkLabel(bottom, text=self._user.full_name, font=FONTS["body_bold"].tk(), text_color=COLORS["text"]).pack(
            anchor="w", padx=14, pady=(12, 2)
        )
        ctk.CTkLabel(bottom, text=self._user.student_code, text_color=COLORS["muted"], font=FONTS["small"].tk()).pack(
            anchor="w", padx=14, pady=(0, 12)
        )

    def add_menu(self, page_key: str, text: str, active: bool = False) -> None:
        btn = ctk.CTkButton(
            self.menu_frame,
            text=text,
            anchor="w",
            height=50,
            corner_radius=8,
            fg_color=COLORS["primary"] if active else "transparent",
            text_color="white" if active else COLORS["text"],
            hover_color=COLORS["primary_hover"] if active else COLORS["primary_soft"],
            font=FONTS["body_bold"].tk() if active else FONTS["body"].tk(),
        )
        btn.pack(fill="x", pady=5)
        btn.configure(command=lambda b=btn, k=page_key: self._clicked(b, k))

        if active:
            self.active_btn = btn

    def _clicked(self, btn, page_key: str) -> None:
        self.set_active(btn)
        self._on_navigate(page_key)

    def set_active(self, btn) -> None:
        if self.active_btn:
            self.active_btn.configure(
                fg_color="transparent",
                text_color=COLORS["text"],
                font=FONTS["body"].tk(),
                hover_color=COLORS["primary_soft"],
            )

        btn.configure(
            fg_color=COLORS["primary"],
            text_color="white",
            font=FONTS["body_bold"].tk(),
            hover_color=COLORS["primary_hover"],
        )
        self.active_btn = btn
