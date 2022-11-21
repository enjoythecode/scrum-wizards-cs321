import pytest
from os import path, remove
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import helper_db

# # Function to create an empty database
# @pytest.fixture()
# def create_test_db(client):
#     # Create a test database
#     from website import db
#     DB_NAME = "database.db"
#     db = SQLAlchemy()
#     if path.exists('instance/' + DB_NAME):
#             # # delete the database if it exists
#             remove("instance/" + DB_NAME)
#     db.create_all()

# Unit tests for helper_db.py

# Unit tests for Add Functions

# Unit tests for addUser()
def test_add_user(client):
    helper_db.addUser(email="test@gmail.com", first_name="first", last_name="last", password="test", permission_id=1)
    test_user = helper_db.getUserByEmail("test@gmail.com")
    assert test_user.email == "test_gmail.com" 
    assert test_user.first_name == "first"
    assert test_user.last_name == "last"
    assert test_user.password == "test"
    assert test_user.permission_id == 1

# Unit tests for addTeam()
def test_add_team(client):
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    test_team = helper_db.getTeamByName("test")
    assert test_team.name == "test"
    assert test_team.season_start_date == "2021-01-01"
    assert test_team.season_end_date == "2021-12-31"

# Unit tests for addEntry()
def test_add_entry(client):
    helper_db.addEntry(user_id=1, team_id=1, category=0, date="2021-01-01", duration=1, intensity=1, notes="test")
    test_entry = helper_db.getEntryByDate("2021-01-01")
    assert test_entry.user_id == 1
    assert test_entry.team_id == 1
    assert test_entry.category == 0
    assert test_entry.date == "2021-01-01"
    assert test_entry.duration == 1
    assert test_entry.intensity == 1
    assert test_entry.notes == "test"

# Unit tests for addPermission()
def test_add_permission(client):
    helper_db.addPermission(name="test", can_view_self_entries=True, can_edit_self_entries=True, can_view_own_teams_entries=True, can_edit_own_teams_entries=True, can_view_all_entries=True, can_edit_all_entries=True)
    test_permission = helper_db.getPermissionByName("test")
    assert test_permission.name == "test"
    assert test_permission.can_view_self_entries == True
    assert test_permission.can_edit_self_entries == True
    assert test_permission.can_view_own_teams_entries == True
    assert test_permission.can_edit_own_teams_entries == True
    assert test_permission.can_view_all_entries == True
    assert test_permission.can_edit_all_entries == True

# Unit tests for Get Functions

# Unit tests for getUsers()
def test_get_users(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    user_list = helper_db.getUsers()
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

# Unit tests for getTeams()
def test_get_teams(client):
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    team_list = helper_db.getTeams()
    assert len(team_list) == 1
    assert team_list[0].name == "test"
    assert team_list[0].season_start_date == "2021-01-01"
    assert team_list[0].season_end_date == "2021-12-31"

# Unit tests for getEntries()
def test_get_entries(client):
    import datetime
    current_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time = current_time, category = "psychology", value = 0, notes = "test notes")
    entry_list = helper_db.getEntries()
    assert len(entry_list) == 1
    assert entry_list[0].user_id == 1
    assert entry_list[0].time == current_time
    assert entry_list[0].category == "psychology"
    assert entry_list[0].value == 0
    assert entry_list[0].notes == "test notes"

# Unit tests for getPermissions()
def test_get_permissions(client):
    helper_db.addPermission(name="test", can_view_self_entries=True, can_edit_self_entries=True, can_view_own_teams_entries=True, can_edit_own_teams_entries=True, can_view_all_entries=True, can_edit_all_entries=True)
    permission_list = helper_db.getPermissions()
    assert len(permission_list) == 1
    assert permission_list[0].name == "test"
    assert permission_list[0].can_view_self_entries == True
    assert permission_list[0].can_edit_self_entries == True
    assert permission_list[0].can_view_own_teams_entries == True
    assert permission_list[0].can_edit_own_teams_entries == True
    assert permission_list[0].can_view_all_entries == True
    assert permission_list[0].can_edit_all_entries == True

