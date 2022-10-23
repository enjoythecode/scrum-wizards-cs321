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

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')

def addDummyDB():
    addDummyTeam()
    addDummyUser()

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

    
    