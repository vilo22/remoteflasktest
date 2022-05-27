# just for user auth

# our aouth blueprint is designed to be a subsection w

from .authforms import LoginForm, RegistrationForm
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user


auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')
#                                                  ^^this looks for the closer
#                                                  templates folder no matter the name

# import our Forms(s)


# dreate our first route within the blueprint
# very similar to our main routes - the only difference is it will belong to the app blueprint rather than the app
# our INIT file don't have idea of this folder, there is nothing to connected to this blueprint
# every time you create a new file, routing or bp you have to go back to the init file
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # happens regardless of method-> we watn access to the Login form on both GET and POST
    lform = LoginForm()
    # everything in this conditional only happens on POST request (aka form submission)
    if request.method == 'POST':
        if lform.validate_on_submit():
            username = lform.username.data
            password = lform.password.data
            print('formdata:', username, password)
            #query our db for a user with that username
            user = User.query.filter_by(username=lform.username.data).first()
            # if the user exists and their password matches, log them in 
            if user and check_password_hash(user.password, lform.password.data):
                # use our login manager!
                login_user(user)
                print(current_user.__dict__)
                flash(f'Success - you have been signed in, {user.username}.', category='success')
                return redirect(url_for('home'))


        flash(f'Incorrect username or password, please try again.', 'danger')
        return redirect(url_for('auth.login'))
    return render_template('signin.html', form=lform)

# a second auth route - registration 
# accepts GET and POST requests 
    # GET - shows the user our registration page (complete with forms)
    # POST - the user has submitted the form
        # I want to check if their form submission is valid 
        # Then check to make sure their registration information matches what I want (Unique email? unique username? valid password?)
            # If everything checks out, register them, log them in, and redirect them to the home page
            # If there is a problem with the registration, redirect them back to the registration page abd provide feedback
@auth.route('/register', methods=['GET' , 'POST'])
def register():
    #utilize our form for both get and post 
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
        #access form data and use it to create a new user object
            print('formdata:', form.data) # all data as a dict
            newuser = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data)
            print('newly created user  obejct:', newuser)
            try:
                #check db to see if this username or email already exists (use try/except)
                db.session.add(newuser)
                db.session.commit()
            except:
                flash("Username or email already registered! Please try a different one.", category= 'danger')
                return redirect(url_for('auth.register'))

            login_user(User.query.filter_by(email=newuser.email).first)
            flash(f'Welcome! thank you for regsitering, {newuser.username}!', 'info')
            return redirect(url_for('home'))
        else: #something went wrong with registration
            flash('Sorry, that username or email us taken. Please try again.', 'danger')
            return redirect(url_for('auth.register')) 
    # GET -> create form instance, then rendering the html the html template with that form
    else: #if the request method == GET
        return render_template('register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been signed out', 'info')
    return redirect(url_for('auth.login'))