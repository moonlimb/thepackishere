from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship, backref

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key = True)
    derby_name = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    firstname = Column(String(20), nullable=True)
    lastname = Column(String(20), nullable=True)
    mobile = Column(String(11), nullable=True)
    twitter = Column(String(20), nullable=True)
    facebook = Column(String(20), nullable=True)
    role = Column(String(20), nullable=True)
    committee = Column(String(20), nullable=True)

    def __init__(self, id= None, derby_name  = None, email = None, 
    			 password=None, firstname=None, lastname=None, mobile=None,
    			 twitter=None, facebook=None, role=None, committee=None):
    	self.id = id
    	self.derby_name = derby_name
    	self.email = email
    	self.password = password
    	self.firstname = firstname
    	self.lastname = lastname
    	self.mobile = mobile
    	self.twitter = twitter
    	self.facebook = facebook
    	self.role = role
    	self.committee = committee

class EventDetails(Base):
	__tablename__ = "eventdetails"
	id = Column(Integer, primary_key = True)
	event_type = Column(String(20), nullable=True)
	event_subject = Column(String(50), nullable=True)
	time_arrive = Column(String(15), nullable=True)
	time_start = Column(String(15), nullable=True)
	#store geolong and geolat as Integer and divide by 65536 to convert to dec
	geolat = Column(String(20), nullable=True)
	geolong = Column(String(20), nullable=True)
	event_address = Column(String(70), nullable=True)
	zipcode = Column(String(5), nullable=True)
	opposing_team = Column(String(10), nullable=True)
	uniform_color = Column(String(15), nullable=True)
	comments = Column(String(130), nullable=True)

	def __init__(self, id=None, event_type=None, event_subject=None, time_arrive=None,
				 time_start=None, geolat=None, geolong=None, event_address=None, 
				 zipcode=None, opposing_team=None, uniform_color=None,
				 comments=None)
		self.id = id
		self.event_type = event_type
		self.event_subject = event_subject
		self.time_arrive = time_arrive
		self.time_start = time_start
		self.geolat = geolat
		self.geolong = geolong
		self.event_address = event_address
		self.zipcode = zipcode
		self.opposing_team = opposing_team
		self.uniform_color = uniform_color
		self.comments = comments



