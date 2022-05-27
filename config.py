import os 

#set up the base firectory of the entire application - aka help our computer understand this app's file structure
basedir = os.path.abspath(os.path.dirname(__name__))

#set up a class for our configuration 

class Config:
    '''
    setting configuration variables that tell our flask app how to run 
    '''

    #all three of these values should not be public information - we should keep these values hidden
        #their actual value will exist in the .env file
        #their value here will just bea function call to access that value in the .env file
    FLASK_APP = os.environ.get('FLASK_APP') #Go get the FLASK_APP variable value from the .env file
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False