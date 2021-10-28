import tempfile
import json

import pytest

from app import create_app


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        yield client


def test_hello_world(client):
    """
    A simple test that checks that the app works
    """

    rv = client.get('/')
    data = json.loads(rv.data)
    assert data['message'] == "Hello world"