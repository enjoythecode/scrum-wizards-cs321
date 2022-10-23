from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

addathlete = Blueprint('addathlete', __name__)

@addathlete.route('/superadmin/addathlete.html', methods= ['POST'])
def add_athlete_form_submission():

    if request.method == 'POST':
        # left hand side
        username = request.form.get('username')
        password = request.form.get('password')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        # below could be wrong since it's a dropdown menu
        # also need to make sure team2 and team3 can be emtpy
        team1 = request.form.get('team1')
        team2 = request.form.get('team2')
        team3 = request.form.get('team3')
        print(username, password, firstname, lastname)
        
        
        # right hand side
        age = request.form.get('age')
        weight = request.form.get('weight')
        height = request.form.get('height')
        gender = request.form.get('gender')
        gradyear = request.form.get('gradyear')
        print(age, weight, height, gender, gradyear)


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

    # return render_template("signup.html", user=current_user)