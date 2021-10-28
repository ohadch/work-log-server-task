import datetime
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

    assert rv.status_code == 403
    assert data["error"] == f'User {user} is attempting to work on his current task,but he is currently not working on anything'


def test_end_log_when_user_is_not_provided(client):
    rv = client.post('/work/end', data=json.dumps({}))
    data = json.loads(rv.data)

    assert rv.status_code == 400
    assert data["error"] == "Must provide user in order to end his work"


def test_report(client):
    """
    Tests the returned report
    """

    log_1 = TEST_DB.add_log("user1", "assignment 1")
    log_1.end_at = log_1.start_at + datetime.timedelta(hours=2)

    log_2 = TEST_DB.add_log("user2", "assignment 2")
    log_2.end_at = log_2.start_at + datetime.timedelta(hours=3)

    rv = client.get('/report')
    data = json.loads(rv.data)

    assert rv.status_code == 200
    assert type(data) is list
    assert len(data) == 2
    assert data[0]['duration_hours'] == 2
    assert data[1]['duration_hours'] == 3
