# simple xmlrpc server. serving content of a directory
from xmlrpc.server import SimpleXMLRPCServer
import logging
import os

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', 5678),
    logRequests=True,
)

def listdir(dir_name):  # dir_name absolute/relative path
    logging.info("list content of dir: {}".format(dir_name))
    try:
        return os.listdir(dir_name)
    except OSError:
        return "no such file or directory!"

# the client must access via "dir()" instead of "listdir()"
# server.register_function(listdir, 'dir')
# namespace  is allowed
server.register_function(listdir, 'dir.list')

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("exit...")
