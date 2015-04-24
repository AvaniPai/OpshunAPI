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
			newUser = User(user, email, password)
			db.session.add(newUser)
			db.session.commit()
		except:
			errors.append("unable to add item to databse.")
	return render_template('login.html')
@app.route('/android', methods=['GET','POST'])
def make_connection():
	if request.method=='POST':
		username = request.json['username']
		password = request.json['password']
		email = request.json['email']
		newPerson = User(username, email, password)
		db.session.add(newUser)
		db.session.commit()

if __name__ == '__main__':
	app.run(debug=True)

