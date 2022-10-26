from flask import Blueprint
from flask import render_template
from flask import send_from_directory, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET'])
@login_required
def home():     
    return render_template("home.html", user=current_user)

@views.route('/superadmin/index.html', methods=['GET'])
@login_required
def super_admin():
        return render_template("superadmin.html")

@views.route('/assets/<path:path>')
def send_asset(path):
        return send_from_directory('assets', path)


