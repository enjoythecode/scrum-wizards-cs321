from . import db
from sqlalchemy.sql import func

# Add Functions for models.py

def addUser(email, first_name, last_name, password, permission_id):
    ''' Adds a user to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import User
    user = User(email = email, first_name = first_name, last_name = last_name, password = password, permission_id = permission_id)
    db.session.add(user)
    db.session.commit()
    return user

def addEntry(time, category, value, notes, user_id):
    ''' Adds an entry to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Entry
    entry = Entry(time = time, category = category, value = value, notes = notes, user_id = user_id)
    db.session.add(entry)
    db.session.commit()
    return entry

def addTeam(name, start_date, end_date):
    ''' Adds a team to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Team
    team = Team(name = name, season_start_date = start_date, season_end_date = end_date)
    db.session.add(team)
    db.session.commit()
    return team

def addPermission(id, name, can_view_self_entries, can_edit_self_entries, can_view_own_teams_entries, can_edit_own_teams_entries, can_view_all_entries, can_edit_all_entries):
    ''' Adds a permission to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Permission
    permission = Permission(id = id, name = name, can_view_self_entries = can_view_self_entries, can_edit_self_entries = can_edit_self_entries, can_view_own_teams_entries = can_view_own_teams_entries, can_edit_own_teams_entries = can_edit_own_teams_entries, can_view_all_entries = can_view_all_entries, can_edit_all_entries = can_edit_all_entries)
    db.session.add(permission)
    db.session.commit()
    return permission

# Get Functions for models.py

def getUsers():
    ''' Get a list of all users in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_users
    '''

    from .models import User
    users = User.query.all()
    return users


def getTeams():
    ''' Get a list of all teams in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_teams
    '''

    from .models import Team
    teams = Team.query.all()
    return teams


def getPermissions():
    ''' Get a list of all permissions in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_permissions
    '''

    from .models import Permission
    permissions = Permission.query.all()
    return permissions


def getEntries():
    ''' Get a list of all entries in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries
    '''

    from .models import Entry
    entries = Entry.query.all()
    return entries


def getUserByEmail(email):
    ''' Queries the database for a specific user by email
    ---------------------------------------
    Returns:
    ---------------------------------------
        User.
    '''

    from .models import User
    user = User.query.filter_by(email=email).first()
    return user


def getUserByName(first_name, last_name):
    ''' Gets user by first_name and last_name
    ---------------------------------------
    Returns:
    ---------------------------------------
        User.
    '''

    from .models import User
    user = User.query.filter_by(first_name=first_name, last_name=last_name).first()
    return user


def getUserById(user_id):
    ''' Gets specific user by id
    ---------------------------------------
    Returns:
    ---------------------------------------
        User.
    '''
    from .models import User
    user = User.query.filter_by(id=user_id).first()
    return user


def getTeamByName(team_name):
    ''' Gets specific team by name
    ---------------------------------------
    Returns:
    ---------------------------------------
        Team.
    '''
    from .models import Team
    team = Team.query.filter_by(name=team_name).first()
    return team


def getTeamById(team_id):
    ''' Gets team of a specific id
    ---------------------------------------
    Returns:
    ---------------------------------------
        Team.
    '''

    from .models import Team
    team = Team.query.filter_by(id=team_id).first()
    return team


def getUsersInTeam(team_id):
    ''' Gets all users of a specific team
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_users_in_team
    '''

    from .models import User, Team
    users = Team.query.filter_by(id=team_id).first().users
    return users


def getPermissionByName(permission_name):
    ''' Gets all permissions of a specific name
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_permissions_by_name
    '''

    from .models import Permission
    permission = Permission.query.filter_by(name=permission_name).first()
    return permission

def getPermissionById(permission_id):
    ''' Gets all permissions of a specific id
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_permissions_by_id
    '''

    from .models import Permission
    permission = Permission.query.filter_by(id=permission_id).first()
    return permission


def getUsersByPermission(permission_id):
    ''' Gets all users of a specific permission
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_users_by_permission
    '''

    from .models import User
    users = User.query.filter_by(permission_id=permission_id).all()
    return users


def getEntryById(entry_id):
    ''' Gets all entries of a specific id
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_for_id
    '''

    from .models import Entry
    entry = Entry.query.filter_by(id=entry_id).first()
    return entry


def getEntriesByUser(user_id):
    ''' Returns all entries for a specific user
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_for_user
    '''

    from .models import Entry
    entries = Entry.query.filter_by(user_id=user_id).all()
    return entries


def getEntriesByCategory(category):
    ''' Returns all entries of a specific category
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Entry
    entries = Entry.query.filter_by(category=category).all()
    return entries

# Update functions for models.py

def updateUserFullName(user_id, first_name, last_name):
    ''' Updates a user's first and last name
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import User
    user = User.query.filter_by(id=user_id).first()
    user.first_name = first_name
    user.last_name = last_name
    db.session.commit()
    return user

def updateUserPermission(user_id, permission_id):
    ''' Updates a user's permission id
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import User
    user = User.query.filter_by(id=user_id).first()
    user.permission_id = permission_id
    db.session.commit()
    return user

def addUserToTeam(user_id, team_id):
    ''' Adds a user to a team
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import User, Team
    user = User.query.filter_by(id=user_id).first()
    user.teams.append(Team.query.filter_by(id=team_id).first())
    db.session.commit()
    return user

def removeUserFromTeam(user_id, team_id):
    ''' Removes a user from a team
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import User, Team
    user = User.query.filter_by(id=user_id).first()
    team = Team.query.filter_by(id=team_id).first()
    user.teams.remove(team)
    db.session.commit()
    return user

def updateTeamName(team_id, team_name):
    ''' Updates a team's name
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Team
    team = Team.query.filter_by(id=team_id).first()
    team.name = team_name
    db.session.commit()
    return team

def updateTeamSeason(team_id, season_start, season_end):
    ''' Updates a team's season start and end
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Team
    team = Team.query.filter_by(id=team_id).first()
    team.season_start_date = season_start
    team.season_end_date = season_end
    db.session.commit()
    return team

def updateEntryValues(entry_id, time, category, value, notes, user_id):
    ''' Updates an entry's title, content, and category
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Entry
    entry = Entry.query.filter_by(id=entry_id).first()
    entry.time = time
    entry.category = category
    entry.value = value
    entry.notes = notes
    entry.user_id = user_id
    db.session.commit()
    return entry

# Delete functions for models.py

def deleteUser(user_id):
    ''' Deletes a user
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import User
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return user

def deleteEntry(entry_id):
    ''' Deletes an entry
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    from .models import Entry
    entry = Entry.query.filter_by(id=entry_id).first()
    db.session.delete(entry)
    db.session.commit()
    return entry
