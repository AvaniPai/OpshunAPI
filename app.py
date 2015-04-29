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
		at = address.index('@')
		user = email[:at]
		found = db.sesssion.query(User)
		exists = [entry for entry in found if entry.username == user]
		if(exists == []):
			newUser = User(user, email, password)
			db.session.add(addend)
			db.session.commit()
		else:
			return "This user already exists. Please select another email."
	return "Welcome to Opshun!"

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == "POST":
			var = request.get_json(force=True)
			loginEmail = var['email']
			password = var['password']
			found = User.query.filter_by(email=loginEmail)
			return str(found)

if __name__ == '__main__':
	app.run()
