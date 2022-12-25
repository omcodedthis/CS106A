"""
File: checkerboard.py
----------------
This file creates a canvas and draws a checkerboard on it, made up of alternating black and white squares.
"""


import tkinter
import time
import random

CANVAS_SIZE = 800

N_ROWS = 8
N_COLS = 8
SIZE = CANVAS_SIZE / N_ROWS - 1

# N_ROWS is the total number of rows and can be assumed as x-coordinates.
# N_COLS is the total number of columns and can be assumed as y-coordinates.
# SIZE = is the length of a single sqaure in the checkerboard.



def main():
    canvas = make_canvas(CANVAS_SIZE, CANVAS_SIZE, "Checkerboard")
    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_checkerboard(canvas, row, col)
# This section, firstly draws the canvas and assigns it to a variable called canvas. the nested for loops draw each
# square in the checkerboard. draw_checkerboard sends arguments such as the canvas, the current row and column the
# square is being drawn at.



    canvas.mainloop()
# This section, constantly loops the canvas to allow the user to see the checkerboard.


def draw_checkerboard(canvas, row, col):
    x = row * SIZE
    y = col * SIZE
# x & y are variables that multiply the current number of the row and column by the length of the square,
# thus, evaluating  to the actual coordinates the starting coordinates / origin of the square that is
# currently being drawn.



    canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=color(row, col))
# This function creates a square with an origin of (x,y) and length SIZE. The color of the square is determined by the
# function color().


def color(row, col):
    if (row + col) % 2 == 0:
        return "black"
    else:
        return "white"

# color(row, col) takes in the addition of the current row and column, if the product is even, it returns a black
# square by returning the text "black to the fill parameter. This is because the squares that has to be black has
# one even number, either from the row or column. As such,the addition of any number to an even number will result
# in an even number result and thus divisible by 2 without any remainder.









######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas




if __name__ == '__main__':
    main()
