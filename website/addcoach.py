from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

addcoach = Blueprint('addcoach', __name__)

@addcoach.route('/superadmin/addcoach.html', methods= ['POST'])
def add_coach_form_submission():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        # below could be wrong because it's a dropdown button
        # also need to make sure team2 and team3 can be emtpy
        team1 = request.form.get('team1')
        team2 = request.form.get('team2')
        team3 = request.form.get('team3')
        


        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', category='error')
#        elif len(username) < 4:
#            flash('Username must be greater than 3 characters.', category='error')
#        elif len(first_name) < 2:
#            flash('First name must be greater than 1 character.', category='error')
#        elif len(password1) < 7:
#            flash('Password must be at least 7 characters.', category='error')
#        elif password1 != password2:
#            flash('Passwords don\'t match.', category='error')
        else:
            # add user to database
            new_user = User(username=username, firstname=firstname, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect("/superadmin/index.html")

    