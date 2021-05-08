import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, redirect


#################################################
# Database Setup
#################################################
#  create database connection
connection_string = "postgres:nopass97@localhost:5432/Project"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
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
        f"/api/v1.0/AIDB<br/>"
        f"/api/v1.0/AID<br/>"
        f"/api/v1.0/TD<br/>"
        f"/api/v1.0/AID_Company<br/>"
        f"/api/v1.0/AID_Deal<br/>"
        f"/api/v1.0/AID_Capital<br/>"
        f"/api/v1.0/AID_Rev<br/>"
        f"/api/v1.0/TD_Company<br/>"
        f"/api/v1.0/TD_Deal<br/>"
        f"/api/v1.0/TD_Capital<br/>"
        f"/api/v1.0/TD_Rev<br/>"
    )


@app.route("/api/v1.0/AIDB")
def AIDB():
    """Return a AI datbase"""
    # Query the databse
    AIDB_J = pd.read_sql('SELECT * FROM "AIDB"',engine).to_dict('record')
    return jsonify(AIDB_J)

@app.route("/api/v1.0/AID")
def AID():

    """Return a AI companies deals"""
    # Query the databse
    AID_J = pd.read_sql('SELECT * FROM "AI_Companies_Deals"',engine).to_dict('record')
    return jsonify(AID_J)

@app.route("/api/v1.0/TD")
def TD():

    """Return a Tech companies deals"""
    # Query the databse
    TD_J = pd.read_sql('SELECT * FROM "Tech_Companies_Deals"',engine).to_dict('record')
    return jsonify(TD_J)

@app.route("/api/v1.0/AID_Company")
def AID_Company():

    """Return a AI deals wrt companies"""
    # Query the databse
    AID_Company_J = pd.read_sql('SELECT * FROM "AICD_Company"',engine).to_dict('record')
    return jsonify(AID_Company_J)

@app.route("/api/v1.0/AID_Deal")
def AID_Deal():

    """Return a AI deals wrt no of deals"""
    # Query the databse
    AID_Deal_J = pd.read_sql('SELECT * FROM "AICD_Deals"',engine).to_dict('record')
    return jsonify(AID_Deal_J)

@app.route("/api/v1.0/AID_Capital")
def AID_Captial():

    """Return a AI deals wrt capital"""
    # Query the databse
    AID_Capital_J = pd.read_sql('SELECT * FROM "AICD_Capital"',engine).to_dict('record')
    return jsonify(AID_Capital_J)

@app.route("/api/v1.0/AID_Rev")
def AID_Rev():

    """Return a AI deals wrt revenue"""
    # Query the databse
    AID_Rev_J = pd.read_sql('SELECT * FROM "AICD_Revenue"',engine).to_dict('record')
    return jsonify(AID_Rev_J)

@app.route("/api/v1.0/TD_Company")
def TD_Company():

    """Return a TECH deals wrt companies"""
    # Query the databse
    TD_Company_J = pd.read_sql('SELECT * FROM "TCD_Company"',engine).to_dict('record')
    return jsonify(TD_Company_J)

@app.route("/api/v1.0/TD_Deal")
def TD_Deal():

    """Return a TECH deals wrt no of deals"""
    # Query the databse
    TD_Deal_J = pd.read_sql('SELECT * FROM "TCD_Deals"',engine).to_dict('record')
    return jsonify(TD_Deal_J)

@app.route("/api/v1.0/TD_Capital")
def TD_Captial():

    """Return a TECH deals wrt capital"""
    # Query the databse
    TD_Capital_J = pd.read_sql('SELECT * FROM "TCD_Capital"',engine).to_dict('record')
    return jsonify(TD_Capital_J)

@app.route("/api/v1.0/TD_Rev")
def TD_Rev():

    """Return a TECH deals wrt revenue"""
    # Query the databse
    TD_Rev_J = pd.read_sql('SELECT * FROM "TCD_Revenue"',engine).to_dict('record')
    return jsonify(TD_Rev_J)

# @app.route("/api/v1.0/AIDB_Cats")
# def AIDB_Cats():

# #     # Create our session (link) from Python to the DB
#     session = Session(engine)

# #     
# #     # Query db
#     results = session.query("AIDB".Category,"AIDB".Name, "AIDB".Country).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list 
#     all_AIDB_Cat = []
#     for Category, Name, Country in results:
#         AIDB_Cat_dict = {}
#         AIDB_Cat_dict["Category"] = Category
#         AIDB_Cat_dict["Name"] = Name
#         AIDB_Cat_dict["Country"] = Country
#         all_AIDB_Cat.append(AIDB_Cat_dict)

#     return jsonify(all_AIDB_Cat)

if __name__ == '__main__':
    app.run(debug=True)


