
from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User, Permission, Team
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@views.route('/<generic>', methods=['GET', 'POST'])
@login_required
def generic(): 
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    ''' Handles login logic on /login path:
    ---------------------------------------
    Returns: 
    ---------------------------------------
        Response object.
    '''

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect') 
        else:
            flash( "User does not exist")


    return render_template("login.html")

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    ''' Logs user out:
    ---------------------------------------
    Returns: 
    ---------------------------------------
        Response object.
    '''
    logout_user()
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
    db.session.commit()
    
    