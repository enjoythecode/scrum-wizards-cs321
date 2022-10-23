from flask import Blueprint
from flask import render_template
from flask import send_from_directory

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def hello():
    return "Hi Ghailan!"

@views.route('/login', methods=['GET'])
def login():
    return render_template("index.html")

@views.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)

@views.route('/superadmin/index.html')
def send_admin():
    return render_template("superadmin/index.html")

@views.route('/individual_dashboard')
def send_individual():
    sleep = [4,-4,4,-4,4,-4,4,-4]
    readyness = [8, -8, 8, -8, 8, -8, 8, -8, 8, -8]
    calorie = [2,2,2,2,2,2,2,2,2,2,2]

    return render_template("individual_dashboard.html", sleep_data = sleep, readyness_data = readyness, calorie_data = calorie)

@views.route('/team_dashboard')
def send_team():
    Teams = ["soccer", "footabll", "track", "basketabll"]
    Sleep = [4,-4,4,-4,]
    Quality = [60,80,20,-4,]
    Calorie = [2,2,2,2]
    Recovery = [6,6,6,6]

    return render_template("team_dashboard.html", team_list = Teams, sleep_data = Sleep, quality_data = Quality, calorie_intake = Calorie, recovery_rate = Recovery)