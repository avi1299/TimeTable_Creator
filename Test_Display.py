import pandas as pd
import numpy as np
import sys
import curses


def print_table(ttseq):
    tt_win.clear()
    tt_win.box(curses.ACS_VLINE,curses.ACS_HLINE)
    h,w=tt_win.getmaxyx()
    tt_win.addstr(1,6,"|  8AM-9AM   |  9AM-10AM  | 10AM-11AM  | 11AM-12PM  | 12PM-1PM   |  1PM-2PM   |  2PM-3PM   |  3PM-4PM   |  4PM-5PM   |  5PM-6PM   |  6PM-7PM   |")
    tt_win.addstr(2,2,"____|____________|____________|____________|____________|____________|____________|____________|____________|____________|____________|____________|")
    tt_win.addstr(3,2,"MON |")
    tt_win.addstr(4,2,"TUE |")
    tt_win.addstr(5,2,"WED |")
    tt_win.addstr(6,2,"THU |")
    tt_win.addstr(7,2,"FRI |")
    tt_win.addstr(8,2,"SAT |")
    tt_win.addstr(9,2,"____|____________|____________|____________|____________|____________|____________|____________|____________|____________|____________|____________|")
    m,n=ttseq.shape
    for idx,val in np.ndenumerate(ttseq):
        i,j=idx
        y=int(i)+3
        x=7+13*int(j)
        tt_win.addstr(y,x,str(val)+' '*(12-len(str(val)))+'|')
    tt_win.refresh()
    
def print_classes(sub_code):
    class_win.clear()
    class_win.box(curses.ACS_VLINE,curses.ACS_HLINE)
    if(sub_code):
        class_win.addstr(1,1,str(sub_code))
    class_win.refresh()
    

    
def print_subjects(index):
    sub_win.clear()
    sub_win.box(curses.ACS_VLINE,curses.ACS_HLINE)
    h,w=sub_win.getmaxyx()
    sub_win.addstr(1, w//2-len("SUBJECTS")//2, "SUBJECTS")
    for idx, row in enumerate(crs):
        x = 1
        y = 2 + idx
        if idx == index:
            sub_win.attron(curses.color_pair(1))
            sub_win.addstr(y, x, row)
            sub_win.attroff(curses.color_pair(1))
        else:
            sub_win.addstr(y, x, row)
        sub_win.refresh()
        
def ma(stdscr):
    current_row=0
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    crs.append("Done")
    print_subjects(current_row)
    sample=np.random.randint(1,101,[6,11])
    print_table(sample)
    print_classes(0)
    while (1):
        key = sub_win.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(crs)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_classes(crs[current_row])
            if current_row==len(crs)-1:
                break
        print_subjects(current_row)
        

stdscr=curses.initscr()
h,w=stdscr.getmaxyx()
tt_win=curses.newwin(14,w-46,0,0)
sub_win=curses.newwin(14,44,0,w-45)
class_win=curses.newwin(h-14,w,14,0)
sub_win.keypad(True)
sub_win.box(curses.ACS_VLINE,curses.ACS_HLINE)
curses.curs_set(0)
curses.noecho()
curses.cbreak()

stdscr.keypad(True)
crs=["PHY F110- Physics Lab","PHY F111- MeOW","PHY F112- EMT1","PHY F211- Optics","PHY F222- Classical Mechanics"]
curses.wrapper(ma)

sub_win.keypad(False)
curses.echo()
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()
