# -*- coding: utf-8 -*-
"""

@author: SYSTEMS
"""

'''UNIT 5:- GUI Programming and Databases '''

#import all contents of tkinter
from tkinter import *
#create root window
root=Tk()
#wait and watch for any event that may take place
#in the root window
root.mainloop()


#import all contents of tkinter
from tkinter import *
#create root window
root=Tk()
#set window title
root.title("My window")
#set window size
root.geometry("400x300")
#set window icon
root.wm_iconbitmap("logoicon.ico")
#wait and watch for any event that may take place
#in the root window
root.mainloop()


'''Python program to know the available font 
families'''
from tkinter import *
from tkinter import font
root=Tk()
list_fonts=list(font.families())
print(list_fonts)

'''WORKING WITH CONTAINERS'''
'''A container is a component that is used as a 
place where drawing or widgets
can be displayed.
1- Canvas:- Shapes like lines, curves, arcs and
 circles.
2- Frame:- Display widgets like buttons, check
 buttons or menus.'''


'''Program to demostrate creation of various shapes 
in canvas.'''
from tkinter import *
root=Tk()
#create canvas as a child to root window
c=Canvas(root,bg="blue",height=700,width=1200,cursor='pencil')
#id=c.create_line(50,50,200,50,200,150,50,50,width=4,fill="white")
#id=c.create_oval(100,200,400,400,width=5,fill="yellow",outline="red",activefill="green")
#id=c.create_polygon(500,500,200,200,300,200, width=3, fill="green",outline="red",smooth=1,activefill="lightblue")
#id=c.create_rectangle(500,200,700,600,width=2,fill="gray",outline="black",activefill="yellow")
fnt=('Times',40,'bold italic underline')
#ide=c.create_text(500,100,text="My Canvas",font=fnt,fill="yellow",activefill="green")
ide=c.create_arc(900,400,1200,600,width=3,start=90,extent=90,outline="black",style="arc")
c.pack()
root.mainloop()

from tkinter import *
root=Tk()
c=Canvas(root,bg="white",height=500,width=500)
file1=PhotoImage(file="logo.png")
id=c.create_image(200,200,image=file1)
fnt=('Times',40,'bold italic underline')
ide=c.create_text(150,100,text="My Canvas",font=fnt,fill="yellow",activefill="green")
c.pack()
root.mainloop()







'''A GUI program to display a frame in the root window.'''
from tkinter import *
root=Tk()
root.title("My Frame")
f=Frame(root,height=400,width=500,bg="YELlOW",cursor="cross")
f.pack()
root.mainloop()

'''Widget- A widget is a GUI component that is displayed on the screen and can
perform a task as desired by the user.
Button
Label
Message
Text
Scrollbar
Checkbutton
Radiobutton
Entry
Spinbox
Listbox
Menu '''

'''........................Push button................................'''
from tkinter import *
#method to be called when the button is clicked
def buttonClick(self):
    print("You can click me")
#create root window
root1=Tk()
#create frame as child to root window
f=Frame(root1,height=500,width=500)
#let the frame not shrink
f.propagate(0)
#attach the frame to root window
f.pack()
#create a push button as child to frame
b=Button(f,text="MY BUTTON",width=15,height=2,bg="yellow",fg="blue",activebackground="green",activeforeground="red")
#attach button to the frame
b.pack()
#bind the left mouse button with the method to be called
b.bind("<Button-1>",buttonClick)
#the root window handles the mouse click event
root1.mainloop()


'''...........................Checkbutton..............................'''
from tkinter import *
class Mycheck:
    def __init__(self,root):
        self.f=Frame(root,height=350,width=500)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to root window
        self.f.pack()
        #create IntVar class variable
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        #create check boxs and bind them to display method
        self.c1=Checkbutton(self.f, text="A",variable=self.var1,command=self.display)
        self.c2=Checkbutton(self.f, text="B",variable=self.var2,command=self.display)
        self.c3=Checkbutton(self.f, text="C",variable=self.var3,command=self.display)
        
        #Attach checkboxs to the frame
        '''self.c1.place(x=50, y=100)
        self.c2.place(x=200, y=100)
        self.c3.place(x=350, y=100)
        
        self.c1.grid(row=0,column=0)
        self.c2.grid(row=1,column=0)
        self.c3.grid(row=2,column=0)'''
        
        self.c1.pack(side=LEFT)
        self.c2.pack(side=LEFT)
        self.c3.pack(side=RIGHT)
              
    def display(self):
        x=self.var1.get()
        y=self.var2.get()
        z=self.var3.get()
        
        #string is empty initially
        str=""
        #catch user choice
        if x==1:
            str+='Java'
        if y==1:
            str+='Python'
        if z==1:
            str+='C++'
        #diaplay the user selection as a label
        lb1=Label(text=str,fg='blue').place(x=50,y=150,width=200,height=20)
