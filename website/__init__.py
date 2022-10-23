from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, remove
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '03745fbcd1b452edcd98a9acb4a0f90d'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import User

    with app.app_context():
        if path.exists('instance/' + DB_NAME):
            # delete the database if it exists
            remove("instance/" + DB_NAME)
            
            
        db.create_all()
        print('Created Database!')
        addDummyDB()




    login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def addDummyDB():
    addDummyTeam()
    addDummyUser()
    addPermissionList()
    addDummyEntry()

def addDummyTeam():
    from .models import Team
    team1 = Team(team_name = "Basketball", seasons = "2020-2021")
    team2 = Team(team_name = "Football", seasons = "2020-2021")
    db.session.add(team1)
    db.session.add(team2)
    db.session.commit()
    print("DB Team added")

def addDummyUser():
    from .models import User, Team
    team1 = Team.query.filter_by(team_name = "Basketball").first()


    team2 = Team.query.filter_by(team_name = "Football").first().id

    user1 = User(email = "chandra@gmail.com", password = "1234", team_id = team1.id)
    user2 = User(email = "sinan@gmail.com", password = "1234", team_id = team2)

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("DB User added")

    print(Team.query.filter_by(team_name = "Basketball").first().users[0].email)

def addPermissionList():
    from .models import Permission
    superAdminPermission = Permission(permission_name = "SuperAdmin", restricted_to_season = "", can_view_self_entries = True, can_edit_self_entries = True, can_view_own_teams_entries = True, can_edit_own_teams_entries = True, can_view_all_entries = True, can_edit_all_entries = True)
    adminPermission = Permission(permission_name = "Admin", restricted_to_season = "", can_view_self_entries = True, can_edit_self_entries = True, can_view_own_teams_entries = True, can_edit_own_teams_entries = True, can_view_all_entries = True, can_edit_all_entries = True)
    coachPermission = Permission(permission_name = "Coach", restricted_to_season = "2020-2021", can_view_self_entries = True, can_edit_self_entries = True, can_view_own_teams_entries = True, can_edit_own_teams_entries = True, can_view_all_entries = False, can_edit_all_entries = False)
    playerPermission = Permission(permission_name = "Player", restricted_to_season = "", can_view_self_entries = True, can_edit_self_entries = False, can_view_own_teams_entries = False, can_edit_own_teams_entries = False, can_view_all_entries = False, can_edit_all_entries = False)
    db.session.add(superAdminPermission)
    db.session.add(adminPermission)
    db.session.add(coachPermission)
    db.session.add(playerPermission)
    db.session.commit()
    print("DB Permissions added")


def addDummyEntry():
    from .models import Entry, User
    user1 = User.query.filter_by(email = "chandra@gmail.com").first()
    entry = Entry(user_id = user1.id, kind = "Psychology Notes", content = "Entry 1 Description")
    db.session.add(entry)
    db.session.commit()
    print("DB Entry added")

    
    