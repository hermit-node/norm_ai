"""N4: shared settings and its aiohttp listener."""
from __future__ import annotations

from aiohttp import web


class N4:
    settings: dict = {}

    @classmethod
    def start_server(cls) -> None:
        async def health(request: web.Request) -> web.Response:
            return web.json_response({"ok": True})

        app = web.Application()
        app.router.add_get("/health", health)
        web.run_app(
            app,
            host=cls.settings["n4"]["host"],
            port=cls.settings["n4"]["port"],
            handle_signals=False,
        )
