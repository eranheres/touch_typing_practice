## main.py
import curses
from touch_typing_practice.frontend import FrontEnd
from touch_typing_practice.user import User

def main(stdscr):
    """
    Main function to initialize the application.
    :param stdscr: standard screen object from curses library
    """
    # Clear screen
    stdscr.clear()
    curses.echo()
    print("Enter your username: \n\r")
    username = stdscr.getstr(0,0,15)
    user = User.load(username)
    frontend = FrontEnd(user, stdscr)
    frontend.run()
        print("1. Start new session\r")
        print("2. View statistics\r")
        print("3. Exit\r\n")
        try:
            choice = int(stdscr.getstr(0,0,3))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            print("Enter text for the session: ")
            text = stdscr.getstr(0, 0, 100)
            typing_practice.start_session(text)
            print("Start typing: ")
            typed_text = stdscr.getstr(0, 0, 100)
            typing_practice.end_session(typed_text)
            print("Session ended. Your progress has been recorded.")
        elif choice == 2:
            statistics = typing_practice.get_user_statistics()
            for session_time, session_statistics in statistics.items():
                print(f"Session at {session_time}:")
                for stat, value in session_statistics.items():
                    print(f"  {stat}: {value}")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    curses.wrapper(main)
## frontend.py
import curses
from touch_typing_practice.typing_practice import TypingPractice

class FrontEnd:
    """
    Class to handle the frontend functions of the application.
    """
    def __init__(self, user, stdscr):
        """
        Initialize FrontEnd with a user and standard screen object.
        :param user: User object
        :param stdscr: standard screen object from curses library
        """
        self.typing_practice = TypingPractice(user)
        self.stdscr = stdscr

    def run(self):
        """
        Run the frontend application.
        """
        while True:
            print("1. Start new session\r")
            print("2. View statistics\r")
            print("3. Exit\r\n")
            try:
                choice = int(self.stdscr.getstr(0,0,3))
            except ValueError:
                print("Invalid choice. Please try again.")
                continue

            if choice == 1:
                print("Enter text for the session: ")
                text = self.stdscr.getstr(0, 0, 100)
                self.typing_practice.start_session(text)
                print("Start typing: ")
                typed_text = self.stdscr.getstr(0, 0, 100)
                self.typing_practice.end_session(typed_text)
                print("Session ended. Your progress has been recorded.")
            elif choice == 2:
                statistics = self.typing_practice.get_user_statistics()
                for session_time, session_statistics in statistics.items():
                    print(f"Session at {session_time}:")
                    for stat, value in session_statistics.items():
                        print(f"  {stat}: {value}")
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")
