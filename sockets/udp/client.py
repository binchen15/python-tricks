import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 10000)
message = b'This is the message.  It will be repeated.'

try:
    sent = sock.sendto(message, server_addr)
    print("sent {} bytes to {}".format(sent, server_addr))
    data, server = sock.recvfrom(4096)
    print("received back {}".format(data))
finally:
    sock.close()
