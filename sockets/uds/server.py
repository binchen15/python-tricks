import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
addr = "./uds_socket"

# addr must be cleared before server start listening
try:
    os.unlink(addr)
except OSError:
    if os.path.exists(addr):
        raise

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

