#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse
from datetime import datetime
import sys

DEFAULT_PORT = 8080
parser = argparse.ArgumentParser()

def logIp(address):
    print("[+] IP Logged " + address)
    if(parser.parse_args().save):
            now = datetime.now()
            with open("loggedIps.txt", "a") as f:
                f.write("(" + sys.argv[0] + ")[" + now.strftime("%d/%m/%Y %H:%M:%S") + "] " +address + "\n")


class HttpHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html>", "utf-8"))
        self.wfile.write(bytes("<script>window.location = 'https://www.incibe.es/protege-tu-empresa/kit-concienciacion/ataque-simulado';</script>", "utf-8"))
        self.wfile.write(bytes("</html>", "utf-8"))

    def do_GET(self):
        logIp(str(self.client_address[0]))
        self._set_response()

def run(server_class=HTTPServer, handler_class=HttpHandler, port=DEFAULT_PORT):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print('Web servers initialized in port', port)
    httpd.serve_forever()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Stopping web server...\n')
        httpd.server_close()

if __name__ == '__main__':
    parser.add_argument("port", nargs='?', type=int, help="Listen port of the web server. (Default " + str(DEFAULT_PORT) + ")", default=DEFAULT_PORT)
    parser.add_argument('-s', '--save', action='store_true', help='Save log to file', dest='save')


    run(port=parser.parse_args().port)
