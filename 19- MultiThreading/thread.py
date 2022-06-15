# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:24:44 2021

@author: SYSTEMS
"""

#Thread in Python

import threading
print("Lets find the current running thread")
print("The name of current thread is: ",threading.current_thread().getName())
if threading.current_thread()==threading.main_thread():
    print("The current thread is the main thread")
    
#Global Interpreter Lock

#Creating a Thread
'''1- Creating a thread without using a class
2- Creating a thread by creating sub class to Thread class
3- Creating a thread without creating sub class to Thread class'''


'''1- Creating a thread without using a class'''
from threading import *
def display():
    print("hello")
for i in range(5):
    t=Thread(target=display)
    t.start()

from threading import *
def display(str):
    print(str)
for i in range(5):
    t=Thread(target=display,args=("hello",))
    t.start()

'''2- Creating a thread by creating sub class to Thread class'''
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(1,6):
            print(i)
t1=MyThread()     
t1.start() 
      
'''3- Creating a thread without creating sub class to Thread class'''

from threading import *
class MyThread:
    def __init__(self,str):
        self.str=str
        
    def display(self,x,y):
        print(self.str)
        print(x,y)
        
obj=MyThread("hello")
t1=Thread(target=obj.display,args=(1,2))
t1.start()

'''
start()
join()
is_alive()
setName(name)
getName()
'''

#Perform two tasks using two threads simultaneously

from threading import *
from time import *

class Theatre:
    def __init__(self,str):
        self.str=str
        
    def movieshow(self):
        for i in range(1,6):
            print(self.str,":",i)
            sleep(10)
    
obj1=Theatre("cut ticket")
obj2=Theatre("show chair")

t1=Thread(target=obj1.movieshow)
t2=Thread(target=obj2.movieshow)

t1.start()
t2.start()

#A program where two threads are acting on the same method to allot a berth for the passengers.

from threading import *
from time import *
class Railway:   
    def __init__(self,available):
        self.available=available
    
    def reserve(self,wanted):
        print("Available number of seats are:", self.available)
        
        if(self.available>=wanted):
            name=current_thread().getName()
            print(wanted,"berths alloted to",name)
            #sleep(1.5)
            self.available-=wanted
            sleep(1.5)           
        else:
            print("seats are not avaialble")
obj=Railway(1)
t1=Thread(target=obj.reserve,args=(1,))
t2=Thread(target=obj.reserve,args=(1,))

t1.setName("First Person")
t2.setName("Second Person")

t1.start()
t2.start()

#A python program achieving thread synchronization using locks.
from threading import *
from time import *
class Railway:   
    def __init__(self,available):
        self.available=available
        self.l=Lock()
    
    def reserve(self,wanted):
        self.l.acquire()
        print("Available number of seats are:", self.available)
        
        if(self.available>=wanted):
            name=current_thread().getName()
            print(wanted,"berths alloted to",name)
            #sleep(1.5)
            self.available-=wanted
            sleep(1.5)           
        else:
            print("seats are not avaialble")
        self.l.release()
obj=Railway(2)
t1=Thread(target=obj.reserve,args=(1,))
t2=Thread(target=obj.reserve,args=(1,))
t1.setName("First Person")
t2.setName("Second Person")
t1.start()
t2.start()

#Program to show dead lock of threads due to locks on objects.

from threading import *
l1=Lock()
l2=Lock()
def bookticket():
    l1.acquire()
    print("Bookticket locked train")
    print("Bookticket wanted to lock one compartment")
    l2.acquire()
    print("Bookticket locked compartment")
    l2.release()
    l1.release()
    print("Booking Ticket Done")
def cancelticket():
    l2.acquire()
    print("Cancelticket locked compartment")
    print("Cancelticket wanted to lock on train")
    l1.acquire()
    print("Cancelticket lock train")
    l1.release()
    l2.release()
    print("Cancelling of Ticket is Done")
t1=Thread(target=bookticket)
t2=Thread(target=cancelticket)
t1.start()
t2.start()

#Program with logic to avoid deadlock.

from threading import *
l1=Lock()
l2=Lock()
def bookticket():
    l1.acquire()
    print("Bookticket locked train")
    print("Bookticket wanted to lock one compartment")
    l2.acquire()
    print("Bookticket locked compartment")
    l2.release()
    l1.release()
    print("Booking Ticket Done")
def cancelticket():
    l1.acquire()
    print("Cancelticket locked compartment")
    print("Cancelticket wanted to lock on train")
    l2.acquire()
    print("Cancelticket lock train")
    l2.release()
    l1.release()
    print("Cancelling of Ticket is Done")
t1=Thread(target=bookticket)
t2=Thread(target=cancelticket)
t1.start()
t2.start()










            















