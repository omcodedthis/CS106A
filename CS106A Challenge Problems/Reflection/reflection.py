"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_IMAGE = "images/mt-rainier.jpg"

def main():
    image1 = SimpleImage(ask_user_image())
    mirror_image1 = add_reflection(image1)
    mirror_image1.show()
# main() assigns the image that is to be reflected to the variable image1. The add_reflection(image1) function is
# called passing image1 and returning the mirrored image. This is then assigned to mirror_image1, which is shown to
# the user.


def ask_user_image():
    filename = input("Enter the directory of the image or a space to use the default image: ")
    if filename == " ":
        filename = DEFAULT_IMAGE
        return filename

    else:
        return filename
# ask_user_image() asks the user for the directory of the image and assigns it to filename. If the user has entered
# a space, DEFAULT_IMAGE is assigned. filename is then returned to image1 in main().

def add_reflection(image):
    mirror_image_height = image.height * 2
    mirror_image = SimpleImage.blank(image.width, mirror_image_height)

    for y in range(image.height):
        for x in range (image.width):
            pixel = image.get_pixel(x,y)
            mirror_image.set_pixel(x, y, pixel)
            mirror_image.set_pixel(x, mirror_image_height - (y + 1), pixel)


    return mirror_image
# add_reflection(image) assigns the new height of the mirror image (twice the height of the original) and is assigned
# to mirror_image_height. A new blank image is created and assigned to mirror_image. The nested loop goes through all
# the coordinates of the pixels only for the original image. The pixel is then drawn onto the blank mirror_image twice,
# one using the original coordinates and the other with the y-coordinate of mirror_image_height - (y + 1), creating
# a reflection w.r.t the horizontal axis (the "+1" was added as pixels are indexed starting from 0. For example, a
# height of 764 will mean that the last pixel on the y-axis is indexed as 763). mirror_image is returned to main().



if __name__ == '__main__':
    main()
