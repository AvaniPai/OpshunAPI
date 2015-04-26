from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class User(db.Model):

	__tablename__ = 'userinfo'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String())
	email = db.Column(db.String())
	password = db.Column(db.String())	
	personalize = relationship("Preferences", order_by="Preferences.id", backref="user")

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return "<User(id='%s',username='%s')>" % (str(self.id), self.username)

class Preferences(db.Model):

	__tablename__ = 'preferences'

	id = db.Column(db.Integer, primary_key=True)
	decisionType = db.Column(db.String())
	option= db.Column(db.String())
	sadPref = db.Column(db.Integer)
	happyPref = db.Column(db.Integer)
	angryPref = db.Column(db.Integer)
	excitedPref = db.Column(db.Integer)
	tiredPref = db.Column(db.Integer)
	boredPref = db.Column(db.Integer)
	user_id = db.Column(db.Integer, ForeignKey('userinfo.id'))

	user = relationship("User", backref=backref('personalize', order_by=id))
	
	def __init__(self, types, option, mood, value):
		self.decisionType=types
		self.option=option
		if mood == "happy":
			self.happyPref = value
		elif mood == "angry":
			self.angryPref = value
		elif mood == "sad":
			self.sadPref = value
		elif mood == "excited":
			self.excitedPref = value
		elif mood == "bored":
			self.boredPref = value
		elif mood == "tired":
			self.tiredPref = value
	
	def __repr__(self):
		return "<Preference(type='%s',option='%s',value='%s')>" % (self.decisionType,self.option,str(self.happyPref)) 	
