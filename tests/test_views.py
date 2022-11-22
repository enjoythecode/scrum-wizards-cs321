'''
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


def test_athlete_login(client):

    response = client.get('/')
    assert response.status_code == 302 # redirect to login page
    assert b'Redirecting' in response.data
    assert b'login' in response.data

    client.post("/login", 
            data={"email": "jasper@gmail.com",
                        "password": "1234"})

    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200 # redirect to login page
    assert b'Notes:' in response.data

def test_coach_login(client):

    response = client.get('/')
    assert response.status_code == 302 # redirect to login page
    assert b'Redirecting' in response.data
    assert b'login' in response.data

    client.post("/login", 
            data={"email": "kelly@gmail.com",
                        "password": "1234"})

    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200 # redirect to login page
    assert b'Team:' in response.data
'''