#create root window
root=Tk()
#create an object to MyButton class
mb=Mycheck(root)
root.mainloop()        
        
        
'''.........................Radiobutton...............................'''        

from tkinter import *
class Myradio:
    def __init__(self,root):
        self.f=Frame(root,height=350,width=500)
        #let the frame will not shrink
        self.f.propagate(0)
        #attach the frame to root window
        self.f.pack()
        #create IntVar class variable
        self.var=IntVar()
        
        #create Radiobuttons and bind them to display method
        self.c1=Radiobutton(self.f,bg='yellow',fg='green', font=("Georgia",20,'underline'), text="A",variable=self.var,value=1,command=self.display)
        self.c2=Radiobutton(self.f, text="B",variable=self.var,value=2,command=self.display)
        self.c3=Radiobutton(self.f, text="C",variable=self.var,value=3,command=self.display)
        
        #Attach radiobuttons to the frame
        self.c1.place(x=50, y=100)
        self.c2.place(x=200, y=100)
        self.c3.place(x=350, y=100)
        
        ''' self.c1.grid(row=0,column=0)
        self.c2.grid(row=1,column=0)
        self.c3.grid(row=2,column=0)
        
        self.c1.pack(side=LEFT)
        self.c2.pack(side=LEFT)
        self.c3.pack(side=RIGHT)'''
              
    def display(self):
        x=self.var.get() 
        #string is empty initially
        str=""
        #catch user choice
        if x==1:
            str+='Java'
        if x==2:
            str+='Python'
        if x==3:
            str+='C++'
        #diaplay the user selection as a label
        lb1=Label(text=str,fg='blue').place(x=50,y=150,width=200,height=20)
#create root window
root=Tk()
#create an object to MyButton class
mb=Myradio(root)
root.mainloop()        
        



















"""............................MenuBar................................."""

from tkinter import *
class MyMenuDemo:
    def __init__(self,root):
        #create a member
        self.menubar=Menu(root)
        #attach the menubar to the root window
        root.config(menu=self.menubar)
        #create file menu
        self.filemenu=Menu(root,tearoff=0)
        
        #create menu items in file menu
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        
        #add a horizontal line as a seperator
        self.filemenu.add_separator()
        
        #create another menu item below the seperator
        self.filemenu.add_command(label='Exit', command=root.destroy)
        
        #add the file menu with a name File to the menubar
        self.menubar.add_cascade(label='File',menu=self.filemenu)
        self.editmenu=Menu(root,tearoff=0)
        
        #create menu items in file menu
        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)
        #add the file menu with a name 'edit' to the menubar
        self.menubar.add_cascade(label='Edit',menu=self.editmenu)
    def donothing(self):
        pass
#create root window
root=Tk()
#title for the root window
root.title("A Menu example.")
#create object to our class
obj=MyMenuDemo(root)
#define the size of the root window
root.geometry('600x350')
#handle any events
root.mainloop()
        
'''.......................Dialog Box...............................'''

import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name= fd.askopenfilename() 
    print(name)
    
tk.Button(text='File Open', 
       command=callback).pack(fill=tk.X)
tk.mainloop()     





from tkinter import * 
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.geometry('200x100') 
  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 
  
mainloop() 



'''......................Message Box................................'''
import tkinter as tk
from tkinter import messagebox as mb

def answer():
    mb.showerror("Answer", "Sorry, no answer available")

def callback():
    if mb.askyesno('Verify', 'Really quit?'):
        mb.showwarning('Yes', 'Not yet implemented')
    else:
        mb.showinfo('No', 'Quit has been cancelled')

tk.Button(text='Quit', command=callback).pack(fill=tk.X)
tk.Button(text='Answer', command=answer).pack(fill=tk.X)
tk.mainloop()











  