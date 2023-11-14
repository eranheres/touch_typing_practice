from touch_typing_practice.user import User
from touch_typing_practice.session import Session

class TypingPractice:
    def __init__(self, user: User):
        self.user = user
        self.current_session = None

    def start_session(self, text: str):
        if self.current_session is not None:
            raise Exception("A session is already in progress. Please end the current session before starting a new one.")
        self.current_session = Session(text)
        self.current_session.start()

    def end_session(self, typed_text: str):
        if self.current_session is None:
            raise Exception("No session is in progress. Please start a session before ending it.")
        self.current_session.end(typed_text)
        self.user.record_session(self.current_session)
        self.user.save()
        self.current_session = None

    def get_user_statistics(self):
        return self.user.get_statistics()
