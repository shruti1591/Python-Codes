# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

class Student:
    a=10    #class variable
    #this is special method called constructor
    def __init__(self):
        self.name="vishnu"
        self.address="mumbai"
        self.marks=900
        
    #this is an instance method
    def talk(self):
        print("hello")
        print("hi, I am ", self.name)
        print("My address is ", self.address)
        #print("My address is ", self._Student__address) #name mangling(abstraction)
        print("My marks are", self.marks)
        print(self.a)
              
#Create a instance to student class.
s1=Student()
id(s1)
s2=Student()
id(s2)
#call the method using the instance.
s1.talk()  
print(s1.__dict__)  
print(Student.__dict__) 

print(Student.a)   #class variable can be accesssed by using class name or object name.

s1.a=30
print(s1.a)
print(s2.a)
    
'''Self Variable'''

#Self is a default variable that contains the memory
# address of instance of the 
#current class

""""when an instance to the class is created,
 the instance name contains memory location
of the instance. This memory location is internally
 passed to 'self' """  

s1=Student()

"""since self knows memory address of the instance, 
it can br refered to all the
members of instance in two ways:-
1- The self variable used as first parameter in constructor
2- The self variable used as first parameter in instance method """

'''Constructor'''
#Constructor with more than one parameter

class Student:
    #this is constructor
    def __init__(self, n=".",m=0):
        self.name=n
        self.marks=m
        
    #this is instance method
    def display(self):
        print("hi", self.name)
        print("your marks", self.marks)
        
#constructor is called without any arguments.
s=Student()
s.display()
print("----------------------------------")

#constructor is called with 2 arguments
s1=Student("lakshmi roy",880)
s1.display()
print("----------------------------------")

''' Namespaces
1- Instance namespace
2- Class namespace '''


'''Types of variables'''
''' The variables which are written inside
 a class are of 2 types:-
1- Instance Variable(whose seperate copy
 is created in every instance)
2- Class variable and static variable
(single copy is available to all 
the instance of the class)'''

#Python program to understand instance variables
class Sample:
    def __init__(self):
        self.x=10
        
    def modify(self):
        self.x+=1
#create two instances
s1=Sample()
s2=Sample()
print("x in s1= ", s1.x)
print("x in s2= ", s2.x)
#modify x in s1
s1.modify()
print("x in s1= ", s1.x)
print("x in s2= ", s2.x)



#Python program to understand class or static variables
class Sample:
    #this is class variable
    x=10
    # this is class method   
    @classmethod    #build-in decorator
    def modify(cls):
        cls.x+=1
#create two instances
s1=Sample()
s2=Sample()
print("x in s1= ", s1.x)
print("x in s2= ", s2.x)
#modify x in s1
s1.modify()
print("x in s1= ", s1.x)
print("x in s2= ", s2.x)






#Types of methods
''' 1- Instance methods
        a-Accessor method (getter)
        b-Mutator method (setter)
    2- Class methods
    3- Static methods '''
    
#Instance method act upon the instance of the class
    
# Instance method to process the data of several students
class student:
    #constructor
    def __init__(self, n=' ',m=0):
        self.name = n
        self.marks = m
    #Instance method
    def display(self):
        print("hi", self.name)
        print("marks",self.marks)        
    def calculate(self):
        if(self.marks>=600):
            print("first grade")
        elif(self.marks>=500):
            print("second grade")
        elif(self.marks>=350):
            print("third grade")
        else:
            print("you are fail")
            #create instances with some data from keyboard
n=int(input("how many students?"))
i=0
while(i<n):
    name=input("enter name:")
    marks=int(input("enter marks: "))
    s=student(name,marks)
    s.display()
    s.calculate()
    i+=1
    print("------------------------------------")
    
    
# Instance method to process the data of several students using mutator and accessor methods
    
class student:
    
    #mutator method
    def setname(self,name):
        self.name=name
        
    #accessor method
    def getname(self):
        return self.name
    
     #mutator method
    def setmarks(self,marks):
        self.marks=marks
        
    #accessor method
    def getmarks(self):
        return self.marks
    
#create instances with some data from keyboard
n=int(input("how many students?"))

i=0
while(i<n):
    s=student()
    name=input("enter name:")
    s.setname(name)
    marks=int(input("enter marks: "))
    s.setmarks(marks)
    
    #retrieve the data
    print("hi",s.getname())
    print("your marks", s.getmarks())
    
    i+=1
    print("----------------------------------")
    
    
#classmethods are the methods which act on class variable or instance variable.
    
class Bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print('{} flies with {} wings'.format(name,cls.wings))
Bird.fly('sparrow')
Bird.fly('Pigeon')

#static methods are used when some processing is related to the class but does not need
#the class or its instances to perform any work.For example setting enviranment variables,
#counting the number of instances of the class or changing an attribute in another class
#etc are the tasks related to a class.

class Myclass:
    n=0
    def __init__(self):
        Myclass.n=Myclass.n+1
        
    @staticmethod    #decorator
    def noobject():
        print('no. of instances created:' , Myclass.n)
        
obj1=Myclass()
obj2=Myclass()
obj3=Myclass()
Myclass.noobject()


#Passing member of one class to another class
class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
        
    def display(self):
        print('Id=',self.id)
        print('Name=',self.name)
        print('Salary=',self.salary)
        
class Myclass:
    @staticmethod
    def mymethod(e):
        e.salary+=1000
        e.display()

e=Emp(10,'Raj Kumar',15000.75)
Myclass.mymethod(e)


#Inner classes
class Person:
    def __init__(self):
        self.name='Bob'
        
    def display(self):
        print('Name= ',self.name)
        
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1988
            
        def display(self):
            print('Dob= {}/{}/{}'.format(self.dd,self.mm,self.yy))            
#creating person class object
p=Person()
p.display()
#create Dob class object as object to person class object
x=Person().Dob()
x.display()
print(x.yy)

'''class Person:
    def __init__(self):
        self.name='Bob'
        self.db=self.Dob()
        
    def display(self):
        print('Name= ',self.name)
        
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1988
            
        def display(self):
            print('Dob= {}/{}/{}'.format(self.dd,self.mm,self.yy))            
#creating person class object
p=Person()
p.display()
#create inner class object
x=p.db
x.display()
'''
