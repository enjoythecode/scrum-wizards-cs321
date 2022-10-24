
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from website import views

athletepermissions = Blueprint('athletepermissions', __name__)

@athletepermissions.route('/superadmin/athletepermissions.html', methods= ['POST'])
def athlete_permissions_form_submission(id):

    if request.method == 'POST':

        deleteaccount = request.form.get('deleteaccount')
        team = request.form.get('team')
        switchrole = request.form.get('switchrole')
        print(deleteaccount, team, switchrole)



        user = User.query.get(id)
        user.team = team
        user.role = switchrole

        if deleteaccount:
            remove(id)
        
        return redirect("/superadmin/index.html")



        

# deleting a user 
@athletepermissions.route("/remove/<string:id>", methods=['GET', "POST"])
@login_required
def remove(id):
    user = User.query.get(id)
    
    if user:
        if user.user_id == current_user.id:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted!', category='success')

    return redirect("/superadmin/index.html")

