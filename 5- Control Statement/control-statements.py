# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''Control Statements:- Controls the change of flow of execution
1- if statement
2- if... else statement
3- if... elif... else statement
4- while statement
5- for loop
6- else suite
7- break statement
8- continue statement
9- pass statement
10- assert statement
11- return statement'''


# 1- if statement
num =int(input("enter the no. to check"))
if num==1:
    print("one")

#2- if....else statement
num =int(input("enter the no. to check if it is even or odd"))
if num%2==0:
    print(num," is even")
else:
    print(num," is odd")
    
# 3- if... elif... else statement
num =int(input("enter the digit to be displayed in word"))
if num==0:
    print("zero")
elif num==1:
    print("one")
elif num==2:
    print("two")
'''else:
    print("enter the number between 0 to 2")'''
    
# 4- while statement
x=1
while x<=10:
    print(x)
    x+=1
print("End")

#5 - for loop
str="hello"
for ch in str:
    print(ch)

#Nested loop
for i in range(3):
    for j in range(4):
        print('i=',i,'\t','j=',j)
  
        
#pattern
for i in range(1,11):
    for j in range(1,i+1):
        print('*',end=" ")
    print()
    
# 6- else suite
for i in range(5):
    print("Yes")
else:
    print("no")
    
group1=[1,2,3,4,5]
search=int(input("Enter the element to search"))
for element in group1:
    if search==element:
        print("element found in the group1")
        break
else:
    print("element not found")

    
#break statement
    
# Continue statement

x=0
while x<10:
    x+=1
    if x>5:
        continue
    print("x=",x)
print("out of the loop")


#Pass statement
#Retrieving only negative numbers from the list.
num=[1,2,3,-4,-5,-6,-7,8,9]
for i in num:
    if(i>0):
        pass   # simple ignore the condition
    else:
        print(i)
        
#assert statement
'''assert statement is useful to
 check if a perticular condition is
 fulfilled or not.
The syntex is as follows:
    assert expression, message'''

x=int(input("enter the number greater than 0: "))
assert x>0, "wrong input entered"
print("U entered: ", x)

#Assertion error caused here is called exception.
# To handle Assertion error exception 

x=int(input("enter the number greater than 0: "))
try:
    assert x>0
    print("U entered: ", x)
except AssertionError:
    print("wrong value entered")
    
    
    
    
    

      
