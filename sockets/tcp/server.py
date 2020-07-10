import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 10000)
sock.bind(addr)
sock.listen(1)  # only 1 connection

while True:
    conn, client_addr = sock.accept()
    print("client address: {}".format(client_addr))
    try:
        while True:
            chunk = conn.recv(16)
            print('Received: {}'.format(chunk))
            if chunk:
                conn.sendall(chunk)
            else:
                print("Done!")
                break
    finally:
        conn.close()

