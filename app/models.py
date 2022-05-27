#this file is responsible for everything database 
# Primarily the instantitiation of our orm 

import email
from email.policy import default
import weakref
from click import password_option
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# setup login manager
from flask_login import LoginManager, UserMixin
#create the instance of our login manager
login = LoginManager()

# tell our login manager how it can access a user object from a user_id 
@login.user_loader
def load_user(userid):
    return User.query.get(userid)

#tools for our models
from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

class Animal (db.Model):
    # Global attributes for each column in the database 
    id = db.Column(db.Integer, primary_key=True) #we need to provide at least a datatype (we can also provide default values and/or constraints)
    name = db.Column(db.String(50), nullable = False)
    latin = db.Column(db.String(255), default = None) 
    created = db.Column(db.DateTime, default = datetime.utcnow())
    cool = db.Column(db.Boolean, default=True)
    #everytime you change your models you are changing your tables 

#create our user model

class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)


