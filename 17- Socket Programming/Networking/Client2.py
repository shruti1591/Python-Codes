# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''A UDP client program that recieves the message from server'''

# A UDP client that recieves message from server
import socket
#take the server name and port number
host="localhost"
port=5000

#create a client side socket using UDP protocol
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#connect it to server with host name and port number
s.bind((host,port))
#receive message string from server, at a time 1024 B
msg,addr=s.recvfrom(1024)

try:
    #let the socket blocks after 5 seconds if the server disconnects
    s.settimeout(5)
    #repeat as long as message strings are not empty
    while msg:
        print("Recieved: "+msg.decode())
        msg,addr=s.recvfrom(1024)
except socket.timeout:
    print("Time is over and hence terminating....")
#disconnect the client
s.close()