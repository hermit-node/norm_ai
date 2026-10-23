"""Norm AI startup: load settings and start N4."""
from __future__ import annotations

import argparse

from config import parse_settings
from router.n4 import N4


def main(gui: bool = False) -> None:
    initialize(gui)


def initialize(gui: bool) -> None:
    N4.settings = parse_settings(gui)
    N4.start_server()


def load_model():
    pass


def load_ui():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", action="store_true")
    args = parser.parse_args()
    main(gui=args.gui)
