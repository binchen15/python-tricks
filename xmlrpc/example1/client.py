import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5678")
print(proxy.listdir("/tmp"))
