from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Proposed definition of the database tables to enable team work

# User
# - uid
# - email
# - first name
# - last name
# - teams (potentially > 1)
# - permissions_assigned

# Permission (hard code the data)
# - permission_name
# - restricted_to_season
# - can_view_self_entries
# - can_edit_self_entries
# - can_view_own_teams_entries
# - can_edit_own_teams_entries
# - can_view_all_entries
# - can_edit_all_entries

# Teams
# - team_id
# - team_name
# - seasons

# Entry
# - time
# - athlete user id
# - kind (force plate? sleep data? psych note?)
# - content
# on 2022-10-18, Sinan jumped 75 (/100)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    permissions_id = db.Column(db.Integer, db.ForeignKey('permission.id'))
    # entries = db.relationship('Entry')

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User')
    permission_name = db.Column(db.String(150), unique=True)
    # restricted_to_season = db.Column(db.String(150))
    # can_view_self_entries = db.Column(db.Boolean)
    # can_edit_self_entries = db.Column(db.Boolean)
    # can_view_own_teams_entries = db.Column(db.Boolean)
    # can_edit_own_teams_entries = db.Column(db.Boolean)
    # can_view_all_entries = db.Column(db.Boolean)
    # can_edit_all_entries = db.Column(db.Boolean)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(150), unique=True)
    seasons = db.Column(db.String(150))
    users = db.relationship('User')

# class Entry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     time = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     kind = db.Column(db.String(150))
#     content = db.Column(db.String(150))
