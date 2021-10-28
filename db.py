import datetime

from typing import List

from exceptions import UserIsAlreadyOccupiedException
from models import WorkLog


class WorkLogDatabase:

    def __init__(self):
        self.work_logs: List[WorkLog] = []

    def get_open_tasks(self, user: str):
        return [log for log in self.work_logs if log.user == user]

    def add_log(self, user: str, assignment: str):
        print(f"User {user} attempts to start working on {assignment}")
        open_tasks = self.get_open_tasks(user)

        if len(open_tasks) > 0:
            raise UserIsAlreadyOccupiedException(f"User {user} is already working on task: {open_tasks[0].assignment}")

        log = WorkLog(user, assignment, datetime.datetime.now())
        self.work_logs.append(log)

        print(f"User {user} started working on task {assignment}")
        return log

    def end_log(self, user: str, assignment: str):
        pass

    def get_all(self):
        return [log for log in self.work_logs]
