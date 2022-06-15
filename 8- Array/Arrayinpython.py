# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

# Python program to demonstrate  
# Creation of Array
#arrayname=array(typecode,[elements])  
  
# importing "array" for array creations 
import array as arr 
  
# creating an array with integer type 
a = arr.array('i', [1, 2, 3]) 
  
# printing original array 
print ("The new created array is : ", end =" ") 
for i in range (0, 3): 
    print (a[i], end =" ") 
print() 
  
# creating an array with float type 
b = arr.array('d', [2.5, 3.2, 3.3]) 
  
# printing original array 
print ("The new created array is : ", end =" ") 
for i in range (0, 3): 
    print (b[i], end =" ") 
print()
    
# Appending the element in the array
a.append(7)
for i in (a):
    print(i)
    
# Inserting element in the array
a.insert(1,10)
for i in (a):
    print(i, end=" ")  
    
#Accessing the element of array
print("Fourth element of array a is",a[4])


#pop function remove the element of specific index
print ("The popped element is : ", end ="") 
print(a.pop(1))

#check if element is poped or not
for i in (a):
    print(i, end=" ")  
    
#remove function remove the specified element. 
#If the element is not there then it will throw the error
print ("The popped element is : ", end ="") 
a.remove(10)

#check if element is removed or not
for i in (a):
    print(i, end=" ")  
    
    
a.remove(10)     #error





# Python program to demonstrate  
# silicing of elements in a Array 
  
# creating a list  
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
  
a = arr.array('i', l) 
print("Intial Array: ") 
for i in (a): 
    print(i, end =" ") 
  
# Print elements of a range 
# using Slice operation 
Sliced_array = a[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_array) 
  
# Print elements from a  
# pre-defined point to end 
Sliced_array = a[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(Sliced_array) 
  
# Printing elements from 
# beginning till end 
Sliced_array = a[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_array) 


# Searching the index of given element.
print (a.index(2)) 

# Updating the elements in the array
a[6]=13
for i in (a): 
    print(i, end =" ")

# count the existance of given element    
print(a.count(1))

#Reversing an array
a.reverse()
for i in (a): 
    print(i, end =" ")



    
