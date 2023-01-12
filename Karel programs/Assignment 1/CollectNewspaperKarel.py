from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    move_to_wall()
    turn_right()
    move_to_door()
    pick_newspaper()
    move_to_wall()
    turn_left()
    move_to_wall()
    flip_side()




def move_to_wall():
    while front_is_clear():
        move()

# move_to_front_wall allows Karel to move to the front wall.

def turn_right():
    for i in range(3):
        turn_left()

# turn_right allows Karel to turn right.

def move_to_door():
    while left_is_blocked():
        move()

# move_to_door allows Karel to move to the door as it the only point where the "box" is open and when Karel's left
# is clear when Karel is facing south.


def pick_newspaper():
    turn_left()
    move()
    pick_beeper()
    flip_side()
    move()
    turn_right()

# pick_newspaper allows Karel to go out of the house, pick the beeper (newspaper) and go back inside the door,
# facing north.


def flip_side():
    for i in range(2):
        turn_left()

# flip_side allows Karel to flip its orientation by rotating 180 degrees.



if __name__ == "__main__":
    run_karel_program()
