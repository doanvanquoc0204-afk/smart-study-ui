from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS


class PlaceholderPage(ctk.CTkFrame):
    def __init__(self, master, *, title: str, on_navigate=None):
        super().__init__(master, fg_color=COLORS["app_bg"])

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        card = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=12)
        card.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)

        ctk.CTkLabel(card, text=title, font=FONTS["title"].tk(), text_color=COLORS["text"]).pack(
            padx=20, pady=(20, 8)
        )
        ctk.CTkLabel(
            card,
            text="Trang này sẽ được triển khai sau.",
            text_color=COLORS["muted"],
            font=(FONTS["h2"].family, 12),
        ).pack(padx=20, pady=(0, 20))

        if on_navigate is not None:
            ctk.CTkButton(
                card,
                text="Về tổng quan",
                width=120,
                command=lambda: on_navigate("dashboard"),
            ).pack(pady=(0, 20))
