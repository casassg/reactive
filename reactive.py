import time
from flask import Flask, render_template, jsonify
import camera
import vision

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/picture/take')
def take():
    id_ = str(int(time.time()))
    path = 'res/img/' + id_ + '.jpg'
    camera.take_photo(path)
    detect = vision.detect(path)
    result = {'id': id_, 'result': detect}
    return jsonify(result)


@app.route('/picture/react/<id_>')
def react(id_):
    path = 'res/img/' + id_ + '_react.jpg'
    camera.take_photo(path)
    detect = vision.detect(path)
    result = {'id': id_, 'result': detect}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
