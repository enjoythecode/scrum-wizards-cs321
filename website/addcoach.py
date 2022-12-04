from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import auth

addcoach = Blueprint('addcoach', __name__)

@addcoach.route('/superadmin/addcoach.html', methods= ['POST'])
def add_coach_form_submission():

    if request.method == 'POST':

        email = request.form.get('username')
        password = request.form.get('password')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        id = request.form.get('id')

        # not sure if this is right
        createuser = request.form.get('createuser')
        permission_id = 1
        # below could be wrong because it's a dropdown button
        team1 = request.form.get('team1')
        team2 = request.form.get('team2')
        team3 = request.form.get('team3')
        print(email, password, firstname, lastname, createuser, id, permission_id)
        print(team1, team2, team3)
        # need to find a way to convert teams to team_ids

        # new_user = User(id = id, email=email, first_name=firstname, last_name = lastname, password=generate_password_hash(password), permission_id = 1)
        # db.session.add(new_user)
        # print('new user added')
        # db.session.commit()
        # return redirect('/superadmin/home.html')
        


        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists.', category='error')
        else:
            # auth.signup_user(id, email, firstname, lastname, password, permission_id)
            new_user = User(id = id, email=email, first_name=firstname, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return redirect('/superadmin/home.html')

    