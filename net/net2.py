#!/usr/bin/env python3
import struct
import sys
import re
from pwnpy.pwn import *

sock = connect_to('10.10.10.4', 2997)

numbs = (struct.unpack('<I', sock.recv(4))[0] for i in range(4))

result = sum(numbs)%2**32

sock.send(struct.pack('<I', result))

print(sock.recv(1024))
