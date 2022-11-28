import pytest
from os import path, remove
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import helper_db
from conftest import app, client
from website.models import User, Team, Entry, Category, Permission


#################################
#                               #
#   UNIT TESTS FOR ADD METHODS  #
#                               #
#################################

def test_add_user(client):
    '''
    Unit test for addUser() 

    GIVEN: 
        There is no user in the database
    WHEN: 
        A new user is added to the database
    THEN: 
        Check that the database contains the user with proper email, 
        first_name, last_name, password, permission_id are 
    '''

    helper_db.addUser(email="test@gmail.com", first_name="first", last_name="last", password="test", permission_id=1)
    test_user = helper_db.getUserByEmail("test@gmail.com")
    assert test_user.email == "test@gmail.com" 
    assert test_user.first_name == "first"
    assert test_user.last_name == "last"
    assert test_user.password == "test"
    assert test_user.permission_id == 1

def test_add_team(client):
    '''
    Unit test for addTeam()

    GIVEN: 
        There is no team in the database
    WHEN: 
        A new team is added to the database
    THEN: 
        Check that the database contains the team with proper start date, 
        end date, and name
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addTeam(name="test", start_date = start_date, end_date=end_date)
    test_team = helper_db.getTeamByName("test")
    assert test_team.name == "test"
    assert test_team.season_start_date.year == start_date.year
    assert test_team.season_start_date.month == start_date.month
    assert test_team.season_start_date.day == start_date.day
    assert test_team.season_end_date.year == end_date.year
    assert test_team.season_end_date.month == end_date.month
    assert test_team.season_end_date.day == end_date.day

def test_add_entry(client):
    '''
    Unit test for addEntry()

    GIVEN: 
        There is no entry in the database
    WHEN: 
        A new entry is added to the database
    THEN: 
        Check that the database contains the entry with proper user_id, 
        category, time, value, and notes 
    '''

    import datetime
    test_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time=test_time, category=Category.psychology, value=0, notes="test")
    test_entry = helper_db.getEntryById(1)
    assert test_entry.user_id == 1
    assert test_entry.category == Category.psychology
    assert test_entry.time.year == test_time.year
    assert test_entry.time.month == test_time.month
    assert test_entry.time.day == test_time.day
    assert test_entry.value == 0
    assert test_entry.notes == "test"

def test_add_permission(client):
    '''
    Unit test for addPermission()

    GIVEN: 
        There is no permission in the database
    WHEN: 
        A new permission is added to the database
    THEN: 
        Check that the database contains the permission with proper boolean
        values for permissions
    '''

    helper_db.addPermission(id = 0, name="test", can_view_self_entries=True, can_edit_self_entries=True, can_view_own_teams_entries=True, can_edit_own_teams_entries=True, can_view_all_entries=True, can_edit_all_entries=True)
    test_permission = helper_db.getPermissionByName("test")
    assert test_permission.name == "test"
    assert test_permission.id == 0
    assert test_permission.can_view_self_entries == True
    assert test_permission.can_edit_self_entries == True
    assert test_permission.can_view_own_teams_entries == True
    assert test_permission.can_edit_own_teams_entries == True
    assert test_permission.can_view_all_entries == True
    assert test_permission.can_edit_all_entries == True


#################################
#                               #
#   UNIT TESTS FOR GET METHODS  #
#                               #
#################################

def test_get_users(client):
    '''
    Unit test for getUsers()

    GIVEN: 
        There exists a user(s) in the database
    WHEN: 
        Calling the getUsers() method
    THEN: 
        Check that the returns all users in the database
    '''

    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    user_list = helper_db.getUsers()
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

def test_get_teams(client):
    '''
    Unit test for getTeams()

    GIVEN: 
        There exist a team(s) in the database
    WHEN: 
        Calling the getTeams() method
    THEN: 
        Check that the method returns all teams, with proper start/end time,
        and team name
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addTeam(name="test", start_date=start_date, end_date=end_date)
    team_list = helper_db.getTeams()
    assert len(team_list) == 1
    assert team_list[0].name == "test"
    assert team_list[0].season_start_date.year == start_date.year
    assert team_list[0].season_start_date.month == start_date.month
    assert team_list[0].season_start_date.day == start_date.day
    assert team_list[0].season_end_date.year == end_date.year
    assert team_list[0].season_end_date.month == end_date.month
    assert team_list[0].season_end_date.day == end_date.day

