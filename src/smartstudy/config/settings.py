from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AppSettings:
    window_title: str = "SmartStudy AI"
    window_geometry: str = "1536x1024"

    # Root window background (light, dark)
    root_fg_color: tuple[str, str] = ("white", "#050A18")
