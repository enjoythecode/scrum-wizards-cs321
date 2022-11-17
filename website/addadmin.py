from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

addadmin = Blueprint('addadmin', __name__)

@addadmin.route('/superadmin/addpeak.html', methods= ['POST'])
def add_admin_form_submission():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        id = request.form.get('id')

        # not sure if this should be here
        createuser = request.form.get('createuser')
        permission_id = 1

        print(email, password, firstname, lastname, createuser, id)

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Username already exists.', category='error')
        else:
            # add user to database
            new_user = User(id = id, email = email, permission_id = permission_id, first_name = firstname, last_name = lastname, password=generate_password_hash(password, method='sha256'), team_id = None)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')

            return redirect('/superadmin/home.html')

    # return render_template("signup.html", user=current_user)
