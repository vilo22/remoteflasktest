#within this file flask routes control what content is show on what url  
# depending on how the user is accessing the url(methods), what buttons they've pressed, or what they've made, what their permission are, etc
# the general structure of a flask route is afunction with a decorator 
# the decorator adds another function/lines of the code that runs before and/or after the function being decorated 

# our first route: 
#just display 'hello word' on our localhost url (when we run a flask app locally, it will default run on the following url)
    # http://127.0.0.1:500/ something
#in order to set up a route we need a fewe tools 
# 1. we need access to our flask object 
from app import app 
# 2. we need to be able to return an html file from our flask routes
#using render_templates() from the flask package
from flask import render_template, flash


#import request package
import requests as r  

#route decorator
# @<flask object/blueprint name>.route('/url endpoint', <methods>)
# followed by a regular python function 
@app.route('/')
def home():
    #this is a regular python function I can write normal python code here 
    greeting = 'Welcome to flask week foxes!'
    print(greeting)
    students = ['jose', 'yair', 'kristen', 'craig']
    #the return value of this functios is what is displayed on the webpage
    flash(f'This is showing multiple flash messages at once!', category='danger')
    return render_template('index.html', g=greeting, students=students)

@app.route('/about')
def about():
    return render_template('about.html')


from .services import getF1Drivers
from flask_login import login_required
@app.route('/drivers')
@login_required
def f1Drivers():
    # in order to make an API call we need the request package... let's install and import the request package
    context_dict = getF1Drivers()
    
    return render_template('f1.html' , **context_dict)
    