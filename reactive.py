from flask import Flask, render_template

import camera

app = Flask(__name__)


@app.route('/')
def hello_world():
    camera.take_photo("static/img/reaction.jpg")
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
