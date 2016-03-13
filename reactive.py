from flask import Flask, render_template
import camera
import vision

app = Flask(__name__)


@app.route('/')
def hello_world():
    #jpg = "static/img/reaction.jpg"
    #camera.take_photo(jpg)
    #return render_template("base.html", result=vision.detect(jpg))
    return render_template("home.html")

@app.route('/take_me/<id_>')
def take(id_):
    camera.take_photo('static/img/' + id_ + '.jpg')
    return 'Nice done'


if __name__ == '__main__':
    app.run(debug=True)
