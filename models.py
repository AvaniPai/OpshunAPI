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

class Preference(db.Model):
	__tablename__ = 'preferences'
	id = db.Column(db.Integer, primary_key=True)
	decisionType = db.Column(db.String(), nullable=False)
	option= db.Column(db.String(), nullable=False)
	sadPref =db.Column(db.Integer)
	happyPref = db.Column(db.Integer)
	angryPref = db.Column(db.Integer)
	excitedPref = db.Column(db.Integer)
	tiredPref = db.Column(db.Integer)
	boredPref = db.Column(db.Integer)
	user_id = db.Column(db.Integer foreign_key(('userinfo.id'))

	user = relationship("User", backref=backref('preferences', order_by=id))
	
	
