# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""
""" Way to create abstract class is to derive
 it from meta class ABC
that belongs to abc(abstract base class) module as:-
class Abstractclass(ABC):
To import abc module's ABC class and abstractmethod decorator 
we can write as follows:
    from abc import ABC, abstractmethod """
    
    
    
from abc import *
class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass
     
#This is sub class of Myclass
class sub1(Myclass):
    def calculate(self,x):
        print("square value= ",x*x)

import math        
class sub2(Myclass):
    def calculate(self,x):
        print("square root value= ",math.sqrt(x))
        
class sub3(Myclass):
    def calculate(self,x):
        print("cube value= ",x**3)
#ob=Myclass()  # will show the error       
obj1=sub1()
obj1.calculate(16)

obj2=sub2()
obj2.calculate(16)

obj3=sub3()
obj3.calculate(16)



"""Interfaces is a class with only abstract methods 
and there are no concrete methods."""
from abc import *
class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
#this is a sub class
class Oracle(Myclass):
    def connect(self):
        print("connecting to oracle database")
    def disconnect(self):
        print("disconnected from oracle")
#this is a another sub class
class Sybase(Myclass):
    def connect(self):
        print("connecting to sybase database")
    def disconnect(self):
        print("disconnected from sybase")
class database:
    #accept database name as a string
    str=input('enter database name:')
    #convert the string into classname
    classname=globals()[str]
    #create the object to that class
    x=classname()
    #call methods
    x.connect()
    x.disconnect()
        

     