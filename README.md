# Simple IPLoggers

Very simple IPLoggers using Python

## WebServer

Usage: `./simple-webserver.py [-s] [port]`

### What's it for?

This simple webserver serves a webpage in the port you specify or by default in `8080` and whenever a client visits the web it logs it's IP and redirects the client to another webpage to make it transparent.

It can also save the loggedIP to a logfile using `-s`

## Socket server

Usage: `./simple-socketserver.py [-s] [port]`

### What's it for?

This server opens a listening socket on the port you send or by default in port `9999` and logs every incomming IP.

It can also save the loggedIP to a logfile using `-s`
