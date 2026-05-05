from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import customtkinter as ctk


@dataclass(frozen=True)
class Route:
    key: str
    factory: Callable[[ctk.CTkFrame], ctk.CTkFrame]


class Router:
    def __init__(self, container: ctk.CTkFrame, routes: list[Route]):
        self._container = container
        self._routes = {r.key: r for r in routes}
        self._active: ctk.CTkFrame | None = None

    def show(self, key: str) -> None:
        route = self._routes.get(key)
        if route is None:
            raise KeyError(f"Unknown route: {key}")

        if self._active is not None:
            self._active.destroy()
            self._active = None

        view = route.factory(self._container)
        view.pack(fill="both", expand=True)
        self._active = view

