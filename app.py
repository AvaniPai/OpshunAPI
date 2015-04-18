from flask import Flask, jsonify, request, render_template, session
from flask import Flask
from flask import Flask, jsonify, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

def importUser():
	from models import User

@app.route('/')
def hello():
	return "Welcome to Opshun!"

@app.route('/<username>')
def specialized(username):
	importUser()
	return "Hello {}!".format(username)
@app.route('/login', methods=['GET','POST'])
def signingup():
	errors = []
	results= {}
	if request.method == "POST":
		email = request.form['email']
		password = request.form['newpass']
		foundAt = email.index('@')
		user = email[:foundAt]
		try:
			newUser = User(username=user, email=email, password=password)
			db.session.add(newUser)
			db.session.commit()
		except:
			errors.append("unable to add item to databse.")
	return render_template('login.html'

if __name__ == '__main__':
	app.run(debug=True)
