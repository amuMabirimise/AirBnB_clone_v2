#!/usr/bin/python3
"""
Runing a Flask web application on 0.0.0.0:5000
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ Returning an HTML page of all States sorted by name """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Removing the current SQLAlchemy session. """
    storage.close()


if __name__ == "__main__":
    """ Run on 0.0.0.0 """
    app.run(host='0.0.0.0')
