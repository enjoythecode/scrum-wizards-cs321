
# Importing the Blueprint, render_template, request, redirect, url_for, flash modules from flask
from flask import Blueprint, render_template, request, redirect, url_for, flash
# Importing the database from the __init__.py file
from . import db
# Importing the User, Permission, Team models
from .models import User, Permission, Team
# Importing the login_required, current_user, login_user, logout_user modules from flask_login
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
# Importing the generate_password_hash, check_password_hash modules
from werkzeug.security import generate_password_hash, check_password_hash

# Creating a Blueprint object called auth
auth = Blueprint('auth', __name__)

# Creating a route for the login page
@auth.route("/", defaults={"path": ""})
@auth.route("/<string:path>")
@auth.route("/<path:path>")

@login_required
def generic():
    # Redirects root path to /login page:
    return redirect(url_for('auth.login'))

# Creating a route for the login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    ''' Handles login logic on /login path:
    ---------------------------------------
    Returns:
    ---------------------------------------
        Response object.
    '''

    # If the user is already logged in, redirect to the home page
    if request.method == 'POST':
        # Get the email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists
        user = User.query.filter_by(email=email).first()
        # If the user exists, check the password
        if user:
            # If the password is correct, redirect to the home page
            if check_password_hash(user.password, password):
                # Log the user in
                login_user(user, remember=True)
                # Redirect to the home page
                return redirect(url_for('views.home'))
            else:
                # If the password is incorrect, redirect to the login page
                flash('Password is incorrect')
        else:
            # If the user does not exist, redirect to the login page
            flash( "User does not exist")

    # Render the login page
    return render_template("login.html")


# @auth.route('/', methods=['GET'])
# def home():
#     ''' Redirects root path to /login page:
#     ---------------------------------------
#     Returns:
#     ---------------------------------------
#         Response object.
#     '''
#     return redirect(url_for('auth.login'))

# Creating a route for the logout page
@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    ''' Logs user out:
    ---------------------------------------
    Returns:
    ---------------------------------------
        Response object.
    '''

    # Log the user out
    logout_user()
    # Redirect to the login page
    return redirect(url_for('auth.login'))


def signup_user(id, email, first_name, last_name, password, permissions_id):
    ''' Helper function to add user to database. All new users created MUST route through this function.
    Parameters:
    ---------------------------------------
    email: string.
    password:  string.
    first_name: string.
    last_name: string.
    password: string.
    permissions_id: string.

    Returns:
    ---------------------------------------
        void
    '''

    # add user to database
    new_user = User(id = id, email=email, first_name=first_name, password=generate_password_hash(password1), method='sha256', permissions_id=permissions_id)
    db.session.add(new_user)
    # commit changes to database
    db.session.commit()
