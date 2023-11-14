## main.py
import curses
from touch_typing_practice.frontend import Frontend

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.echo()
    print("Enter your username: \n\r")
    username = stdscr.getstr(0,0,15).decode("utf-8")
    frontend = Frontend(username)

frontend.start()

if __name__ == "__main__":
    curses.wrapper(main)
