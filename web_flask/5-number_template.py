#!/usr/bin/python3
"""
Starts Flask web app with various routes.

Routes:
    / - Displays "Hello HBNB!"
    /hbnb - Displays "HBNB"
    /c/<text> - Displays "C <text>"
    /python - Displays "Python is cool"
    /python/<text> - Displays "Python <text>"
    /number/<n> - Displays n if it is an integer
    /number_template/<n> - Displays an HTML page if n is an integer
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """Displays "Hello HBNB!" when accessing root"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays "HBNB" when accessing /hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Displays "C <text>" where underscores are replaced with spaces"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays "Python <text>" where underscores are replaced with spaces"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Displays n if it is an integer"""
    return "{} is a number".format(n)
