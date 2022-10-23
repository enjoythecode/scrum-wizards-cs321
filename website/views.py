from flask import Blueprint
from flask import render_template
from flask import send_from_directory

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def hello():
    return "Hi Sinan!"

@views.route('/login', methods=['GET'])
def login():
    return render_template("index.html")

@views.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)

@views.route('/superadmin/index.html')
def send_admin():
    return render_template("superadmin/index.html")
@views.route('/login', methods=['GET'])
def login():
    return render_template('index.html')

@views.route('/superadmin/index.html', methods=['GET'])
def goto_superadmin_dash():
    return render_template('superadmin/index.html')

@views.route('/admin/index.html', methods=['GET'])
def goto_admin_dash():
    return render_template('admin/index.html')

@views.route('/athlete/index.html', methods=['GET'])
def goto_athlete_dash():
    return render_template('athlete/index.html')






