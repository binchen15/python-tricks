two primary properties
	address family
		AF_INET
		AF_INET6
		AF_UNIX
			for Unix Domain Socket (UDS)

	socket type
		SOCK_DGRAM
			UDP
				User Datagram Protocol
			TCP
				Transmission Control Protocol
	
	import socket
	socket.gethostname()
	socket.gethostbyname()
	socket.gethostbyname_ex()	
	socket.getfqdn()
		hostname, aliases, addresses = 
	socket.gethostbyaddr('10.9.0.10')

service information

	The combination of IP address, protocol, and port number uniquely identify a 
	communication channel and ensure that messages sent through a socket arrive 
	at the correct destination.


	In [2]: socket.getservbyport(443)                                                         Out[2]: 'https'


TCP/IP Client and Server


