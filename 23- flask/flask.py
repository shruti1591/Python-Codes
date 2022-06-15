# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:21:24 2021

@author: SYSTEMS
"""

'''Flask is a web application framework written in Python. 
Armin Ronacher, who leads an international group of Python
 enthusiasts named Pocco, develops it. Flask is based on 
 Werkzeug WSGI toolkit and Jinja2 template engine. 
 Both are Pocco projects.'''
 
'''WSGI
Web Server Gateway Interface (WSGI) has been adopted as
 a standard for Python web application development. 
 WSGI is a specification for a universal interface 
 between the web server and the web applications.

Werkzeug
It is a WSGI toolkit, which implements requests, 
response objects, and other utility functions. 
This enables building a web framework on top of it. 
The Flask framework uses Werkzeug as one of its bases.

Jinja2
Jinja2 is a popular templating engine for Python. 
A web templating system combines a template with 
a certain data source to render dynamic web pages.'''


'''Install virtualenv for development environment
virtualenv is a virtual Python environment builder. 
It helps a user to create multiple Python environments
 side-by-side. Thereby, it can avoid compatibility
 issues between the different versions of the libraries.

The following command installs virtualenv

pip install virtualenv

Once installed, new virtual environment 
is created in a folder.

mkdir newproj
cd newproj
virtualenv venv

On Windows, following can be used

venv\scripts\activate

We are now ready to install 
Flask in this environment.

pip install Flask'''


#test Flask installation 

from flask import *    
app = Flask(__name__)   # Flask constructor
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/')    #app.route(rule, options)    
def hello():
    return 'HELLO'
  
if __name__=='__main__':
   app.run()   #app.run(host, port, debug, options)
#Try URL http://127.0.0.1:5000/   



#Routing
from flask import Flask    
app = Flask(__name__)      
   
@app.route('/hello')
def hello_world():
   return 'hello world'

if __name__=='__main__':
   app.run()
#Try URL http://127.0.0.1:5000/hello  
   
   
#Variable rules  
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run()
##Try URL http://127.0.0.1:5000/hello/abc
   
   
   
#In addition to the default string variable part, 
#rules can be constructed using int, float and path −   
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()
#Try URL http://127.0.0.1:5000/blog/34  
#Try URL http://127.0.0.1:5000/rev/1.1     
   


from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()
#Try URL http://127.0.0.1:5000/flask   
   
   
   
   
#URL Building
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run()
#Try http://127.0.0.1:5000/admin   
#Try http://127.0.0.1:5000/guest/abc
#Try http://127.0.0.1:5000/user/abc




#HTTP Methods
'''1	GET
Sends data in unencrypted form to the server.
 Most common method.
2	HEAD
Same as GET, but without response body
3	POST
Used to send HTML form data to server. 
Data received by POST method is not 
cached by server.
4	PUT
Replaces all current representations of the 
target resource with the uploaded content.
5	DELETE
Removes all current representations of the
 target resource given by a URL'''

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
 return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
 if request.method == 'POST':
     user = request.form['nm']
     return redirect(url_for('success',name = user))
 else:
     user = request.args.get('nm')
     return redirect(url_for('success',name = user))

if __name__ == '__main__':
      app.run()