def test_get_entries(client):
    '''
    Unit test for getEntries()

    GIVEN: 
        There exists an entry in the database
    WHEN: 
        Calling the getEntries() method
    THEN: 
        Check that the method returnes all entries in the database
    '''

    import datetime
    current_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time = current_time, category = Category.psychology, value = 0, notes = "test notes")
    entry_list = helper_db.getEntries()
    assert len(entry_list) == 1
    assert entry_list[0].user_id == 1
    assert entry_list[0].time == current_time
    assert entry_list[0].category == Category.psychology
    assert entry_list[0].value == 0
    assert entry_list[0].notes == "test notes"

def test_get_permissions(client):
    '''
    Unit test for getPermissions()

    GIVEN: 
        There exists a permission(s) in the database
    WHEN: 
        The getPermissions() method is invoked
    THEN: 
        Check that the method returns all permissions in the database
        with proper boolean values 
    '''

    helper_db.addPermission(id = 1, name="test", can_view_self_entries=True, can_edit_self_entries=True, can_view_own_teams_entries=True, can_edit_own_teams_entries=True, can_view_all_entries=True, can_edit_all_entries=True)
    permission_list = helper_db.getPermissions()
    assert len(permission_list) == 1
    assert permission_list[0].name == "test"
    assert permission_list[0].id == 1
    assert permission_list[0].can_view_self_entries == True
    assert permission_list[0].can_edit_self_entries == True
    assert permission_list[0].can_view_own_teams_entries == True
    assert permission_list[0].can_edit_own_teams_entries == True
    assert permission_list[0].can_view_all_entries == True
    assert permission_list[0].can_edit_all_entries == True

def test_get_user_by_email(client):
    '''
    Unit test for getUserByEmail()

    GIVEN: 
        There exists a user in the database
    WHEN: 
        Calling the getUserByEmail() method
    THEN: 
        Check that the method returns the proper user associated with that email
    '''

    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserByEmail("cmgowd25@colby.edu")
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

def test_get_user_by_name(client):
    '''
    Unit test for getUserByName()

    GIVEN: 
        There exists a user in the database
    WHEN: 
        Calling the getUserByName() method
    THEN: 
        Check that the method returns the user with the proper first and lastname 
    '''

    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserByName("Chandra", "Gowda")
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1


def test_get_user_by_id(client):
    '''
    Unit test for getUserById()

    GIVEN: 
        There exists a user in the database
    WHEN: 
        Calling the getUserById() method
    THEN: 
        Check that the method returns the user with associated with said ID, and has 
        the proper email, name, and password
    '''

    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserById(1)
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

def test_get_team_by_name(client):
    '''
    Unit test for getTeamByName()

    GIVEN: 
        There exists a team in the database
    WHEN: 
        Invoking the getTeamByName() method
    THEN: 
        Check that the database returns the team with input name and that team has proper
        start, and end dates
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addTeam(name="test", start_date=start_date, end_date=end_date)
    test_team = helper_db.getTeamByName("test")
    assert test_team.name == "test"
    assert test_team.season_start_date.year == start_date.year
    assert test_team.season_start_date.month == start_date.month
    assert test_team.season_start_date.day == start_date.day
    assert test_team.season_end_date.year == end_date.year
    assert test_team.season_end_date.month == end_date.month
    assert test_team.season_end_date.day == end_date.day

def test_get_team_by_id(client):
    '''
    Unit test for getTeamById()

    GIVEN: 
        There exists a team in the database
    WHEN: 
        Invoking the getTeamById() method
    THEN: 
        Check that the method returns the team associated with said ID, and
        that team contains the proper start date and enddate
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addTeam(name="test", start_date=start_date, end_date=end_date)
    team_id = helper_db.getTeamByName("test").id
    test_team = helper_db.getTeamById(team_id)
    assert test_team.name == "test"
    assert test_team.season_start_date.year == start_date.year
    assert test_team.season_start_date.month == start_date.month
    assert test_team.season_start_date.day == start_date.day
    assert test_team.season_end_date.year == end_date.year
    assert test_team.season_end_date.month == end_date.month
    assert test_team.season_end_date.day == end_date.day

