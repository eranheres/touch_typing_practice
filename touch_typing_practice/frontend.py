import curses
from touch_typing_practice.typing_practice import TypingPractice
from touch_typing_practice.user import User

class Frontend:
    def __init__(self, username: str):
        self.user = User.load(username)
        self.typing_practice = TypingPractice(self.user)

    def get_user_input(self, prompt: str, max_length: int):
        print(prompt)
        return curses.getstr(0, 0, max_length)

    def display_options(self):
        print("1. Start new session")
        print("2. View statistics")
        print("3. Exit")

    def start_typing_session(self):
        text = self.get_user_input("Enter text for the session: ", 100)
        self.typing_practice.start_session(text)
        print("Start typing: ")

    def end_typing_session(self):
        typed_text = self.get_user_input("", 100)
        self.typing_practice.end_session(typed_text)
        print("Session ended. Your progress has been recorded.")

    def display_user_statistics(self):
        statistics = self.typing_practice.get_user_statistics()
        for session_time, session_statistics in statistics.items():
            print(f"Session at {session_time}:")
            for stat, value in session_statistics.items():
                print(f"  {stat}: {value}")
