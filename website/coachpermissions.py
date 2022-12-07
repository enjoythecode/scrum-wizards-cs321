
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Permission
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from website import views

coachpermissions = Blueprint('coachpermissions', __name__)

@coachpermissions.route('/superadmin/coachpermissions.html', methods= ['POST'])
def coach_permissions_form_submission(user):

    # changing permissions
    if request.method == 'POST' and request.id == 'changeandsave':

        team = request.form.get('team')
        role = request.form.get('switchrole')
        print(team, role)

        # these permissiosn could be wrong
        user.Permission = Permission(users = current_user, restricted_to_season = True, can_view_self_entries = True, can_edit_self_entries = False, can_view_own_teams_entries = True, can_edit_own_teams_entries = False, can_view_all_entries = False, can_edit_all_entries = False)

    # deleting user
    elif request.method == 'POST' and request.id == 'delete':

        user = User.query.get(user.id) # how to know which id to get

        if user:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted!', category='success')

    return redirect("/superadmin/home.html")





# # deleting a user
# @coachpermissions.route("/remove/<string:id>", methods=['GET', "POST"])
# @login_required
# def remove(id):
#     user = User.query.get(id)

#     if user:
#         if user.user_id == current_user.id:
#             db.session.delete(user)
#             db.session.commit()
#             flash('User deleted!', category='success')

#     return redirect("/superadmin/home.html")
