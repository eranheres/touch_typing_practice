## main.py
import curses
from touch_typing_practice.frontend import Frontend

def main(stdscr):
    frontend = Frontend()
    frontend.run(stdscr)
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
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    curses.wrapper(main)
