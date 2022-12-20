# Importing flask and flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Importing path and remove from os
from os import path, remove
# Importing the LoginManager from flask_login
from flask_login import LoginManager
# Importing generate_password_hash and check_password_hash from werkzeug.security
from werkzeug.security import generate_password_hash, check_password_hash

# Creating a database
db = SQLAlchemy()
DB_NAME = "database.db"
# Creating a list of dummy emails
dummyEmailList = []

def create_test_app():
    '''
    Function to create a test application
    '''

    # Importing the models from the website package
    from .models import User, Team, Entry, Permission

    # Creating a test application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    db.init_app(app)

    # Creating a test database
    create_test_database(app)

    # Importing all blueprints for routing urls to .html files
    from .views import views
    from .auth import auth
    from .api import api
    # Registering all blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Creating a login manager
    login_manager = LoginManager()
    # Setting the login view to the login page
    login_manager.login_view = 'auth.login'
    # Initializing the login manager
    login_manager.init_app(app)

    # Creating a user loader
    @login_manager.user_loader
    def load_user(id):
        # Returning the user with the given id
        return User.query.get(int(id))

    return app

def create_app():
    ''' Initalizes the flask application and creates a database.db file if it does not currently exist.
    ---------------------------------------
    Returns:
    ---------------------------------------
    Flask app.
        Initialized flask app object.
    '''

    # Creating a flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '03745fbcd1b452edcd98a9acb4a0f90d'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Imports all blueprints for routing urls to .html files
    from .views import views
    from .auth import auth
    from .api import api
    from .addcoach import addcoach
    from .addathlete import addathlete
    from .addadmin import addadmin
    from .adduser import adduser
    from .athletepermissions import athletepermissions
    from .coachpermissions import coachpermissions
    from .userpermissions import userpermissions
    from .hawkins import hawkins

    # Registers all blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(addcoach, url_prefix='/')
    app.register_blueprint(addadmin, url_prefix='/')
    app.register_blueprint(addathlete, url_prefix='/')
    app.register_blueprint(adduser, url_prefix='/')
    app.register_blueprint(athletepermissions, url_prefix='/')
    app.register_blueprint(coachpermissions, url_prefix='/')
    app.register_blueprint(userpermissions, url_prefix='/')
    app.register_blueprint(hawkins, url_prefix='/')

    # Creates database if it does not exist
    with app.app_context():
        if path.exists('instance/' + DB_NAME):
            # # delete the database if it exists
            remove("instance/" + DB_NAME)

        db.create_all()
        print('Created Database!')
        # Adds dummy data to database
        addDummyDB()



    # Creates database
    from .models import User
    create_database(app)

    # Initializes login_manager, sets login view, and initializes login manager to the app
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Creates a user loader
    @login_manager.user_loader
    def load_user(id):
        # Returns the user with the given id
        return User.query.get(int(id))

    return app


def create_database(app):
    ''' If database.db does not exist, creates the file, and populates it with data
    Parameters:
    ---------------------------------------
    app: Flask(). Flask application object.

    Returns:
    ---------------------------------------
        void
    '''

    with app.app_context():
        # Creates database if it does not exist
        if not path.exists('instance/' + DB_NAME):
            print("Creating new database...")
            db.create_all()
            # hydrates database (populates it with objects)
            print("Hydrating database...")
            addDummyDB()
            print("Database hydration complete!")
        else:
            print("Existing database detected!")
    # Importing the writeUsersCSV function
    from .writecsv import writeUsersCSV
    # writing dummy users to csv file
    writeUsersCSV()

def create_test_database(app):
    ''' If database.db does not exist, creates the file, and populates it with data
    Parameters:
    ---------------------------------------
    app: Flask(). Flask application object.

    Returns:
    ---------------------------------------
        void
    '''

    with app.app_context():
        # Creates database if it does not exist
        if path.exists('instance/' + DB_NAME):
            remove("instance/" + DB_NAME)

        print("Creating new database...")
        db.create_all()

def addDummyDB():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    # Adding dummy data to database
    addDummyTeams()
    addPermissionList()
    addDummyUser()
    addDummyEntriesList()
    addDummyUserList()
    # Reading user csv file and populating database
    # readUsersCSV('users.csv')


def createCSVFiles():
    '''Creates csv files for all tables in the database'''

    # Importing the writeUsersCSV function
    from .writecsv import writeUsersCSV
    # writing dummy users to csv file
    writeUsersCSV()

def readUsersCSV(filepath):
    ''' Reads a csv file and adds the data to the database'''

    # Importing the csv module
    import csv
    # Importing the User, Entry, and Team models
    from .models import User, Entry, Team

    # Opening the csv file
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        # Iterating through each row in the csv file
        for row in reader:
            # Create a new user object
            user = User(email=row[0], first_name=row[1], last_name=row[2], password=row[3], permission_id=row[4])
            # Add the new User to the database
            db.session.add(user)
        # Commit all the changes
        db.session.commit()
        print('Read User CSV files and added to the database')

def addDummyTeams():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    # Importing the Team model
    from .models import Team
    # Importing the faker module
    from faker import Faker
    # Importing the datetime module
    import datetime
    # Creating a faker object
    fake = Faker()

    # Adding dummy team data to database
    db.session.add(Team(name = "Men's Alpine Skiing", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Baseball", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Basketball", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Crew", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Cross Country", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Football", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Golf", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Ice Hockey", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Lacrosse", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Nordic Skiing", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Soccer", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Squash", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Swimming & Diving", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Tennis", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Men's Track & Field", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Alpine Skiing", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Basketball", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Crew", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Cross Country", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Field Hockey", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Ice Hockey", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Lacrosse", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Nordic Skiing", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Soccer", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Softball", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Squash", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Swimming & Diving", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Tennis", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Track & Field", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))
    db.session.add(Team(name = "Women's Volleyball", season_start_date = datetime.datetime(2022, 11, 1), season_end_date = datetime.datetime(2023, 3, 1)))

    db.session.commit()
    print("All Teams added")

