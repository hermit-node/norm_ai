"""Norm AI startup: load settings and start N4."""
from __future__ import annotations

import argparse

from config.config_middleman import norm_boot
from router.n4 import N4


def main(gui: bool = False) -> None:
    initialize(gui)


def initialize(gui: bool) -> None:
    settings = norm_boot(gui)
    n4 = N4(gui)
    n4.start_server(settings)


def load_model():
    pass


def load_ui():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", action="store_true")
    args = parser.parse_args()
    main(gui=args.gui)
