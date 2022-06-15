# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

''' Polymorphism:-
      1-Duck typing philosophy of python
      2- Operators overloading
      3- Method Overloading
      4- Method Overriding'''
      
      
      
#Python program to check the object type to know whether the
# method exist in the object or not
      

class Dog:
    def bark(self):
        print("This is dog")

class Duck:
    def talk(self):
        print("Quack,Quack!!!!")
class Human:
    def talk(self):
        print("Hello, hiiii!!!!")
        
def call_talk(obj):
    obj.talk()
        
x=Duck()
call_talk(x)
x=Human()
call_talk(x)
x=Dog()
call_talk(x)






















class Dog:
    def bark(self):
        print("BOW, BOW!!!!")
class Duck:
    def talk(self):
        print("Quack,Quack!!!!")
class Human:
    def talk(self):
        print("Hello, hiiii!!!!")
        
def call_talk(obj):
    
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
    else:
        print("Wrong object passed")
        
x=Duck()
call_talk(x)
x=Human()
call_talk(x)
x=Dog()
call_talk(x)


#Method Overloading
class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print("sum of three=", a+b+c)
        elif a!=None and b!=None :
            print("sum of two=", a+b)
        else:
            print("please enter two or three arguments")
            
m=Myclass()
m.sum(10,15,50)
m.sum(10.5,19.8)
m.sum(100)



    

        