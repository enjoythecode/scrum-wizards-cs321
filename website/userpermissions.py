
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Permission
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from website import views

userpermissions = Blueprint('userpermissions', __name__)

@userpermissions.route('/superadmin/<path>permissions.html', methods= ['POST'])
# @userpermissions.route('/superadmin/<path:coachpermissions.html>', methods= ['POST'])

def user_permissions_form_submission(user, path):

    # changing permissions
    if request.method == 'POST' and request.id == 'changeandsave':

        team = request.form.get('team')
        role = request.form.get('switchrole')

        if path == 'athlete':
            user.Permission = Permission(users = current_user, restricted_to_season = False, can_view_self_entries = True, can_edit_self_entries = False, can_view_own_teams_entries = False, can_edit_own_teams_entries = False, can_view_all_entries = False, can_edit_all_entries = False)
        elif path == 'coach':
                    user.Permission = Permission(users = current_user, restricted_to_season = True, can_view_self_entries = True, can_edit_self_entries = False, can_view_own_teams_entries = True, can_edit_own_teams_entries = False, can_view_all_entries = False, can_edit_all_entries = False)


    # deleting user
    elif request.method == 'POST' and request.id == 'delete':

        user = User.query.get(user.id) # how to know which id to get

        if user:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted!', category='success')

    return redirect("/superadmin/home.html")