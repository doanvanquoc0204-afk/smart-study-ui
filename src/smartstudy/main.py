from __future__ import annotations

from smartstudy.app import App
from smartstudy.config.theme import init_theme


def main() -> None:
    init_theme(appearance_mode="Light")

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

