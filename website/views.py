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


