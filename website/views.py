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
    
@views.route('/superadmin/index.html')
def send_admin():
    names1 = ["Robert Reyes", "Casey Brown", "Jenna Carter", "Jennifer Smith"]
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

    return render_template("superadmin/index.html", 
    athlete_names = names1, 
    athlete_images = images1,
    coach_names = names2,
    coach_images = images2,
    teams_out = out_season,
    num_athletes= len(names1),
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

    return render_template("team_dashboard.html", 
    team_list = Teams, 
    num_teams = len(Teams),
    sleep_data = Sleep, 
    quality_data = Quality, 
    calorie_intake = Calorie, 
    recovery_rate = Recovery, sleep_circle = sleep_circle, readyness_circle=readyness_circle, calorie_circle=calorie_circle)

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

