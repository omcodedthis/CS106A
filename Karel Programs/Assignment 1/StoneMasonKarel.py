from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    while front_is_clear():
        repair_column()
        move_to_next_column()
    repair_column()

# main allows Karel to repair each column and move to the next column. The additional repair_column was added to
# prevent an "off by one" error as the front is not clear as Karel approaches the final column.





def repair_column():
    check_for_base_beeper()
    scale_column()
    rotate()
    scale_column()
    turn_left()

# repair_column allows Karel to scale up and scale down a column, fixing it in the process by placing beepers.
# turn_left is added to ensure that Karel is facing east to match the pre-condition of repairing the first column.


def check_for_base_beeper():
    if beepers_present():
        turn_left()
    else:
        put_beeper()
        turn_left()

# check_for_base_beeper allows Karel to check the base of the column and places a beeper if required.


def scale_column():
    while front_is_clear():
        check_for_beeper()

# scale_up allows Karel to check for beepers at the base and then scale up the column,
# fixing it in the process using check_for_beeper.


def check_for_beeper():
    if beepers_present():
        move()
    else:
        put_beeper()

# check_for_beeper checks for beepers and places a beeper (fixing the column) if no beeper is present.

def rotate():
    for i in range(2):
        turn_left()

# rotate allows Karel to face the floor in order for it to scale down the column.

def move_to_next_column():
    for i in range(4):
        move()

# move_to_next_column allows Karel to move to the next column which is always four corners apart.



if __name__ == "__main__":
    run_karel_program()
