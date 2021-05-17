#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if path.exists("/unhealth"):
            self.send_response(500)
            self.end_headers()
        else:
            self.send_response(200)
            self.end_headers()
        return

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 7000), RequestHandler)
    server.serve_forever()