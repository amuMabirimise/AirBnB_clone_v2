#!/usr/bin/python3
"""
<<<<<<< HEAD
starts a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""

from flask import Flask
=======
Starting a Flask web application.
"""

from flask import Flask

>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
<<<<<<< HEAD
    """Display Hello HBNB!"""
=======
    """
    Returns 'Hello HBNB!' when accessing the root path.
    """
>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """Display HBNB"""
=======
    """
    Returns 'HBNB' when accessing the /hbnb path.
    """
>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
<<<<<<< HEAD
    """Returns “C ” followed by the value of the text variable"""
=======
    """
    Displays 'C ' followed by the value of the text variable.
    Replaces underscores in the text with spaces.
    """
>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
<<<<<<< HEAD
    """Return “Python ”, followed by the value of the text variable"""
=======
    """
    Displays 'Python ' followed by the value of the text variable.
    If no text is provided, defaults to 'is cool'.
    Replaces underscores in the text with spaces.
    """
>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
<<<<<<< HEAD
    """/number/<n>: display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

=======
    """
    Displays '{n} is a number' only if n is an integer.
    """
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