def addDummyUserList():
    ''' Adds 100 random users to the database.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    # Importing the User model here to avoid circular import
    from .models import User
    # Importing the faker library to generate random data
    from random import randint
    # Importing the faker library to generate random data
    from faker import Faker
    # Creating an instance of the faker library
    fake = Faker()

    # Creating 100 random users
    for i in range(100):
        # Creating a random user
        fakeUser = User(email = fake.email(), password = generate_password_hash("password", method='sha256'), first_name = fake.first_name(), last_name = fake.last_name(), permission_id = randint(1, 3))
        # Adding the user to the database
        db.session.add(fakeUser)
        # Adding the user's email to the dummyEmailList
        dummyEmailList.append(fakeUser.email)
    db.session.commit()
    print("100 Users added")

def addDummyUser():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    # Importing the User model here to avoid circular import
    from .models import User, Team
    # Querying the database for the teams
    team1 = Team.query.filter_by(name = "Basketball").first()
    team2 = Team.query.filter_by(name = "Football").first()

    # Creating the users for each role and adding them to the database
    chandra = User(first_name = "Chandra", last_name = "Gowda", email = "chandra@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=0)
    sinan = User(first_name = "Sinan", last_name = "Yumurtaci", email = "sinan@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=1)
    kelly = User(first_name = "Kelly", last_name = "Putnam", email = "kelly@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=2)
    jasper = User(first_name = "Jasper", last_name = "Loverude", email = "jasper@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=3)
    zehra = User(first_name = "Zehra", last_name = "", email = "zehra@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=3)
    ghailan = User(first_name = "Ghailan", last_name = "", email = "ghailan@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=3)
    # Adding the users to the dummyEmailList
    dummyEmailList.append(chandra.email)
    dummyEmailList.append(sinan.email)
    dummyEmailList.append(kelly.email)
    dummyEmailList.append(jasper.email)
    dummyEmailList.append(zehra.email)
    dummyEmailList.append(ghailan.email)

    db.session.add(chandra)
    db.session.add(sinan)
    db.session.add(kelly)
    db.session.add(jasper)
    db.session.add(zehra)
    db.session.add(ghailan)
    db.session.commit()
    print("DB User added")

def addPermissionList():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    # Importing the Permission model here to avoid circular import
    from .models import Permission
    # Creating the permissions for each role and adding them to the database
    superAdminPermission = Permission(
        id = 0,
        name = "SuperAdmin",
        can_view_self_entries = True,
        can_edit_self_entries = True,
        can_view_own_teams_entries = True,
        can_edit_own_teams_entries = True,
        can_view_all_entries = True,
        can_edit_all_entries = True
    )
    adminPermission = Permission(
        id = 1,
        name = "Admin",
        can_view_self_entries = True,
        can_edit_self_entries = True,
        can_view_own_teams_entries = True,
        can_edit_own_teams_entries = True,
        can_view_all_entries = True,
        can_edit_all_entries = True
    )
    coachPermission = Permission(
        id = 2,
        name = "Coach",
        can_view_self_entries = True,
        can_edit_self_entries = True,
        can_view_own_teams_entries = True,
        can_edit_own_teams_entries = True,
        can_view_all_entries = False,
        can_edit_all_entries = False
    )
    playerPermission = Permission(
        id = 3,
        name = "Player",
        can_view_self_entries = True,
        can_edit_self_entries = False,
        can_view_own_teams_entries = False,
        can_edit_own_teams_entries = False,
        can_view_all_entries = False,
        can_edit_all_entries = False
    )
    db.session.add(superAdminPermission)
    db.session.add(adminPermission)
    db.session.add(coachPermission)
    db.session.add(playerPermission)
    db.session.commit()
    print("DB Permissions added")

def addDummyEntriesList():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    # Importing the Entry model here to avoid circular import
    from .models import Entry, User
    # Importing the random library to generate random numbers
    from random import randint
    # Importing the faker library to generate fake data
    from faker import Faker
    # Importing the datetime library to generate a random date
    import datetime
    # Creating a Faker object
    fake = Faker()

    # creating a loop that runs 100 times
    for i in range(100):
        # creating a random user from the database
        # Getting a random email from the dummyEmailList
        randomEmail = dummyEmailList[randint(0, len(dummyEmailList) - 1)]
        randomUser = User.query.filter_by(email = randomEmail).first()
        cat = randint(1, 4)

        # creating a random entry
        fakeEntry = Entry(
            time = datetime.datetime.now(),
            # setting category to a random number between 0 and 4
            category = 'psychology',
            value = 0,
            notes = fake.text(max_nb_chars=200),
            user_id = randomUser.id,
        )
        # adding the random entry to the database
        db.session.add(fakeEntry)
    db.session.commit()

def addDummyEntry():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    # Importing the Entry and User model here to avoid circular import
    from .models import Entry, User
    # Querying the database for the user with the email
    user1 = User.query.filter_by(email = "chandra@gmail.com").first()
    # Creating a new entry
    entry = Entry(user_id = user1.id, category = 'sleep', value = 8, notes = '')
    # Adding the entry to the database
    db.session.add(entry)
    # Committing the changes to the database
    db.session.commit()
    print("DB Entry added")
