import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, "Hello")  # Add "Hello" to the screen
    stdscr.refresh()  # Refresh the screen to display changes
    stdscr.getkey()  # Wait for a key press

# Ensure the wrapper is called at the top level
wrapper(main)