import pytest
from app import app, birthdays_db, UserModel


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            birthdays_db.create_all()
        yield client


def test_index_route(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Birthday Tracker Application" in response.data


def test_add_birthday(client):
    """Test adding a birthday entry"""
    response = client.post('/add', data={'name': 'John', 'year': 1990, 'month': 5, 'day': 10})
    assert response.status_code == 302  # Check if redirected after adding
    with app.app_context():
        user = UserModel.query.filter_by(name='John').first()
        assert user is not None  # Check if the user exists in the database


def test_delete_birthday(client):
    """Test deleting a birthday entry"""
    with app.app_context():
        # Add a user to the database
        user = UserModel(name='Alice', year=1985, month=3, day=15)
        birthdays_db.session.add(user)
        birthdays_db.session.commit()

    # Attempt to delete the user
    response = client.post('/delete/Alice')
    assert response.status_code == 302  # Check if redirected after deleting
    with app.app_context():
        user = UserModel.query.filter_by(name='Alice').first()
        assert user is None  # Check if the user no longer exists in the database
