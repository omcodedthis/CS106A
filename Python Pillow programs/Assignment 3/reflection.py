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



def ask_user_image():
    filename = input("Enter the directory of the image or a space to use the default image: ")
    if filename == " ":
        filename = DEFAULT_IMAGE
        return filename

    else:
        return filename

def add_reflection(image):
    mirror_image_height = image.height * 2
    mirror_image = SimpleImage.blank(image.width, mirror_image_height)

    for y in range(image.height):
        for x in range (image.width):
            pixel = image.get_pixel(x,y)
            mirror_image.set_pixel(x, y, pixel)
            mirror_image.set_pixel(x, mirror_image_height - (y + 1), pixel)



    return mirror_image







if __name__ == '__main__':
    main()
