"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/greenland-fire.png'
INTENSITY_THRESHOLD = 1.08
# INTENSITY_THRESHOLD is the constant multiplier that checks whether a pixel is "red" enough. The value was determined
# through testing values ranging from 1.0 to 1.2.


def main():
    image = SimpleImage(ask_user_image())
    find_fires(image)
    image.show()
# main() assigns the desired image to the variable image and identifies the hot spots of fires and shows the edited
# image to the user.


def ask_user_image():
    filename = input("Enter the filename to locate its fires or a space to use the default image: ")
    if filename == " ":
        filename = DEFAULT_FILE
        return filename

    else:
        return filename
# ask_user_image() asks the user for the directory of the desired image and assigns it to filename. If the user enters
# a space, DEFAULT_IMAGE image is assigned instead. filename is then assigned to the variable image in main().



def find_fires(image1):
    for pixel in image1:
        avg_intensity = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.red >= (avg_intensity * INTENSITY_THRESHOLD):
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0

        else:
            pixel.red = avg_intensity
            pixel.green = avg_intensity
            pixel.blue = avg_intensity
# find_fires(image1) for each pixel checks whether a pixel is sufficiently red (fire) and makes it entirely red,
# the pixel is grey-scaled by making the rgb values for the pixels the average value. No return was required as
# it is a mutable variable.





if __name__ == '__main__':
    main()
