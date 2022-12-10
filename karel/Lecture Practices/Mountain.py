from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size
and plants a beeper at the top
"""
def main():
    ascend_mountain()
    put_beeper()
    descend_mountain()

def ascend_mountain():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()

def descend_mountain():
    while front_is_clear():
        move()
        turn_right()
        move()
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()











if __name__ == "__main__":
    run_karel_program()