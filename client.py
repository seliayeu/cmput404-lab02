"""
This code is identical to the code found on the eClass page for Lab 2 code, bar some
stylistic changes.

Authors: CMPUT TAs
"""

#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("epic")

s.connect((socket.gethostbyname("www.google.com"), 80))
print("epic")
payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\n"
s.send(bytearray(payload, "utf-8"))
buffer = ''
print("epic")


data = s.recv(1024)
print(data)