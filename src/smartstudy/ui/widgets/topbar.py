from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS
from smartstudy.core.models import User


class TopBar(ctk.CTkFrame):
    def __init__(self, master, *, user: User):
        super().__init__(master, fg_color="transparent", height=58)

        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text="Lịch học", font=FONTS["title"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=2, pady=(10, 4)
        )

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.grid(row=0, column=1, sticky="e", pady=(8, 4))

        notification = ctk.CTkFrame(right, fg_color="transparent")
        notification.pack(side="left", padx=8)
        ctk.CTkLabel(notification, text="🔔", font=(FONTS["body"].family, 18)).pack()
        ctk.CTkLabel(
            notification,
            text="3",
            width=18,
            height=18,
            fg_color=COLORS["danger"],
            corner_radius=9,
            text_color="white",
            font=FONTS["tiny"].tk(),
        ).place(x=14, y=-4)

        ctk.CTkButton(
            right,
            text="☼",
            width=36,
            height=36,
            fg_color="transparent",
            text_color=COLORS["text"],
            hover_color=COLORS["primary_soft"],
            corner_radius=12,
        ).pack(side="left", padx=8)

        user_box = ctk.CTkFrame(right, fg_color="transparent")
        user_box.pack(side="left", padx=(10, 0))

        avatar = ctk.CTkFrame(user_box, width=42, height=42, fg_color=COLORS["border"], corner_radius=21)
        avatar.pack(side="left", padx=(0, 8))
        avatar.pack_propagate(False)
        ctk.CTkLabel(avatar, text="👤", font=(FONTS["body"].family, 18)).pack(expand=True)

        ctk.CTkLabel(user_box, text=user.full_name, font=FONTS["body"].tk(), text_color=COLORS["text"]).pack(
            side="left"
        )
        ctk.CTkLabel(user_box, text="  ▼", font=FONTS["small"].tk(), text_color=COLORS["text"]).pack(side="left")
