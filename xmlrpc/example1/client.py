import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5678")
print(proxy.dir.list("/tmp"))
try:
    proxy.listdir("/tmp")
except xmlrpc.client.Fault as err:
    print("Err {}".format(err))
