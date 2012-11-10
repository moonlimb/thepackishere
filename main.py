from flask import Flask, session, render_template, redirect, request, url_for, g, flash, abort
# from model import session as db_session, .. Classes
# import model
import os
import sqlite3
from model import session as db_session, Player, EventDetails
# flask session: browser session (info identifying particular user of a web app)
# model session: database session (connection to db)

app = Flask(__name__)
SECRET_KEY = "Let's win espnW hackathon!"
app.config.from_object(__name__)

#@app.route('/')
@app.teardown_request
def shutdown_session(exception = None):
	db_session.remove()

# create a main page containing calendar and embedded tweets
@app.route("/calendar", methods=["GET"])
def show_calendar():
	return render_template("calendar.html")

@app.route("/events/", methods = ['GET'])
def show_all_events():
	event_list = db_session.query(EventDetails).all()
	return render_template("event_list.html", events = event_list)

@app.route("/event", methods = ['GET'])
def show_event():
	#event_detail = Event
	return render_template("details.html")
	#return render_template("details.html", event=event_detail)

@app.route("/roster", methods = ['GET'])
def show_roster():
	player_list = db_session.query(Player).all()	
	# grab user's derby_name, mobile number
	return render_template("roster.html", players= player_list)

if __name__ == "__main__":
	app.run(debug = True)
