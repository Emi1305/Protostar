#!/usr/bin/env python3
import struct
import sys
import re
from pwnpy.pwn import *

sock = connect_to('10.10.10.4', 2998)

expected = struct.unpack('<i', sock.recv(1024))[0]
print(expected)
sock.send(str(expected).encode())

print(sock.recv(1024))
