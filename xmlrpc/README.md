**python3 only**

#### refer to https://pymotw.com/3/xmlrpc.server/index.html

	xmlrpc.client.ServerProxy('http://localhost:9000', verbose=True)
	allow_none=False
		None -> Nil
	use_datetime=True
	object sent as dictory
		use pickle as an alternative

### example 1
	register_function

### example 2
	register_instance (class instance)

### example 3
	register_isntance with _dispatch logic, to protect methods in classes.

### multicall wrapper extension

```
import xmlrpc.client
server = xmlrpc.client.ServerProxy('http://localhost:9000')

multicall = xmlrpc.client.MultiCall(server)
multicall.ping()
multicall.show_type(1)
multicall.raises_exception('Next to last call stops execution')
multicall.show_type('string')

try:
    for i, r in enumerate(multicall()):
        print(i, r)
except xmlrpc.client.Fault as err:
    print('ERROR:', err)
````

