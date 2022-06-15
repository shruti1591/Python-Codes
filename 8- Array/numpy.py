# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:52:43 2021

@author: SYSTEMS
"""

#********************************************************************************************#
    
import numpy
arr=numpy.array([10,20,30.0,40,50])
print(arr)

import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)

from numpy import *
arr=array([10,20,30,40,50])
print(arr)

#Creating array
"""array()
linspace()
logspace()
arange()
zeros() and ones()"""


#linspace() function is used to create an 
#array with evenly spaced points between a starting point 
#and ending point
#linspace(start,stop,step)

from numpy import *
a=linspace(0,10,5)
print("a= ",a)
print(a.dtype)

#logspace() produces evenly spaced points on a logarithmically spaced scale
#logspace(start,stop,n)
from numpy import *
a=logspace(0,4,5)
print("a= ",a)
n=len(a)
for i in range(n):
    print('%.1f' % a[i], end=' ')

#The arange() function in numpy is same as range() function in python.
#arange(start,stop,stepsize)
from numpy import *
a=arange(2,12,2)
print(a)

#zeros(n,datatypes)    ones(n,datatypes)
from numpy import *
a=zeros(5,int)
b=ones(5)
print(a)
print(b)

#Mathematical operations
from numpy import *
arr=array([10,20,30,40])
print(min(arr+5))

#Comparing Array
from numpy import *
arr1=array([10,20,30,40])
arr2=array([6,80,30,90])
#c=arr1>=arr2
c=where(arr1>arr2,arr1,arr2)
print(c)
print(any(c))
print(all(c))

#Aliasing , viewing and copying Arrays
#aliasing
from numpy import *
a=arange(1,6)
b=a
print(a)
id(a)
print(b)
id(b)
b[0]=99
print(a)
id(a)
print(b)
id(b)

#viewing and copying
from numpy import *
a=arange(1,6)
#b=a.view()
b=a.copy()
print(a)
id(a)
print(b)
id(b)
b[0]=99
print(a)
id(a)
print(b)
id(b)

#indexing and slicing of array
from numpy import *
a=arange(10,16)
b=a[1:6:2]
b=a[-2:2:-1]
b=a[:-2:]
print(b)

#dimensions in arrays
from numpy import *
a=array([10,11,12,13,14,15])
print(a)
b=array([[1,2,3],[9,8,7]])
print(b)

#Attributes of an Array
"""ndim
shape
size
itemsize
dtype
nbytes"""
 
#reshape()
a=array([1,2,3,4,5,6])
b=reshape(a,(3,2))
print(b)
a=arange(12)
print(a)
b=reshape(a,(2,3,1))
print(b)

b=b.flatten()
print(b)


#Multi-dimensional Arrays

a=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
                print(a[i][j][k])


from numpy import *
b=[[1,2,3],[9,8,7]]
b=reshape(b,(2,3))
print(b[1:2,1:4])



a=arrange(11,36,1)
print(a)

a=random.rand(15)
print(reshape(a,(3,5)))








