import sys
import os
import pytest

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from app import create_app, db

@pytest.fixture(scope="module")
def test_client():
    """
    Create a Flask test client and configure an in-memory SQLite database.
    """
    flask_app = create_app()
    flask_app.config["TESTING"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # In-memory DB
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Create the test client
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()  # Create the tables
            yield testing_client  # Provide the test client to the tests
            db.session.remove()
            db.drop_all()  # Drop all tables after tests
