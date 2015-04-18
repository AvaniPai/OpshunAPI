from app import db


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
