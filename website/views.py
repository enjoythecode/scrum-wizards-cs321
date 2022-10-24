from flask import Blueprint
from flask import render_template
from flask import send_from_directory, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)
auth = Blueprint('auth', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def hello(): 
    return redirect(url_for('auth.login'))

@views.route('/home', methods=['GET'])
@login_required
def home():     
    return render_template("home.html", user=current_user)


@views.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@views.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)

@views.route('/superadmin/<path:path>', methods=["GET"])
def send_superadmin(path):
    return send_from_directory('templates/superadmin', path)

@views.route("/superadmin/athletepermissions.html", methods = ["GET"])
def goto_athlete_permissions():
    return render_template('superadmin/athletepermissions.html')

@views.route("/superadmin/permissions.html", methods = ["GET"])
def backto_home():
    return render_template('superadmin/index.html')

@views.route("/superadmin/coachpermissions.html", methods = ["GET"])
def goto_coach_permissions():
    return render_template('superadmin/coachpermissions.html')


@views.route('/admin/index.html', methods=['GET'])
def goto_admin_dash():
    return render_template('admin/index.html')

@views.route('/athlete/index.html', methods=['GET'])
def goto_athlete_dash():
    return render_template('athlete/index.html')






