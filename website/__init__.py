from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
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

    from .models import User, Permission, Team, Entry

    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created Database!')
            addDummyData()
            queryDummyData()



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

def addDummyData():
    # Create a dummy user
    from .models import User, Permission, Team, Entry
    user = User()
    user.email = 'cmgowd25@colby.edu'
    user.first_name = 'Chandra'
    user.last_name = 'Gowda'
    user.set_password('password')
    user.permissions = Permission.ADMIN
    db.session.add(user)
    db.session.commit()
    print("DB Committed")

# Print all users
def printAllUsers():
    from .models import User, Permission, Team, Entry
    users = User.query.all()
    print(users)
    print("DB printed all users")

# Query dummy data
def queryDummyData():
    from .models import User, Permission, Team, Entry
    user = User.query.filter_by('first_name' == 'Chandra').first()
    print(user)
    print("DB printed query")
    