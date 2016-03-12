from flask import Flask, render_template
from cv2 import *

app = Flask(__name__)

#indicates the port for the webcam used by the computer (usually 0)
camera_port = 0

#number of frames to throw away while the camera adjusts light level
n_frame = 10


def take_photo(output_path):
    cam = VideoCapture(camera_port)
    #Cam weight&height properties
    cam.set(3,1280)
    cam.set(4,1024)

    #we take n_frame photos to adjust light
    for i in xrange(n_frame):
        temp = cam.read()

    #we take the photo we want to finally use
    s, img = cam.read()
    imwrite(output_path,img) #we save the image

    #we delete the camera so it can be used by other apps
    del(cam)


@app.route('/')
def hello_world():
    take_photo("static/img/reaction.jpg")
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
