# -*- coding: utf-8 -*-
"""

@author: SYSTEMS
"""

'''A TCP/IP server program that sends the message to a client'''

# A TCP/IP server that sends message to client
import socket
#take the server name and port number
host='localhost'
port=5000
#create a socket server side using TCP/IP protocol
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket with server and port number
s.bind((host,port))
#allow maximum 1 connection to the socket
s.listen(1)
#wail till client accepts connection
c,addr=s.accept()
#display client address
print("connection from: ",str(addr))
#send message to the client after encoding into binary string
c.send(b"Hello client,how are you")
msg="Bye!"
c.send(msg.encode())

#disconnect the server
c.close()