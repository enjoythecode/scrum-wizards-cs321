import pytest
from website import create_app


def test_send_admin():

    # redirecting
    flask_app = create_app()
    with flask_app.test_client() as client:


        response = client.get('/superadmin/home.html')
        print(response.data)
        assert response.status_code == 302
        assert b'Redirecting' in response.data
        assert b'Edit Coach Permissions' in response.data

        # making mock database
        assert len(response.athletes) == 4
        assert len(response.athlete_images) == 4
        assert len(response.coach_names) == 4
        assert len(response.coach_images) == 4

    def test_goto_athlete_permissions(client):

        # redirecting
        response = client.get('/superadmin/athletepermissions.html')
        print(response.data)
        assert response.status_code == 302
        assert b'Redirecting' in response.data
        
        # making user
        