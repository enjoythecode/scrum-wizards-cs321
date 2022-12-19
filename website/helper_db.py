# Importing the database
from . import db

# Add Functions for models.py

def addUser(email, first_name, last_name, password, permission_id):
    ''' Adds a user to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the User model
    from .models import User
    # Create a new user object
    user = User(email = email, first_name = first_name, last_name = last_name, password = password, permission_id = permission_id)
    # Add the new User to the database
    db.session.add(user)
    # Commit all the changes
    db.session.commit()
    # Return the user
    return user

def addEntry(time, category, value, notes, user_id):
    ''' Adds an entry to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Entry model
    from .models import Entry
    # Create a new entry object
    entry = Entry(time = time, category = category, value = value, notes = notes, user_id = user_id)
    # Add the new Entry to the database
    db.session.add(entry)
    # Commit all the changes
    db.session.commit()
    # Return the entry
    return entry

def addTeam(name, start_date, end_date):
    ''' Adds a team to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Team model
    from .models import Team
    # Create a new team object
    team = Team(name = name, season_start_date = start_date, season_end_date = end_date)
    # Add the new Team to the database
    db.session.add(team)
    # Commit all the changes
    db.session.commit()
    # Return the team
    return team

def addPermission(id, name, can_view_self_entries, can_edit_self_entries, can_view_own_teams_entries, can_edit_own_teams_entries, can_view_all_entries, can_edit_all_entries):
    ''' Adds a permission to the database
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Permission model
    from .models import Permission
    # Create a new permission object
    permission = Permission(id = id, name = name, can_view_self_entries = can_view_self_entries, can_edit_self_entries = can_edit_self_entries, can_view_own_teams_entries = can_view_own_teams_entries, can_edit_own_teams_entries = can_edit_own_teams_entries, can_view_all_entries = can_view_all_entries, can_edit_all_entries = can_edit_all_entries)
    # Add the new Permission to the database
    db.session.add(permission)
    # Commit all the changes
    db.session.commit()
    # Return the permission
    return permission

# Get Functions for models.py

def getUsers():
    ''' Get a list of all users in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_users
    '''

    # Import the User model
    from .models import User
    # Get all users
    users = User.query.all()
    # Return the users
    return users


def getTeams():
    ''' Get a list of all teams in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_teams
    '''

    # Import the Team model
    from .models import Team
    # Get all teams
    teams = Team.query.all()
    # Return the teams
    return teams


def getPermissions():
    ''' Get a list of all permissions in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_permissions
    '''

    # Import the Permission model
    from .models import Permission
    # Get all permissions
    permissions = Permission.query.all()
    # Return the permissions
    return permissions


def getEntries():
    ''' Get a list of all entries in the DB
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries
    '''

    # Import the Entry model
    from .models import Entry
    # Get all entries
    entries = Entry.query.all()
    # Return the entries
    return entries


def getUserByEmail(email):
    ''' Queries the database for a specific user by email
    ---------------------------------------
    Returns:
    ---------------------------------------
        User.
    '''

    # Import the User model
    from .models import User
    # Get the user
    user = User.query.filter_by(email=email).first()
    # Return the user
    return user


def getUserByName(first_name, last_name):
    ''' Gets user by first_name and last_name
    ---------------------------------------
    Returns:
    ---------------------------------------
        User.
    '''

    # Import the User model
    from .models import User
    # Get the user
    user = User.query.filter_by(first_name=first_name, last_name=last_name).first()
    # Return the user
    return user


def getUserById(user_id):
    ''' Gets specific user by id
    ---------------------------------------
    Returns:
    ---------------------------------------
        User.
    '''

    # Import the User model
    from .models import User
    # Get the user
    user = User.query.filter_by(id=user_id).first()
    # Return the user
    return user


def getTeamByName(team_name):
    ''' Gets specific team by name
    ---------------------------------------
    Returns:
    ---------------------------------------
        Team.
    '''

    # Import the Team model
    from .models import Team
    # Get the team by name
    team = Team.query.filter_by(name=team_name).first()
    # Return the team
    return team


def getTeamById(team_id):
    ''' Gets team of a specific id
    ---------------------------------------
    Returns:
    ---------------------------------------
        Team.
    '''

    # Import the Team model
    from .models import Team
    # Get the team by id
    team = Team.query.filter_by(id=team_id).first()
    # Return the team
    return team


def getUsersInTeam(team_id):
    ''' Gets all users of a specific team
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_users_in_team
    '''

    # Import the User model
    from .models import User, Team
    # Get the users in the team
    users = Team.query.filter_by(id=team_id).first().users
    # Return the users
    return users


def getPermissionByName(permission_name):
    ''' Gets all permissions of a specific name
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_permissions_by_name
    '''

    # Import the Permission model
    from .models import Permission
    # Get the permission by name
    permission = Permission.query.filter_by(name=permission_name).first()
    # Return the permission
    return permission

