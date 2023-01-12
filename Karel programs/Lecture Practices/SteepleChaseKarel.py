from karel.stanfordkarel import *

"""
File: OurSteepleChaseKarel.py
--------------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""


def main():
    for i in range(8):
        if front_is_clear():
            move()
        else:
            ascend_hurdle()
            move()
            descend_hurdle()

def ascend_hurdle():
    turn_left()
    while right_is_blocked():
        move()
    turn_right()

def descend_hurdle():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
