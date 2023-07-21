#!/usr/bin/python3
"""Script that starts a Flask web application.
    Web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of the text varible"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")