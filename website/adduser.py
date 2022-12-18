from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

addcoach = Blueprint('addcoach', __name__)

@addcoach.route('/superadmin/<path:addcoach.html>', methods= ['POST'])
@addcoach.route('/superadmin/<path:addpeak.html>', methods= ['POST'])
@addcoach.route('/superadmin/<path:addathlete.html>', methods= ['POST'])
def add_user_form_submission(path):

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
            if path == 'addcoach.html':
                new_user = User(first_name = firstname, last_name = lastname, email = email, password = generate_password_hash(password, method='sha256'), permission_id=2)
            elif path == 'addathlete.html':
                new_user = User(first_name = firstname, last_name = lastname, email = email, password = generate_password_hash(password, method='sha256'), permission_id=3)
            elif path == 'addpeak.html':
                new_user = User(first_name = firstname, last_name = lastname, email = email, password = generate_password_hash(password, method='sha256'), permission_id=0)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/superadmin/home.html')
