# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''Syllabus:- Network Programming. Understanding Protocols, 
Introduction to Sockets, TCP/IP Server, TCP/IP Client,
 UDP Server, UDP Client, File Server, File Client, 
 Two-Way Communication between Server and Client,
 Multithreaded Client-Server Chat Application'''


''' A Python program to find IP address of the website'''
import socket
host='www.google.co.in'

try:
    addr=socket.gethostbyname(host)
    print("IP Address= "+addr)
except socket.gaierror: #get address information error
    print('The website does not exist')
    
    
    
    
'''A python program to retrieve different parts of URL and display them'''
import urllib.parse
url="http://www.example.com:8080/path/"
#get a tuple with parts of the url
tpl=urllib.parse.urlparse(url)
#display the contents of the tuple
print(tpl)

#display different parts of the url
print("scheme= ",tpl.scheme)
print("Net location= ",tpl.netloc)
print("Path= ",tpl.path)
print("Parameters= ",tpl.params)
print("Port number= ",tpl.port)
print("Total url= ",tpl.geturl())





'''A python program that reads the source code of a web page'''
import urllib.request
#store the url of page into file object
file = urllib.request.urlopen("https://www.python.org/")

#read data from file and display
print(file.read())





'''A python program to download a web page from internet and save it into our computer'''

import urllib.request
try:
 #store the url of page into file object
 file = urllib.request.urlopen("https://www.python.org/")

 #read data from file and store into content object
 content=file.read()
 
except urllib.error.HTTPError:
    print("The web page does not exist")
    exit()

f=open ("myfile.html","wb")
f.write(content)
f.close()




'''Python program to download an image from internet into our computer system'''
import urllib.request
url="https://hi.m.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BF%E0%A4%A4%E0%A5%8D%E0%A4%B0:Rainbow_Rose_(3366550029).jpg"
download=urllib.request.urlretrieve(url,"myimage.jpg")

