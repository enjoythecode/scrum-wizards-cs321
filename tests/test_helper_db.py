import pytest
from os import path, remove
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import helper_db
from conftest import app, client
from website.models import User, Team, Entry, Category, Permission

# Unit tests for addUser()
def test_add_user(client):
    '''
    GIVEN a User model 
    WHEN a new User is created
    THEN check the email, first_name, last_name, password, permission_id
    '''
    helper_db.addUser(email="test@gmail.com", first_name="first", last_name="last", password="test", permission_id=1)
    test_user = helper_db.getUserByEmail("test@gmail.com")
    assert test_user.email == "test@gmail.com" 
    assert test_user.first_name == "first"
    assert test_user.last_name == "last"
    assert test_user.password == "test"
    assert test_user.permission_id == 1


# # Unit tests for addTeam()
def test_add_team(client):
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


# # Unit tests for addEntry()
def test_add_entry(client):
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

# # Unit tests for addPermission()
def test_add_permission(client):
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

# # Unit tests for Get Functions

# # Unit tests for getUsers()
def test_get_users(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    user_list = helper_db.getUsers()
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

# # Unit tests for getTeams()
def test_get_teams(client):
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

# # Unit tests for getEntries()
def test_get_entries(client):
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

# # Unit tests for getPermissions()
def test_get_permissions(client):
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

# # Unit tests for getUserByEmail() 
def test_get_user_by_email(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserByEmail("cmgowd25@colby.edu")
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

# # Unit tests for getUserByName()
def test_get_user_by_name(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserByName("Chandra", "Gowda")
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

# # Unit tests for getUserByID()
def test_get_user_by_id(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserById(1)
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

# # Unit tests for getTeamByName()
def test_get_team_by_name(client):
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

# # Unit tests for getTeamByID()
def test_get_team_by_id(client):
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

# # Unit tests for getUsersInTeam()
def test_get_users_in_team(client):
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

# # Unit tests for getPermissionsByName()
def test_get_permissions_by_name(client):
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

# # Unit tests for getPermissionsByID()
def test_get_permissions_by_id(client):
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

# # Unit tests for getUsersByPermission()
def test_get_users_by_permission(client):
    helper_db.addPermission(id = 1, name="test", can_view_self_entries=False, can_edit_self_entries=True, can_view_own_teams_entries=False, can_edit_own_teams_entries=True, can_view_all_entries=False, can_edit_all_entries=True)
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    user_list = helper_db.getUsersByPermission(1)
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

# # Unit tests for getEntriesById()
def test_get_entries_by_id(client):
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

# # Unit tests for getEntriesByUser()
def test_get_entries_by_user(client):
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

# Unit tests for getEntriesByCategory()
def test_get_entries_by_category(client):
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


# Tests update username method
def test_update_full_username(client):
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=1)
    user_id = helper_db.getUserByEmail("email@email.com").id
    helper_db.updateUserFullName(user_id, "final_1", "final_2")
    updated_user = helper_db.getUserByName("final_1", "final_2")
    assert updated_user.first_name == "final_1"
    assert updated_user.last_name == "final_2"

# Tests update username method
def test_update_user_permission(client):
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    user_id = helper_db.getUserByEmail("email@email.com").id
    helper_db.updateUserPermission(user_id, 2)
    updated_user_permission_id = helper_db.getUserByEmail("email@email.com").permission_id
    assert updated_user_permission_id == 2

# Tests add user to team method
def test_add_user_to_team(client):
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

# Tests remove user from team method
def test_remove_user_from_team(client):
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

# Tests remove user from team method
def test_update_team_name(client):
    import datetime
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    helper_db.addTeam(name="init_name", start_date=start_date, end_date=end_date)
    team_id = helper_db.getTeamByName("init_name").id
    helper_db.updateTeamName(team_id, "new_name")
    team_name = helper_db.getTeamById(team_id).name
    assert team_name == "new_name"

# Tests update team season start/end
def test_update_team_season_start_end(client):
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

# Test update entry values (notes, time, value, category, etc...)
def test_update_entry_values(client):
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

# Test Delete functions for models.py

# Test for delete user functinoality
def test_delete_user(client):
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    user_id = helper_db.getUserByEmail("email@email.com").id
    helper_db.deleteUser(user_id)
    assert helper_db.getUserByEmail("email@email.com") == None

# Test delete user functionality
def test_delete_entry(client):
    from website.models import Category
    import datetime
    helper_db.addUser("email@email.com", "init_1", "init_2", "1234", permission_id=0)
    user_id = helper_db.getUserByName("init_1", "init_2").id
    init_time = datetime.datetime.now()
    helper_db.addEntry(init_time, Category.sleep, 5, "Take a break on saturday.", user_id)
    
    entry_id = helper_db.getEntriesByUser(user_id)[0].id

    helper_db.deleteEntry(entry_id)

    assert helper_db.getEntryById(entry_id) == None
