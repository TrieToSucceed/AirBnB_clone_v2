#!/usr/bin/python3
"""
Starts a Flask web application listening on port 5000
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    """
    print hello
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """
    print hbnb
    """
    return "HBNB"

if __name__ == "__main__":
    app.run()
