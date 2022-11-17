
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Permission
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from website import views

coachpermissions = Blueprint('coachpermissions', __name__)

@coachpermissions.route('/superadmin/coachpermissions.html', methods= ['POST'])
def coach_permissions_form_submission():

    if request.method == 'POST':

        deleteaccount = request.form.get('deleteaccount')
        team = request.form.get('team')
        role = request.form.get('role')
        save = request.form.get('save')
        print(deleteaccount, team, role)

        # permissions
        view_teams_entries = request.form.get('viewteamsentries')
        edit_teams_entries = request.form.get('editteamsentries')
        view_team_outofseason = request.form.get('outofseason')



        current_user.permissions = Permission(users = current_user, restricted_to_season = True, can_view_self_entries = True, can_edit_self_entries = True, can_view_own_teams_entries = True, can_edit_own_teams_entries = False, can_view_all_entries = False, can_edit_all_entries = False)

        # user = User.query.get(id)
        # user.team = team
        # user.role = switchrole

        # if deleteaccount:
        #     remove(id)

        return redirect("/superadmin/home.html")





# deleting a user
@coachpermissions.route("/remove/<string:id>", methods=['GET', "POST"])
@login_required
def remove(id):
    user = User.query.get(id)

    if user:
        if user.user_id == current_user.id:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted!', category='success')

    return redirect("/superadmin/home.html")
