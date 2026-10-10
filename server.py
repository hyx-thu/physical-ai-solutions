"""Cloud Run production web server and API for Agent and solutions for Physical AI portal."""
import http.server
import json
import os
from pathlib import Path
import socketserver
import sys
import yaml

REPO_ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", 8080))
HOST = "0.0.0.0"

# Registry helper
registry_path = REPO_ROOT / "_shared" / "table_registry.yaml"

def get_registry_data():
    if registry_path.exists():
        try:
            return yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"Warning: Failed to load table registry: {e}", file=sys.stderr)
    return {}


class PhysicalAIPortalHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(REPO_ROOT), **kwargs)

    def do_GET(self):
        # Health check endpoint for Cloud Run
        if self.path in ("/healthz", "/health", "/_health"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "HEALTHY", "service": "agent-solutions-physical-ai"}')
            return

        # API endpoint returning all registered Physical AI agents and solutions
        if self.path == "/api/agents":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(get_registry_data(), indent=2).encode("utf-8"))
            return

        # Default route serves index.html
        if self.path in ("/", ""):
            self.path = "/index.html"

        # Support HTTP Range requests (206 Partial Content) for smooth video seeking/scrubbing
        range_header = self.headers.get("Range")
        if range_header and range_header.startswith("bytes="):
            path = self.translate_path(self.path)
            if os.path.isfile(path):
                try:
                    file_size = os.path.getsize(path)
                    byte_range = range_header.replace("bytes=", "").split(",")[0].strip()
                    start_str, end_str = byte_range.split("-")
                    start = int(start_str) if start_str else 0
                    end = int(end_str) if end_str else file_size - 1
                    if start >= file_size:
                        self.send_error(416, "Requested Range Not Satisfiable")
                        return
                    end = min(end, file_size - 1)
                    length = end - start + 1

                    ctype = self.guess_type(path)
                    self.send_response(206)
                    self.send_header("Content-Type", ctype)
                    self.send_header("Content-Range", f"bytes {start}-{end}/{file_size}")
                    self.send_header("Content-Length", str(length))
                    self.send_header("Cache-Control", "public, max-age=3600")
                    self.end_headers()

                    with open(path, "rb") as f:
                        f.seek(start)
                        remaining = length
                        chunk_size = 64 * 1024
                        while remaining > 0:
                            chunk = f.read(min(chunk_size, remaining))
                            if not chunk:
                                break
                            self.wfile.write(chunk)
                            remaining -= len(chunk)
                    return
                except (BrokenPipeError, ConnectionResetError):
                    return
                except Exception as e:
                    print(f"Range request error: {e}", file=sys.stderr)

        return super().do_GET()

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()

    def log_message(self, format, *args):
        # Concise structured access logs
        sys.stdout.write(f"[{self.log_date_time_string()}] {self.address_string()} {format % args}\n")
        sys.stdout.flush()


class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


def run():
    with ThreadedHTTPServer((HOST, PORT), PhysicalAIPortalHandler) as httpd:
        print(f"🚀 Agent and solutions for Physical AI Portal listening on http://{HOST}:{PORT}", flush=True)
        print(f"📊 Serving Enterprise Agents and Solutions across Physical AI Domains (Range-enabled)", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...", flush=True)
            httpd.server_close()


if __name__ == "__main__":
    run()
