"""
File: move_rect.py
----------------
This program draws a square on a canvas and moves it towards the center of the canvas.
"""


import tkinter
import time



CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels
SQUARE_SIZE = 70        # Size of the square in pixels




def main():
   canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Move to center!")
   sq_start_y = (CANVAS_HEIGHT / 2) - (SQUARE_SIZE / 2)
   sq_end_y = (CANVAS_HEIGHT / 2) + (SQUARE_SIZE / 2)
   rect = canvas.create_rectangle(0, sq_start_y, SQUARE_SIZE, sq_end_y, fill="steel blue", outline="steel blue")
   while check_if_center(canvas, rect):
       canvas.move(rect, 1, 0)
       canvas.update()
       time.sleep(1/60)
       canvas.mainloop()

# This section creates the canvas and denotes where the square is first drawn. sq_start_y is the origin and it is such
# that it is drawn in the center of the vertical axis, hence half the square length must be subtracted.

def check_if_center(canvas, object):
    current_x = get_left_x(canvas, object)
    max_x = (CANVAS_WIDTH / 2) - (SQUARE_SIZE / 2)
    return current_x <= max_x
# check_if_center() checks whether the square is in the center by taking the current x-coordinate(top-left) and checking
# whether it is equal to max_x, the desired coordinate for the center, a boolean is returned.


def get_left_x(canvas, object):
    return canvas.coords(object)[0]

# get_left_x() gets the x-coordinate of the top-left corner of the square.














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
