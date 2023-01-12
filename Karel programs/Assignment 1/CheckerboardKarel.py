from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    while left_is_clear():
        paint_checkers()


def paint_checkers():
    paint_odd_line()
    paint_even_line()







# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
