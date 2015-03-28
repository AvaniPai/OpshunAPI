from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import User

@app.route('/')
def hello():
	return "Hello World!This is Avani Speaking!"
@app.route('/<username>')
def specialized(username):
	return "I love you {}!".format(username)


