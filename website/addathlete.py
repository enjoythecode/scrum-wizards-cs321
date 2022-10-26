from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

addathlete = Blueprint('addathlete', __name__)

@addathlete.route('/superadmin/addathlete.html', methods= ['POST'])
def add_athlete_form_submission():

    if request.method == 'POST':
        # left hand side
        email = request.form.get('email')
        user,password = request.form.get('password')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        id = request.form.get('id')
        createuser = request.form.get('createuser')
        role = 'coach'
        permission = 0
        # below could be wrong since it's a dropdown menu
        # also need to make sure team2 and team3 can be emtpy
        team1 = request.form.get('team1')
        team2 = request.form.get('team2')
        team3 = request.form.get('team3')
        print(email, password, firstname, createuser, lastname, id, team1, team2, team3)

        # # coming up with teamid
        # team_ids = []
        # for team in [team1, team2, team3]:
        #     if team is not None:
        #         team_ids.append(team.team_id())
        # return team_ids
                


        user = User.query.filter_by(email=email).first()
        if user:
            flash('Username already exists.', category='error')
        else:
            # add user to database
            new_user = User(id = id, email = email, first_name = firstname, last_name = lastname, permission = permission, password=generate_password_hash(password, method='sha256'), role = role)
            # new_user = User(id = id, email = email, first_name = firstname, last_name = lastname, password=generate_password_hash(password, method='sha256'), team_id = team_ids, permissions_id = permissions, entries = entries)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')

            
            # userlist = []
            # for user in User.query.all():
            #     if user.role == 'athlete':
            #         userlist.append(user)
            # return render_template("/superadmin/home.html", athletelist = userlist)


            return redirect('/superadmin/home.html')

    # return redirect("/superadmin/home.html")