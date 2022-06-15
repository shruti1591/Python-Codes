# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

#Operators in Python!!!!!!!!!!!!!!!
"""An operator is a symbol that performs operation on operands.
Classification of operators:-
1- Arithmatic Operators
2- Assignment Operators
3- Unary minus Operators
4- Relational Operators
5- Logical Operators
6- Boolean Operators
7- Bitwise Operators
8- Membership operators
9- Identity Operators   """


# 1- Arithmatic Operators

print(3+4)   #Addition Operator
print(3-4)   #Subtraction Operator
print(3*4)   #Multiplication Operator
print(3/4)   #Division Operator
print(3**4)   #Exponent Operator
print(4%3)    #Modulo Operator gives remainder
print(8//3)   #Integer Division returns floor value

''' In the case of multiple operators, the order of evaluation is:-
1- Parentheses
2- Exponentiation
3- Multiplication, Division,Modulus and floor division
4- Addition and Substration
5- Assignment operators 
#Associativity= Left to Right'''

d=(1+2)*3**2//2+3
print(d)

# 2- Assignment Operators

x=20
y=30
z=40

a=x+y      #Assignment Operator
print(a)

z+=x   #Addition Assignment z=z+x
print(z)

#Subtraction Assignment
#Multiplication Assignment
#Division Assignment
#Modulus Assignment
#Exponentiation Assignment
#Integer Division Assignment


# 3- Unary Minus Operator
n=10
print(-n)

# 4- Relational Operators

a=5
b=6
print(a>b)    #Greater than operator
print(a>=b)     #Greater than or equal operator
print(a<b)    #Less than operator
print(a<=b)   #Less than or equal to operator
print(a==b)   #equals operator
print(a!=b)   #Not equals operator


# 5- Logical Operators
a=10
b=20
c=30
print(a<b and b<c)
print(a>b or b<c)
print(not a>b)

#6- Boolean Operators

a=True
b=False
print(a and b)
print(a or b)
print(not a)


# 7- Bitwise Operators

x=7
y=9
print(x&y)  #Bitwise AND
print(x|y)   #Bitwise OR
print(x^y)   # Bitwise XOR
print(x<<2)  #Bitwise left shift operator
print(x>>2)  #Bitwise right shift operator

00000111
00000011
00000001
00011100

# 8- Membership Operators
n=['a','b','c','d']   #in
for name in n:
    print (name)
print ('d' not in n)    #not in
 
 #9- Identity Operators

a=5
b=a
id(a)  #identity number of object 5
id(b)

x=10
y=11
id(x)
id(y)


#Two operators is and is not
a=25
b=28
if(a is b):
    print("a and b have same identity")
else:
    print("different identity")



          