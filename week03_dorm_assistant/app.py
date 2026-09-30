"""Run a local-only application using the existing project Python environment."""
from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from urllib.parse import urlsplit

import core

STATIC = Path(__file__).resolve().parent / "static"
ASSETS = {"/": ("index.html", "text/html; charset=utf-8"),
          "/index.html": ("index.html", "text/html; charset=utf-8"),
          "/styles.css": ("styles.css", "text/css; charset=utf-8"),
          "/app.js": ("app.js", "text/javascript; charset=utf-8")}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # Do not record user questions, preparation notes, request bodies or secrets.
        pass

    def send(self, status: int, data: bytes, content_type="application/json; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)

    def json(self, status, payload):
        self.send(status, json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    def valid_host(self):
        allowed = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        return self.headers.get("Host") in allowed

    def do_GET(self):
        if not self.valid_host():
            return self.json(403, {"error": "invalid_host", "message": "只允许本机访问。"})
        path = urlsplit(self.path).path
        if path in ASSETS:
            filename, content_type = ASSETS[path]
            try:
                return self.send(200, (STATIC / filename).read_bytes(), content_type)
            except OSError:
                return self.json(503, {"error": "missing_asset", "message": "界面文件尚未就绪。"})
        try:
            if path == "/api/health":
                return self.json(200, core.health())
            if path == "/api/catalog":
                return self.json(200, core.catalog())
        except Exception:
            return self.json(500, {"error": "configuration", "message": "本地资料或配置读取失败。"})
        return self.json(404, {"error": "not_found", "message": "页面不存在。"})

    def do_POST(self):
        if not self.valid_host():
            return self.json(403, {"error": "invalid_host", "message": "只允许本机访问。"})
        origin = self.headers.get("Origin")
        if origin and origin not in {f"http://127.0.0.1:{self.server.server_port}", f"http://localhost:{self.server.server_port}"}:
            return self.json(403, {"error": "invalid_origin", "message": "请求来源不匹配。"})
        if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
            return self.json(415, {"error": "content_type", "message": "请发送 JSON。"})
        routes = {"/api/check": core.check, "/api/interpret": core.interpret, "/api/ask": core.ask}
        operation = routes.get(urlsplit(self.path).path)
        if not operation:
            return self.json(404, {"error": "not_found", "message": "接口不存在。"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 1 <= length <= 20000:
                return self.json(413, {"error": "body_size", "message": "请求为空或内容过长。"})
            self.connection.settimeout(10)
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            return self.json(200, operation(payload))
        except (core.InputError, ValueError, UnicodeDecodeError):
            return self.json(400, {"error": "invalid_input", "message": "输入格式无效，请核对身份、状态和日期。"})
        except core.AIError as exc:
            return self.json(503, {"error": "ai_unavailable", "message": str(exc)})
        except Exception:
            return self.json(500, {"error": "internal", "message": "处理失败，请保留当前记录并重试。"})


def make_server(port=8765):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    return server


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        data = core.catalog()
        print(json.dumps({**core.health(), "knowledge_items": len(data["items"]),
                          "sources": len(data["sources"]), "verified_date": data["verified_date"]}, ensure_ascii=False))
        return 0
    server = make_server(args.port)
    print(f"入住有数: http://127.0.0.1:{server.server_port}", flush=True)
    print("本机服务；按 Ctrl+C 停止。", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
