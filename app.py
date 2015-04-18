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
	if request.method == "POST":
		person = request.form['email']
		password = requst.form['password']
		print(person)
	return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True)
