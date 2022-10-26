from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, remove
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
DB_NAME = "database.db"

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

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

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

    
def addDummyDB():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    addDummyTeam()
    addDummyUser()
    addPermissionList()
    addDummyEntry()

def addDummyTeam():
    ''' Calls database hydration functions.
    Parameters:
    ---------------------------------------
    Returns:
    ---------------------------------------
        void
    '''

    from .models import Team
    team1 = Team(name = "Basketball")
    team2 = Team(name = "Football")
    db.session.add(team1)
    db.session.add(team2)
    db.session.commit()
    print("DB Team added")

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

    user1 = User(first_name = "Chandra", last_name = "Gowda", email = "chandra@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=0)
    user2 = User(first_name = "Sinan", last_name = "Yumurtaci", email = "sinan@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=1)
    user3 = User(first_name = "Kelly", last_name = "Putnam", email = "kelly@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=2)
    user4 = User(first_name = "Jasper", last_name = "Loverude", email = "jasper@gmail.com", password = generate_password_hash("1234", method='sha256'), permission_id=3)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
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

    