import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///hawaii.sqlite")
#  create database connection
connection_string = "postgres:nopass97@localhost:5432/Project"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
# AIDB = Base.classes.aidb
# TCD = Base.classes.tech_companies_deals
# AICD = Base.classes.ai_companies_deals


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/names")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(aidb.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)




######################################################################

# # Create our session (link) from Python to the DB
# session = Session(engine)

# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# @app.route("/")
# def welcome():
#     return (
#         f"Welcome to the Hawaii Climate Analysis API!<br/>"
#         f"Available Routes:<br/>"
#         f"/api/v1.0/precipitation<br/>"
#         f"/api/v1.0/stations<br/>"
#         f"/api/v1.0/tobs<br/>"
#         f"/api/v1.0/temp/start/end"
#     )


# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     """Return the precipitation data for the last year"""
#     # Calculate the date 1 year ago from last date in database
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#     # Query for the date and precipitation for the last year
#     precipitation = session.query(Measurement.date, Measurement.prcp).\
#         filter(Measurement.date >= prev_year).all()

#     # Dict with date as the key and prcp as the value
#     precip = {date: prcp for date, prcp in precipitation}
#     return jsonify(precip)


# @app.route("/api/v1.0/stations")
# def stations():
#     """Return a list of stations."""
#     results = session.query(Station.station).all()

#     # Unravel results into a 1D array and convert to a list
#     stations = list(np.ravel(results))
#     return jsonify(stations=stations)


# @app.route("/api/v1.0/tobs")
# def temp_monthly():
#     """Return the temperature observations (tobs) for previous year."""
#     # Calculate the date 1 year ago from last date in database
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#     # Query the primary station for all tobs from the last year
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()

#     # Unravel results into a 1D array and convert to a list
#     temps = list(np.ravel(results))

#     # Return the results
#     return jsonify(temps=temps)


# @app.route("/api/v1.0/temp/<start>")
# @app.route("/api/v1.0/temp/<start>/<end>")
# def stats(start=None, end=None):
#     """Return TMIN, TAVG, TMAX."""

#     # Select statement
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

#     if not end:
#         # calculate TMIN, TAVG, TMAX for dates greater than start
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         # Unravel results into a 1D array and convert to a list
#         temps = list(np.ravel(results))
#         return jsonify(temps)

# #     # calculate TMIN, TAVG, TMAX with start and stop
# #     results = session.query(*sel).\
# #         filter(Measurement.date >= start).\
# #         filter(Measurement.date <= end).all()
# #     # Unravel results into a 1D array and convert to a list
# #     temps = list(np.ravel(results))
# #     return jsonify(temps=temps)


# # if __name__ == '__main__':
# #     app.run()


#     import numpy as np

# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func

# from flask import Flask, jsonify




# # Save reference to the table
# Passenger = Base.classes.passenger

