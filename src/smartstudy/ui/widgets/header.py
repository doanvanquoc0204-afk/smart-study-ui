from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS


class Header(ctk.CTkFrame):
    def __init__(self, master, *, on_add_event=None):
        super().__init__(master, fg_color="transparent")

        self._on_add_event = on_add_event
        self.grid_columnconfigure(1, weight=1)

        left = ctk.CTkFrame(self, fg_color="transparent")
        left.grid(row=0, column=0, sticky="w")

        self._ghost_button(left, "Hôm nay", width=96).pack(side="left", padx=(0, 10))
        self._ghost_button(left, "<", width=42).pack(side="left", padx=4)
        self._ghost_button(left, ">", width=42).pack(side="left", padx=(4, 16))
        ctk.CTkLabel(
            left,
            text="20/04/2026 - 26/04/2026",
            font=FONTS["body_bold"].tk(),
            text_color=COLORS["text"],
        ).pack(side="left", padx=8)

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.grid(row=0, column=2, sticky="e")

        segmented = ctk.CTkFrame(right, fg_color=COLORS["surface"], corner_radius=12)
        segmented.pack(side="left", padx=(0, 16))
        self._segment_button(segmented, "Tuần", active=True).pack(side="left", padx=(4, 2), pady=4)
        self._segment_button(segmented, "Tháng", active=False).pack(side="left", padx=(2, 4), pady=4)

        ctk.CTkButton(
            right,
            text="+  Thêm lịch",
            width=128,
            height=38,
            corner_radius=10,
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            text_color="white",
            font=FONTS["body_bold"].tk(),
            command=self.add_event,
        ).pack(side="left")

    def _ghost_button(self, parent, text: str, *, width: int) -> ctk.CTkButton:
        return ctk.CTkButton(
            parent,
            text=text,
            width=width,
            height=38,
            corner_radius=10,
            fg_color=COLORS["surface"],
            hover_color=COLORS["primary_soft"],
            border_width=1,
            border_color=COLORS["border"],
            text_color=COLORS["text"],
            font=FONTS["body"].tk(),
        )

    def _segment_button(self, parent, text: str, *, active: bool) -> ctk.CTkButton:
        return ctk.CTkButton(
            parent,
            text=text,
            width=86,
            height=34,
            corner_radius=9,
            fg_color=COLORS["primary_soft"] if active else "transparent",
            hover_color=COLORS["primary_soft"],
            border_width=1 if active else 0,
            border_color="#BBD2FF",
            text_color=COLORS["primary"] if active else COLORS["text"],
            font=FONTS["body_bold"].tk() if active else FONTS["body"].tk(),
        )

    def add_event(self):
        popup = ctk.CTkToplevel(self)
        popup.geometry("340x310")
        popup.title("Thêm lịch")
        popup.configure(fg_color=COLORS["app_bg"])

        frame = ctk.CTkFrame(popup, fg_color=COLORS["surface"], corner_radius=14)
        frame.pack(fill="both", expand=True, padx=16, pady=16)

        ctk.CTkLabel(frame, text="Thêm lịch mới", font=FONTS["h2"].tk(), text_color=COLORS["text"]).pack(
            anchor="w", padx=14, pady=(14, 8)
        )

        title = ctk.CTkEntry(frame, placeholder_text="Tên môn")
        title.pack(fill="x", padx=14, pady=6)

        day = ctk.CTkEntry(frame, placeholder_text="Ngày (1-7)")
        day.pack(fill="x", padx=14, pady=6)

        start = ctk.CTkEntry(frame, placeholder_text="Giờ bắt đầu")
        start.pack(fill="x", padx=14, pady=6)

        end = ctk.CTkEntry(frame, placeholder_text="Giờ kết thúc")
        end.pack(fill="x", padx=14, pady=6)

        error = ctk.CTkLabel(frame, text="", text_color=COLORS["danger"], font=FONTS["small"].tk(), wraplength=280)
        error.pack(anchor="w", padx=14, pady=(6, 0))

        def save():
            payload = {"title": title.get(), "day": day.get(), "start": start.get(), "end": end.get()}

            if self._on_add_event is None:
                popup.destroy()
                return

            ok, message = self._on_add_event(payload)
            if ok:
                popup.destroy()
                return

            error.configure(text=message)

        ctk.CTkButton(frame, text="Thêm", height=36, corner_radius=12, command=save).pack(fill="x", padx=14, pady=14)
