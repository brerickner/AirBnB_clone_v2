#!/usr/bin/python3
'''Module to start Flask web app'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from sqlalchemy import orm

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000


@app.teardown_appcontext
def teardown(context):
    '''Method to remove current SQLAlchemy Session'''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''Method to load classes'''
    stateDict = storage.all(State)
    amenDict = storage.all(Amenity)

    return render_template('10-hbnb_filters.html',
                           stateDict=stateDict, amenDict=amenDict)


if __name__ == "__main__":
    app.run(HOST, PORT)
