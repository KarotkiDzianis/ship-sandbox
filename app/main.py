#!/usr/bin/env python3
"""app/main.py — the entire ship-sandbox "app". Standard library only, no
dependencies to install: this project exists to prove Ship's deploy
mechanics work, not to prove anything about a real service. Serves the
deployed VERSION (the git sha it was built from) on `/`, and answers 200
on `/healthz` -- that's the whole health contract scripts/ship/health
checks."""
from __future__ import annotations

import http.server
from pathlib import Path

PORT = 8091
VERSION_FILE = Path(__file__).resolve().parent / "VERSION"


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok\n")
            return
        version = VERSION_FILE.read_text().strip() if VERSION_FILE.exists() else "unknown"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"ship-sandbox ok\nversion={version}\n".encode())

    def log_message(self, fmt, *args):
        pass  # keep systemd journal quiet -- this app has nothing worth logging


if __name__ == "__main__":
    http.server.HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
