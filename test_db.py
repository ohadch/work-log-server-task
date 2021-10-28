import datetime
from freezegun import freeze_time

from db import WorkLogDatabase
from exceptions import UserIsAlreadyOccupiedException


def mocked_get_now(timezone):
    dt = datetime.datetime(2012, 1, 1, 10, 10, 10)
    return timezone.localize(dt)


def test_db_add_log_when_user_is_free():
    db = WorkLogDatabase()

    user, assignment = "user1", "assignment1"
    log = db.add_log(user, assignment)

    assert log.user == user
    assert log.assignment == assignment


def test_db_add_log_when_user_is_occupied():
    db = WorkLogDatabase()

    user, assignment = "user1", "assignment1"
    db.add_log(user, "previous assignment")

    try:
        db.add_log(user, assignment)
    except UserIsAlreadyOccupiedException:
        pass


def test_get_open_task_when_user_has_open_task():
    db = WorkLogDatabase()

    user, assignment = "user1", "assignment1"
    db.add_log(user, assignment)
    task = db.get_open_task(user)

    assert task.user == user


def test_get_open_task_when_user_has_only_closed_tasks():
    db = WorkLogDatabase()

    user, assignment = "user1", "assignment1"
    db.add_log(user, assignment)
    db.end_log(user)

    task = db.get_open_task(user)

    assert task is None


def test_get_open_task_when_user_does_not_have_any_tasks():
    db = WorkLogDatabase()
    task = db.get_open_task("user1")

    assert task is None


def test_end_log_when_user_has_open_task():
    db = WorkLogDatabase()

    with freeze_time("2020-03-25"):
        user, assignment = "user1", "assignment1"
        log = db.add_log(user, assignment)
        db.end_log(user)
        assert log.end_at.year == 2020
        assert log.end_at.month == 3
        assert log.end_at.day == 25
