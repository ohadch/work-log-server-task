from db import WorkLogDatabase
from exceptions import UserIsAlreadyOccupiedException


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
        log = db.add_log(user, assignment)
    except UserIsAlreadyOccupiedException:
        pass
