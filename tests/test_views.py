import pytest
from website import create_test_app
from website import models
from website import views


def test_send_admin(client):

    # testing the redirecting to a home page for a PEAK admin

    response = client.get('/superadmin/home.html')
    print(response.data)
    assert response.status_code == 200
    assert b'Edit Coach Permissions' in response.data



def test_send_superadmin(client):

    # testing the redirecting to a home page for a superadmin

    response = client.get('/superadmin/home.html')
    print(response.data)
    assert response.status_code == 200
    assert b'Edit Athlete Permissions' in response.data


def test_goto_athlete_permissions(client):

    # testing the redirecting to change the permissions of athlete with id 2 
    response = client.get('/superadmin/athletepermissions.html/2')
    print(response.data)
    assert response.status_code == 200
    assert b'Team' in response.data

    # testing the redirecting to change the permissions of athlete with id 4 
    response2 = client.get('/superadmin/athletepermissions.html/4')
    print(response2.data)
    assert response2.status_code == 200
    assert b'Team' in response2.data

def test_goto_coach_permissions(client):

    # testing the redirecting to change the permissions of coach with id 6 
    response = client.get('/superadmin/coachpermissions.html/6')
    print(response.data)
    assert response.status_code == 200
    assert b'Team' in response.data

    # testing the redirecting to change the permissions of coach with id 7 
    response2 = client.get('/superadmin/coachpermissions.html/7')
    print(response2.data)
    assert response2.status_code == 200
    assert b'Team' in response2.data

def test_send_athlete(client):
    # testing the redirecting to the athlete page 
    response = client.get('/athlete')
    print(response.data)
    assert response.status_code == 200
    assert b'Sleep' in response.data
    assert b'Readyness' in response.data
    assert b'Calorie' in response.data
    assert b'Weekly Overview' in response.data

def test_send_individual(client):
    # testing the redirecting to the individual dashboard for athlete
    response = client.get('/individual_dashboard')
    print(response.data)
    assert response.status_code == 200
    assert b'Sleep' in response.data
    assert b'Readyness' in response.data
    assert b'Calorie' in response.data
    assert b'Overview' in response.data
    assert b'Notes' in response.data

def test_send_coach(client):
    # testing the redirecting to the coach home page 
    response = client.get('/coach_dashboard')
    print(response.data)
    assert response.status_code == 200
    assert b'Team Overview' in response.data
    assert b'Athletes' in response.data

def test_send_team(client):
    # testing the redirecting to the team dashboards
    response = client.get('/team_dashboard')
    print(response.data)
    assert response.status_code == 200
    assert b'Team Averages' in response.data



