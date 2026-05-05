from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS


class BottomCards(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent", height=150)
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.suggest_card()
        self.stats_card()

    def suggest_card(self):
        frame = self.card("Gợi ý lịch học thông minh")

        ctk.CTkLabel(
            frame,
            text="AI đề xuất lịch học dựa trên môn học, deadline và mức độ ưu tiên.",
            text_color=COLORS["muted"],
            font=FONTS["body"].tk(),
            wraplength=520,
            justify="left",
        ).pack(anchor="w", padx=16)

        ctk.CTkButton(frame, text="Xem gợi ý", width=140, height=36, corner_radius=12).pack(
            anchor="e", padx=16, pady=(4, 14)
        )

        frame.grid(row=0, column=0, padx=(0, 10), pady=0, sticky="nsew")

    def stats_card(self):
        frame = self.card("Thống kê tuần")

        stats = [("28", "Tổng số tiết"), ("22", "Tiết học"), ("6", "Tự học"), ("85%", "Hoàn thành")]

        grid = ctk.CTkFrame(frame, fg_color="transparent")
        grid.pack(fill="x", padx=12, pady=(4, 12))

        for index, (num, label) in enumerate(stats):
            grid.grid_columnconfigure(index, weight=1)
            box = ctk.CTkFrame(grid, fg_color=COLORS["surface_2"], corner_radius=12)
            box.grid(row=0, column=index, padx=4, sticky="ew")

            ctk.CTkLabel(box, text=num, font=FONTS["h2"].tk(), text_color=COLORS["primary"]).pack(pady=(10, 2))
            ctk.CTkLabel(box, text=label, text_color=COLORS["muted"], font=FONTS["small"].tk()).pack(pady=(0, 10))

        frame.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="nsew")

    def card(self, title):
        frame = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=12)
        frame.configure(border_width=1, border_color=COLORS["border"])

        ctk.CTkLabel(frame, text=title, font=FONTS["h3"].tk(), text_color=COLORS["text"]).pack(
            anchor="w", padx=16, pady=(16, 10)
        )
        return frame
