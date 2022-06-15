'''Basic Input Output in python'''

print()

#printing strings
print("hello")
print("hello"+"Loy")
print("hello","Loy")
print("hello\nLoy")
print("hello\tLoy")
print("hello\\nLoy")
print(3*"hello Loy")

#printing variables
a,b=3,4
print(a,b)


print("hi", end="%")
print("how are you")

# using sep attribute of print
print(a,b,sep="$")

#using end operator
print("""hello""",end=' ')
print("How are you Loy",end="\t")
print("?")

#using objects
lst=[1,3,'hi']
print(lst)

#format fuction
n1, n2, n3= 1,5,3
print(n1,n2,n3)
print("number1=",n1,"number2=",n2,"number3=",n3)
print("number1={2},number2={1},number3={0}".format(n1,n2,n3))

#Input Statements
str=input("enter the value of str")
print("The value entered by user is ",str)

str=input("Enter the name")
print("The name is:", str)
print(type(str))



print("Let's add two numbers!!!! Can you please pass the input from keyboard")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(type(a))
c=a+b
print("The addition of two numbers is: ",c)
print("The addition of two numbers {} and {} is {}. ".format(a,b,c))

#use of split() function
v1, v2, v3=[int(x) for x in input("Enter the numbers: ").split()]
print("sum= ",v1+v2+v3)

#use of eval()function:- it takes a string and evaluates the result of the string by taking python expression.
a,b=5,10
result=eval("a+b-4")
print(result) 



"""Program 1:- Write a program to accept a character from keyboard and print it.
Program 2:- Write a python program to accept a group of string seperated by commas and display them.
Program 3:- Write a Python program to find sum and product of two numbers.
"""




txt = "welcome to the jungle"

x = txt.split()

print(x)


#string.split(separator, maxsplit)

txt = "apple#banana#cherry#orange"

x = txt.split("#", 2)

print(x)

