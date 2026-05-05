from __future__ import annotations

import customtkinter as ctk

from smartstudy.core.models import CalendarDay, Event
from smartstudy.config.theme import COLORS, FONTS


class Calendar(ctk.CTkFrame):
    def __init__(
        self,
        master,
        *,
        days: list[CalendarDay],
        events: list[Event],
        current_day_index: int = 1,
    ):
        super().__init__(master, fg_color=COLORS["surface"], corner_radius=18)
        self.configure(border_width=1, border_color=COLORS["border"])

        self.days = days
        self.current_day = current_day_index
        self.events = events

        self.draw()

    def set_data(
        self,
        *,
        days: list[CalendarDay] | None = None,
        events: list[Event] | None = None,
        current_day_index: int | None = None,
    ) -> None:
        if days is not None:
            self.days = days
        if events is not None:
            self.events = events
        if current_day_index is not None:
            self.current_day = current_day_index

        self.draw()

    def draw(self) -> None:
        for w in self.winfo_children():
            w.destroy()

        self.grid_columnconfigure(0, weight=0)
        for i in range(7):
            self.grid_columnconfigure(i + 1, weight=1)

        for i, day in enumerate(self.days):
            label = "Chủ nhật" if day.label == "CN" else day.label
            frame = ctk.CTkFrame(
                self,
                fg_color=COLORS["calendar_today"] if i == self.current_day else COLORS["app_bg"],
                corner_radius=8,
            )
            frame.grid(row=0, column=i + 1, sticky="ew", padx=4, pady=(10, 8))

            ctk.CTkLabel(frame, text=label, font=FONTS["body_bold"].tk(), text_color=COLORS["text"]).pack(
                pady=(8, 2)
            )
            ctk.CTkLabel(frame, text=day.date_text, font=FONTS["small"].tk(), text_color=COLORS["muted"]).pack(
                pady=(0, 8)
            )

        row = 1

        ctk.CTkLabel(self, text="Sáng", font=FONTS["body_bold"].tk(), text_color=COLORS["text"]).grid(
            row=row, column=0, sticky="w", padx=10, pady=(4, 8)
        )
        row += 1

        for h in range(7, 12):
            for half in [0, 0.5]:
                self.draw_cell(row, h + half)
                self.grid_rowconfigure(row, weight=1)
                row += 1

        ctk.CTkLabel(self, text="Chiều", font=FONTS["body_bold"].tk(), text_color=COLORS["text"]).grid(
            row=row, column=0, sticky="w", padx=10, pady=(10, 8)
        )
        row += 1

        for h in range(13, 18):
            for half in [0, 0.5]:
                self.draw_cell(row, h + half)
                self.grid_rowconfigure(row, weight=1)
                row += 1

        for e in self.events:
            self.create_event(e)

        self._draw_legend(row)

    def draw_cell(self, row: int, hour: float) -> None:
        label = f"{int(hour)}:{'30' if hour % 1 else '00'}"

        ctk.CTkLabel(self, text=label, font=FONTS["tiny"].tk(), text_color=COLORS["muted"]).grid(
            row=row, column=0, padx=(10, 8)
        )

        for c in range(7):
            ctk.CTkFrame(
                self,
                fg_color=COLORS["calendar_cell_today"] if c == self.current_day else COLORS["calendar_cell"],
                corner_radius=6,
            ).grid(row=row, column=c + 1, sticky="nsew", padx=2, pady=2)

    def create_event(self, e: Event) -> None:
        row = self.get_row(e.start_hour)
        span = int((e.end_hour - e.start_hour) * 2)

        frame = ctk.CTkFrame(self, fg_color=e.color, corner_radius=10)
        frame.grid(
            row=row,
            column=e.day_index + 1,
            rowspan=span,
            sticky="nsew",
            padx=4,
            pady=4,
        )

        text_color = "white" if e.color not in ["#d1fae5", "#fef3c7"] else "black"

        ctk.CTkLabel(
            frame,
            text=e.title,
            text_color=text_color,
            font=FONTS["small"].tk(),
            justify="left",
            wraplength=118,
        ).pack(anchor="w", padx=8, pady=(8, 2))
        ctk.CTkLabel(frame, text=e.room, text_color=text_color, font=FONTS["tiny"].tk()).pack(anchor="w", padx=8)
        ctk.CTkLabel(
            frame,
            text=f"{self.format_time(e.start_hour)} - {self.format_time(e.end_hour)}",
            text_color=text_color,
            font=FONTS["tiny"].tk(),
        ).pack(anchor="w", padx=8, pady=(2, 0))

        place = ctk.CTkFrame(frame, fg_color="transparent")
        place.pack(anchor="w", padx=8, pady=(4, 8))
        ctk.CTkLabel(place, text="●", text_color=self._dot_color(e.color), font=FONTS["tiny"].tk()).pack(
            side="left", padx=(0, 5)
        )
        ctk.CTkLabel(place, text=f"P. {e.room.split('.')[-1] if '.' in e.room else e.room}", text_color=text_color, font=FONTS["tiny"].tk()).pack(side="left")

    def get_row(self, hour: float) -> int:
        if hour < 12:
            return 2 + int((hour - 7) * 2)
        return 2 + 10 + 1 + int((hour - 13) * 2)

    def format_time(self, t: float) -> str:
        h = int(t)
        m = int((t - h) * 60)
        return f"{h}:{m:02d}"

    def _draw_legend(self, row: int) -> None:
        legend = ctk.CTkFrame(self, fg_color="transparent")
        legend.grid(row=row, column=0, columnspan=8, sticky="ew", padx=16, pady=(12, 14))

        items = [
            ("Khoa học máy tính", "#10b981"),
            ("Ngoại ngữ", "#2563eb"),
            ("Toán", "#78716c"),
            ("GDTC", "#7f1d1d"),
            ("Khác", "#6d28d9"),
        ]
        for label, color in items:
            item = ctk.CTkFrame(legend, fg_color="transparent")
            item.pack(side="left", padx=(0, 24))
            ctk.CTkLabel(item, text="●", text_color=color, font=FONTS["small"].tk()).pack(side="left", padx=(0, 6))
            ctk.CTkLabel(item, text=label, text_color=COLORS["muted"], font=FONTS["small"].tk()).pack(side="left")

    def _dot_color(self, color: str) -> str:
        if color in ["#d1fae5", "#14532d"]:
            return "#10b981"
        if color in ["#1e3a8a", "#1f2937"]:
            return "#60a5fa"
        if color in ["#fef3c7", "#78350f"]:
            return "#78716c"
        if color == "#7c2d12":
            return "#ec4899"
        return "#8b5cf6"

