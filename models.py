from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class User(db.Model):

	__tablename__ = 'userinfo'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String())
	email = db.Column(db.String())
	password = db.Column(db.String())	

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return "<User(id='%s',username='%s')>" % (str(self.id), self.username)

class Preferences(db.Model):

	__tablename__ = 'preferences'

	id = db.Column(db.Integer, primary_key=True)
	decisiontype = db.Column(db.String())
	option= db.Column(db.String())
	characteristic = db.Column(db.String())
	sadpref = db.Column(db.Integer)
	happypref = db.Column(db.Integer)
	angrypref = db.Column(db.Integer)
	excitedpref = db.Column(db.Integer)
	tiredpref = db.Column(db.Integer)
	boredpref = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('userinfo.id'))

	user= db.relationship("User", backref=db.backref('personalize', order_by=id))
	
	def __init__(self, types, option, mood, value):
		self.decisiontype=types
		self.option=option
		if mood == "happy":
			self.happypref = value
		elif mood == "angry":
			self.angrypref = value
		elif mood == "sad":
			self.sadpref = value
		elif mood == "excited":
			self.excitedpref = value
		elif mood == "bored":
			self.boredpref = value
		elif mood == "tired":
			self.tiredpref = value
	
	def __init__(self, types, option, kind):
		self.decisiontype = types
		self.option = option
		self.characteristic = kind
	
	#make sure to fix representation
	def __repr__(self, types, option):
		return "<Preference(type='%s',option='%s',value='%s')>" % (self.decisiontype,self.option,str(self.happypref)) 	