def getPermissionById(permission_id):
    ''' Gets all permissions of a specific id
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_permissions_by_id
    '''

    # Import the Permission model
    from .models import Permission
    # Get the permission by id
    permission = Permission.query.filter_by(id=permission_id).first()
    # Return the permission
    return permission


def getUsersByPermission(permission_id):
    ''' Gets all users of a specific permission
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_users_by_permission
    '''

    # Import the User model
    from .models import User
    # Get the users by permission
    users = User.query.filter_by(permission_id=permission_id).all()
    # Return the users
    return users


def getEntryById(entry_id):
    ''' Gets all entries of a specific id
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_for_id
    '''

    # Import the Entry model
    from .models import Entry
    # Get the entry by id
    entry = Entry.query.filter_by(id=entry_id).first()
    # Return the entry
    return entry


def getEntriesByUser(user_id):
    ''' Returns all entries for a specific user
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_for_user
    '''

    # Import the Entry model
    from .models import Entry
    # Get the entries by user
    entries = Entry.query.filter_by(user_id=user_id).all()
    # Return the entries
    return entries


def getEntriesByCategory(category):
    ''' Returns all entries of a specific category
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Entry model
    from .models import Entry
    # Get the entries by category
    entries = Entry.query.filter_by(category=category).all()
    # Return the entries
    return entries

# Update functions for models.py

def updateUserFullName(user_id, first_name, last_name):
    ''' Updates a user's first and last name
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the User model
    from .models import User
    # Get the user
    user = User.query.filter_by(id=user_id).first()
    # Update the user's first and last name
    user.first_name = first_name
    user.last_name = last_name
    # Commit the changes
    db.session.commit()
    # Return the user
    return user

def updateUserPermission(user_id, permission_id):
    ''' Updates a user's permission id
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the User model
    from .models import User
    # Get the user
    user = User.query.filter_by(id=user_id).first()
    # Update the user's permission id
    user.permission_id = permission_id
    # Commit the changes
    db.session.commit()
    # Return the user
    return user

def addUserToTeam(user_id, team_id):
    ''' Adds a user to a team
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the User and Team models
    from .models import User, Team
    # Get the user and team
    user = User.query.filter_by(id=user_id).first()
    # Add the user to the team
    user.teams.append(Team.query.filter_by(id=team_id).first())
    # Commit the changes
    db.session.commit()
    # Return the user
    return user

def removeUserFromTeam(user_id, team_id):
    ''' Removes a user from a team
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the User and Team models
    from .models import User, Team
    # Get the user and team
    user = User.query.filter_by(id=user_id).first()
    team = Team.query.filter_by(id=team_id).first()
    # Remove the user from the team
    user.teams.remove(team)
    # Commit the changes
    db.session.commit()
    # Return the user
    return user

def updateTeamName(team_id, team_name):
    ''' Updates a team's name
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Team model
    from .models import Team
    # Get the team
    team = Team.query.filter_by(id=team_id).first()
    # Update the team's name
    team.name = team_name
    # Commit the changes
    db.session.commit()
    # Return the team
    return team

def updateTeamSeason(team_id, season_start, season_end):
    ''' Updates a team's season start and end
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Team model
    from .models import Team
    # Get the team
    team = Team.query.filter_by(id=team_id).first()
    # Update the team's season start and end
    team.season_start_date = season_start
    team.season_end_date = season_end
    # Commit the changes
    db.session.commit()
    # Return the team
    return team

def updateEntryValues(entry_id, time, category, value, notes, user_id):
    ''' Updates an entry's title, content, and category
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Entry model
    from .models import Entry
    # Get the entry
    entry = Entry.query.filter_by(id=entry_id).first()
    # Update the entry's title, content, and category
    entry.time = time
    entry.category = category
    entry.value = value
    entry.notes = notes
    entry.user_id = user_id
    # Commit the changes
    db.session.commit()
    # Return the entry
    return entry

# Delete functions for models.py

def deleteUser(user_id):
    ''' Deletes a user
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the User model
    from .models import User
    # Get the user
    user = User.query.filter_by(id=user_id).first()
    # Delete the user
    db.session.delete(user)
    # Commit the changes
    db.session.commit()
    # Return the user
    return user

def deleteEntry(entry_id):
    ''' Deletes an entry
    ---------------------------------------
    Returns:
    ---------------------------------------
    Python List. len = total_entries_of_category
    '''

    # Import the Entry model
    from .models import Entry
    # Get the entry
    entry = Entry.query.filter_by(id=entry_id).first()
    # Delete the entry
    db.session.delete(entry)
    # Commit the changes
    db.session.commit()
    # Return the entry
    return entry
