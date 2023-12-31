#!/usr/bin/python3
"""
<<<<<<< HEAD
Starts a Flask web application.
"""
=======
Starting a Flask web application.
"""

>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Displays 'C' followed by the value of <text>.
    (Replaces any underscores in <text> with slashes)
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Display “Python ”, followed by the value of the text variable 
    (Replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port 5000)
=======
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
