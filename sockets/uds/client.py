import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
addr = "./uds_socket"
try:
    sock.connect(addr)
except socket.error as msg:
    print(msg)
    sys.exit(1)

message = b'This is the message.  It will be echoed from the server.'

try:
    sock.sendall(message)
    counts = 0
    amount = len(message)
    while counts < amount:
        chunk = sock.recv(16)
        counts += len(chunk)
        print("Got {}".format(chunk))
finally:
    sock.close()
