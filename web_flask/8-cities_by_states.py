#!/usr/bin/python3
"""
Run Flask to listen on port 5000
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def print_city_state():
    """
    Format tempate with states
    """
    objects = storage.all("State")
    states = [v for k, v in objects.items()]
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tear_down(response_or_exc):
    """
    tear down method
    """
    storage.close()


if __name__ == "__main__":
    app.run()
