"""
This code is identical to the code found on the eClass page for Lab 2 code, bar some
stylistic changes.

Authors: CMPUT TAs
"""

#!/usr/bin/env python3

import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        
        s.bind((HOST, PORT))
        s.listen(2)
        
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            print(conn)
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()
