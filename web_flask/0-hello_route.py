#!/usr/bin/python3
"""
<<<<<<< HEAD
Starts a Flask web application.

My web application should listening on 0.0.0.0, port 5000.

Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays this when called 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port 5000)
=======
starting a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns the string Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 202934359f7e3ee6f1b2b51feb7c790ca06323a1
