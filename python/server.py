from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class HttpHandler(BaseHTTPRequestHandler):
    handlers = {"GET": None, "POST": None}
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.handlers["GET"](self.command, self.wfile)

class HttpServer(HTTPServer):
    def runForever():
        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass        

webServer = HttpServer()
webServer.server_close()
print("Server stopped.")