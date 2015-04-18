<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, jsonify, request, render_template
>>>>>>> ca313d63fdf4c7270113115c7bc479be7ce45574
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
	if request.method == "POST":
		person = request.form['email']
		password = requst.form['password']
		print(person)
	return render_template('login.html')

<<<<<<< HEAD
=======

if __name__ == '__main__':
	app.run(debug=True)
>>>>>>> ca313d63fdf4c7270113115c7bc479be7ce45574
