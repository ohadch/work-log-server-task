import json

from fixtures import client


def test_hello_world(client):
    """
    A simple test that checks that the app works
    """

    rv = client.get('/')
    data = json.loads(rv.data)
    assert data['message'] == "Hello world"


def test_report(client):
    """
    Tests the returned report
    """

    rv = client.get('/report')
    data = json.loads(rv.data)
    assert type(data) is list


def test_add_valid_work_log(client):
    """
    Tests that a new report is added successfully
    """

    rv = client.get('/report')
    data = json.loads(rv.data)
    assert type(data) is list
