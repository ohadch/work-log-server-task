import datetime

from typing import Optional


class WorkLog:

    def __init__(self,user: str, assignment: str, start_at: datetime.datetime, end_at: Optional[datetime.datetime]):
        self.user: str = user
        self.assignment: str = assignment
        self.start_at: datetime.datetime = start_at
        self.end_at: Optional[datetime.datetime] = end_at

    def duration_hours(self) -> float:
        """
        Returns the length of the task in hours
        :return: The length of the task in hours
        """
        diff = (self.end_at or datetime.datetime.now()) - self.start_at
        return diff.total_seconds() / 3600

    def __dict__(self) -> dict:
        return {
            "user": self.user,
            "name": self.assignment,
            "duration_hours": self.duration_hours()
        }
