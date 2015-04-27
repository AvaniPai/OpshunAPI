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
		foundAt = email.index('@')
		user = email[:foundAt]
		found = User.query.filter_by(email=testEmail)
		return str(found)
	return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def make_connection():
	errors = []
	if request.method == "POST":
		var = request.get_json(force=True)
		secret = var['password']
		address = var['email']
		at = address.index('@')
		person = address[:at]
		try:
			addend = User(person, address, secret)
			db.session.add(addend)
			db.session.commit()
		except:
			errors.append("unable to add item to database")
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
