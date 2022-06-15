# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''Python program to create a file client that sends a file name to the server
 and recieves the content of the file'''
# A client that sends and recieves data
import socket
#take the server name and sort number
host='localhost'
port=6767
#create a TCP socket 
s=socket.socket()

#connect to server
s.connect((host,port))
#type file name from the keyboard
filename=input("Enter Filename: ")
#send the file name to the server
s.send(filename.encode())
#recieve file content from server
content=s.recv(1024)
print(content.decode())

s.close()
