"""Read settings.ini for Norm startup."""
from __future__ import annotations

from configparser import ConfigParser
from pathlib import Path


def norm_boot(gui: bool) -> dict:
    # we're just going to pretend this is boilerplate
    if not isinstance(gui, bool):
        raise TypeError("gui must be True or False")

    config = ConfigParser(interpolation=None)
    path = Path(__file__).with_name("settings.ini")
    with path.open("r", encoding="utf-8") as source:
        config.read_file(source)

    if not config.has_section("n4"):
        raise ValueError("Missing [n4] section in settings.ini")

    settings = {section: dict(config.items(section))
                for section in config.sections()}
    n4 = settings["n4"]
    if n4.get("host") != "127.0.0.1":
        raise ValueError("N4 must listen on 127.0.0.1")
    port = config.getint("n4", "port")
    if not 1 <= port <= 65535:
        raise ValueError("Invalid N4 port")
    n4["port"] = port
    settings["gui"] = gui
    return settings
