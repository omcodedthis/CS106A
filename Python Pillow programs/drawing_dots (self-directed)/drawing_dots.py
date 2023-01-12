"""
File: drawing_dots.py
----------------
A one of a kind art piece, a mosaic of dots, is created each time the program runs. No two pieces are unique.
"""


import tkinter
import time
import random
from PIL import ImageTk
from PIL import Image

HEIGHT = 400
WIDTH = 400
DIAMETER = 26
# HEIGHT determines the height of the canvas.
# WIDTH determines the width of the canvas.
# DIAMETER determines the diameter of each dot.



def main():
    canvas = make_canvas(HEIGHT, WIDTH, "dots")
    create_art(canvas)
    canvas.mainloop()
# main() creates a canvas and draws dots on the canvas. canvas.mainloop() constantly loops the canvas for
# the user to see.




def create_art(canvas):
    MAX_DOTS = random.randint(1, 99)
# MAX_DOTS is a constant determining the total number of dots on the canvas, which is a randomly generated number from
# 1 to 99.


    for i in range(MAX_DOTS):
        x = random.randint(25, WIDTH - 50)
        y = random.randint(25, HEIGHT - 50)
        color = random_color()
        canvas.create_oval(x, y, x + DIAMETER, y + DIAMETER, fill=color, outline=color)
    return canvas
# This section, for each dot, assigns starting x & y coordinates for each dot. They are randomly generated numbers
# ranging from 25 and till WIDTH - 50 (to ensure even borders). random_color() assigns a random color to the variable
# color.
# canvas.create_oval() then draws a circle with an origin (x, y) and DIAMETER. The loop is then repeated.



def random_color():
    navajo_white = 1
    dodger_blue = 2
    medium_spring_green = 3
    deep_pink = 4
    red2 = 5
    dark_violet = 6
    yellow = 7
    picked_color = random.randint(1, 7)
# These are possible colors for a given dot assigned with a integer value. A random integer is picked which is then
# assigned to a color.

    if picked_color == navajo_white:
        return "navajo white"

    if picked_color == dodger_blue:
        return "dodger blue"

    if picked_color == medium_spring_green:
        return "medium spring green"

    if picked_color == deep_pink:
        return "deep pink"

    if picked_color == red2:
        return "red2"

    if picked_color == dark_violet:
        return "dark violet"

    if picked_color == yellow:
        return "yellow"
# This section is multiple if statements checking which color was picked and then text of the color is returned to the
# fill and outline in canvas.create_oval().









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


    return canvas




if __name__ == '__main__':
    main()
