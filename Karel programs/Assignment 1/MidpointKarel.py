from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    put_beeper()
    while front_is_clear():
        paint_corner(RED)
        move_to_edge()
        paint_corner(RED)
        turn_around()
        move_to_edge()
        while corner_color_is(YELLOW):
            put_beeper()
        while corner_color_is(WHITE):
            move()
        while corner_color_is(RED):
            turn_around()
            move()
            paint_corner(YELLOW)
            move()
            paint_corner(YELLOW)
            move_to_red()


def move_to_red():
    while corner_color_is(WHITE):
        move()
        put_beeper()
    while corner_color_is(RED):
        turn_around()
        move()
        paint_corner(RED)
        move()
    while corner_color_is(YELLOW):
        put_beeper()
        clean_up()



def turn_around():
    for i in range(2):
        turn_left()


def move_to_edge():
    while front_is_clear():
        move()

def clean_up():
    while front_is_clear():
        paint_corner(WHITE)
        move()
    paint_corner(WHITE)
    turn_around()
    while front_is_clear():
        paint_corner(WHITE)
        move()
    pick_beeper()
    paint_corner(WHITE)
    turn_around()
    while front_is_clear():
        if beepers_present():
            turn_left()
        else:
            move()





if __name__ == "__main__":
    run_karel_program()
