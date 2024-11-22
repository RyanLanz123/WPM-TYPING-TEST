import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    # Display target text
    stdscr.addstr(0, 0, target)

    # Display current text with color highlighting
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # Green for correct
        if char != correct_char:
            color = curses.color_pair(2)  # Red for incorrect
        stdscr.addstr(0, i, char, color)

    # Display WPM
    stdscr.addstr(1, 0, f"WPM: {wpm}")

def wpm_test(stdscr):
    target_text = "Hello world"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # Escape key to exit
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):  # Handle backspace
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):  # Add valid characters
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correct character
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Incorrect character
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

# Ensure the wrapper is called at the top level
wrapper(main)
