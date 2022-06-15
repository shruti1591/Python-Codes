# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""


'''Single Inheritence'''
# Python program to demonstrate 
# single inheritance 
  
  
# Base class 
class Parent: 
     def func1(self): 
          print("This function is in parent class.") 
  
# Derived class 
class Child(Parent): 
     def func2(self): 
          print("This function is in child class.") 
  
# Driver's code 
object = Child() 
object.func1() 
object.func2() 

'''Multiple Inheritence'''
# Python program to demonstrate 
# multiple inheritance 
  
  
# Base class1 
class Mother: 
    mothername = "" 
    def mother(self): 
        print(self.mothername) 
  
# Base class2 
class Father: 
    fathername = "" 
    def father(self): 
        print(self.fathername) 
  
# Derived class 
class Son(Mother, Father): 
    def parents(self): 
        print("Father :", self.fathername) 
        print("Mother :", self.mothername) 
  
# Driver's code 
s1 = Son() 
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents() 

'''Multilevel Inheritence'''
# Python program to demonstrate 
# multilevel inheritance 
  
  
# Base class 
class Grandfather: 
    grandfathername =""  
    def grandfather(self): 
        print(self.grandfathername) 
  
# Intermediate class 
class Father(Grandfather): 
    fathername = "" 
    def father(self): 
        print(self.fathername) 
  
# Derived class 
class Son(Father): 
    def parent(self): 
        print("GrandFather :", self.grandfathername) 
        print("Father :", self.fathername) 
  
# Driver's code 
s1 = Son() 
s1.grandfathername = "Srinivas"
s1.fathername = "Ankush"
s1.parent() 

'''Hierarical Inheritence'''
# Python program to demonstrate 
# Hierarchical inheritance 
  
  
# Base class 
class Parent: 
      def func1(self): 
          print("This function is in parent class.") 
  
# Derived class1 
class Child1(Parent): 
      def func2(self): 
          print("This function is in child 1.") 
  
# Derivied class2 
class Child2(Parent): 
      def func3(self): 
          print("This function is in child 2.") 
   
# Driver's code 
object1 = Child1() 
object2 = Child2() 
object1.func1() 
object1.func2() 
object2.func1() 
object2.func3() 

'''Hybrid Inheritance'''
# Python program to demonstrate 
# hybrid inheritance 
  
  
class School: 
     def func1(self): 
         print("This function is in school.") 
   
class Student1(School): 
     def func2(self): 
         print("This function is in student 1. ") 
   
class Student2(School): 
     def func3(self): 
         print("This function is in student 2.") 
   
class Student3(Student1, School): 
     def func4(self): 
         print("This function is in student 3.") 
   
# Driver's code 
object = Student3() 
object.func1() 
object.func2() 



'''super keyword'''
# Program to define the use of super() 
# function in multilevel inheritance 
class A: 
    def __init__(self): 
        print('HEY !!!!!!  I am initialised(Class A)') 
  
    def sub_X(self, b): 
        print('Printing from class A:', b) 
# class B inherits the A 
class B(A): 
    def __init__(self): 
        print('HEY !!!!!!  I am initialised(Class B)') 
        super().__init__() 
  
    def sub_X(self, b): 
        print('Printing from class B:', b) 
        super().sub_X(b + 1) 
# class C inherits the A ang B both 
class C(B): 
    def __init__(self): 
        print('HEY !!!!!!  I am initialised(Class C)') 
        super().__init__() 
  
    def sub_X(self, b): 
        print('Printing from class C:', b) 
        super().sub_X(b + 1) 
  
# created the object M 
m = C()   
    # calling the function sub_X() from class C
    # which inherits both A and B classes 
m.sub_X(10)

'''Method Resolution Order'''

# Python program to show the order 
# in which methods are resolved 
  
class A: 
    def rk(self): 
        print(" In class A") 
        super().rk()
class B: 
    def rk(self): 
        print(" In class B") 
  
# classes ordering 
class C(A, B): 
    def __init__(self): 
        print("Constructor C")      
    def rk(self):
        print("test")
        super().rk()
  
r = C() 
r.rk()  
# it prints the lookup order  
print(C.__mro__) 
print(C.mro()) 

#Next program

class A:
    def method(self):
        print('A class method')
        super().method()
class B:
    def method(self):
        print('B class method')
        super().method()
class C:
    def method(self):
        print('C class method')
        #super().method()
        
class X(A,B):
    def method(self):
        print('X class method')
        super().method()
class Y(C):
    def method(self):
        print('Y class method')
        super().method()
class P(X,Y,C):
    def method(self):
        print('P class method')
        super().method()
p=P()
p.method()


print(P.mro())

