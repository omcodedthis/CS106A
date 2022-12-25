"""
This program generates the Warhol effect and applies it to a selected image. This was an optional Challenge Problem
from Assignment 3. Do note that you can test this program using "images/lewis_hamilton.jpg" ,
"images/max_verstappen.jpg" or "images/simba-sq.jpg" or any square sized image of your choice.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE    # Width of the whole Warhol Effect Image
HEIGHT = N_ROWS * PATCH_SIZE   # Height of the whole Warhol Effect Image
DEFAULT_IMAGE = "images/lewis_hamilton.jpg"


def main():
  image1 = SimpleImage(ask_user_image())
  warhol_effect_image = apply_warhol(image1)
  warhol_effect_image.show()
# main() assigns the image the user desires to use to the variable image1. It is then passed to the apply_warhol(image)
# function, where the Warhol Effect is applied. This new image is then assigned to warhol_effect_image which is then
# shown to the user.

def ask_user_image():
    filename = input("Enter the directory of the image to apply the Warhol Effect or a space for the default image: ")
    if filename == " ":
        filename = DEFAULT_IMAGE
        return filename

    else:
        return filename
# ask_user_image() takes the input of the directory of the file and assigns it to filename. If a space is entered,
# DEFAULT_IMAGE is then assigned to filename. filename is returned to image1 in main().

def apply_warhol(image):
    warhol_image = SimpleImage.blank(WIDTH, HEIGHT)
    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_patch(warhol_image, image, row, col)
            color_patch(warhol_image, row, col)
    return warhol_image
# apply_warhol(image) creates a new blank image. Since there are six variations of the image, there are two rows &
# three columns. For each row and column combination, the chosen image is drawn and a filter is applied. This repeats
# until the image is drawn at all rows & columns.


def draw_patch(warhol_image, image, row, col):
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            x_cord = x + (col * PATCH_SIZE)
            y_cord = y + (row * PATCH_SIZE)
            pixel = image.get_pixel(x, y)
            warhol_image.set_pixel(x_cord, y_cord, pixel)
# draw_patch(warhol_image, image, row, col) draws the image for a given row & column. The nested loop goes through all
# the pixels within the "square" created using the row and column. The actual x & y coordinates are determined by
# adding the product of the row/col with PATCH_SIZE. This expression offsets the coordinates by the length horizontally
# & vertically (for bottom row) with the length of each patch (chosen image).

def color_patch(warhol_image, row, col):
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            x_cord = x + (col * PATCH_SIZE)
            y_cord = y + (row * PATCH_SIZE)
            pixel = warhol_image.get_pixel(x_cord, y_cord)
            pick_color_pixel(pixel, row, col)
# color_patch(warhol_image, row, col) applies the same principle as draw_patch(warhol_image, image, row, col), but
# paints the pixel using pick_color_pixel(pixel, row, col) instead of adding the pixel to warhol_image (pixel from
# image has been drawn when this function is called).




def pick_color_pixel(pixel, row, col):
     if row == 0 and col == 0:
         color_pixel(pixel, 1.5, 0, 1.5)

     if row == 0 and col == 1:
         color_pixel(pixel, 0, 1.5, 1.5)

     if row == 0 and col == 2:
         color_pixel(pixel, 1.5, 1.5, 1.5)

     if row == 1 and col == 0:
         color_pixel(pixel, 1.5, 1.5, 0)

     if row == 1 and col == 1:
         color_pixel(pixel, 1, 1, 1)

     if row == 1 and col == 2:
         color_pixel(pixel, 0.45, 0.65, 2.5)
# pick_color_pixel(pixel, row, col) adjusts the intensities of the RGB values of a given pixel for part of a image in
# a given row & column by calling the function color_pixel(pixel, red_scale, green_scale, blue_scale).


def color_pixel(pixel, red_scale, green_scale, blue_scale):
    pixel.red *= red_scale
    pixel.green *= green_scale
    pixel.blue *= blue_scale
# color_pixel(pixel, red_scale, green_scale, blue_scale) adjusts the overall color of the pixel by varying the
# intensity of the RGB values.

if __name__ == '__main__':
    main()