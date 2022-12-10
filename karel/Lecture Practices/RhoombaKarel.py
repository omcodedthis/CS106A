from karel.stanfordkarel import * 

"""
File: RhoombaKarel.py
----------------------------
Pick up all the beepers in the world.
"""
def main():
    for i in range(7):
        scan_line()
        move_up()
        scan_line()
"""
This allows Karel to pick all the beepers in the world by scanning each line horizontally and moving up vertically.
"""

def scan_line():
    while front_is_clear():
        check_for_beeper()
        move()
        if beepers_present():
            pick_beeper()

# scan_line allows Karel to pick beepers along a line horizontally in the world

def move_up():
    if front_is_blocked():
        if facing_east():
            turn_left()
            move()
            turn_left()

        else:
            turn_right()
            move()
            turn_right()

# move_up firstly checks which direction Karel is facing and turns left/right depending on the direction he is facing.

def check_for_beeper():
    if beepers_present():
        pick_beeper()

# check_beeper allows Karel to check for beepers at the point before he starts to scan the line.

def turn_right():
    for i in range(3):
        turn_left()

# Gives Karel the power to turn right.










# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
