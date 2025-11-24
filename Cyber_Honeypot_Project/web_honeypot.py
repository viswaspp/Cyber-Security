
import http.server, socketserver, json, time, os

PORT = 8080
LOG_FILE = "logs/web_requests.log"

os.makedirs("logs", exist_ok=True)

class HoneyWebHandler(http.server.SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.ctime()} | {self.client_address} | {self.path} | HTTP {code}\n")

    def do_GET(self):
        self.log_request(200)
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(b'{"device":"Fake IoT Camera","status":"online"}')

with socketserver.TCPServer(("", PORT), HoneyWebHandler) as httpd:
    print("Web Honeypot running on port", PORT)
    httpd.serve_forever()
