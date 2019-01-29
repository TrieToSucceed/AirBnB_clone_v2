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


@app.route("/c/<text>", strict_slashes=False)
def print_c_text(text):
    """
    print c with passed in value
    """
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python_text(text="is cool"):
    """
    print python with passed in value
    """
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    """
    print number that is passed in
    """
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_page(n):
    """
    use number passed in as template for html
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_even(n):
    """
    determine if number is odd or even and then pass into template
    """
    num_type = "odd" if n % 2 else "even"
    return render_template("6-number_odd_or_even.html",
                           number=n, num_type=num_type)

if __name__ == "__main__":
    app.run()
