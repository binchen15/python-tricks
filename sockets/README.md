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

	stream oriented protocol

User Datagram Client and server
	
	message oriented protocol

	UDP messages must fit within a single datagram (for IPv4, 
	that means they can only hold 65,507 bytes because the 65,535 byte 
	packet also includes header information) and delivery is not 
	guaranteed as it is with TCP.

Unix Domain Socket

	the address of the socket is a path on the file system
	the node created in the file system to represent the socket persists 
	 after the socket is closed, and needs to be removed each time the server starts up


