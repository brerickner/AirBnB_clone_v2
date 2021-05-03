#!/usr/bin/python3
'''Module to start Flask web app'''
from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy import orm

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000


@app.teardown_appcontext
def teardown(context):
    '''Method to remove current SQLAlchemy Session'''
    storage.close()


@app.route('/states', strict_slashes=False)
def states_route():
    '''Method to load states'''
    stateDict = storage.all(State)

    return render_template('9-states.html', stateDict=stateDict)


@app.route('/states/<id>', strict_slashes=False)
def state_id_route(id):
    '''Method to load states'''
    stateDict = storage.all(State)
    try:
        state = stateDict.get("State.{}".format(id))
        return render_template('9-states.html', state=state)
    except BaseException:
        return render_template('9-states.html')


if __name__ == "__main__":
    app.run(HOST, PORT)
