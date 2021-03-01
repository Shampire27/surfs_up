# Set Up the Flask Weather App

## Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

## Add the SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# Reflect the database
Base.prepare(engine, reflect=True)

# Create variable
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to the database
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# Define the welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# run in command: 
## conda activate PythonData
## install flask
## export FLASK_APP=app.py
## flask run
# http://127.0.0.1:5000/

##########################################
# Precipitation Route 9.5.3

@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# http://127.0.0.1:5000/api/v1.0/precipitation


############################################
# Stations Route 9.5.4

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# http://localhost:5000/
# http://127.0.0.1:5000/api/v1.0/stations

##########################################
# Monthly Temperature Route 9.5.5

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# http://127.0.0.1:5000/api/v1.0/tobs
# OR
# http://localhost:5000/api/v1.0/tobs

###########################################
# Statistics Route 9.5.6
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# http://127.0.0.1:5000/api/v1.0/temp/start/end%20route
    # {temps: [null,null,null]}
# http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30
    # {temps: [71,77.21989528795811,83]}





##################################################
# 1. import Flask
# from flask import Flask

# 2. Create an app, being sure to pass __name__
# app = Flask(__name__)

# 3. Define what to do when a user goes to the index route
# @app.route('/')
# def hello_world():
#     return 'Hello world'

# 4. Run a Flask App (in TERMINAL):
# conda activate PythonData
# for Mac, run in command lines: export FLASK_APP=app.py
# for Windows system run: set FLASK_APP=app.py
# then: flask run

