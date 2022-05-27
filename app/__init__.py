#from the flask package import the FLASK object/class

from flask import Flask
#from the config file import the config class that we created
from config import Config

#import bp for registration
from .auth.routes import auth


# Don't import things that you don't need
#define /instantiate our flask app... aka create the actual object that will be our flask app
app = Flask(__name__)

# tell this app how it is going to be configured 
app.config.from_object(Config)
# aka configuring our flask app based on the config class we made in the config.py file

#create the link of communication between blueprints and app
# aka register our bp 

app.register_blueprint(auth)
#this line is what conects the bp and the init 

#imports for database stuff
from .models import db, login 
from flask_migrate import Migrate

# set up ORM Migrate Communication with app and eachother
db.init_app(app) #if this isnt here our app and our database don't know how to talk to each other 
migrate = Migrate(app, db)# this is giving us the ability to modify the data structure from ourflask app (aka create tables,etc)

# set up for LoginManager
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to see this page mtfkr'
login.login_message_category = 'danger'


# our flask app is really dumb. if we do not tell it about the existance of other files, it will assume they do not exist
# import the routes file here so that our flask app knows the routes exist
# this is one of the only scenarios where imports will be at the bottom of a file
    #these import MUST be after instantiation of the falsk app (line 11) an the configuration (line 14)
from . import routes #from the app folder (this folder), import the entire routes file
