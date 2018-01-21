from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        a = [{"name":"bob", "pos":0.1, "size":0.3}]
        self.wfile.write(json.dumps(a))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        a = [{"name":"bob", "pos":0.1, "size":0.3}]
        self.wfile.write(json.dumps(a))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
