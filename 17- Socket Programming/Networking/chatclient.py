# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''A python program to create basic chat client program in python '''

# A client that send and recieve the messages
import socket
#take the server name and sort number
host='127.0.0.1'
port=9000
#create server side socket 
s=socket.socket()

s.connect((host,port))

#enter data at client
str=input("Enter data: ")
#continue as long as exit not entered by user
while str!='exit':
    #send data from client to server
    s.send(str.encode())
    #recieve the response data from server
    data=s.recv(1024)
    data=data.decode()
    print("From server: "+data)
    #enter data
    str=input("Enter data:")
    
s.close()