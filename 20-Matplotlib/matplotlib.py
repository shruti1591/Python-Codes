# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:28:45 2021

@author: SYSTEMS
"""


'''Matplotlib is one of the most popular Python
 packages used for data visualization. 
It is a cross-platform library for making 2D plots
 from data in arrays. Matplotlib is written 
in Python and makes use of NumPy, the numerical 
mathematics extension of Python. It provides an
 object-oriented API that helps in embedding plots
 in applications using Python GUI toolkits such
 as PyQt, WxPythonotTkinter.
 It can be used in Python and IPython shells,
 Jupyter notebook and web application servers also.'''


from matplotlib import pyplot as plt
#Plotting to our canvas
plt.plot((1,2,3),(4,5,1))
#Showing what we plotted
plt.show()


#display a simple line plot of angle in radians 
#vs. its sine value in Matplotlib
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()

from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #[left, bottom, width, height]
ax.plot(x,y)
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()

import matplotlib.pyplot as plt
y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
fig = plt.figure()
ax = fig.add_axes([0,0,0.5,1])   #[left, bottom, width, height]
ax1 = fig.add_axes([0.5,0,1,1])
l1 = ax.plot(x1,y,'ys-') # solid line with yellow colour and square marker
l2 = ax1.plot(x2,y,'go--') # dash line with green colour and circle marker
ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()

import matplotlib.pyplot as plt
y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]

l1 = plt.plot(x1,y,'ys-') # solid line with yellow colour and square marker
l2 = plt.plot(x2,y,'go--') # dash line with green colour and circle marker
plt.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
plt.set_title("Advertisement effect on sales")
plt.set_xlabel('medium')
plt.set_ylabel('sales')
plt.show()








from matplotlib import pyplot as plt
x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

#grid

from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='line one', linewidth=1)
plt.plot(x2,y2,'c',label='line two',linewidth=1)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
#plt.grid(True,color='k')
plt.grid(color='b', ls = '-.', lw = 5)
plt.show()



#Python Matplotlib: Bar Graph

from matplotlib import pyplot as plt
 
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi",color='c',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()


#Python Matplotlib – Histogram

import matplotlib.pyplot as plt
population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='step', rwidth=0.8) #try step, barstacked,stepfilled
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()


#Python Matplotlib : Scatter Plot

import matplotlib.pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='high income low saving',color='r')
plt.scatter(x1,y1,label='low income high savings',color='b')
plt.xlabel('saving*100')
plt.ylabel('income*1000')
plt.title('Scatter Plot')
plt.legend()
plt.show()


#Python Matplotlib : Area Plot
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
  
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
  
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()


#Python Matplotlib : Pie Chart
import matplotlib.pyplot as plt
 
#days = [1,2,3,4,5]
 
#sleeping =[7,8,6,11,7]
#eating = [2,3,4,3,2]
#working =[7,8,7,2,2]
#playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= False,
  explode=(0,0.2,0.2,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()

#Python Matplotlib : Working With Multiple Plots
import numpy as np
import matplotlib.pyplot as plt
 
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.subplot(221)  #nrows, ncols, index
plt.plot(t1, f(t1), 'bo', t2, f(t2))
plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()



import matplotlib.pyplot as plt
fig,a =  plt.subplots(2,2) #The function returns a figure object and a tuple containing axes objects equal to nrows*ncols.
import numpy as np
x = np.arange(1,5)
a[0][0].plot(x,x*x)
a[0][0].set_title('square')
a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('square root')
a[1][0].plot(x,np.exp(x))
a[1][0].set_title('exp')
a[1][1].plot(x,np.log10(x))
a[1][1].set_title('log')
plt.show()


