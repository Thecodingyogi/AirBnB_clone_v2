#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy session after each request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main hbnb filters HTML page"""
    states = storage.all(State)
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
