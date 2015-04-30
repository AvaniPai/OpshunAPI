from flask import Flask, jsonify, request, render_template, session
from flask.ext.sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello():
	return "Welcome to Opshun!"

@app.route('/test', methods=['GET','POST'])
def signingup():
	errors = []
	results= {}
	if request.method == "POST":
		testEmail = request.form['email']
		password = request.form['newpass']
		foundAt = testEmail.index('@')
		found = db.session.query(User)
		exists = [entry for entry in found if entry.username == testEmail[:foundAt]]
		if(exists == []):
			newUser = User(testEmail[:foundAt], testEmail, password)
			db.session.add(newUser)
			db.session.commit()
	return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def make_connection():
	errors = []
	if request.method == "POST":
		var = request.get_json(force=True)
		password = var['password']
		email = var['email']
		at = email.index('@')
		user = email[:at]
		found = db.session.query(User)
		exists = [entry for entry in found if entry.username == user]
		if(exists == []):
			newUser = User(user, email, password)
			db.session.add(newUser)
			db.session.commit()
			message = "Welcome to Opshun!"
		else:
			message = "This user already exists. Please enter a different email."
	return message


@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == "POST":
			var = request.get_json(force=True)
			loginEmail = var['email']
			password = var['password']
			search = User.query.filter_by(email=loginEmail)
			found = [entry for entry in search if entry.email == loginEmail]
			return "Welcome back! "



if __name__ == '__main__':
	app.run()
