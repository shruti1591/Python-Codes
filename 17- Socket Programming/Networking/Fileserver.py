# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''Python program to create a file server that recieves a file name from a 
client and sends the content of the file'''
# A server that sends file contents to client
import socket
#take the server name and sort number
host='localhost'
port=6767
#create a TCP socket 
s=socket.socket()

#bind socket to host and port number
s.bind((host,port))
#maximum 1 connection is excepted
s.listen(1)

#wait till client accept a connection
c,addr=s.accept()
print("A client accepted connection")

#accept file name from client
fname=c.recv(1024)

#convert file name into a normal string
fname=str(fname.decode())
print("file name recieved from client: "+fname)
try:
    #open the file at server side
    f=open(fname,'rb')
    #read content of the file
    content=f.read()
    #send file content to client
    c.send(content)
    print("File content sent to client")
    #close the file
    f.close()
except FileNotFoundError:
    c.send(b'File does not exist')
c.close()