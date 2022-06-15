# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

"""Type of errors:-
1- Compile-time error:- Syntactical error found in the code
2- Logical error:- depict flaws in the logic of the program.
3- Run-time error:- When PVM cannot execute the byte code"""
 
"""The runtime error which can be handled by the programmer
 are called exceptions"""

"""
try: Run this code
except:Execute the code when there is as exception.
else: No exception? Run this code
finally: Always run this code 
raise:
assert:
        
"""
#an exception handling example
a=int(input("enter first number"))
b=int(input("enter second number"))

try:
    c=a/b
#except ZeroDivisionError:
except Exception as e:
    print("division by zero error")
    print(e)
else:
    print("Program has not entered in except block")
finally:
    print("I am in finally block")
    
    
#python program to handle multiple exceptions
def avg(list):
    tot=0
    for x in list:
        tot+=x
    avg=tot/len(list)
    return tot,avg

try:  
    t,a=avg([1,2,3,4,"b"]) 
    #t,a=avg([])
    #t,a=avg([1,2,3,4]) 
    print("total={}, Average={}".format(t,a))
except TypeError:
    print("Type error, please provide numbers")
except ZeroDivisionError:
    print("Please don't give empty list")
    
    
    
#Apython program to understand the usage of try with finally block
try:
    x=int(input("enter a number:"))
    y=1/x
finally:
    print("we are not catching exception")
print("the inverse is:",y)


"""The assert statement:- The assert statement is useful to ensure that a 
given condition is true.If it is not true,it raises AssertionError.
Syntax is:
    assert condition,message
If condition is False, then the exception by the name AssertionError 
is raised along with the "message" writtent in the assert statement"""

try:
    x=int(input("enter the number between 5 and 10:"))
    assert x>=5 and x<=10, "your input is not correct"
    print("the number entered : ",x)
except AssertionError as obj:
    print(obj)
    
#A python program to create our own exception and raise it when needed
class MyException(Exception):
    def __init__(self,arg):
        self.msg=arg
    def check(di):
        for k,v in di.items():
            print('Name={:15s} Balance={:10.2f}'.format(k,v))
            if(v<2000.00):
                raise MyException("Balance is less for:"+k)
    bank={"raj":5000.00,"vani":1900.50}   
    try:
        check(bank)
    except MyException as me:
        print(me)











a=5
b=2
k=int(input("hello"))
try:
    print(a/b)
    #k=int(input("hello"))



 '''except Exception as error:
    print("hey its an error",error)'''
print("something")
 
 