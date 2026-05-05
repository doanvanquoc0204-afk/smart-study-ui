from __future__ import annotations

import customtkinter as ctk

from smartstudy.config.theme import COLORS, FONTS
from smartstudy.core.models import Event
from smartstudy.services.schedule_service import ScheduleService


class SchedulePage(ctk.CTkFrame):
    def __init__(self, master, *, schedule_service: ScheduleService, on_navigate=None):
        super().__init__(master, fg_color=COLORS["app_bg"])
        self._schedule_service = schedule_service
        self._on_navigate = on_navigate

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_content()
        self._render_events()

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color=COLORS["surface"], corner_radius=10)
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 10))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(header, text="Lịch học", font=FONTS["h1"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=16, pady=(12, 2)
        )
        ctk.CTkLabel(
            header,
            text="Quản lý lịch học mẫu. Sau này dữ liệu lấy từ database qua ScheduleService.",
            font=FONTS["body"].tk(),
            text_color=COLORS["muted"],
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 12))

        if self._on_navigate is not None:
            ctk.CTkButton(header, text="Về tổng quan", width=110, command=lambda: self._on_navigate("dashboard")).grid(
                row=0, column=1, rowspan=2, padx=16, pady=12
            )

    def _build_content(self) -> None:
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew", padx=24, pady=(10, 24))
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(1, weight=0)
        content.grid_rowconfigure(0, weight=1)

        self._event_list = ctk.CTkScrollableFrame(content, fg_color=COLORS["surface"], corner_radius=10)
        self._event_list.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

        form = ctk.CTkFrame(content, fg_color=COLORS["surface"], corner_radius=10, width=320)
        form.grid(row=0, column=1, sticky="ns")
        form.grid_propagate(False)

        ctk.CTkLabel(form, text="Thêm lịch nhanh", font=FONTS["h2"].tk(), text_color=COLORS["text"]).pack(
            anchor="w", padx=14, pady=(14, 8)
        )
        self._title = self._entry(form, "Tên môn")
        self._day = self._entry(form, "Ngày (1-7)")
        self._start = self._entry(form, "Giờ bắt đầu")
        self._end = self._entry(form, "Giờ kết thúc")

        self._error = ctk.CTkLabel(form, text="", font=FONTS["small"].tk(), text_color=COLORS["danger"], wraplength=280)
        self._error.pack(anchor="w", padx=14, pady=(6, 0))

        ctk.CTkButton(form, text="Thêm lịch", command=self._add_event).pack(fill="x", padx=14, pady=14)

    def _entry(self, parent: ctk.CTkFrame, placeholder: str) -> ctk.CTkEntry:
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder)
        entry.pack(fill="x", padx=14, pady=6)
        return entry

    def _render_events(self) -> None:
        for widget in self._event_list.winfo_children():
            widget.destroy()

        for event in self._schedule_service.list_events():
            self._event_card(event)

    def _event_card(self, event: Event) -> None:
        frame = ctk.CTkFrame(self._event_list, fg_color=COLORS["surface_2"], corner_radius=8)
        frame.pack(fill="x", padx=12, pady=8)
        frame.grid_columnconfigure(0, weight=1)

        day_label = "CN" if event.day_index == 6 else f"Thứ {event.day_index + 2}"
        title = f"{day_label} - {event.title}"
        ctk.CTkLabel(frame, text=title, font=FONTS["body_bold"].tk(), text_color=COLORS["text"]).grid(
            row=0, column=0, sticky="w", padx=12, pady=(10, 2)
        )
        ctk.CTkLabel(
            frame,
            text=f"{self._format_time(event.start_hour)} - {self._format_time(event.end_hour)} | {event.room}",
            font=FONTS["small"].tk(),
            text_color=COLORS["muted"],
        ).grid(row=1, column=0, sticky="w", padx=12, pady=(0, 10))

    def _add_event(self) -> None:
        payload = {
            "title": self._title.get(),
            "day": self._day.get(),
            "start": self._start.get(),
            "end": self._end.get(),
        }
        ok, message = self._schedule_service.add_event_from_payload(payload)
        if not ok:
            self._error.configure(text=message)
            return

        self._error.configure(text="")
        for entry in [self._title, self._day, self._start, self._end]:
            entry.delete(0, "end")
        self._render_events()

    def _format_time(self, hour: float) -> str:
        h = int(hour)
        m = int((hour - h) * 60)
        return f"{h}:{m:02d}"
