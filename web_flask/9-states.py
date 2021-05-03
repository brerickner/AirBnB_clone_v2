#!/usr/bin/python3
'''Module to start Flask web app'''
from flask import Flask, render_template
from models import storage
from models.state import State

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
    stateList = storage.all(State)

    return render_template('9-states.html', stateList=stateList)


@app.route('/states/<id>', strict_slashes=False)
def state_id_route(id):
    '''Method to load states'''
    stateList = storage.all(State)
    match = True
    for state in stateList.values():
        if state.id == id:
            matchState = state
            return render_template('9-states.html', state=matchState)

if __name__ == "__main__":
    app.run(HOST, PORT)
