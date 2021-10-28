import datetime

from typing import List, Optional

from exceptions import UserIsAlreadyOccupiedException, UserIsNotOccupiedException
from models import WorkLog


class WorkLogDatabase:

    def __init__(self):
        self.work_logs: List[WorkLog] = []

    def get_open_task(self, user: str) -> Optional[WorkLog]:
        tasks = [log for log in self.work_logs if log.user == user]
        if len(tasks) > 0:
            return tasks[0]
        return None

    def add_log(self, user: str, assignment: str) -> WorkLog:
        """
        Creates a new work log for a user on an assignment.
        If the user is already occupied, raises UserIsAlreadyOccupiedException
        :param user: The working user
        :param assignment: The assignment that the user attempts to start working on
        :return: The created work log object
        """

        print(f"User {user} attempts to start working on {assignment}")
        open_task = self.get_open_task(user)

        if open_task is not None:
            raise UserIsAlreadyOccupiedException(f"User {user} is already working on task: {open_task.assignment}")

        log = WorkLog(user, assignment, datetime.datetime.now())
        self.work_logs.append(log)

        print(f"User {user} started working on task {assignment}")
        return log

    def end_log(self, user: str) -> WorkLog:
        """
        Adds end_at value to the user's open task.
        If the user is free, raises UserIsNotOccupiedException
        :param user:
        :return:
        """
        log = self.get_open_task(user)
        if log is None:
            raise UserIsNotOccupiedException(f"User {user} is attempting to work on his current task,"
                                             f"but he is currently not working on anything")
        log.end_at = datetime.datetime.now()
        return log

    def get_all(self):
        return [log for log in self.work_logs]
