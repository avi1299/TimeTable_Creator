import pandas as pd
import numpy as np
import sys
import curses
import curses
    
def print_subjects(stdscr, index):
    stdscr.clear()
    h,w=stdscr.getmaxyx()
    stdscr.addstr(0, w-25-len("SUBJECTS")//2, "SUBJECTS")
    for idx, row in enumerate(crs):
        x = w-50
        y = 1 + idx
        if idx == index:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
        stdscr.refresh()
    
def ma(stdscr):
    current_row=0
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    print_subjects(stdscr, current_row)
    while (1):
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(crs)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break
        print_subjects(stdscr,current_row)

stdscr=curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
crs=["PHY F110- Physics Lab","PHY F111- MeOW","PHY F112- EMT1","PHY F211- Optics","PHY F222- Classical Mechanics"]
curses.wrapper(ma)

curses.echo()
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
