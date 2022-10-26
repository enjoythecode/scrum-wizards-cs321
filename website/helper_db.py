from . import db
from sqlalchemy.sql import func


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
    team = Team.query.filter_by(team_name=team_name).first()
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

    from .models import User
    users = User.query.filter_by(teams=team_id).all()
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


def getUsersByPermission(permission_name):
    ''' Gets all users of a specific permission
    ---------------------------------------
    Returns: 
    ---------------------------------------
    Python List. len = total_users_by_permission
    '''

    from .models import User
    users = User.query.filter_by(permissions_id=permission_name).all()
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


def getEntriesForUser(user_id):
    ''' Handles login logic on /login path:
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