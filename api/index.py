from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    """Minimal Vercel Python entrypoint for the hydroDL repository.

    This endpoint intentionally does not import the heavy hydroDL ML stack.
    It provides a lightweight health/info route so Vercel can build and serve
    the repository without changing the hydroDL package itself.
    """

    def _send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send_json(
            {
                "status": "ok",
                "service": "hydroDL",
                "runtime": "vercel-python",
                "message": "hydroDL Vercel entrypoint is running",
            }
        )

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
