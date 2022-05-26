#!/usr/bin/env python3
import socket
import sys
import argparse

def logger(port):
    s = socket.socket()
    
    try:
        s.bind(("0.0.0.0", port))
    except Exception as e:
         print(e)
    
    print("Comenzando el logeo de IPs...")
    while True:
        try:
            s.listen(5)
            address = s.accept()
            
            print("[+] IP Logged " + str(address[0]))
        
        except:
            pass
            print("Exiting. . .")
            sys.exit(0)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("port", nargs='?', type=int, help="Listen port of the socket server. (Default 8080)", default=9999)

    logger(port=parser.parse_args().port)