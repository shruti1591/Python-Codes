# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''A UDP server program that sends the message to a client'''

# A UDP server that sends message to client
import socket
import time
#take the server name and sort number
host='localhost'
port=5000
#create a socket server side using UDP protocol
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#let the server waits for 5 seconds
time.sleep(5)
#send message to the client after encoding into binary string
s.sendto(b"Hello client,how are you",(host,port))
msg="Bye!"
s.sendto(msg.encode(),(host,port))
#disconnect the server
s.close()