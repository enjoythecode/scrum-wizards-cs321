# Importing pytest for unit testing
import pytest
# Importing helper_db to test the functions
from website import helper_db, addDummyTeams, addDummyUserList, addDummyUser, addDummyEntriesList, addPermissionList, addDummyEntry, addDummyEntriesList, addDummyDB

# Importing app and client from conftest.py
from conftest import app, client
# Importing models to test the database
from website.models import User, Team, Entry, Category, Permission

def test_addDummyTeams(client):
    addDummyTeams()

    assert helper_db.getTeamByName("Men's Basketball")
    assert helper_db.getTeamByName("Men's Crew")
    assert helper_db.getTeamByName("Men's Cross Country")
    assert helper_db.getTeamByName("Men's Football")
    assert helper_db.getTeamByName("Men's Golf")
    assert helper_db.getTeamByName("Men's Lacrosse")
    assert helper_db.getTeamByName("Men's Alpine Skiing")
    assert helper_db.getTeamByName("Men's Basketball")
    assert helper_db.getTeamByName("Men's Basketball")
    assert helper_db.getTeamByName("Men's Basketball")
    assert helper_db.getTeamByName("Men's Basketball")
    assert helper_db.getTeamByName("Men's Soccer")
    assert helper_db.getTeamByName("Men's Basketball")
    assert helper_db.getTeamByName("Men's Squash")
    assert helper_db.getTeamByName("Men's Swimming & Diving")
    assert helper_db.getTeamByName("Men's Tennis")
    assert helper_db.getTeamByName("Men's Track & Field")
    assert helper_db.getTeamByName("Women's Crew")
    assert helper_db.getTeamByName("Women's Field Hockey")
    assert helper_db.getTeamByName("Women's Ice Hockey")
    assert helper_db.getTeamByName("Women's Lacrosse")
    assert helper_db.getTeamByName("Women's Ice Hockey")
    assert helper_db.getTeamByName("Women's Alpine Skiing")
    assert helper_db.getTeamByName("Women's Soccer")
    assert helper_db.getTeamByName("Women's Squash")
    assert helper_db.getTeamByName("Women's Swimming & Diving")
    assert helper_db.getTeamByName("Women's Tennis")
    assert helper_db.getTeamByName("Women's Track & Field")
    assert helper_db.getTeamByName("Women's Cross Country")
    assert helper_db.getTeamByName("Women's Tennis")
    assert helper_db.getTeamByName("Women's Volleyball")


def test_addDummyUserList(client):
    addDummyUserList()
    addDummyUser()

    assert len(helper_db.getUsers()) == 106

    assert helper_db.getUserByName(first_name = "Chandra", last_name = "Gowda")
    assert helper_db.getUserByName(first_name = "Sinan", last_name = "Yumurtaci")
    assert helper_db.getUserByName(first_name = "Kelly", last_name = "Putnam")
    assert helper_db.getUserByName(first_name = "Jasper", last_name = "Loverude")
    assert helper_db.getUserByName(first_name = "Zehra", last_name = "")
    assert helper_db.getUserByName(first_name = "Ghailan", last_name = "")

def test_addPermissionList(client):
    addPermissionList()

    assert helper_db.getPermissionByName("SuperAdmin").id == 0
    assert helper_db.getPermissionByName("Admin").id == 1
    assert helper_db.getPermissionByName("Coach").id == 2
    assert helper_db.getPermissionByName("Player").id == 3

def test_addDummyEntry(client):
    addDummyUser()
    addDummyEntry()

    test_user_id = helper_db.getUserByName("Chandra", "Gowda").id
    test_entry = helper_db.getEntriesByUser(test_user_id)[0]
    assert test_entry.category == Category.sleep
    assert test_entry.value == 8

def test_addDummyEntriesList(client):
    addDummyUserList()
    addDummyUser()
    addDummyEntriesList()

    assert len(helper_db.getEntries()) == 100

    entries = []

    entries.append(helper_db.getEntriesByCategory(1))
    entries.append(helper_db.getEntriesByCategory(2))
    entries.append(helper_db.getEntriesByCategory(3))
    entries.append(helper_db.getEntriesByCategory(4))

    assert len(entries) == 4


def test_addDummyDB(client):

    addDummyDB()

    assert len(helper_db.getEntries()) == 100

    entries = []

    entries.append(helper_db.getEntriesByCategory(1))
    entries.append(helper_db.getEntriesByCategory(2))
    entries.append(helper_db.getEntriesByCategory(3))
    entries.append(helper_db.getEntriesByCategory(4))

    assert len(entries) == 4

    test_user_id = helper_db.getUserByName("Chandra", "Gowda").id
    test_entry = helper_db.getEntriesByUser(test_user_id)[0]
    assert test_entry.value == 0

    assert len(helper_db.getTeams()) == 30
