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
