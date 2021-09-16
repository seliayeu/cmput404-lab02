"""
This code is heavily based on code and psuedocode obtained from the CMPUT 404 Lab on 9/13/2021.
whose author is Zoe Riell
"""

#!/usr/bin/env python3

import socket,sys

from multiprocessing import Process
HOST=""
PORT=8001
BUFFER_SIZE=1024

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit()
    return remote_ip

def handle_request(addr, conn, proxy_end):
    print("Getting data...")
    send_full_data = conn.recv(BUFFER_SIZE)
    print("Sending data out...")
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(BUFFER_SIZE)
    conn.send(data)
    conn.close()
    print("Connection closed!")

def main():
    extern_host = "www.google.com"
    extern_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
            conn, addr = proxy_start.accept()
            print("Connected to by " + conn)
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = get_remote_ip(extern_host)
                
                print("Connecting to " + str(remote_ip) + ":" + str(extern_port))
                proxy_end.connect((remote_ip, extern_port))

                print("Starting new process to handle the request...")
                p = Process(target=handle_request, args=(addr, conn, proxy_end))
                p.daemon = True
                p.start()
                

if __name__ == "__main__":
    main()