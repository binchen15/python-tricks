import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 10000))

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
