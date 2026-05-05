from __future__ import annotations

import sys
from pathlib import Path


def _bootstrap_src_on_path() -> None:
    repo_root = Path(__file__).resolve().parent
    src_dir = repo_root / "src"
    sys.path.insert(0, str(src_dir))


def main() -> None:
    _bootstrap_src_on_path()
    from smartstudy.main import main as app_main  # noqa: E402

    app_main()


if __name__ == "__main__":
    main()

