from flask import Flask, session, render_template, redirect, request, url_for, g, flash, abort
# from model import session as db_session, .. Classes
# import model
import os
import sqlite3
from model import session as db_session, Player, EventDetails
import gflags
import httplib2
import json
from apiclient.discovery import build_from_document, build
import random
from oauth2client.client import OAuth2WebServerFlow

# flask session: browser session (info identifying particular user of a web app)
# model session: database session (connection to db)

app = Flask(__name__)
SECRET_KEY = "Let's win espnW hackathon!"
app.config.from_object(__name__)

CLIENT_ID = "788211985789.apps.googleusercontent.com"
CLIENT_SECRET = '8m9f9ZYb2FMkjvId7gW3kMMB'

#@app.route('/')
@app.teardown_request
def shutdown_session(exception = None):
	db_session.remove()

@app.route('/login')
def login():
	flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET,
		scope='https://www.googleapis.com/auth/calendar',
		redirect_uri='http://localhost:5000/oauth2callback',
		approval_prompt='force',
		access_type='offline')

	auth_uri = flow.step1_get_authorize_url()
	return redirect(auth_uri)

@app.route('/signout')
def signout():
	del session['credentials']
	session['message'] = "You have logged out"
	return redirect(url_for('index'))

@app.route('/oauth2callback')
def oauth2callback():
	code = request.args.get('code')
	if code:
    # exchange the authorization code for user credentials
		flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, "https://www.googleapis.com/auth/calendar")
		flow.redirect_uri = request.base_url
	try:
		credentials = flow.step2_exchange(code)
	except Exception as e:
		print "Unable to get an access token because ", e.message
    # store these credentials for the current user in the session
	session['credentials'] = credentials
	return redirect(url_for('index'))

@app.route('/addevent', methods = ['GET', 'POST'])
def add_event():
	credentials = session['credentials']
	if credentials == None:
		return redirect(url_for('login'))
	http = httplib2.Http()
	http = credentials.authorize(http)
	service = build("calendar", "v3", http=http)
	location = request.form['location']
	summary = request.form['title']
	start_time = request.form['start_time']
	end_time = request.form['end_time']

	location = 'here'
	summary = 'test'
	start_time = '2012-11-10T10:00:00.000-07:00'
	end_time = '2012-11-10T10:25:00.000-07:00'
	end_time = request.form['end_time']

	event = {
	'summary': summary,
	'location': location,
	'start': {
	'dateTime': start_time
	},
	'end': {
	'dateTime': end_time
	},
	calendar_id: calendar_id
	}

	imported_event = service.events().import_(calendarId=calendar_id, body=event).execute()

	print imported_event['id']

@app.route('/')
def index():
	credentials = session['credentials']
	if credentials == None:
		return redirect(url_for('login'))
	http = httplib2.Http()
	http = credentials.authorize(http)
	service = build("calendar", "v3", http=http)
	calendar_list = service.calendarList().list().execute()
	calendar = service.calendars().get(calendarId='9kcpuhe9mj27uffcjlopnnpfrs@group.calendar.google.com').execute()

	print calendar['summary']
	return render_template("calendar.html", calendar_list=calendar_list, calendar=calendar)

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
	player_list = db_session.query(Player).all()
	#event_detail = Event
	event_list =db_session.query(EventDetails).all()
	event = event_list.pop()
	return render_template("details.html", event=event, players = player_list)
	#return render_template("details.html", event=event_detail)

@app.route("/roster", methods = ['GET'])
def show_roster():
	player_list = db_session.query(Player).all()	
	# grab user's derby_name, mobile number
	return render_template("roster.html", players= player_list)

if __name__ == "__main__":
	app.run(debug = True)
