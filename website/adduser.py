from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

adduser = Blueprint('adduser', __name__)

@adduser.route('/superadmin/add<user>.html', methods= ['POST'])
# @adduser.route('/superadmin/addpeak.html', methods= ['POST'])
# @adduser.route('/superadmin/addathlete.html', methods= ['POST'])
def add_user_form_submission(user):

    if request.method == 'POST':

        email = request.form.get('username')
        password = request.form.get('password')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        id = request.form.get('id')
        createuser = request.form.get('createuser')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists.', category='error')
        else:
            if user == 'coach':
                new_user = User(first_name = firstname, last_name = lastname, email = email, password = generate_password_hash(password, method='sha256'), permission_id=2)
            elif user == 'athlete':
                new_user = User(first_name = firstname, last_name = lastname, email = email, password = generate_password_hash(password, method='sha256'), permission_id=3)
            elif user == 'peak':
                new_user = User(first_name = firstname, last_name = lastname, email = email, password = generate_password_hash(password, method='sha256'), permission_id=0)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/superadmin/home.html')
