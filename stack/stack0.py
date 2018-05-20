#!/usr/bin/env python3
import struct
import sys

buf = b'A' * 100
buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.buffer.flush()
