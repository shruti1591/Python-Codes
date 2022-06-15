# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

'''To download "MySQL datbase" URL:- "https://dev.mysql.com/downloads/windows/installer"
To install "MySQLdb interface":- "https://pypi.python.org/pypi/mysqlclient"     '''




'''A python program to retrieve and display all rows from the employee table using fetchone'''
import MySQLdb
#connect to MySQL database
conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
#prepare a cursor object using cursor() method
cursor=conn.cursor()
#execute a sql query using execute() method
cursor.execute("select * from emptab")
#get all rows
row=cursor.fetchone()
#if the row exist
while row is not None:
    print(row)
    row=cursor.fetchone()
#close connection
cursor.close()
conn.close()




'''A python program to retrieve and display all rows from the employee table using fetchall'''
import MySQLdb
#connect to MySQL database
conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
#prepare a cursor object using cursor() method
cursor=conn.cursor()
#execute a sql query using execute() method
cursor.execute("select * from emptab")
#get all rows
rows=cursor.fetchall()
#display the number of rows
print("Total number of rows=",cursor.rowcount)
#display the rows from rows object
for row in rows:
    '''print(row)'''
    eno=row[0]
    ename=row[1]
    sal=row[2]
    print('%-6d %-15s %10.2f'% (eno,ename,sal))   
#connection close
cursor.close()
conn.close()






'''A Python program to insert a row into a table in MySQL'''
import MySQLdb
#connect to MySQL database
conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
#prepare a cursor object using cursor() method
cursor=conn.cursor()
#prepare SQL query stringto insert a row
str="insert into emptab(eno,ename,sal) values(1009,'f',1999)"
try:
    #execute the SQL query using execute() method
    cursor.execute(str)
    #save the changes to the database
    conn.commit()
    print('1 row inserted.....')
except:
    #rollback if there is any error
    conn.rollback()
#connection close
cursor.close()
conn.close()






'''A python program to insert several rows into a table from the keyboard.'''
import MySQLdb
#function to store row into the emptab table
def insert_rows(eno,ename,sal):
 #connect to MySQL database
 conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
 #prepare a cursor object using cursor() method
 cursor=conn.cursor()
 #prepare SQL query stringto insert a row
 str="insert into emptab(eno,ename,sal) values('%d','%s','%f')"
 #define the arguments
 args=(eno,ename,sal)
 try:
    cursor.execute(str % args)
    conn.commit()
    print('1 row inserted.....')
 except:
    conn.rollback()
 finally:
    cursor.close()
    conn.close()
n=int(input("how many rows?"))
for i in range(n):
    x=int(input("enter eno:"))
    y=input("enter name")
    z=float(input("enter salary:"))
    insert_rows(x,y,z)
    print("---------------------------------------------")





    
    
'''A python program to delete a row from emptab by accepting the employee number.'''
import MySQLdb
#function to delete row into the emptab table
def delete_rows(eno):
 #connect to MySQL database
 conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
 #prepare a cursor object using cursor() method
 cursor=conn.cursor()
 #prepare SQL query string to delete a row
 str="delete from emptab where eno='%d'"
 #define the arguments
 args=(eno)
 try:
    cursor.execute(str %args)
    conn.commit()
    print('1 row deleted.....')
 except:
    conn.rollback()
 finally:
    cursor.close()
    conn.close()
n=int(input("enter eno"))
delete_rows(n)






'''A python program to increase the salary of an employee by accepting the employee number.'''
import MySQLdb
#function to update row into the emptab table
def update_rows(eno):
 #connect to MySQL database
 conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
 #prepare a cursor object using cursor() method
 cursor=conn.cursor()
 #prepare SQL query string to update a row
 str="update emptab set sal=sal+1000 where eno='%d'"
 #define the arguments
 args=(eno)
 try:
    cursor.execute(str %args)
    conn.commit()
    print('1 row updated.....')
 except:
    conn.rollback()
 finally:
    cursor.close()
    conn.close()
n=int(input("enter eno"))
update_rows(n)







'''A python program to create table2 in MySQL database'''
import MySQLdb
#connect to MySQL database
conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
#prepare a cursor object using cursor() method
cursor=conn.cursor()
#execute a sql query using execute() method
cursor.execute("drop table if exists table2")
#prepare sql string to create a new table
str="create table table2(eno int,ename char(20),gender char(1),salary float)"
#execute the  query to create the table
cursor.execute(str)
print("Table created")  
cursor.close()
conn.close()








'''A python program using GUI to retrieve a row from a MySQL database table'''
import MySQLdb
from tkinter import *

#create root window
root=Tk()

def retrieve_rows(eno):
    #connect to MySQL database
    conn=MySQLdb.connect(host='localhost', database='world', user='root', password='root')
    #prepare a cursor object using cursor() method
    cursor=conn.cursor()
    #prepare SQL query string to retrieve a row
    str="select * from emptab where eno='%d'"
    #define the arguments
    args=(eno)
    #execute the SQL query using execute() method
    cursor.execute(str % args)
    #get only one row
    row = cursor.fetchone()
    #if the row exists display it using a label
    if row is not None:
        lbl=Label(text=row, font=('Arial',14)).place(x=50, y=200)
    cursor.close()
    conn.close()
#a function that takes input from Entry widget
def display(self):
    #retrieve the value from entry widget
    str=e1.get()
    #display the values using Label
    lbl=Label(text="You entered:" + str, font=('Arial',14)).place(x=50, y=150)
    retrieve_rows(int(str))

f=Frame(root , height=350,width=600)
f.propagate(0)
f.pack()
l1= Label(text="enter employee number: ",font=('Arial',14))
#create entry widget for accepting employee number
e1=Entry(f,width=15,fg='blue',bg='yellow',font=('Arial',14))
#when user presses enter, bind that event to display method
e1.bind("<Return>",display)
#place label and entry widgets in the frame
l1.place(x=50,y=100)
e1.place(x=300,y=100)
root.mainloop()
    

        
    