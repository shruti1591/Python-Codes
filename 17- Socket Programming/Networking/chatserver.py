# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''Two way communication between server and client'''

'''A python program to create a basic chat server program python'''

# A server that recieve and send messages
import socket
#take the server name and sort number
host='127.0.0.1'
port=9000
#create server side socket 
s=socket.socket()

#bind socket to host and port number
s.bind((host,port))
#maximum 1 connection is excepted
s.listen(1)
#wait till a client connects
c, addr=s.accept()
print("A client connected")
#server runs continuously
while True:
    #recieve data from client
    data=c.recv(1024)
    #if client sends empty string, come out
    if not data:
        break
    print("From client: "+str(data.decode()))
    
    #enterresponse data from server
    data1=input("enter response:")
    c.send(data1.encode())
c.close()