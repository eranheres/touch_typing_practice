## user.py
import json
from typing import Dict
from touch_typing_practice.session import Session

class User:
    def __init__(self, username: str):
        self.username = username
        self.history = {}

    def record_session(self, session: Session):
        session_statistics = session.calculate_statistics()
        self.history[session.start_time.strftime("%Y-%m-%d %H:%M:%S")] = session_statistics

    def get_statistics(self) -> Dict:
        return self.history

    def save(self):
        with open(f'{self.username}.json', 'w') as file:
            json.dump(self.history, file)

    @classmethod
    def load(cls, username: str):
        try:
            with open(f'{username}.json', 'r') as file:
                history = json.load(file)
        except FileNotFoundError:
            return cls(username)
        else:
            user = cls(username)
            user.history = history
            return user