def test_get_users_in_team(client):
    '''
    Unit test for getUsersInTeam()

    GIVEN: 
        There exists a team in the database with user(s) associated with it
    WHEN: 
        Invoking the getUsersInTeam() method
    THEN: 
        Check that the method returns all users associated with that team,
        and that the users have the proper name, email, password, etc.
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", start_date=start_date, end_date=end_date)
    helper_db.addUserToTeam(user_id=1, team_id=1)
    user_list = helper_db.getUsersInTeam(1)
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

def test_get_permission_by_name(client):
    '''
    Unit test for getPermissionByName()

    GIVEN: 
        There exists a permission in the database
    WHEN: 
        Invoking the getPermissionsByName() method
    THEN: 
        Check that the method returns the permission of the stated name,
        and it contains all proper boolean values 
    '''

    helper_db.addPermission(id = 1, name="test", can_view_self_entries=False, can_edit_self_entries=True, can_view_own_teams_entries=False, can_edit_own_teams_entries=True, can_view_all_entries=False, can_edit_all_entries=True)
    permission = helper_db.getPermissionByName("test")
    assert permission.name == "test"
    assert permission.id == 1
    assert permission.can_view_self_entries == False
    assert permission.can_edit_self_entries == True
    assert permission.can_view_own_teams_entries == False
    assert permission.can_edit_own_teams_entries == True
    assert permission.can_view_all_entries == False
    assert permission.can_edit_all_entries == True

def test_get_permission_by_id(client):
    '''
    Unit test for getPermissionById()

    GIVEN: 
        There exists a permission in the database
    WHEN: 
        Invoking the getPermissionById() method
    THEN: 
        Check that the method returns the permission with the proper boolean values
    '''

    helper_db.addPermission(id = 1, name="test", can_view_self_entries=False, can_edit_self_entries=True, can_view_own_teams_entries=False, can_edit_own_teams_entries=True, can_view_all_entries=False, can_edit_all_entries=True)
    permission = helper_db.getPermissionById(1)
    assert permission.name == "test"
    assert permission.id == 1
    assert permission.can_view_self_entries == False
    assert permission.can_edit_self_entries == True
    assert permission.can_view_own_teams_entries == False
    assert permission.can_edit_own_teams_entries == True
    assert permission.can_view_all_entries == False
    assert permission.can_edit_all_entries == True

def test_get_users_by_permission(client):
    '''
    Unit test for getUsersByPermission()

    GIVEN: 
        There exists a user and permission in the database, and they are associated
    WHEN: 
        Invoking the getUsersByPermission() method
    THEN: 
        Check that the method returns the proper users associated that that permission
    '''

    helper_db.addPermission(id = 1, name="test", can_view_self_entries=False, can_edit_self_entries=True, can_view_own_teams_entries=False, can_edit_own_teams_entries=True, can_view_all_entries=False, can_edit_all_entries=True)
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    user_list = helper_db.getUsersByPermission(1)
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

def test_get_entry_by_id(client):
    '''
    Unit test for getEntryById()

    GIVEN: 
        There exist an entry in the database
    WHEN: 
        Invoking the getEntryById() method
    THEN: 
        Check that the method returns the proper entry associated with that Id
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", start_date=start_date, end_date=end_date)
    helper_db.addUserToTeam(user_id=1, team_id=1)
    current_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time = current_time, category = Category.psychology, value = 0, notes = "test notes")
    entry = helper_db.getEntryById(1)
    assert entry.user_id == 1
    assert entry.time.year == current_time.year
    assert entry.time.month == current_time.month
    assert entry.time.day == current_time.day
    assert entry.category == Category.psychology
    assert entry.value == 0
    assert entry.notes == "test notes"

