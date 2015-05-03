from flask import Flask, jsonify, request, render_template, session
from flask.ext.sqlalchemy import SQLAlchemy
import algorithm 
import os
import json
import init_pref

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
		blah = testEmail[:foundAt]
		found = db.session.query(User)
		exists = [entry for entry in found if entry.username == blah]
		search = db.session.query(Preferences)
		edit = [row for row in search if row.user_id == exists[0].id]
		for i in edit:
			if i.characteristic == 'Mexican':
				i.happypref = 6
			db.session.commit()

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
			amfoods = dct.get_amfoods()
			for i in amfoods:
				newPref = Preferences("food", i, "American", newUser.id)
				db.session.add(newPref)
			asfoods = dct.get_asfoods()
			for j in asfoods:
				newPref = Preferences("food", j, "Asian", newUser.id)
				db.session.add(newPref)
			itfoods = dct.get_itfoods()
			for k in itfoods:
				newPref = Preferences("food", k, "Italian", newUser.id)
				db.session.add(newPref)
			mexfoods = dct.get_mexfoods()
			for l in mexfoods:
				newPref = Preferences("food", l, "Mexican", newUser.id)
				db.session.add(newPref)
			outact = dct.get_outact()
			for m in outact:
				newPref = Preferences("activity", m, "Outdoor", newUser.id)
				db.session.add(newPref)
			nightact = dct.get_nightact()
			for n in nightact:
				newPref = Preferences("activity", n, "Night", newUser.id)
				db.session.add(newPref)
			miscact = dct.get_miscact()	
			for o in miscact:
				newPref = Preferences("activity", o, "Miscellaneous", newUser.id)
				db.session.add(newPref)
			clothes = dct.get_clothes()
			for k in clothes:
				newPref = Preferences("clothes", k, "Clothing", newUser.id)
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
			search = User.query.filter_by(email=loginEmail)
			found = [entry for entry in search if entry.email == loginEmail]
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
			for i in update:
				if i.characteristic == 'American':
					i.happypref = am
				elif i.characteristic == 'Asian':
					i.happypref = asian
			db.session.commit()
			for k in update:
				if k.characteristic == 'Mexican':
					i.happypref = mex
				if k.characteristic == 'Italian':
					i.happypref = it
			db.session.commit()
		return "You can do it!"



@app.route('/algorithm', methods=['GET','POST'])
def algy_test():
	'''remember to filter by userid'''
	food = db.session.query(Preferences)
	temp = [item.happypref for item in food]
	answer = algorithm.wrapper(temp)
	opshun = 0
	for item in food:
		if(item.id == (answer+1)):
			opshun = item.option
	
	return "Suggested food %r" % opshun

if __name__ == '__main__':
	app.run(debug=True)
