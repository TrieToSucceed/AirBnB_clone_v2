#!/usr/bin/python3
"""
Run Flask to listen on port 5000
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def print_state_id(state_id=False):
    """
    Format template with states
    """
    objects = storage.all("State")
    states = [v for k, v in objects.items()]
    states.sort(key=lambda x: x.name)
    if not state_id:
        return render_template("9-states.html", states=states,
                               state_id=state_id)
    target_state = None
    for state in states:
        if state.id == state_id:
            target_state = []
            target_state.append(state)
            target_state[0].cities.sort(key=lambda x: x.name)
            break
    return render_template("9-states.html", states=target_state,
                           state_id=state_id)


@app.teardown_appcontext
def tear_down(response_or_exc):
    """
    tear down method
    """
    storage.close()


if __name__ == "__main__":
    app.run()
