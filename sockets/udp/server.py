import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('localhost', 10000)
sock.bind(addr)

while True:
    data, client_addr = sock.recvfrom(4096)
    if data:
        print("received {} bytes from {}".format(len(data), client_addr))
        size = sock.sendto(data, client_addr)
        print("sent {} bytes to {}".format(size, client_addr))
