# Import the dependencies.

import pandas as pd
import numpy as np 
import flask
print(flask.__version__)
import datetime as dt
import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# engine for the hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)



#################################################
# Flask Setup
#################################################
# Create an app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")

def welcome(): 
    """List available API routes"""
    return(
        "All Available Routes <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start <br/>"
        f"/api/v1.0/start/end <br/>"
        )

# 2. Convert the query results from precipitation analysis (retrieve only the last12 months of data) to a dictinary using date as the key and prcp as the value
@app.route("/api/v1.0/precipitation")

def precipitation():
    session = Session(engine) 
    one_year_recent = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    one_year_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_recent, Measurement.prcp != None).order_by(Measurement.date).all()
    prcp = {date: prcp for date, prcp in one_year_prcp}
    return jsonify(prcp)


# 3. Return a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")

def stations():
    session = Session(engine) 
    station = session.query(Station.station).all()
    all_stations = list(np.ravel(station))
    return jsonify (all_stations)

# 4. Query the dates and temperature observations of the most-active station for the previous year of the data and return a JSON list of temperature observations for the previous year
@app.route("/api/v1.0/tobs")

def tobs ():
    session = Session(engine) 
    recent_point = dt.date(2017, 8, 23)
    one_year_recent = recent_point - dt.timedelta(days = 365)
    active_year = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= one_year_recent).all()
    temperature = list(np.ravel(active_year))
    return jsonify (temperature)

# 5. Return a JSON list of the minimum temperature, the average temperature, adn the maximum temperature for a specified start or start-end range.
### For specificed start, calculate TMIN, TAVG, TMAX
### /api/v1.0/'2016-08-23'
@app.route("/api/v1.0/<start>")

def start_date(start):
    session = Session(engine)
    summary = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    start_list = []
    for i in range(len(summary)):
        start_list.append(summary[i][0:])
    return jsonify(start_list)
    

### For a specifed start date and end date, calculate TMIN, TAVE, and TMAX for the dates from teh start date to the end date, inclusive
### /api/v1.0/2016-10-11/2017-08-11
@app.route("/api/v1.0/<start>/<end>")

def start_end_date(start,end):
    session = Session(engine)
    summary = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    start_end_list = list(np.ravel(summary))
    return jsonify(start_end_list)


#################################################
if __name__ == "__main__":
    app.run(debug=True)