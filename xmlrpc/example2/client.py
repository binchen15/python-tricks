import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:6789')
# namespace allowed. concept of service tree
print(proxy.dir.list('/tmp'))
