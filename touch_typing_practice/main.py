## main.py
import curses
from touch_typing_practice.typing_practice import TypingPractice
from touch_typing_practice.user import User

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.echo()
    print("Enter your username: \n\r")
    username = stdscr.getstr(0,0,15).decode("utf-8")
    frontend = Frontend(username)
    frontend.run()
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
