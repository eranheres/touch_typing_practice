import curses

from touch_typing_practice.typing_practice import TypingPractice
from touch_typing_practice.user import User


class Frontend:
    def __init__(self, username: str):
        self.user = User.load(username)
        self.typing_practice = TypingPractice(self.user)

    def start_session(self):
        print("Enter text for the session: ")
        text = input()
        self.typing_practice.start_session(text)
        print("Start typing: ")
        typed_text = input()
        self.typing_practice.end_session(typed_text)
        print("Session ended. Your progress has been recorded.")

    def display_statistics(self):
        statistics = self.typing_practice.get_user_statistics()
        for session_time, session_statistics in statistics.items():
            print(f"Session at {session_time}:")
            for stat, value in session_statistics.items():
                print(f"  {stat}: {value}")

    def run(self):
        while True:
            print("1. Start new session")
            print("2. View statistics")
            print("3. Exit")
            try:
                choice = int(input())
            except ValueError:
                print("Invalid choice. Please try again.")
                continue

            if choice == 1:
                self.start_session()
            elif choice == 2:
                self.display_statistics()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")
