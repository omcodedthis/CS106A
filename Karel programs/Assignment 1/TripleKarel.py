from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    for i in range(3):
        paint_building()
        reposition_karel()
    turn_left()

# main() allows Karel to paint 3 buildings in the world.
# turn_left is added to ensure that it is facing west after painting all the buildings.




def paint_building():
    for i in range(3):
        paint_side()
        move_to_next_wall()

# main() allows Karel to paint 3 walls of a given building.

def paint_side():
    while left_is_blocked():
        put_beeper()
        move()

# paint_side allows Karel to place along a wall.

def move_to_next_wall():
    if left_is_clear():
        turn_left()
        move()

# move_to_next_wall allows Karel to move to the next wall after painting the previous wall.

def reposition_karel():
    turn_left()
    turn_left()
    move()

# reposition_karel allows Karel to reposition itself to begin painting the next building, to match the pre-condition
# of the first building. Thus, paint_building does not have to be changed in order to continue painting.



if __name__ == "__main__":
    run_karel_program()
