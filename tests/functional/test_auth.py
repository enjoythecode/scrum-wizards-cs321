import pytest
from website import create_test_app
from website import models
from website import views


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
   