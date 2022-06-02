#!/usr/bin/env python3
import socket
import sys
import argparse
from datetime import datetime

DEFAULT_PORT = 9999
parser = argparse.ArgumentParser()

def printLog(address):
    print("[+] IP Logged " + address)
    if(parser.parse_args().save):
            now = datetime.now()
            with open("loggedIps.txt", "a") as f:
                f.write("(" + sys.argv[0] + ")[" + now.strftime("%d/%m/%Y %H:%M:%S") + "] " +address + "\n")

def logger(port):
    s = socket.socket()
    
    try:
        s.bind(("0.0.0.0", port))
    except OSError as e:
        print("Port is already in use, try another.")
        sys.exit(1)
    except Exception as e:
        print(e)
    
    print("Starting IPLogger...")
    while True:
        try:
            s.listen(5)
            conn, address = s.accept()
            
            printLog(str(address[0]))
            
        except Exception as e:
            pass
            print(e)
            print("Exiting. . .")
            sys.exit(0)
            
if __name__ == '__main__':
    parser.add_argument("port", nargs='?', type=int, help="Listen port of the web server. (Default " + str(DEFAULT_PORT) + ")", default=DEFAULT_PORT)
    parser.add_argument('-s', '--save', action='store_true', help='Save log to file', dest='save')


    logger(port=parser.parse_args().port)