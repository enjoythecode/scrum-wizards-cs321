from flask import flash
from flask import Blueprint
from flask import render_template
from flask import send_from_directory, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)
auth = Blueprint('auth', __name__)

def mock_database(user_id):
    if user_id == 1:
        return {"user_id": 1, "Name" : "Robert Reyes"}
    if user_id == 2:
        return{"user_id": 2, "Name" : "Casey Brown"}
    if user_id == 3:
        return{"user_id": 3, "Name" : "Jenna Carter"}
    if user_id == 4:
        return{"user_id": 4, "Name" : "Jennifer Smith"}
    

@views.route('/', methods=['GET', 'POST'])
@login_required
def hello(): 
    return redirect(url_for('auth.login'))

# @views.route('/home', methods=['GET'])
# @login_required
# def home():     
#     return render_template("home.html", user=current_user)


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
    users1 = [mock_database(1), mock_database(2), mock_database(3), mock_database(4)]
    images1 = ["/assets/images/faces/face6.jpg",
    "/assets/images/faces/face8.jpg",
    "/assets/images/faces/face9.jpg",
    "/assets/images/faces/face11.jpg"]

    names2 = ["Todd Mckee", "Emily Stephenson", "Keith Freeman", "Jeffrey Abbott"]
    images2 = ["/assets/images/faces/face2.jpg",
    "/assets/images/faces/face3.jpg",
    "/assets/images/faces/face7.jpg",
    "/assets/images/faces/face5.jpg"]

    out_season = ["Lacrosse", "Nordic Ski", "Basketball", "Swimming", "Indoor Track", "Hockey"]

    return render_template("superadmin/home.html", 
    athletes = users1, 
    athlete_images = images1,
    coach_names = names2,
    coach_images = images2,
    teams_out = out_season,
    num_athletes= len(users1),
    num_coaches = len(names2),
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

@views.route('/coach_dashboard')
def send_coach():
    users1 = [mock_database(1), mock_database(2), mock_database(3), mock_database(4)]
    images1 = ["/assets/images/faces/face6.jpg",
    "/assets/images/faces/face8.jpg",
    "/assets/images/faces/face9.jpg",
    "/assets/images/faces/face11.jpg"]

    sleep = [4,-4,4,-4,4,-4,4,-4]
    readyness = [8, -8, 8, -8, 8, -8, 8, -8, 8, -8]
    calorie = [2,2,2,2,2,2,2,2,2,2,2]

    sleep_circle = 80
    readyness_circle = 90
    calorie_circle = 55

    return render_template("coach_dashboard.html", 
    sleep_data = sleep,
    athletes = users1, 
    num_athletes= len(users1),
    athlete_images = images1,
    readyness_data = readyness,
    calorie_data = calorie,
    sleep_circle = sleep_circle, readyness_circle = readyness_circle, calorie_circle = calorie_circle )


@views.route('/team_dashboard')
def send_team():
    # print('reached the method')
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
    return render_template('superadmin/' + path)

@views.route("/superadmin/athletepermissions.html/<int:userid>", methods = ["GET"])
def goto_athlete_permissions(userid):
    user = mock_database(userid)
    return render_template('superadmin/athletepermissions.html', user = user)

@views.route("/superadmin/home.html", methods = ["GET"])
def backto_home():
    return render_template('superadmin/home.html')

@views.route("/superadmin/coachpermissions.html", methods = ["GET"])
def goto_coach_permissions():
    return render_template('superadmin/coachpermissions.html')


@views.route('/admin/index.html', methods=['GET'])
def goto_admin_dash():
    return render_template('admin/index.html')

@views.route('/athlete/index.html', methods=['GET'])
def goto_athlete_dash():
    return render_template('athlete/index.html')

