# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""
'''
CRUD Operations
flow: create-> open-> work -> close
Open:- 1-File Name 2- Mode
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"rb"- Opens a file for reading only in binary format.
 The file pointer is placed at the beginning of the file. 
 This is the default mode.
"r+"- Opens a file for both reading and writing.
 The file pointer placed at the beginning of the file.
"wb+"- Opens a file for both writing and reading in binary format.
 Overwrites the existing file if the file exists.
 If the file does not exist, creates a new file for reading and writing.
"a+" - Opens a file for both appending and reading. 
The file pointer is at the end of the file if the file exists. 
The file opens in the append mode.
 If the file does not exist, it creates a new file for reading and writing.
"ab+" - Opens a file for both appending and reading in binary format. 
The file pointer is at the end of the file if the file exists. 
The file opens in the append mode. 
If the file does not exist, it creates a new file for reading and writing.

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''
f=open('python.txt','w')
str=input("enter the data to the file")
f.write(str)

f=open('python.txt','r')
str1=f.read()
print(str1)
f.close()

f=open('python.txt','a')
str=input("enter the data to the file")
f.write(str)
f=open('python.txt','r')
str=f.read()
print(str)

f.close()


#A python program to store a group of strings into a text
f=open('c2.txt','w')
print('enter text (@ at end):')
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")
f.close()
#To test
f=open('c2.txt','r')
#str=f.read()
str=f.read().splitlines()
#str=f.readlines()
print(str)
f.close()

#use of seek
#f.seek(offset,fromwhere)
#offset represents how many bytes to move
#fromwhere represents from which position to move.
#0 represents beginning, 1 represents from current 2 repesents end of the file
#put the file pointer to beginning of file

f=open('myfile1.txt','+a')
print('enter text (@ at end):')
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")
#put the file pointer to the beginning of file.
f.seek(5,0)
print("the file contents are:")
str=f.read()
print(str)
f.close()

#Knowing whether a file exists or not
import os,sys
fname=input("enter filename:")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+' does not exist')
    sys.exit()
print("the file content is:")
str=f.read()
print(str)
f.close()

#Python program to count no. of lines, words and characters in a text file

import os, sys
fname=input("Enter filename: ")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+' does not exist')
    sys.exit()
cl=cw=cc=0
for shruti in f:
    loy=shruti.split()
    print(loy)
    cl+=1
    cw+=len(loy)
    cc+=len(shruti)
print('no. of lines:', cl)
print('no. of words:', cw)
print('no. of character:', cc)
f.close()


#Binary files
f1=open('testimage.png','rb')
f2=open('testimage3.png','wb')
byte=f1.read()
f2.write(byte)
f1.close()
f2.close()



