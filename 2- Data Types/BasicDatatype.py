# -*- coding: utf-8 -*-
"""
@author: SYSTEMS
"""

'''None Datatype'''

'''1- Numeric Datatypes'''

#int, float, complex and bool

year_of_birth = 1999999999999999
print(year_of_birth)
print(type(year_of_birth))

height_cm = 170.50
print(height_cm)
print(type(height_cm))

comp=4.7+3j
print(comp)
print(type(comp))

subject = 'Data Science'
is_success = True
print(is_success)
print(type(is_success))

print(type(year_of_birth), type(height_cm), type(comp), type(subject), type(is_success))

#binary, octal and hexadecimal
a=0o17
b=0B1110010
c=0x1c2

#Conversion to decimal
n=int(a)
print('octal 17 =',n)       
n=int(b)
print('Binary 110010 =',n)
n=int(c)
print('Hexadecimal 1c2 =',n)

#int(string,base)
str="1892"
n=int(str,2)
print(n)




#***********************************************************************************
'''2- sequences'''

#String
s="The subject 'Python' is interesting"
print(type(s))

print(s)
print(s[0:9])
print(s*2)


#Bytes- contains positive integers between 0 to 255 and like an array. Also cann't modify or edit.
elements=[10,20,30,199,254] #creating a list
x=bytes(elements)    #converting the list into byte type array
print(x[2])   #printing single element
for i in x:   #for loop
     print(i)
x[2]=90   #will give error

#bytearray- Elements can be modified
elements1=[10,20,30,199]
y=bytearray(elements1)
print(y[0])
y[0]=99    #will change the value
print(y[0])


#list- can store different type of element and can grow dynamically
list1=[2,-2,0.9,"vijay",'hello','''hi''']
print(type(list1))
print(list1)
print(list1*2)
listnew=list1[2:4]   #Slicing in the list
print(listnew)
list1[2]=44    #modification is allowed
print(list1)
list1.append(2)
print(list1)
list1.insert(4,"test")
print(list1)
print(2 in list1) #will check if element 2 is there in the list and return bool.
a=[90,30,list1]
print(a) #nested list

a=[1,2,3]
print(id(a))
b=a         #aliasing
print(id(b))
b=a[:]       #cloning
print(id(b))




#tuple - similar to list, not possible to modify so it is read only list.
tp1=(2,-2,0.9,"vijay",'hello','''hi''')
print(id(tp1))
tp2=(4,2,"hello")
tp1=tp1+tp2
print(tp1)
print(id(tp1))
print(type(tp1))
tp2=tp1[0:2]
print(tp2)
tp1[1]=7    #will give the error
print(tp1)
print(tp1.count(2)) #will give the count of specified element
print(tp1.index('''hi''')) #will return the index of the element given


#range
r=range(10,30,4)
r1=range(10)
for i in r1:
    print(i)

#**********************************************************************************
'''3- Sets'''

#unordered collection which do not accept duplicate data
a={10,20,30,60,70,70}
print(type(a))

b="hello"
print(b)

ch=set("hello")
print(ch)

lst=[1,3,4,5,8]
print(lst)
print(set(lst)) #converting list to set

print(a[0:3]) #will give error as we cann't retrive the elements using indexing and slicing
a.update([3,4,5]) #updating set with three elements.
print(a)
a.remove(4)  #removing element 4
print(a)
a.add(10) #adding element 10
print(a)

#******************************************************************************************
'''4- mapping types'''

#Key-value pair(Dictionaries)
d={10:'divA', 11:'divB', 11:'divB', 12:'divC'}
print(type(d))
print(d)
print(d[10])   #will display the value of specific key 
print(d.keys())   #will return all the keys
print(d.values())  #will return all the values
d[11]='SE'    #will change the value on that specific key .
print(d[11])
print(d)
del d[11]   #delete the element with specified key
print(d)
d.items()    #will return key-value pairs
d.clear()    #clear the complete dictionary
print(d)

#converting list to dictionary
a=[1,2,3,4,5]
b=["a","b","c","d"]
z=zip(a,b) #convert sequence into zip class object
print(z)
d=dict(z)  #convert zip object to dictionary
print(d)


