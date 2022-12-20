"""
File: bouncing_ball.py
----------------
A ball (circle) is drawn and it bounces around the canvas, indefinitely.
"""


import tkinter
import time



CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels
BALL_DIAMETER = 70      # Diameter of the ball.

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Bouncing Ball")
    ball = canvas.create_oval(2, 2, BALL_DIAMETER, BALL_DIAMETER, fill="steel blue", outline="steel blue")
    change_x = 2
    change_y = 6
# This section of the code creates a canvas and a ball which is assigned to "ball". change_x & change_y are variables
# that determine how many pixels the ball moves each frame.

    while True:
        canvas.move(ball, change_x, change_y)


        if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
            change_y *= -1

        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            change_x *= -1
# This section checks the current coordinates (denoted by pixels) and if it has hit the wall, the variables change_x &
# change_y's signs are inverted to change its direction in that respective axis, thus, it bounces.

        canvas.update()
        time.sleep(1 / 60)
# The program runs at a frame-rate of 60Hz.


    canvas.mainloop()




def hit_bottom_wall(canvas, object):
    current_y = get_top_y(canvas, object) + BALL_DIAMETER
    return current_y > CANVAS_WIDTH
# hit_bottom_wall() assigns the coordinates of the "bottom" of the circle and assigns it to current_y. If current_y
# is equal to the canvas width, it means that the ball has hit the bottom and a boolean (True) is returned.
# not == as it may skip the wall as the starting coordinates are not zero and it moves by a value >0 each frame.


def hit_top_wall(canvas, object):
    current_y = get_top_y(canvas, object)
    return current_y < 0

def hit_left_wall(canvas, object):
    current_x = get_left_x(canvas, object)
    return current_x < 0

def hit_right_wall(canvas, object):
    current_x = get_left_x(canvas, object) + BALL_DIAMETER
    return current_x > CANVAS_HEIGHT

# These remaning functions have the same functionality as hit_bottom_wall(), for each side of the canvas.




def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def get_top_y(canvas, object):
    return canvas.coords(object)[1]
# get_left_x() & get_top_y() return the x and y coordinates of the top left corner of the circle respectively.


















######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas




if __name__ == '__main__':
    main()
