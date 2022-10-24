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
#     if(current_user):
#         return render_template("home.html", user=current_user)
#     else:
#         return "Hi Sinan!"

@views.route('/home', methods=['GET'])
@login_required
def home():     
    return render_template("home.html", user=current_user)

@auth.route('/login', methods=['GET'])
def login():
        return render_template("login.html")

@views.route('/superadmin/index.html', methods=['GET'])
def super_admin():
        return render_template("superadmin.html")

@views.route('/assets/<path:path>')
def send_asset(path):
        return send_from_directory('assets', path)

@views.route('/assets/<path:path>')
def send_admin(path):
        print(path)
        return send_from_directory('assets', path)


