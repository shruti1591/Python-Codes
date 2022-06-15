# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

#Strings

s1='welcome to "VIT"'
print(s1)


""" 

\b Backspace
\n New line
\t horizontal tab space
\v vertical tab space
\r enter button
\x character x
\\ display single \ """

#adding r before the string to get raw string

s1="welcome to\\t core python\\n learning"
print(s1)

#unicode character:- Hindi, French, German

name=u"\u0915\u094b\u0930 \u092a\u0948\u0925\u0964\u0928"
print(name)

#length

print(len(s1))

#Indexing in string
str="core python"
n=len(str)
i=0
while i<n:
    print(str[i], end=' ')
    i+=1

print(str[-n])
print(str[-1])
    
#reversing the string

i=-1
while i>=-n:
    print(str[i], end=' ')
    i-=1   
    

for i in str[: :-1]:
    print(i,end=' ')

#Slicing the string
print(str[0:9:2]) #index from 0 to 8 with step size 2

#repeating string
print(str*2)

#Concatination

#checking membership
spr=input("Enter the main string")
sub=input("Enter the sub string")
if sub in spr:
    print(sub+" is found")
else:
    print(sub+" is not found")
    
#comparing
if(sub==spr):
    print("both are same")
    
#removing space
name=" core python core "
print(name.lstrip())  #remove left space
print(name.rstrip())  #remove right space
print(name.strip())  #remove both space

#counting substring
print(name.count("core"))

#replacing string with another string
str="this is a beautiful house"
str1="house"
str2="flower"
print(str.replace("house","flower"))

#splitting
str="one two three"
str1=str.split(" ")
print(str1)

#changing the case
print(str.upper())
#try swapcase()

#formating
a=10
b=20
str="the sum of {} and {} =" .format(a,b)
print(str,a+b)

#immutable
str="abcd"
print(str[0])

str[0]="x" #error