import datetime

from typing import Optional


class WorkLog:

    def __init__(self, user: str, assignment: str, start_at: datetime.datetime):
        self.user: str = user
        self.assignment: str = assignment
        self.start_at: datetime.datetime = start_at
        self.end_at: Optional[datetime.datetime] = None

    def duration_hours(self) -> float:
        """
        Returns the length of the task in hours
        :return: The length of the task in hours
        """
        diff = (self.end_at or datetime.datetime.now()) - self.start_at
        return diff.total_seconds() / 3600

    def __repr__(self):
        return f"WorkLog(user={self.user}, assignment={self.assignment}, ended={'Yes' if self.end_at is not None else 'No'})"

    def __dict__(self) -> dict:
        return {
            "user": self.user,
            "assignment": self.assignment,
            "start_at": self.start_at.isoformat(),
            "end_at": None if self.end_at is None else self.end_at.isoformat(),
            "duration_hours": int(self.duration_hours())
        }
