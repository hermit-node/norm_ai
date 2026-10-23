from __future__ import annotations

from aiohttp import web
from munch import Munch


class N4:
    settings = Munch()
    def __init__(self, gui: bool = True) -> None:
        self.server = None
        self.app = self.server
        self.router = None

    def start_server(self, settings: dict) -> None:
        self.settings.fromDict(settings)
        self.server = web.Application()
        self.router = self.server.router
        self.router.add_get("/health", self.health)
        web.run_app(
            self.server,
            host=self.settings.n4.host,
            port=self.settings.n4.port,
            handle_signals=False,
        )

    async def health(self, request: web.Request) -> web.Response:
        return web.json_response({"ok": True})

    def stop_server(self) -> None:
        self.server.close()