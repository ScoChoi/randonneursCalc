"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""
import os
from pymongo import MongoClient
import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

###
# Pages
###
#db.tododb.insert_one({'open_time': "12 pm", 'close_time': "3 pm"})

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 0, type=float)
    begin_date = request.args.get('begin_date')
    begin_time = request.args.get('begin_time')
    arrow_start = arrow.get(begin_date + " " + begin_time + ":00")
    brevet_dist = request.args.get('brevet_dist', 999, type=int)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    # FIXME: These probably aren't the right open and close times
    # and brevets may be longer than 200km
    percent120 = brevet_dist * 1.2
    possible_brev = [200, 300, 400, 600, 1000]
    if brevet_dist not in possible_brev:
        note = "Current brevet distance is abnormal. Choose from 200, 300, 400, 600, or 1000"
    elif km > percent120:
        note = "Control location is more than 20% over the selected distance."
    else:
        note = ""
    open_time = acp_times.open_time(km, brevet_dist, arrow_start.isoformat())
    close_time = acp_times.close_time(km, brevet_dist, arrow_start.isoformat())
    result = {"open": open_time, "close": close_time, "note": note}
    return flask.jsonify(result=result)

@app.route("/_submit")
def _submit():
    open_time = request.args.get("open_time") 
    close_time = request.args.get("close_time") 
    km = request.args.get('km', 0, type=float)
    item_doc = {
        'km': km,
        'open_time': open_time,
        'close_time': close_time
    }
    if open_time != '':
        db.tododb.insert(item_doc)
    #app.logger.debug("db is :{}", db.tododb.find())
    return flask.render_template('calc.html')

@app.route("/display")
def display():
    _items = db.tododb.find()
    items = [item for item in _items]
    if db.tododb.count({}) == 0:
        return flask.render_template('display_error.html')
    return flask.render_template('display.html', items=items)

@app.route("/submit_error")
def submit_error():
    return flask.render_template('submit_error.html')

@app.route("/display_error")
def display_error():
    return flask.render_template('display_error.html')

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

