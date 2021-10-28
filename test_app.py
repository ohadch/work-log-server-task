import json

from db import TEST_DB
from fixtures import client


def test_hello_world(client):
    """
    A simple test that checks that the app works
    """

    rv = client.get('/')
    data = json.loads(rv.data)
    assert data['message'] == "Hello world"


def test_add_log_when_user_is_provided(client):
    user = "test1"
    rv = client.post('/work/start', data=json.dumps({"user": user}))
    data = json.loads(rv.data)

    assert data['user'] == user


def test_add_log_when_user_is_not_provided(client):
    rv = client.post('/work/start', data=json.dumps({}))
    data = json.loads(rv.data)

    assert type(data['user']) is str
    assert len(data['user']) > 0


def test_add_log_when_assignment_is_provided(client):
    assignment = "assignment1"
    rv = client.post('/work/start', data=json.dumps({"assignment": assignment}))
    data = json.loads(rv.data)

    assert data['assignment'] == assignment


def test_add_log_when_assignment_is_not_provided(client):
    rv = client.post('/work/start', data=json.dumps({}))
    data = json.loads(rv.data)

    assert type(data['assignment']) is str
    assert len(data['assignment']) > 0


def test_end_log_when_user_is_provided_and_occupied(client):
    user = "user1"
    assignment = "assignment1"

    TEST_DB.add_log(user, assignment)

    rv = client.post('/work/end', data=json.dumps({"user": user}))
    data = json.loads(rv.data)

    assert rv.status_code == 200
    assert data.get("end_at") is not None, "Log end should contain end time"


def test_end_log_when_user_is_provided_and_not_occupied(client):
    user = "test1"
    rv = client.post('/work/end', data=json.dumps({"user": user}))
    data = json.loads(rv.data)

    assert data['user'] == user


def test_end_log_when_user_is_not_provided(client):
    user = "test1"
    rv = client.post('/work/start', data=json.dumps({"user": user}))
    data = json.loads(rv.data)

    assert data['user'] == user


def test_report(client):
    """
    Tests the returned report
    """

    rv = client.get('/report')
    data = json.loads(rv.data)
    assert type(data) is list


# def test_add_valid_work_log(client):
#     """
#     Tests that a new report is added successfully
#     """
#
#     rv = client.get('/report')
#     data = json.loads(rv.data)
#     assert type(data) is list
