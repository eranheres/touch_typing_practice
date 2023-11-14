import curses
from touch_typing_practice.typing_practice import TypingPractice
from touch_typing_practice.user import User

class Frontend:
    def __init__(self):
        self.typing_practice = None

    def get_username(self, stdscr):
        stdscr.clear()
        curses.echo()
        stdscr.addstr("Enter your username: \n\r")
        username = stdscr.getstr(0,0,15)
        return username

    def get_menu_choice(self, stdscr):
        stdscr.clear()
        stdscr.addstr("1. Start new session\r")
        stdscr.addstr("2. View statistics\r")
        stdscr.addstr("3. Exit\r\n")
        try:
            choice = int(stdscr.getstr(0,0,3))
        except ValueError:
            stdscr.addstr("Invalid choice. Please try again.")
            return None
        return choice

    def get_session_text(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Enter text for the session: ")
        text = stdscr.getstr(0, 0, 100)
        return text

    def get_typed_text(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Start typing: ")
        typed_text = stdscr.getstr(0, 0, 100)
        return typed_text

    def display_statistics(self, stdscr):
        stdscr.clear()
        statistics = self.typing_practice.get_user_statistics()
        for session_time, session_statistics in statistics.items():
            stdscr.addstr(f"Session at {session_time}:\n")
            for stat, value in session_statistics.items():
                stdscr.addstr(f"  {stat}: {value}\n")

    def run(self, stdscr):
        username = self.get_username(stdscr)
        user = User.load(username)
        self.typing_practice = TypingPractice(user)

        while True:
            choice = self.get_menu_choice(stdscr)
            if choice == 1:
                text = self.get_session_text(stdscr)
                self.typing_practice.start_session(text)
                typed_text = self.get_typed_text(stdscr)
                self.typing_practice.end_session(typed_text)
                stdscr.addstr("Session ended. Your progress has been recorded.")
            elif choice == 2:
                self.display_statistics(stdscr)
            elif choice == 3:
                break
            else:
                stdscr.addstr("Invalid choice. Please try again.")
