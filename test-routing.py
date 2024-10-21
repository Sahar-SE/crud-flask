from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p> index page=</p>"

@app.route("/hello")
def hello_world():
    return "<p>Hello Page</p>"