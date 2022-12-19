# Importing the enum library to allow for the use of Enum types
import enum
# Importing the SQLAlchemy library to allow for the use of the ORM
import sqlalchemy
# Importing the datetime library to allow for the use of datetime objects
from time import timezone
# Importing the database object from the __init__.py file
from . import db
# Importing the UserMixin class from flask_login to allow for the use of the UserMixin class
from flask_login import UserMixin
# Importing the func object from sqlalchemy.sql to allow for the use of the func object
from sqlalchemy.sql import func

# Creating the association table for the many-to-many relationship between the User and Team tables
team_user_assoc_table = db.Table(
    "association_table",
    db.Column('left_id', db.ForeignKey('user.id'), primary_key=True),
    db.Column('right_id', db.ForeignKey('team.id'), primary_key=True),
)

class User(db.Model, UserMixin):
    ''' Defines the User table in the database '''

    # Defining the table name as 'user'
    __tablename__ = "user"
    # Defining the columns in the table
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150), default = '')
    last_name = db.Column(db.String(150), default = '')
    password = db.Column(db.String(150), default = '')
    # Defining the foreign key relationship between the User and Permission tables
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'))
    entries = db.relationship('Entry')
    # Defining the many-to-many relationship between the User and Team tables
    teams = db.relationship(
        'Team', secondary=team_user_assoc_table, back_populates='users'
    )

class Permission(db.Model):
    ''' Defines the Permission table in the database'''

    # Defining the table name as 'permission'
    __tablename__ = "permission"
    # Defining the columns in the table
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(150), unique=True)
    can_view_self_entries = db.Column(db.Boolean, default = False)
    can_edit_self_entries = db.Column(db.Boolean, default = False)
    can_view_own_teams_entries = db.Column(db.Boolean, default = False)
    can_edit_own_teams_entries = db.Column(db.Boolean, default = False)
    can_view_all_entries = db.Column(db.Boolean, default = False)
    can_edit_all_entries = db.Column(db.Boolean, default = False)
    # Defining the foreign key relationship between the Permission and User tables
    users = db.relationship(
        'User'
    )

class Team(db.Model):
    ''' Defines the Team table in the database '''

    # Defining the table name as 'team'
    __tablename__ = "team"
    # Defining the columns in the table
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True)
    season_start_date = db.Column(db.Date(), default=func.now())
    season_end_date = db.Column(db.Date(), default=func.now())
    # Defining the many-to-many relationship between the User and Team tables
    users = db.relationship(
        'User', secondary=team_user_assoc_table, back_populates='teams'
    )


class Category(enum.Enum):
    ''' Defines the possible categories for an entry- an entry can only be on of these Enum values
    ----------
    syntax: category_variable = Category(0)
        - instantiates a 'Category' of type Sleep
    ----------
    '''
    sleep = 0
    recovery = 1
    force_plate = 2
    readiness = 3
    psychology = 4


class Entry(db.Model):
    ''' Defines the Entry table in the database '''

    # Defining the table name as 'entry'
    __tablename__ = "entry"
    # Defining the columns in the table
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    category = db.Column(db.Enum(Category, validate_strings=True))
    value = db.Column(db.Integer, default=0)
    notes = db.Column(db.String, default='')
    # Defining the foreign key relationship between the Entry and User tables
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
