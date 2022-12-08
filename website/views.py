from flask import flash
from flask import Blueprint
from flask import render_template
from flask import send_from_directory, redirect, url_for
from flask_login import login_required, current_user
from . import helper_db
from random import *
# from data import *
from . import db
import pandas as pd
import os

views = Blueprint('views', __name__)
auth = Blueprint('auth', __name__)

def make_database(user_id):

    return {'user_id' : user_id, 'Name':helper_db.getUserById(user_id).first_name + ' ' + helper_db.getUserById(user_id).last_name}


@views.route('/', methods=['GET', 'POST'])
@login_required
def hello():
    return redirect(url_for('auth.login'))

@views.route('/home', methods=['GET'])
@login_required
def home():
    if current_user.permission_id == 0:
        return redirect("/superadmin/home.html")
    elif current_user.permission_id == 1:
        return redirect("/superadmin/home.html")
    elif current_user.permission_id == 2:
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
    ids = []
    for user in users:
        ids.append(user.id)

    allusers = []
    coaches = []
    athletes = []
    admin = []
    for id in ids:
        allusers.append(make_database(id))

        permission_id = helper_db.getUserById(id).permission_id

        if permission_id == 3:
            athletes.append(make_database(id))
        elif permission_id == 2:
            coaches.append(make_database(id))
        else:
            admin.append(make_database(id))

    playerStatus = []
    for i in range(len(allusers)):
        randnum = random()
        if randnum < 0.7:
            playerStatus.append('Cleared')
        elif randnum < 0.9:
            playerStatus.append('Partially Cleared')
        else:
            playerStatus.append('Not Cleared')

    out_season = ["Lacrosse", "Nordic Ski", "Basketball", "Swimming", "Indoor Track", "Hockey"]

    return render_template("superadmin/home.html",
    athletes = athletes,
    status = playerStatus,
    coach_names = coaches,
    teams_out = out_season,
    num_athletes= len(athletes),
    num_coaches = len(coaches),
    num_out_teams = len(out_season)
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
    nutrition = nutritionNotes, sleep_circle = sleep_circle, readyness_circle = readyness_circle, calorie_circle = calorie_circle )

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
    sleep_circle = sleep_circle, readyness_circle = readyness_circle, calorie_circle = calorie_circle )



@views.route('/coach_dashboard')
def send_coach():

    users = helper_db.getUsers()
    ids = []
    for user in users:
        ids.append(user.id)

    athletes = []

    for id in ids:
        # allusers.append(make_database(id))

        permission_id = helper_db.getUserById(id).permission_id

        if permission_id == 3:
            athletes.append(make_database(id))

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
    sleep_circle = sleep_circle, readyness_circle = readyness_circle, calorie_circle = calorie_circle )


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
    recovery_rate = Recovery, sleep_circle = sleep_circle, readyness_circle=readyness_circle, calorie_circle=calorie_circle)

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

def readUsersCSV(filepath):

    import csv
    from .models import User, Entry, Team

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Create a new user object
            user = User(email=row[0], first_name=row[1], last_name=row[2], password=row[3], permission_id=row[4])
            # Add the new User to the database
            db.session.add(user)
        # Commit all the changes
        db.session.commit()
        print('Read User CSV files and added to the database')

# Adding 100 random users to the database
def addDummyUserList():
    ''' Adds 100 random users to the database.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    from .models import User
    from random import randint
    from faker import Faker
    fake = Faker()

    for i in range(100):
        fakeUser = User(email = fake.email(), password = generate_password_hash("password", method='sha256'), first_name = fake.first_name(), last_name = fake.last_name(), permission_id = randint(1, 3))
        db.session.add(fakeUser)
        dummyEmailList.append(fakeUser.email)
    db.session.commit()
    print("100 Users added")