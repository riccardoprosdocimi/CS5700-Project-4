from http.server import BaseHTTPRequestHandler, HTTPServer
from functools import lru_cache
from urllib.request import urlopen

PORT = 25016
ORIGIN_PORT = "8080"
ORIGIN_SERVER = "cs5700cdnorigin.ccs.neu.edu"


class CdnHttpServer(BaseHTTPRequestHandler):

    def do_GET(self):
        data = self.get_data()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Host", )
        self.end_headers()
        self.wfile.write(data)

    @lru_cache
    def get_data(self) -> bytes:
        with urlopen("http://" + ORIGIN_SERVER + ":" + ORIGIN_PORT + self.path) as response:
            return response.read()


if __name__ == "__main__":
    webServer = HTTPServer(("localhost", PORT), CdnHttpServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("server stopped")
