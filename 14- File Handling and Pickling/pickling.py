# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''Pickling is creating an object and storing
 the actual data into that object.
Later this object should be stored into a binary 
file in the form of bytes.
This is called pickling or serialization.
Unpickle is a processwhereby a byte stream 
is converted back into a class object. ''' 

import pickle
#pickling
example={1:"a",2:"b"}
pickle_out=open("d11.txt","wb")
pickle.dump(example, pickle_out)
pickle_out.close()
#unpickling
pickle_in=open("d11.txt","rb")
example1=pickle.load(pickle_in)
print(example1)

#Next example

class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def display(self):
        print(self.id,self.name,self.sal)
#Python program to pickle Emp class
import  pickle
f=open("emp.txt","ab")
n=int(input("how many employees?"))
for i in range(n):
    id=int(input("enter id:"))
    name=input("enter name:")
    sal=float(input("enter salary:"))
    e=Emp(id,name,sal)
    pickle.dump(e,f)
f.close()
#Python program to unpickle Emp class object
import pickle
f=open("emp.txt","rb")
print("employees details:")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("end of file reached:")
        break
f.close()


#map function

'''map=(function,iterables)
function:- REquired.The function to execute 
for each item
iterable:- Required. A sequence, collection or 
an iterator object.
You can send as many iterables as you like,
 just make sure the
 function has one parameter for each iterable.'''

#Program 1
def addition(n):
     return n+n
numbers=(1,2,3,4)
results=map(addition,numbers)
print(list(results))


#Program 2
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

#Program 3
# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 
  
# map() can listify the list of strings individually 
test = list(map(list, l))
print(test)

'''lambda function:- lambda arguments: expression
In Python, anonymous function is a function that
 is defined without a name.
While normal functions are defined using the def keyword,
 in Python anonymous functions are defined using
 the lambda keyword.
Lambda functions can have any number of arguments 
but only one expression. 
The expression is evaluated and returned. 
Lambda functions can be used wherever 
function objects are required.'''

# Double all numbers using map and lambda 
  
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 

# Add two lists using map and lambda 
  
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
  
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 

'''filter():-
The filter() function in Python takes in a
 function and a list as arguments.
The function is called with all the 
items in the list and a new list is 
returned which contains items for
 which the function evaluats to True.
Here is an example use of filter()
 function to filter out only even numbers 
from a list.'''

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# Output: [4, 6, 8, 12]
print(new_list)

        
    
    
    