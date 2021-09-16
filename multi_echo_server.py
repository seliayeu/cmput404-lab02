"""
This code is heavily based on code and psuedocode obtained from the CMPUT 404 Lab on 9/13/2021.
whose author is Zoe Riell
"""

#!/usr/bin/env python3

import socket
from multiprocessing import Process
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started process ", p)

def handle_echo(addr, conn):
    print("Connected by", addr)
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(.5)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()
