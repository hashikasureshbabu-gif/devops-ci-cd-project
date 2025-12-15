from http.server import BaseHTTPRequestHandler, HTTPServer

class DevOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"DevOps CI/CD Pipeline Running on Kubernetes")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 80), DevOpsHandler)
    print("Starting DevOps app on port 80...")
    server.serve_forever()