# Unit tests for getUserByEmail() 
def test_get_user_by_email(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserByEmail("cmgowd25@colby.edu")
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

# Unit tests for getUserByName()
def test_get_user_by_name(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserByName("Chandra", "Gowda")
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

# Unit tests for getUserByID()
def test_get_user_by_id(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    test_user = helper_db.getUserByID(1)
    assert test_user.email == "cmgowd25@colby.edu"
    assert test_user.first_name == "Chandra"
    assert test_user.last_name == "Gowda"
    assert test_user.password == "12345"
    assert test_user.permission_id == 1

# Unit tests for getTeamByName()
def test_get_team_by_name(client):
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    test_team = helper_db.getTeamByName("test")
    assert test_team.name == "test"
    assert test_team.season_start_date == "2021-01-01"
    assert test_team.season_end_date == "2021-12-31"

# Unit tests for getTeamByID()
@pytest.fixture()
def test_get_team_by_id(client):
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    test_team = helper_db.getTeamByID(1)
    assert test_team.name == "test"
    assert test_team.season_start_date == "2021-01-01"
    assert test_team.season_end_date == "2021-12-31"

# Unit tests for getUsersInTeam()
def test_get_users_in_team(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    helper_db.addUserToTeam(user_id=1, team_id=1)
    user_list = helper_db.getUsersInTeam(1)
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

# Unit tests for getPermissionsByName()
def test_get_permissions_by_name(client):
    helper_db.addPermission(name="test", can_view_self_entries=False, can_edit_self_entries=True, can_view_own_teams_entries=False, can_edit_own_teams_entries=True, can_view_all_entries=False, can_edit_all_entries=True)
    permission = helper_db.getPermissionsByName("test")
    assert permission.name == "test"
    assert permission.can_view_self_entries == False
    assert permission.can_edit_self_entries == True
    assert permission.can_view_own_teams_entries == False
    assert permission.can_edit_own_teams_entries == True
    assert permission.can_view_all_entries == False
    assert permission.can_edit_all_entries == True

# Unit tests for getPermissionsByID()
def test_get_permissions_by_id(client):
    helper_db.addPermission(name="test", can_view_self_entries=False, can_edit_self_entries=True, can_view_own_teams_entries=False, can_edit_own_teams_entries=True, can_view_all_entries=False, can_edit_all_entries=True)
    permission = helper_db.getPermissionsByID(1)
    assert permission.name == "test"
    assert permission.can_view_self_entries == False
    assert permission.can_edit_self_entries == True
    assert permission.can_view_own_teams_entries == False
    assert permission.can_edit_own_teams_entries == True
    assert permission.can_view_all_entries == False
    assert permission.can_edit_all_entries == True

# Unit tests for getUsersByPermission()
def test_get_users_by_permission(client):
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addPermission(name="test", can_view_self_entries=False, can_edit_self_entries=True, can_view_own_teams_entries=False, can_edit_own_teams_entries=True, can_view_all_entries=False, can_edit_all_entries=True)
    user_list = helper_db.getUsersByPermission(1)
    assert len(user_list) == 1
    assert user_list[0].email == "cmgowd25@colby.edu"
    assert user_list[0].first_name == "Chandra"
    assert user_list[0].last_name == "Gowda"
    assert user_list[0].password == "12345"
    assert user_list[0].permission_id == 1

# Unit tests for getEntriesById()
def test_get_entries_by_id(client):
    import datetime
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    helper_db.addUserToTeam(user_id=1, team_id=1)
    current_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time = current_time, category = "psychology", value = 0, notes = "test notes")
    entry = helper_db.getEntriesById(1)
    assert entry.user_id == 1
    assert entry.time == current_time
    assert entry.category == "psychology"
    assert entry.value == 0
    assert entry.notes == "test notes"

# Unit tests for getEntriesByUser()
def test_get_entries_by_user(client):
    import datetime
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    helper_db.addUserToTeam(user_id=1, team_id=1)
    current_time = datetime.datetime.now()
    helper_db.addEntry(user_id=1, time = current_time, category = "psychology", value = 0, notes = "test notes")
    entry_list = helper_db.getEntriesByUser(1)
    assert len(entry_list) == 1
    assert entry_list[0].user_id == 1
    assert entry_list[0].time == current_time
    assert entry_list[0].category == "psychology"
    assert entry_list[0].value == 0
    assert entry_list[0].notes == "test notes"

# Unit tests for getEntriesByCategory()
def test_get_entries_by_category(client):
    import datetime
    helper_db.addUser(email="cmgowd25@colby.edu", first_name="Chandra", last_name="Gowda", password="12345", permission_id=1)
    helper_db.addTeam(name="test", season_start_date="2021-01-01", season_end_date="2021-12-31")
    helper_db.addUserToTeam(user_id=1, team_id=1)
    current_time = datetime.datetime.now()
    from helper_db import Category
    helper_db.addEntry(user_id=1, time = current_time, category = Category.psychology, value = 0, notes = "test notes")
    entry_list = helper_db.getEntriesByCategory(Category.psychology)
    assert len(entry_list) == 1
    assert entry_list[0].user_id == 1
    assert entry_list[0].time == current_time
    assert entry_list[0].category == Category.psychology
    assert entry_list[0].value == 0
    assert entry_list[0].notes == "test notes"



    