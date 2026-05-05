from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import customtkinter as ctk


@dataclass(frozen=True)
class FontSpec:
    family: str
    size: int
    weight: str | None = None

    def tk(self):
        if self.weight:
            return (self.family, self.size, self.weight)
        return (self.family, self.size)


FONT_FAMILY: Final[str] = "Segoe UI"

FONTS: Final[dict[str, FontSpec]] = {
    "title": FontSpec(FONT_FAMILY, 22, "bold"),
    "h1": FontSpec(FONT_FAMILY, 20, "bold"),
    "h2": FontSpec(FONT_FAMILY, 14, "bold"),
    "h3": FontSpec(FONT_FAMILY, 13, "bold"),
    "body_bold": FontSpec(FONT_FAMILY, 11, "bold"),
    "body": FontSpec(FONT_FAMILY, 11),
    "small": FontSpec(FONT_FAMILY, 10),
    "tiny": FontSpec(FONT_FAMILY, 8),
}


# Use (light, dark) tuples so CTk automatically adapts in System/Dark modes.
COLORS: Final[dict[str, tuple[str, str]]] = {
    "app_bg": ("#F6F9FC", "#0B1220"),
    "surface": ("#FFFFFF", "#0F172A"),
    "surface_2": ("#F8FBFF", "#111C33"),
    "border": ("#E6EDF5", "#1F2A44"),
    "text": ("#0F172A", "#E5E7EB"),
    "muted": ("#64748B", "#94A3B8"),
    "primary": ("#2563EB", "#60A5FA"),
    "primary_hover": ("#1D4ED8", "#93C5FD"),
    "primary_soft": ("#EAF2FF", "#102A56"),
    "success": ("#16A34A", "#4ADE80"),
    "success_soft": ("#DCFCE7", "#103A27"),
    "warning": ("#D97706", "#FBBF24"),
    "warning_soft": ("#FEF3C7", "#45310B"),
    "danger": ("#EF4444", "#F87171"),
    "calendar_today": ("#DBEAFE", "#102A56"),
    "calendar_cell_today": ("#EFF6FF", "#0B254A"),
    "calendar_cell": ("#F8FAFC", "#0D1A2D"),
}


def init_theme(*, appearance_mode: str = "System") -> None:
    """Initialize global CustomTkinter theme settings.

    appearance_mode: "System" | "Light" | "Dark"
    """
    ctk.set_appearance_mode(appearance_mode)
    ctk.set_default_color_theme("blue")

