from flask import Flask, session, render_template, redirect, request, url_for, g, flash, abort
# from model import session as db_session, .. Classes
# import model
import os
import sqlite3

# flask session: browser session (info identifying particular user of a web app)
# model session: database session (connection to db)

app = Flask(__name__)
SECRET_KEY = "Make a mark at espnW hackathon!"
app.config.from_object(__name__)

#@app.route('/')
"""
@app.teardown_request
def shutdown_session(exception = None):
	db_session.remove()
"""

# create a main page containing calendar and embedded tweets
@app.route("/calendar", methods=["GET"])
def show_calendar():
	return render_template("calendar.html")

#@app.route("/event/<int:id>", methods=['GET'])
@app.route("/event", methods = ['GET'])
def show_event():
	return render_template("event.html")

def show_roster():
	return render_tempalate("roster.html", roster=players	

if __name__ == "__main__":
	app.run(debug = True)
