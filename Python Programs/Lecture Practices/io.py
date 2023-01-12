"""
File: io.py
------------------
prints a series of "io"s that create a the illusion that the "io" is bouncing.
"""

"""
NOTE THAT FOR WHEN BOUNCING IS REFERENCED, IT IS RELATIVE TO THE VERTICAL LHS OF THE SCREEN. FOR EXAMPLE, 
BOUNCING UP - MOVING AWAY FROM THE LHS.
"""
import math

MAX_LENGTH = 20
# This constant determines the length of the "io" line, and is also used to determine the max number of spaces before
# io in a given line horizontally.


def main():
    for i in range(MAX_LENGTH):
        print_io_line(i)
# this section of the body prints the "io" that is bouncing up.


    for i in range(MAX_LENGTH):
        print_io_line(MAX_LENGTH - i)
# this section of the body prints the "io" that is bouncing down.


    for i in range(MAX_LENGTH):
        print_i_and_o_line(i)
# this section of the body prints the "i" always at the LHS and the "o" bouncing up.



    for i in range(MAX_LENGTH):
        print_i_and_o_line(MAX_LENGTH - i)
# this section of the body prints the "i" always at the LHS and the "o" bouncing down.







def print_io_line(spaces_before_io):
    print_n_spaces(spaces_before_io)
    print("io")


def print_i_and_o_line(spaces_before_io):
    print("i", end="")
    print_n_spaces(spaces_before_io)
    print("o")



def print_n_spaces(n):
    for i in range(n):
        print_space_no_new_line(" ")

# spaces_before_io is the same as n, just different variable notations as they created in different functions.



















def print_space_no_new_line(to_print):
    print(to_print, end="")
# takes in a string, and prints without the enter

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()