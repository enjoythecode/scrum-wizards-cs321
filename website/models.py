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
teamlist = ["soccer", "tennis", "football", "track"]
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

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship('Note')