#!/usr/bin/python3
"""
Starting a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns 'Hello HBNB!' when accessing the root path.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB' when accessing the /hbnb path.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Displays 'C ' followed by the value of the text variable.
    Replaces underscores in the text with spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    Displays 'Python ' followed by the value of the text variable.
    If no text is provided, defaults to 'is cool'.
    Replaces underscores in the text with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """
    Displays '{n} is a number' only if n is an integer.
    """
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
