from flask import Flask, jsonify, request, render_template, session
from flask.ext.sqlalchemy import SQLAlchemy
import algorithm 
import os
import json
import init_pref
from sqlalchemy import update

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello():
	return "Welcome to Opshun!"

@app.route('/test', methods=['GET','POST'])
def signingup():
	if request.method == "POST":
		email = request.form['email']
		password = request.form['newpass']
		user = email[:email.index('@')]
		data = db.session.query(User)
		exists = [entry for entry in exists if entry.username == user]
		if(exists == []):
			new = User(user, email, password)
			db.session.add(new)
			db.session.commit()
			print "All done!"
	return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def make_connection():
	message = ""
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
			dct = init_pref.Dictionaries()
			food = dct.get_foods()
			for i in food:
				newPref = Preferences("food", i, newUser.id)
				db.session.add(newPref)
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
			search = db.session.query(User)
			found = [entry for entry in search if entry.email == loginEmail and entry.password == password]
			return "Welcome back! " 

@app.route('/profile/food', methods=['GET', 'POST'])
def create_profile():
		if request.method == "POST":
			var = request.get_json(force=True)
			email = var['email']
			am = var['American']
			asian = var['Asian']
			it = var['Italian']
			mex = var['Mexican']
			search = db.session.query(User)
			found = [entry for entry in search if entry.email == email]
			peruse = db.session.query(Preferences)
			update = [row for row in peruse if row.user_id == found[0].id]
			for i, row in enumerate(update):
				if i < 5:
					row.happypref = am
					row.characteristic= "American"
				elif i >=5 and i<11:
					row.happypref = asian
					row.characteristic = "Asian"
				elif i >= 11 and i<16:
					row.happypref = it
					row.characteristic = "Italian"
				elif i >=16:
					row.happypref = mex
					row.characteristic = "Mexican"
			db.session.commit()
		return "You can do it!"



@app.route('/algorithm', methods=['GET','POST'])
def algy_test():
	result = ""
	if request.method == "POST":
		email = request.form['email']
		password = request.form['passoword']
		foundAt = email.index('@')
		blah = email[:foundAt]
		found = db.session.query(User)
		exists = [entry for entry in found if entry.username == blah]
		search = db.session.query(Preferences)
		temp = [row.happypref for row in search if row.user_id == exists[0].id]
		answer = algorithm.wrapper(temp)
		doodle = [r.option for r in search if r.user_id == exists[0].id]
		result = doodle[answer]
	else:
		result = "sad"
	return str(result)

if __name__ == '__main__':
	app.run(debug=True)
