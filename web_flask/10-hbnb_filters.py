#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBNB filters HTML page."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