def test_get_entries_by_user(client):
    '''
    Unit test for getEntriesByUser()

    GIVEN: 
        There exists a user in the DB, with entries associated with them
    WHEN: 
        Invoking the getEntriesByUser() method
    THEN: 
        Check that the method returns the proper entries associated with said user
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", start_date=start_date, end_date=end_date)
    helper_db.addUserToTeam(user_id=1, team_id=1)
    current_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time = current_time, category = Category.psychology, value = 0, notes = "test notes")
    entry_list = helper_db.getEntriesByUser(1)
    assert len(entry_list) == 1
    assert entry_list[0].user_id == 1
    assert entry_list[0].time.year == current_time.year
    assert entry_list[0].time.month == current_time.month
    assert entry_list[0].time.day == current_time.day
    assert entry_list[0].category == Category.psychology
    assert entry_list[0].value == 0
    assert entry_list[0].notes == "test notes"

def test_get_entries_by_category(client):
    '''
    Unit test for getEntiesByCategory()

    GIVEN: 
        There exists entries of a specific category in the database
    WHEN: 
        Invoking the getEntriesByCategory() method with specific category
    THEN: 
        Check that the method returns the proper entries of said category
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", start_date=start_date, end_date=end_date)
    helper_db.addUserToTeam(user_id=1, team_id=1)
    current_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time = current_time, category = Category.psychology, value = 0, notes = "test notes")
    entry_list = helper_db.getEntriesByCategory(Category.psychology)
    assert len(entry_list) == 1
    assert entry_list[0].user_id == 1
    assert entry_list[0].time.year == current_time.year
    assert entry_list[0].time.month == current_time.month
    assert entry_list[0].time.day == current_time.day
    assert entry_list[0].category == Category.psychology
    assert entry_list[0].value == 0
    assert entry_list[0].notes == "test notes"

####################################
#                                  #
#   UNIT TESTS FOR UPDATE METHODS  #
#                                  #
####################################

def test_update_full_username(client):
    '''
    Unit test for updateUserFullName()

    GIVEN: 
        There exists a user in the database
    WHEN: 
        Invoking the updateUserFullName() method
    THEN: 
        Check that the user in the database is updated with the new first name, last name
    '''

    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=1)
    user_id = helper_db.getUserByEmail("email@email.com").id
    helper_db.updateUserFullName(user_id, "final_1", "final_2")
    updated_user = helper_db.getUserByName("final_1", "final_2")
    assert updated_user.first_name == "final_1"
    assert updated_user.last_name == "final_2"

def test_update_user_permission(client):
    '''
    Unit test for updateUserPermission()

    GIVEN: 
        There exists a user, permission the database such that the user and permission are associated
    WHEN: 
        Invoking the updateUserPermission() method
    THEN: 
        Check that the user in the database is updated with the correct permission
    '''

    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    user_id = helper_db.getUserByEmail("email@email.com").id
    helper_db.updateUserPermission(user_id, 2)
    updated_user_permission_id = helper_db.getUserByEmail("email@email.com").permission_id
    assert updated_user_permission_id == 2

def test_add_user_to_team(client):
    '''
    Unit test for addUserToTeam()

    GIVEN: 
        There exists a user, team in the database
    WHEN: 
        Invoking the addUserToTeam() method with said user and team
    THEN: 
        Check that the user in the database is associated with the correct team
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    helper_db.addTeam(name="team", start_date=start_date, end_date=end_date)
    user_id = helper_db.getUserByEmail("email@email.com").id
    team_id = helper_db.getTeamByName("team").id
    helper_db.addUserToTeam(user_id=user_id, team_id=team_id)
    user_list = helper_db.getUsersInTeam(team_id)
    assert user_list[0].id == user_id

def test_remove_user_from_team(client):
    '''
    Unit test for removeUserFromTeam()

    GIVEN: 
        There exists a user in the database, associated with a team
    WHEN: 
        Invoking the removeUserFromTeam() method
    THEN: 
        Check that the user is no longer associated with a team entry in the DB
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    helper_db.addTeam(name="team", start_date=start_date, end_date=end_date)
    user_id = helper_db.getUserByEmail("email@email.com").id
    team_id = helper_db.getTeamByName("team").id
    helper_db.addUserToTeam(user_id=user_id, team_id=team_id)
    user_list = helper_db.getUsersInTeam(team_id)
    assert user_list[0].id == user_id
    helper_db.removeUserFromTeam(user_id=user_id, team_id=team_id)
    user_list = helper_db.getUsersInTeam(team_id)
    assert len(user_list) == 0

