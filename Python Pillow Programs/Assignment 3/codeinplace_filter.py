"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    while True:
        image = SimpleImage(ask_user_image())
# This section asks the user for the image that they desire to apply the filter using ask_user_image().

        for pixel in image:
            pixel.red *= 1.5
            pixel.green *= 0.7
            pixel.blue *= 1.5
        image.show()
# This section edits the values of the red, green & blue intensities for all pixels in the image. The while loop
# was added so that the user can apply the filter to as many images they desire.





def ask_user_image():
    filename = input("Enter the directory (e.g images/quad.jpg) of the image or a space to use the default image: ")
    if filename == " ":
        filename = DEFAULT_FILE
        return filename

    else:
        return filename
# ask_user_image() asks the user's input (type string) and assigns it to the variable filename, if a space was inputted
# DEFAULT_IMAGE is assigned to filename. filename is then assigned to the variable image, returned to main().













if __name__ == '__main__':
    main()