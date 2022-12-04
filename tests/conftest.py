import pytest
from website import create_test_app

@pytest.fixture()
def app():

    app = create_test_app()
    with app.app_context():
        app.config.update({
        "TESTING": True,
        })

        yield app


@pytest.fixture()
def client(app):
    return app.test_client()
