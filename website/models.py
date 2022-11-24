import enum
import sqlalchemy
from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


team_user_assoc_table = db.Table(
    "association_table",
    db.Column('left_id', db.ForeignKey('user.id'), primary_key=True),
    db.Column('right_id', db.ForeignKey('team.id'), primary_key=True),
)

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150), default = '')
    last_name = db.Column(db.String(150), default = '')
    password = db.Column(db.String(150), default = '')
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'))
    entries = db.relationship('Entry')
    teams = db.relationship(
        'Team', secondary=team_user_assoc_table, back_populates='users'
    )
    
class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(150), unique=True)
    can_view_self_entries = db.Column(db.Boolean, default = False)
    can_edit_self_entries = db.Column(db.Boolean, default = False)
    can_view_own_teams_entries = db.Column(db.Boolean, default = False)
    can_edit_own_teams_entries = db.Column(db.Boolean, default = False)
    can_view_all_entries = db.Column(db.Boolean, default = False)
    can_edit_all_entries = db.Column(db.Boolean, default = False)
    users = db.relationship(
        'User'
    )

class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True)
    season_start_date = db.Column(db.Date(), default=func.now())
    season_end_date = db.Column(db.Date(), default=func.now())
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
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    category = db.Column(db.Enum(Category, validate_strings=True))
    value = db.Column(db.Integer, default=0)
    notes = db.Column(db.String, default='')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))







