from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, remove
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
DB_NAME = "database.db"
dummyEmailList = []

def create_test_app():

    from .models import User, Team, Entry, Permission

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    db.init_app(app)

    create_test_database(app)

    from .views import views
    from .auth import auth
    from .api import api
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
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
    from .athletepermissions import athletepermissions
    from .coachpermissions import coachpermissions
    from .hawkins import hawkins

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(addcoach, url_prefix='/')
    app.register_blueprint(addadmin, url_prefix='/')
    app.register_blueprint(addathlete, url_prefix='/')
    app.register_blueprint(athletepermissions, url_prefix='/')
    app.register_blueprint(coachpermissions, url_prefix='/')
    app.register_blueprint(hawkins, url_prefix='/')

    with app.app_context():
        if path.exists('instance/' + DB_NAME):
            # # delete the database if it exists
            remove("instance/" + DB_NAME)

        db.create_all()
        print('Created Database!')
        addDummyDB()



    # Creates database
    from .models import User
    create_database(app)

    # Initializes login_manager, sets login view, and initializes login manager to the app
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
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
    from .writecsv import writeUsersCSV
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

    addDummyTeams()
    addPermissionList()
    addDummyUser()
    addDummyUserList()
    addDummyEntriesList()

def createCSVFiles():
    from writecsv import writeUsersCSV
    writeUsersCSV()

def addDummyTeams():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    from .models import Team
    from faker import Faker
    import datetime
    fake = Faker()
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

def addDummyUser():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''
    from .models import User, Team
    team1 = Team.query.filter_by(name = "Basketball").first()
    team2 = Team.query.filter_by(name = "Football").first()

    chandra = User(first_name = "Chandra", last_name = "Gowda", email = "chandra@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=0)
    sinan = User(first_name = "Sinan", last_name = "Yumurtaci", email = "sinan@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=1)
    kelly = User(first_name = "Kelly", last_name = "Putnam", email = "kelly@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=2)
    jasper = User(first_name = "Jasper", last_name = "Loverude", email = "jasper@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=3)

    db.session.add(chandra)
    db.session.add(sinan)
    db.session.add(kelly)
    db.session.add(jasper)
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
    from .models import Permission
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

# Adding 100 dummy entries to random atheletes in the database
def addDummyEntriesList():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''
    from .models import Entry, User
    from random import randint
    from faker import Faker
    import datetime
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
    from .models import Entry, User
    user1 = User.query.filter_by(email = "chandra@gmail.com").first()
    entry = Entry(user_id = user1.id, category = 'sleep', value = 8, notes = '')
    db.session.add(entry)
    db.session.commit()
    print("DB Entry added")
