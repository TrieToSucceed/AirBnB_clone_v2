#!/usr/bin/python3
"""
Run Flask to listen on port 5000
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page that shows States and Amenities
    """
    state_obj = storage.all("State")
    states = [v for k, v in state_obj.items()]
    states.sort(key=lambda x: x.name)
    amenity_obj = storage.all("Amenity")
    amenities = [v for k, v in amenity_obj.items()]
    amenities.sort(key=lambda x: x.name)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def tear_down(response_or_exc):
    """
    tear down method
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
