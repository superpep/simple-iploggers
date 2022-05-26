#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse

DEFAULT_PORT = 8080

class HttpHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html>", "utf-8"))
        self.wfile.write(bytes("<script>window.location = 'https://www.incibe.es/protege-tu-empresa/kit-concienciacion/ataque-simulado';</script>", "utf-8"))
        self.wfile.write(bytes("</html>", "utf-8"))

    def do_GET(self):
        print("GET request: %s", str(self.client_address))
        self._set_response()

def run(server_class=HTTPServer, handler_class=HttpHandler, port=DEFAULT_PORT):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print('Servidor web iniciado en el puerto', port)
    httpd.serve_forever()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Deteniendo servidor web...\n')
        httpd.server_close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port", nargs='?', type=int, help="Listen port of the socket server. (Default " + str(DEFAULT_PORT) + ")", default=DEFAULT_PORT)

    run(port=parser.parse_args().port)
