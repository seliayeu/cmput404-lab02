"""
This code is heavily based on code and psuedocode obtained from the CMPUT 404 Lab on 9/13/2021.
whose author is Zoe Riell
"""

#!/usr/bin/env python3

import socket,sys
HOST=""
PORT=8001
BUFFER_SIZE=1024

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit()
    return remote_ip

def handle_request(addr, conn):
    conn.recv(BUFFER_SIZE)


def main():
    extern_host = "www.google.com"
    extern_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        while True:
            conn, addr = server_socket.accept()
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                remote_ip = get_remote_ip(extern_host)
                
                client_socket.connect((remote_ip, extern_port))

                send_full_data = conn.recv(BUFFER_SIZE)
                
                client_socket.sendall(send_full_data)

                client_socket.shutdown(socket.SHUT_WR)

                data = client_socket.recv(BUFFER_SIZE)

                conn.send(data)
            conn.close()
        
if __name__ == "__main__":
    main()