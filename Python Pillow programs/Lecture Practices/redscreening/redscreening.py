"""
File: redscreening.py
--------------------
This program shows an example of "greenscreening" (actually
"redscreening" in this case).  This is where we replace the
pixels of a certain color intensity in a particular channel
(here, we use red) with the pixels from another image.
"""


from simpleimage import SimpleImage


INTENSITY_THRESHOLD = 1.55

def main():
    main_image = SimpleImage("images/stop.png")
    main_image.show()
# This section takes a .png image and assigns it to main_image, this is then shown to the user.


    final_image = redscreen("images/stop.png", "images/leaves.png")
    final_image.show()
# This section takes the "redscreened" image and assigns it to final_image, this is then shown to the user.









def redscreen(filename1, filename2):
    image = SimpleImage(filename1)
    back_image = SimpleImage(filename2)
# This section assigns the image that is getting "redscreened" under image and the image that is replacing the
# red pixels of that image is assigned to back_image.


    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
# This section, for 1 loop assigns the respective pixel to the variable pixel. The loop goes through each x-coordinate
# (the max is the width of the image) for a given y-coordinate.



            avg_intensity = (pixel.red + pixel.green + pixel.blue) // 3
            if (pixel.red) >= (avg_intensity * INTENSITY_THRESHOLD):
                pixel = image.set_pixel(x, y, back_image.get_pixel(x, y))
# This section checks whether the pixel has a substantial intensity of red by comparing it to the average intensity. If
# True, the pixel of the image gets replaced by a pixel from the back_image with the same coordinates.


    return image
# The for-loop continues for all pixels in image and then returns the "redscreened" image.






if __name__ == '__main__':
    main()
