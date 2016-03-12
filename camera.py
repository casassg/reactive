from cv2 import *


def take_photo(output_path):
    cam = VideoCapture(0)
    # Cam weight&height properties
    cam.set(3, 1280)
    cam.set(4, 1024)

    # we take n_frame photos to adjust light
    for i in xrange(20):
        tmp=cam.read()

    # we take the photo we want to finally use
    s, img = cam.read()
    imwrite(output_path, img)  # we save the image

    # we delete the camera so it can be used by other apps
    del cam
