
from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User, Permission, Team, Entry
from flask_login import login_required, current_user, login_user, logout_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if password == user.password:
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                return "password is incorrect"
        else:
            return "User does not exist"

    return render_template("login.html")


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # user password code from Moodle, this one is quick
        if password1 == password2 and len(email) > 6:
            user = User.query.filter_by(email=email).first()

            if user:
                return "User already exists"
            else: 
                new_user = User(email=email, password=password1)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('views.home'))

    return render_template("signup.html")