def test_update_team_name(client):
    '''
    Unit test for updateTeamName()

    GIVEN: 
        There exists a team in the database
    WHEN: 
        Invoking the updateTeamName() method
    THEN: 
        Check that the team in the database is updated with the new name
    '''

    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addTeam(name="init_name", start_date=start_date, end_date=end_date)
    team_id = helper_db.getTeamByName("init_name").id
    helper_db.updateTeamName(team_id, "new_name")
    team_name = helper_db.getTeamById(team_id).name
    assert team_name == "new_name"

def test_update_team_season_start_end(client):
    '''
    Unit test for updateTeamSeason()

    GIVEN: 
        There exists a team in the database
    WHEN: 
        Invoking the updateTeamSeason() method
    THEN: 
        Check that the team is associated with the newly set start and end date
    '''

    import datetime
    init_start_date = datetime.datetime.now()
    init_end_date = datetime.datetime.now()
    helper_db.addTeam(name="init_name", start_date=init_start_date, end_date=init_end_date)
    final_start_date = datetime.date( init_start_date.year + 1, init_start_date.month, init_start_date.day)
    final_end_date = datetime.date( init_end_date.year + 1, init_end_date.month, init_end_date.day)
    assert init_start_date != final_start_date
    assert init_end_date != final_end_date
    team_id = helper_db.getTeamByName("init_name").id
    helper_db.updateTeamSeason(team_id, final_start_date, final_end_date)
    new_team_start = helper_db.getTeamById(team_id).season_start_date
    new_team_end = helper_db.getTeamById(team_id).season_end_date
    assert new_team_start == final_start_date
    assert new_team_end == final_end_date

def test_update_entry_values(client):
    '''
    Unit test for updateEntryValues()

    GIVEN: 
        There exists an entry in the database
    WHEN: 
        Invoking the updateEntryValues() on the specified entry
    THEN: 
        Check that the specified entry is updated with the proper values
    '''

    from website.models import Category
    import datetime
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    user_id = helper_db.getUserByName("init_1", "init_2").id
    init_time = datetime.datetime.now()
    helper_db.addEntry(init_time, Category.sleep, 5, "Take a break on saturday.", user_id)
    
    entry = helper_db.getEntriesByUser(user_id)[0]

    new_time = datetime.datetime(init_time.year + 1, init_time.month, init_time.day, 0, 0)
    helper_db.updateEntryValues(entry.id, new_time, Category.force_plate, 10, "Cleared to play on Saturday.", user_id)

    entry = helper_db.getEntryById(entry.id)

    assert entry.time == new_time
    assert entry.category == Category.force_plate
    assert entry.value == 10
    assert entry.notes == "Cleared to play on Saturday."
    assert entry.user_id == user_id


####################################
#                                  #
#   UNIT TESTS FOR DELETE METHODS  #
#                                  #
####################################

def test_delete_user(client):
    '''
    Unit test for deleteUser()

    GIVEN: 
        There exists a user in the database
    WHEN: 
        Invoking the deleteUser() method
    THEN: 
        Check that the database no longer contains that user
    '''

    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    user_id = helper_db.getUserByEmail("email@email.com").id
    helper_db.deleteUser(user_id)
    assert helper_db.getUserByEmail("email@email.com") == None

def test_delete_entry(client):
    '''
    Unit test for deleteEntry()

    GIVEN: 
        There exists a entry in the database
    WHEN: 
        Invoking the deleteEntry() method
    THEN: 
        Check that the database no longer contains that entry 
    '''

    from website.models import Category
    import datetime
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    user_id = helper_db.getUserByName("init_1", "init_2").id
    init_time = datetime.datetime.now()
    helper_db.addEntry(init_time, Category.sleep, 5, "Take a break on saturday.", user_id)
    
    entry_id = helper_db.getEntriesByUser(user_id)[0].id

    helper_db.deleteEntry(entry_id)

    assert helper_db.getEntryById(entry_id) == None
