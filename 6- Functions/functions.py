# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

# Functions
# Difference between a function and a method is,
# when a function is written within the class 
#it is called method.


def summation(a,b):
    '''To add two numbers'''
    c=a+b
    print("the value of c is:",c)
summation(2.8,9.8)

#Returning results 
'''return c
return 100
return lst
return x,y,z'''

#Function to check if a given number is prime or not
def prime(n):
    '''to check if n is prime or not'''
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x

num=int(input("enter a number"))
result=prime(num)
print(result)
if result==1:
    print(num,"is prime")
else:
    print(num,"is not prime")
    
#Returning multiple values from the function
def sum_sub_mul_div(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f

t=sum_sub_mul_div(10,5)
print(type(t))
print("The results are:")
for i in t:
    print(i,end=',')

#Functions are first class objects
'''1- It is possible to assign a function to a variable
   2- It is possible to define one funstion inside another function
   3- It is possible to pass a function as parameter to another function
   4- It is possible that a function can return another function'''
# Case 1:-
def display(str):
    return 'Hello '+str
x=display("friend")
print(x)

#Case 2:-
def display(str):
    def message():
        x=input("enter the string")
        return x
    result=message()+str
    return result
print(display("Krishna"))

#Case 3:-
def display(fun):
    return "hello "+ fun
def message():
    return "how are you?"

print(display(message()))

#Case 4:-
def display():
    def message():
        return "how are you?"
    return message
fun=display()
print(fun())

#Recursive Functions
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
n=int(input("enter the number"))
print(factorial(n))
'''for i in range(1,11):
    print('factorial of {} is {}'.format(i, factorial(i)))'''
    
    
    
#Pass by object reference

'''In python ,values are passed to function by object 
references.
If the object is immutable, the modified value is
 not available
 outside
the function and if the object is mutable, 
its modified version is available 
outside the function'''

#A Python program to pass an integer to a function and modify
def modify(x):
    x=15
    print(x, id(x))
x=10
modify(x)
print(x,id(x))   #integer objects are immutable

#A python program to pass a list to a function and modify
def modify(lst):
    lst.append(9)
    print(lst,id(lst))
lst=[1,2,3,4]
modify(lst)
print(lst, id(lst))

#A python program to create a new object inside the function does not modify outside object.
def modify(lst):
    lst=[10,11,12]
    print(lst,id(lst))
lst=[1,2,3,4]
modify(lst)
print(lst,id(lst))


#Anonymous Functions or Lambdas

#lambda argument_list:expression

f=lambda x:x*x
print("Square of 5=",f(5))


#lambda function to find the bigger number in two given numbers
max=lambda x,y:x if x>y else y
a,b=[int(n) for n in input("Enter two numbers: ").split(',')]
print("Bigger number= ",max(a,b))


#filter() function :- It is useful to filter out the elements of a sequence 
#depending on the results of a function.
#filter(function,sequence)

lst=[10,20,30,40,50,67,89,90]
lst1=list(filter(lambda x:(x%2==0),lst))
print(lst1)

#map():- It acts on each element of the sequence and perhaps changes the elements.
#map(function,sequence)

lst=[1,2,3,4,5]
lst1=tuple(map(lambda x: x*x, lst))
print(lst1)

#reduce():- It reduces a sequence of elements to a 
#single value by processing the elements according to a function 
#supplied.
from functools import *
lst=[1,2,3,4,5]
result=reduce(lambda x,y:x*y, lst)
print(result)


#Decorators
    
#take a function to which decorator should be applied
def num():
    return 10

#A decorator that increments the value of a function by 2
def decor(fun): #decorator function
    def inner(): #inner function that modifies
        value=fun()
        return value+2
    return inner
    
#call decorator function and pass num
result_fun=decor(num)
print(result_fun())


#take a function to which decorator should be applied
@decor
def num():
    return 10
    
print(num())


#Iterators
#Generators

    