# Importing the pytest module for testing
import pytest
# Importing the create_test_app function from the website package
from website import create_test_app
# Importing the models from the website package
from website import models
# Importing the views from the website package
from website import views


def test_athlete_login(client):
    '''
    Functional test for test_athlete_login(client)

    GIVEN:
        There exists response and client
    WHEN:
        Calling the post method on the login page for an athlete
    THEN:
        Check that the response status code is 200
    '''

    # Get the response from the client
    response = client.get('/')
    # Check that the response status code is 302
    assert response.status_code == 302 # redirect to login page
    # Check that the response data contains 'Redirecting'
    assert b'Redirecting' in response.data
    # Check that the response data contains 'login'
    assert b'login' in response.data

    # Post the athlete login data to the login page
    client.post("/login",
            data={"email": "jasper@gmail.com",
                        "password": "1234"})

    # Get the response from the client
    response = client.get('/', follow_redirects=True)
    # Check that the response status code is 200
    assert response.status_code == 200 # redirect to login page


def test_coach_login(client):
    '''
    Functional test for test_coach_login(client)

    GIVEN:
        There exists response and client
    WHEN:
        Calling the post method on the login page for a coach
    THEN:
        Check that the response status code is 200
    '''

    # Get the response from the client
    response = client.get('/')
    # Check that the response status code is 302
    assert response.status_code == 302 # redirect to login page
    # Check that the response data contains 'Redirecting'
    assert b'Redirecting' in response.data
    # Check that the response data contains 'login'
    assert b'login' in response.data


    # Post the coach login data to the login page
    client.post("/login",
            data={"email": "kelly@gmail.com",
                        "password": "1234"})

    # Get the response from the client
    response = client.get('/', follow_redirects=True)
    # Check that the response status code is 200
    assert response.status_code == 200 # redirect to login page
