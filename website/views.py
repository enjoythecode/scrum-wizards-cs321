from flask import flash
from flask import Blueprint
from flask import render_template
from flask import send_from_directory, redirect, url_for
from flask_login import login_required, current_user
from . import helper_db
from random import *
from website import addDummyUserList, readUsersCSV
# from data import *
from . import db
import pandas as pd
import os

views = Blueprint('views', __name__)
auth = Blueprint('auth', __name__)

def getStatus():
    randnum = randrange(1, 11)
    status = "Not Cleared"
    if randnum < 8:
        status = ('Cleared')
    elif randnum < 10:
        status = ('Partially Cleared')

    return status

#creates database with user names and ids
def make_database(user_id):
    name = helper_db.getUserById(user_id).first_name + ' ' + helper_db.getUserById(user_id).last_name
    return {'user_id' : user_id, 'Name':name}

def restructure_user_data(user):
    return {'user_id' : user.id, 'Name':user.first_name + ' ' + user.last_name}


@views.route('/', methods=['GET', 'POST'])
@login_required
def hello():
    return redirect(url_for('auth.login'))

@views.route('/home', methods=['GET'])
@login_required
def home():
    user_per = current_user.permission_id
    if  user_per== 0:
        return redirect("/superadmin/home.html")
    elif  user_per == 1:
        return redirect("/superadmin/home.html")
    elif  user_per == 2:
        return redirect("/team_dashboard")
    else:
        return redirect("/individual_dashboard")

@views.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@views.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)

@views.route('/superadmin/home.html')
def send_admin():
    # need to fix this so it filters the user by permission id
    users = helper_db.getUsers()

    coaches = []
    athletes = []
    admin = []
    for user in users:
        permission_id = user.permission_id

        if permission_id == 3:
            athletes.append(restructure_user_data(user))
        elif permission_id == 2:
            coaches.append(restructure_user_data(user))
        else:
            admin.append(restructure_user_data(user))

    allusers = coaches + athletes + admin

    playerStatus = []
    for i in range(len(allusers)):
        status = getStatus()
        playerStatus.append(status)

    out_season = ["Lacrosse", "Nordic Ski", "Basketball", "Swimming", "Indoor Track", "Hockey"]
    num_ath = len(athletes)
    num_coach = len(coaches)
    num_oteam = len(out_season)

    return render_template("superadmin/home.html",
    athletes = athletes,
    status = playerStatus,
    coach_names = coaches,
    teams_out = out_season,
    num_athletes= num_ath,
    num_coaches = num_coach,
    num_out_teams = num_oteam
    )

@views.route('/individual_dashboard')
def send_individual():
    sleep = [4,-4,4,-4,4,-4,4,-4]
    readyness = [8, -8, 8, -8, 8, -8, 8, -8, 8, -8]
    calorie = [2,2,2,2,2,2,2,2,2,2,2]

    sportsNotes = "Can only take part in 50% of practice and cannot exceed a heart-rate of 120bpm."
    performanceNotes= "Consistent"
    nutritionNotes = "Extra emphasis on vitamin E"

    sleep_circle = 80
    readyness_circle = 90
    calorie_circle = 55

    return render_template("individual_dashboard.html",
    sleep_data = sleep,
    readyness_data = readyness,
    calorie_data = calorie,
    sports = sportsNotes,
    performance = performanceNotes,
    nutrition = nutritionNotes,
    sleep_circle = sleep_circle,
    readyness_circle = readyness_circle,
    calorie_circle = calorie_circle )

@views.route('/athlete')
def send_athlete():
    sleep = [4,-4,4,-4,4,-4,4,-4]
    readyness = [8, -8, 8, -8, 8, -8, 8, -8, 8, -8]
    calorie = [2,2,2,2,2,2,2,2,2,2,2]

    sleep_circle = 80
    readyness_circle = 90
    calorie_circle = 55

    return render_template("athlete.html",
    sleep_data = sleep,
    readyness_data = readyness,
    calorie_data = calorie,
    sleep_circle = sleep_circle,
    readyness_circle = readyness_circle,
    calorie_circle = calorie_circle )



@views.route('/coach_dashboard')
def send_coach():

    users = helper_db.getUsers()


    athletes = []

    for user in users:

        permission_id = user.permission_id

        if permission_id == 3:
            athletes.append(restructure_user_data(user))

    # creating table from csv file
    cwd = os.getcwd() + '/data/tennis_hawkins_anonymized.csv'
    file =  open(cwd)
    dataframe = pd.read_csv(file)
    html_df = dataframe.to_html()

    users1 = athletes
    images1 = ["/assets/images/faces/face6.jpg",
    "/assets/images/faces/face8.jpg",
    "/assets/images/faces/face9.jpg",
    "/assets/images/faces/face11.jpg"]
    playerStatus = ["Cleared", "Not Cleared", "Partially Cleared", "Cleared"]
    sleep = [4,-4,4,-4,4,-4,4,-4]
    readyness = [8, -8, 8, -8, 8, -8, 8, -8, 8, -8]
    calorie = [2,2,2,2,2,2,2,2,2,2,2]

    sleep_circle = 80
    readyness_circle = 90
    calorie_circle = 55

    return render_template("coach_dashboard.html", file = file, html_df = html_df,
    sleep_data = sleep,
    status = playerStatus,
    athletes = users1,
    num_athletes= len(users1),
    athlete_images = images1,
    readyness_data = readyness,
    calorie_data = calorie,
    sleep_circle = sleep_circle,
    readyness_circle = readyness_circle,
    calorie_circle = calorie_circle )


@views.route('/team_dashboard')
def send_team():

    Teams = ["Soccer (M)", "Football (M)", "Track (W) ", "Basketball (W)"]
    Sleep = [4,4,4,4,]
    Quality = [60,80,20,-4,]
    Calorie = [2,2,2,2]
    Recovery = [6,6,6,6]

    sleep_circle = 80
    readyness_circle = 90
    calorie_circle = 55

    return render_template("/team_dashboard.html",
    team_list = Teams,
    num_teams = len(Teams),
    sleep_data = Sleep,
    quality_data = Quality,
    calorie_intake = Calorie,
    recovery_rate = Recovery,
    sleep_circle = sleep_circle,
    readyness_circle=readyness_circle,
    calorie_circle=calorie_circle)

@views.route('/superadmin/<path:path>', methods=["GET"])
def send_superadmin(path):
    if path == '':
        addDummyUserList()
        readUsersCSV("/Users/jasperloverude/Desktop/CS-321/scrum-wizards-cs321/users.csv")
        return send_admin()
    return render_template('superadmin/' + path)

@views.route("/superadmin/athletepermissions.html/<int:userid>", methods = ["GET"])
def goto_athlete_permissions(userid):
    user = make_database(userid)
    return render_template('superadmin/athletepermissions.html', user = user)

@views.route("/superadmin/home.html", methods = ["GET"])
def backto_home():
    return render_template('superadmin/home.html')

@views.route("/superadmin/coachpermissions.html/<int:userid>", methods = ["GET"])
def goto_coach_permissions(userid):
    user = make_database(userid)
    return render_template('superadmin/coachpermissions.html', user = user)

@views.route('/coach_dashboard', methods=['GET'])
def goto_superadmin_teamview():
    return render_template('coach_dashboard')

@views.route('/admin/index.html', methods=['GET'])
def goto_admin_dash():
    return render_template('admin/index.html')

@views.route('/athlete/index.html', methods=['GET'])
def goto_athlete_dash():
    return render_template('athlete/index.html')
