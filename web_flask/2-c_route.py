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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

