# Importing the pytest module for testing
import pytest
# Importing the create_test_app function from the website package
from website import create_test_app

# Creating a fixture for the app
@pytest.fixture()
def app():
    # Creating a test app
    app = create_test_app()
    # Configuring the app
    with app.app_context():
        # Setting the testing flag to True
        app.config.update({
        "TESTING": True,
        })
        yield app

# Creating a fixture for the client
@pytest.fixture()
def client(app):
    # Returning the test client
    return app.test_client()
